# dspaces

> Margo Based DataSpaces

## Documentation Files

### README.md (8,092 bytes)

# DataSpaces 2

This package contains the source code and test applications for
[DataSpaces](https://www.dataspaces.org) run-time library, which is a flexible interaction and
coordination framework to support coupled applications. Documentation can be found [here](https://dspaces.readthedocs.io/en/latest/usage.html).

DataSpaces is a distributed framework built on a dynamic set of nodes
of a HPC cluster, which implements a virtual shared-space abstraction
that can be accessed concurrently by all applications in a coupled
simulation workflow. The coupled applications can coordinate and
interact using DataSpaces by inserting and fetching scientific data
of interest through the distributed in-memory space.

DataSpaces provides a simple, yet powerful interface similar to the
tuple-space model, e.g., dspaces_put()/dspaces_get() to insert/retrieve data
objects into/from the virtual space.

## Dependencies

* mercury (git clone --recurse-submodules https://github.com/mercury-hpc/mercury.git)
* argobots (git clone https://github.com/pmodels/argobots.git)
* margo (git clone https://xgitlab.cels.anl.gov/sds/margo.git)
* MPI (for building the storage server binary and test utilities)

## Building
Create a build directory
```
$ mkdir build
$ cd build
```
Now install the dspaces provider
```
$ make
$ make install
```

## APIs

Please read header files include/dspaces.h for detailed API documentation. 

Some notable differences from the orignal DataSpaces API:

DataSpaces no longer requires an MPI communicator or appid be passed to `dspaces_init()`. Additionally, dspaces_init returns a libary handle that must be passed to other API calls.

`dspaces_get()` has now takes a timeout value. This value can be `0` or `-1`. If set to `0`, the user must ensure that the data being read has been written through external means. If timeout is set to `-1`, then the reader will wait for all the requested data to be written in the style of a data subscription.

`dspaces_put_local()` stashed staged data in the writing process' memory space, rather than pushing it to the server. This is analogous to DIMES in original DataSpaces. `dspaces_put()` and `dspaces_put_local()` can be used together.

`dspaces_lock` operations have been removed.

(*NEW in 2.1*): pub/sub operation: specify a data range and a callback to perform upon that data range. See the `test_sub` utility for example usage.

(*NEW in 2.1*): metadata functionality: post unstructured buffers indexed by name/version, with various access modes. 

(*NEW in 2.1*): `dspaces_aget()` allocates the data buffer instead of requiring a properly sized buffer be allocated.

(*NEW in 2.2*): hybrid client/server operation, with a server-side data access API. Access API calls:
  - `dspaces_server_find_objs()`: retrieve a list of locally-stored objects of a given variable version
  - `dspaces_server_get_objdata()`: retrieve a local data object into a buffer

(*NEW in 2.2*): Non-blocking put with `dspaces_iput()`

## DataSpaces usage

Setting the `DSPACES_DEBUG` environment variable generates debugging output.

### Running the Server Binary

The server binary, `dspaces_server`, takes a single argument: the listen_address. This is a Mercury-specific connection string (see Mercury documentation for details.) Common values are: `sockets` to use TCP for communication, `sm` for shared memory (if all clienta and server processes are on the same node) and `ofi+X` for RDMA, where `X` is `verbs`, `psm2`, or `cray` as is appropriate for the system fabric.

The server writes the `conf.ds` file, which provides connectivity bootstrapping data to the clients. Clients must be run with this file in their working directory.

Several environment variables influence server behavior:

`DSPACES_DEFAULT_NUM_HANDLERS` - the number of request handling threads launched by the server (in addition to the main thread). Default: 4.
`DSPACES_DRAIN` (EXPERIMENTAL) - asynchronously drain data written to local process spaces using `dspaces_put_local()` to the server. Off by default.

#### dataspaces.conf

The DataSpaces server expects to find the `dataspaces.conf` file in the working directory of the server. This is a list of configuration variables of the format

`<variable> = <value>`, e.g.
`num_apps = 1`

(*NEW in 2.0*): `num_apps`: this value is the number of `dspaces_kill()` calls that are needed to kill the server binary.

`ndim`: number of dimensions for the default global data domain.

`dims`: size of each dimension for the default global data domain.

`max_versions`: maximum number of versions of a data object to be cached in DataSpaces servers.

`hash_version`: indexing hash to use. A value of 1 means Hilbert SFC ; 2 means recursive bisection

- (*NEW in 2.2*) `hash_version` will be assigned per-variable by heuristic if not set in conf file (recommended!)

#### dataspaces.toml
DataSpaces supports configuration in the TOML format. If `dataspaces.conf` is not found by the server binary, it will search for `dataspaces.toml`. All configuration variables are the same.

### The terminator utility

DataSpaces provides a terminator utility for sending a kill signal to the server. Effectively, the terminator joins the server, sends the kill signal, and disconnects. This can be useful for workflows in which it's not clear from inside each application when the workflow should be stopped.

### Example DataSpaces programs

`test_writer`, `test_reader`, and `test_sub` are example DataSpaces client programs. `test_writer` iteratively writes variables into DataSpaces storage and `test_reader` reads those variables, checking for data corruption. `test_sub` performs the same function as `test_reader`, but using the pub/sub mode of operation.

#### test_writer usage:
```
test_writer <dims> np[0] .. np[dims-1] sp[0] ... sp[dims-1] <timesteps> [-s <elem_size>] [-m (server|local)] [-c <var_count>] [-t]
   dims              - number of data dimensions. Must be at least one
   np[i]             - the number of processes in the ith dimension. The product of np[0],...,np[dim-1] must be the number of MPI ranks
   sp[i]             - the per-process data size in the ith dimension
   timesteps         - the number of timestep iterations written
   -s <elem_size>    - the number of bytes in each element. Defaults to 8
   -m (server|local) - the storage mode (stage to server or stage in process memory). Defaults to server
   -c <var_count>    - the number of variables written in each iteration. Defaults to one
   -t                - send server termination after writing is complete
```

#### test_reader usage:
```
test_reader <dims> np[0] .. np[dims-1] sp[0] ... sp[dims-1] <timesteps> [-s <elem_size>] [-c <var_count>] [-t]
   dims              - number of data dimensions. Must be at least one
   np[i]             - the number of processes in the ith dimension. The product of np[0],...,np[dim-1] must be the number of MPI ranks
   sp[i]             - the per-process data size in the ith dimension
   timesteps         - the number of timestep iterations written
   -s <elem_size>    - the number of bytes in each element. Defaults to 8
   -c <var_count>    - the number of variables written in each iteration. Defaults to one
   -t                - send server termination signal after reading is complete
   -a                - ask dataspaces to allocate read data buffer
```

#### test_sub usage
```
test_sub <dims> np[0] .. np[dims-1] sp[0] ... sp[dims-1] <timesteps> [-s <elem_size>] [-c <var_count>] [-t]
   dims              - number of data dimensions. Must be at least one
   np[i]             - the number of processes in the ith dimension. The product of np[0],...,np[dim-1] must be the number of MPI ranks
   sp[i]             - the per-process data size in the ith dimension
   timesteps         - the number of timestep iterations written
   -s <elem_size>    - the number of bytes in each element. Defaults to 8
   -c <var_count>    - the number of variables written in each iteration. Defaults to one
   -t                - send server termination signal after reading is complete
```
 
 

---

### docs/requirements.txt (19 bytes)

renku-sphinx-theme

---

### CMakeLists.txt (3,615 bytes)

#
#  general cmake flags:
#    -DCMAKE_INSTALL_PREFIX=/usr/local     -- the prefix for installing
#    -DCMAKE_BUILD_TYPE=type               -- type can be Debug, Release, ...
#    -DCMAKE_PREFIX_PATH=/dir              -- external packages
#
#     note that CMAKE_PREFIX_PATH can be a list of directories:
#      -DCMAKE_PREFIX_PATH='/dir1;/dir2;/dir3'
#

cmake_minimum_required (VERSION 3.16)
project (dspaces VERSION 2.2.0 LANGUAGES C)

cmake_policy(SET CMP0078 NEW)
cmake_policy(SET CMP0086 NEW)

#enable_testing ()

include(GNUInstallDirs)

if(NOT CMAKE_ARCHIVE_OUTPUT_DIRECTORY)
  set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY
    ${PROJECT_BINARY_DIR}/${CMAKE_INSTALL_LIBDIR})
endif()
if(NOT CMAKE_LIBRARY_OUTPUT_DIRECTORY)
  set(CMAKE_LIBRARY_OUTPUT_DIRECTORY
    ${PROJECT_BINARY_DIR}/${CMAKE_INSTALL_LIBDIR})
endif()
if(NOT CMAKE_RUNTIME_OUTPUT_DIRECTORY)
  set(CMAKE_RUNTIME_OUTPUT_DIRECTORY
    ${PROJECT_BINARY_DIR}/${CMAKE_INSTALL_BINDIR})
endif()

include(CMakeDependentOption)
get_property(SHARED_LIBS_SUPPORTED GLOBAL PROPERTY TARGET_SUPPORTS_SHARED_LIBS)
cmake_dependent_option(BUILD_SHARED_LIBS
  "Build shared libraries (so/dylib/dll)." ${SHARED_LIBS_SUPPORTED}
  "SHARED_LIBS_SUPPORTED" OFF
)
mark_as_advanced(BUILD_SHARED_LIBS)
if((NOT BUILD_SHARED_LIBS) AND (NOT DEFINED CMAKE_POSITION_INDEPENDENT_CODE))
  set(CMAKE_POSITION_INDEPENDENT_CODE ON)
endif()

option(ENABLE_TESTS    "Build tests" OFF)
set(DSPACES_PYTHON_BINDINGS AUTO CACHE STRING  "Build Python bindings")
set_property(CACHE DSPACES_PYTHON_BINDINGS PROPERTY STRINGS "ON;TRUE;AUTO;OFF;FALSE")

# add our cmake module directory to the path
set (CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH}
     "${CMAKE_CURRENT_SOURCE_DIR}/cmake")

# link shared lib with full rpath
set (CMAKE_INSTALL_RPATH "${CMAKE_INSTALL_PREFIX}/lib")
set (CMAKE_INSTALL_RPATH_USE_LINK_PATH TRUE)

set (CMAKE_PREFIX_PATH "" CACHE STRING "External dependencies path")
set (BUILD_SHARED_LIBS "OFF" CACHE BOOL "Build a shared library")

# packages we depend on
include (xpkg-import)
xpkg_import_module (margo REQUIRED margo)
xpkg_import_module (liblz4 REQUIRED liblz4)

include(python_bindings)

find_package(MPI COMPONENTS REQUIRED)

set(DSPACES_USE_OPENMP ON CACHE STRING "Use OpenMP for operations")
mark_as_advanced(DSPACES_USE_OPENMP)
find_package(OpenMP)
if(OPENMP_FOUND AND DSPACES_USE_OPENMP)
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${OpenMP_C_FLAGS}")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${OpenMP_CXX_FLAGS}")
    add_definitions(-DOPS_USE_OPENMP)
endif()
find_package(CURL)
if(CURL_FOUND)
    add_definitions(-DDSPACES_HAVE_CURL)
endif()

include(CheckLanguage)
check_language(Fortran)
if(CMAKE_Fortran_COMPILER)
    enable_language(Fortran)
endif()
if(CMAKE_Fortran_COMPILER_LOADED)
    include(CheckFortranCompilerFlag)
    set(DSPACES_HAVE_FORTRAN TRUE)
    check_fortran_compiler_flag("-fallow-argument-mismatch" FORTRAN_HAS_ARG_MISMATCH_FLAG)
    if(FORTRAN_HAS_ARG_MISMATCH_FLAG)
        SET(CMAKE_Fortran_FLAGS "${CMAKE_CXX_FLAGS} -fallow-argument-mismatch -Wno-lto-type-mismatch")
    endif()
endif()

add_subdirectory(src)
add_subdirectory(include)
add_subdirectory(bindings)
add_subdirectory(modules)
if(${ENABLE_TESTS})
  enable_testing()
  add_subdirectory(tests)
endif(${ENABLE_TESTS})
if(${ENABLE_EXAMPLES})
    configure_file(
        ${PROJECT_SOURCE_DIR}/examples/opts.mk.in
        ${PROJECT_BINARY_DIR}/examples/opts.mk
        @ONLY
    )
    file(GLOB EXAMPLE_DIRS ${PROJECT_SOURCE_DIR}/examples/ex*)
    file(COPY ${PROJECT_SOURCE_DIR}/examples/Makefile ${EXAMPLE_DIRS} DESTINATION ${PROJECT_BINARY_DIR}/examples)
endif(${ENABLE_EXAMPLES})

---

### bindings/CMakeLists.txt (135 bytes)

if(DSPACES_HAVE_FORTRAN)
    add_subdirectory(fortran)
endif()

if(DSPACES_BUILD_PYTHON_BINDINGS)
    add_subdirectory(python)
endif()

---

### bindings/fortran/CMakeLists.txt (956 bytes)

set(CMAKE_Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR})
include(FortranCInterface)

FortranCInterface_HEADER(FC.h MACRO_NAMESPACE "FC_")

add_library(dspaces_fortran
    dspaces_f2c.c
    dspaces_mod.f90
)

set_property(TARGET dspaces_fortran PROPERTY EXPORT_NAME fortran)
set_property(TARGET dspaces_fortran PROPERTY OUTPUT_NAME dspaces_f)

target_include_directories(dspaces_fortran
    PUBLIC
        $<BUILD_INTERFACE:${CMAKE_Fortran_MODULE_DIRECTORY}>        
        $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>
    PRIVATE
        ${CMAKE_CURRENT_BINARY_DIR}
)

target_link_libraries(dspaces_fortran
    PRIVATE
        dspaces
)

install (TARGETS dspaces_fortran EXPORT dspaces-targets
    ARCHIVE DESTINATION lib
    LIBRARY DESTINATION lib)

install (
    DIRECTORY ${CMAKE_Fortran_MODULE_DIRECTORY}/
    DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
    FILES_MATCHING
        PATTERN "dspaces*.mod"
        PATTERN "CMakeFiles" EXCLUDE
)

---

### bindings/python/CMakeLists.txt (1,269 bytes)

string(REGEX REPLACE "^.*(lib/.*)$" "\\1" CMAKE_INSTALL_PYTHONDIR_DEFAULT "${Python_SITEARCH}")

set(CMAKE_INSTALL_PYTHONDIR "${CMAKE_INSTALL_PYTHONDIR_DEFAULT}"
        CACHE PATH "Install directory for python modules"
     ) 
mark_as_advanced(CMAKE_INSTALL_PYTHONDIR)
set(CMAKE_PYTHON_OUTPUT_DIRECTORY
  ${PROJECT_BINARY_DIR}/${CMAKE_INSTALL_PYTHONDIR}
)

include_directories(SYSTEM ${PYTHON_INCLUDE_PATH} ${_Python_NumPy_INCLUDE_DIR} ${MPI4Py_INCLUDE_DIR})
include_directories($<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>)

if(SWIG_FOUND)
  message("-- SWIG found: ${SWIG_EXECUTABLE}")
endif()

swig_add_library(dspaces_wrapper
                LANGUAGE python
                SOURCES dspaces_wrapper.i dspaces_wrapper.c
                )
set_target_properties(dspaces_wrapper PROPERTIES
    SWIG_USE_TARGET_INCLUDE_DIRECTORIES TRUE)
swig_link_libraries(dspaces_wrapper dspaces dspaces-server)

set(CMAKE_PYTHON_OUTPUT_DIRECTORY "${PROJECT_BINARY_DIR}/bindings/python")

install(TARGETS dspaces_wrapper
  DESTINATION ${CMAKE_INSTALL_PYTHONDIR}/dspaces
)

install(FILES 
    ${CMAKE_CURRENT_SOURCE_DIR}/__init__.py
    ${CMAKE_PYTHON_OUTPUT_DIRECTORY}/dspaces_wrapper.py
    ${CMAKE_CURRENT_SOURCE_DIR}/dspaces.py
  DESTINATION ${CMAKE_INSTALL_PYTHONDIR}/dspaces
)

---

### docs/api.rst (32 bytes)

DataSpaces API
==============

---

### docs/examples.rst (453 bytes)

DataSpaces Examples
===================

The DataSpaces repo includes a set of examples. When built using cmake, 
DataSpaces configures a Makefile and copies these examples in to the `examples/` 
directory in the build environment. This process can easily be manually duplicated
by moving opts.mk.in to opts.mk and filling in a valid value for `CC` (usually `mpicc`).

Each example contains everything needed to build a run a program using dataspaces. 

---

### docs/index.rst (1,177 bytes)

.. DataSpaces documentation master file, created by
   sphinx-quickstart on Tue Sep 28 14:04:59 2021.

Welcome to DataSpaces
=====================

DataSpaces is a communication library aimed at supporting interactions between large-scale scientific simulation, analysis, and visualization programs. 
DataSpaces enables programs to write to and read from shared N-dimensional arrays without centralized query processing or indexing using low-latency RDMA transfers. 
The result is highly-scalable data access between components of an HPC workflow. 
DataSpaces can be used to tranfer data in *in-situ* workflows, such as coupled simulations and in-situ analysis workflows, 
moving data through shared memory and RDMA tranfers, rather than using the file system.
Like a shared file system, DataSpaces allow data readers to be decoupled from writers in both space in time.
In other words, no sychronization of writers and readers is required, and readers may access data written by any process.

Contents
========

.. toctree::
   
   installation
   usage
   running
   API
   examples

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

---

### docs/installation.rst (1,859 bytes)

Installing
==========

The easiest way to install DataSpaces is using `Spack <https://spack.readthedocs.io/en/latest/>`_. Spack is a package manager aimed at HPC and scientific computing.
Using Spack simplifies the installation of DataSpaces and its dependencies.

If you wish to install DataSpaces directly from source, the distribution repo can be found on `GitHub <https://github.com/rdi2dspaces/dspaces>`_.

Installing Spack
----------------

To install Spack, follow the getting started instructions found `here <https://spack.readthedocs.io/en/latest/getting_started.html>`_. 
This will install the package manager, and make a large variety of packages available.

Installing the DataSpaces repository
------------------------------------

The DataSpaces group maintains a repository for the DataSpaces spack package (and any relevant ancillary packages). This can be found `here <https://github.com/rdi2dspaces/dspaces-spack>`_. 
In order to use this package, you will need to first install Spack using the above instructions.
Once you have done this, you can load the DataSpaces package repository by doing the following:

.. code-block:: console

   git clone https://github.com/rdi2dspaces/dspaces-spack.git
   spack repo add dspaces-spack

Installing DataSpaces
---------------------

One the DataSpaces repository has been loaded, the dataspaces package can be installed with:

.. code-block:: console

   spack install dataspaces

This will automatically install allDdataSpaces dependencies and the dataspaces package itself. 
Once the package has been installed the command:

.. code-block:: console

   spack load dataspaces

Configures the environment to use DataSpaces, adding the server binary's directory to ``PATH``, any shared library paths to ``LD_LIBRARY_PATH``, etc. 
This simplifies building and running programs that use DataSpaces.

---

### docs/running.rst (3,624 bytes)

How to Run
==========

Running the Server
-----------------
The DataSpaces server expects to find the ``dataspaces.conf`` file in its working directory. 
The format of this file is a list of configuration values, one per line:

``<variable> = <value>``, e.g.
``num_apps = 1``

The possible values are as follows:

**num_apps**: this value is the number of ``dspaces_kill()`` calls from clients that are needed to kill the server binary.

**ndim**: number of dimensions for the default global data domain.

**dims**: size of each dimension for the default global data domain.

**max_versions**: maximum number of versions of a data object to be cached in DataSpaces servers.

**hash_version**: the type of distributed hash table used. A value of ``1`` means that a Hilbert SFC is partitioned into continuous segments and distributed across the servers.
A value of ``2`` means the space is partitioned by repeating bisection along the longest domain.

**NOTES** on what values to use:

The global dimensions have implications for performance. Data indexing will be partitioned evently across the global dimensions, 
and so if data is only being writtent to a subset of the global dimensions there is a risk of unabalanced indexing load.
Ideally, the data domain being written to will match the global dimensions as closely as possible. The default value set in
``dataspaces.conf`` is for convenience. The application can set this per variable with ``dspaces_define_gdim()``.

``hash_version = 1`` has better locality in the most general case, and should be preferred unless the dimensions of the data 
domain are not a power of two or the ratio of longest to shortest dimension is greater than two.

``num_apps`` should be set in conjunction with how ``dspaces_kill()`` is used in the application(s) using dataspaces. Generally, one rank
of each application should call ``dspaces_kill()``, and the number of process groups using dataspaces will be the same as ``num_apps``. 
Occasionally, it is not practical to have a client call ``dspaces_kill()``, and the dataspaces repo provides a standalone binary ``terminator`` 
to send a single ``dspaces_kill()`` and then exit.

Bootstrapping communication
---------------------------
The server produces a bootstrap file during its init phase, ``conf.ds``. This file must be read by the clients (or rank zero of the clients 
if ``dspaces_init_mpi()`` is being used. This file provides the clients with enough information to make initial contact with the server and
perform wire-up. In order to find this file, the server and client application must be run in the same working directory, or at last a symlink of ``conf.ds`` should be present.

Environment variables
---------------------
There are a few environment variables that can be used to influence DataSpaces.

``DSPACES_DEBUG`` - enables substantial debug output for both clients and server.

``DSPACES_DEFAULT_NUM_HANDLERS`` - the number of request handling threads launched by the server (in addition to the main thread). Default: 4.
 This value should be changed if it is likely to oversubscribe or underutilize the node the server is running on.

 Running the server
 ------------------

The server binary, ``dspaces_server``, takes a single argument: the listen_address. 
This is a Mercury-specific connection string (see Mercury documentation for details.) 
Common values are: ``sockets`` to use TCP for communication, ``sm`` for shared memory 
(if all clienta and server processes are on the same node) and ``ofi+X`` for RDMA, 
where ``X`` is ``verbs``, ``psm2``, or ``cray`` as is appropriate for the system fabric.

---

### docs/usage.rst (3,024 bytes)

How to Use DataSpaces
=====================

DataSpaces consists of two components: a client library and a server library. 
Additionally, the DataSpaces package comes packaged with a standalone, MPI-based server binary.
The typical usage of DataSpaces is to run the server binary along-side the user's application, 
and use the DataSpaces calls provided by the client library to store and access data from the server. 
It is also possible to run the server in a subset of application proccesses, if it is not desired to run 
the server as an independent binary.

DataSpaces provides a full set of bindings for C/C++, and a subset of the API for fortran and python.
This makes it possible to share data between applications written in different programming languages via the common put/get abstraction.

Building a C/C++ program with DataSpaces
----------------------------------------

Flags necessary for compiling a program that uses DataSpaces can be found from the pkg-config file installed by DataSpaces in ``<INSTALL_ROOT>/lib/pkgconfig``.
If installing using spack, the appropriate directory will be added to ``PGK_CONFIG_PATH`` when the dataspaces module is loaded. 
``pkg-config`` can provide useful information that depends on which flag is provided:

    
Provides compilation flags for building a program that uses the dataspaces API:

.. code-block:: console
    
    pkg-config --cflags dspaces

Provides linking flags for building a program that uses the dataspaces API:

.. code-block:: console
    
    pkg-config --libs dspaces

Provides the path to the dspaces_server binary:

.. code-block:: console
    
    pkg-config --variable=exec_prefix dspaces

Alternatively, dataspaces installs a CMake targets file that makes it easy to include dspaces in a CMake project. 
If dataspaces was installed with Spack, ``CMAKE_PREFIX_PATH`` will be updated when the dataspaces package is loaded.
Recent versions of cmake will also be able to find dspaces if ``<INSTALL_ROOT>/bin`` is in the users ``PATH`` environment variable. 

To include dspaces in a CMake project, simply add ``find_package(dspaces)`` to the project's CMakeLists.txt file and include ``dspaces::dspaces`` 
in the target_link_libraries for whatever target is using dspaces.

Building a Fortran program with DataSpaces
------------------------------------------

Flags for Fortran compilation cannot be obtained through pkg-config. However, a CMake project can be configured to automatically configure 
compilation for dataspaces with Fortran. To do this, add ``find_package(dspaces)`` to the project's CMakeLists.txt file and include ``dspaces::fortran``
in the target_link_libraries for whatever target is using dspaces.

Using DataSpaces with Python
----------------------------

In order to use the DataSpaces pythong bindings, ``<INSTALL_ROOT>/lib/<PYTHONVER>/dist-packages`` must be added to ``PYTHONPATH``. 
Spack will do this automatically when the dataspaces package is loaded. To use the Python bindings, import the ``dspaces`` module.`

---

### include/CMakeLists.txt (123 bytes)

install(
    FILES dspaces.h dspaces-common.h dspaces-server.h dspaces-ops.h
    DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
)

---

### modules/CMakeLists.txt (210 bytes)

set(DSPACES_INSTALL_MODULE_PATH "${CMAKE_INSTALL_PREFIX}/share/modules")
set(script-mods s3nc_mod.py azure_mod.py url_mod.py ds_reg.py)

install(FILES ${script-mods} DESTINATION ${DSPACES_INSTALL_MODULE_PATH})

---

### src/CMakeLists.txt (3,815 bytes)

find_package(DRC)
if(HAVE_DRC)
    include_directories(${DRC_INCLUDE_DIRS})
    add_definitions( -DHAVE_DRC)
endif()

# list of source files
set(dspaces-src util.c bbox.c ss_data.c dspaces-client.c dspaces-ops.c dspaces-logging.c)

# load package helper for generating cmake CONFIG packages
include (CMakePackageConfigHelpers)

# where to install files for "find_package"
set (dspaces-pkg "share/cmake/dspaces")

set (dspaces-vers "${dspaces_VERSION_MAJOR}.${dspaces_VERSION_MINOR}")

add_library(dspaces ${dspaces-src})
if(HAVE_DRC)
    target_link_libraries (dspaces margo m pthread ${DRC_LIBRARIES} liblz4)
    target_include_directories (dspaces PUBLIC $<INSTALL_INTERFACE:include> ${DRC_INCLUDE_DIRS})
else()
    target_link_libraries (dspaces margo m pthread liblz4)
    target_include_directories (dspaces PUBLIC $<INSTALL_INTERFACE:include>)
endif()

# local include's BEFORE, in case old incompatable .h files in prefix/include
target_include_directories (dspaces BEFORE PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/../include>)

# for shared libs, establish the lib version
set_target_properties (dspaces
    PROPERTIES VERSION ${dspaces_VERSION}
    SOVERSION ${dspaces_VERSION_MAJOR})

set(dspaces-server-src util.c bbox.c ss_data.c dspaces-server.c dspaces-conf.c dspaces-modules.c dspaces-logging.c toml.c)

add_library(dspaces-server ${dspaces-server-src} ${dspaces-src})
if(HAVE_DRC)
    target_link_libraries (dspaces-server margo m pthread ${DRC_LIBRARIES} liblz4)
    target_include_directories (dspaces-server BEFORE PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/../include> ${DRC_INCLUDE_DIRS})
else()
    target_link_libraries (dspaces-server margo m pthread liblz4)
    target_include_directories (dspaces-server BEFORE PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/../include>)
endif()

if(Python_FOUND)
    target_link_libraries(dspaces-server Python::Python)
    target_include_directories (dspaces-server BEFORE PUBLIC ${PYTHON_INCLUDE_PATH} ${_Python_NumPy_INCLUDE_DIR})
    target_compile_definitions(dspaces-server PRIVATE DSPACES_HAVE_PYTHON)
endif()

if(CURL_FOUND)
    target_link_libraries(dspaces-server curl)
    target_include_directories (dspaces-server BEFORE PUBLIC ${CURL_INCLUDE_DIR})
endif()

target_compile_definitions(dspaces-server PRIVATE DSPACES_MOD_DIR=${CMAKE_INSTALL_PREFIX}/share/modules)

# for shared libs, establish the lib version
set_target_properties (dspaces-server
    PROPERTIES VERSION ${dspaces_VERSION}
    SOVERSION ${dspaces_VERSION_MAJOR})

#
# installation stuff (packaging and install commands)
#
write_basic_package_version_file(
    "dspaces-config-version.cmake"
    VERSION ${dspaces_VERSION}
    COMPATIBILITY AnyNewerVersion)

# generate our config file for find_package()
configure_file (dspaces-config.cmake.in dspaces-config.cmake @ONLY)

# some bits for the pkg-config file
set (DEST_DIR "${CMAKE_INSTALL_PREFIX}")
set (PRIVATE_LIBS "-ldspaces -lpthread -lmargo -labt -lmercury -lm")
configure_file ("dspaces.pc.in" "dspaces.pc" @ONLY)
configure_file ("dspaces-server.pc.in" "dspaces-server.pc" @ONLY)

#
# "make install" rules
#
install (TARGETS dspaces dspaces-server EXPORT dspaces-targets
         ARCHIVE DESTINATION lib
         LIBRARY DESTINATION lib)
install (EXPORT dspaces-targets NAMESPACE dspaces::
         DESTINATION ${dspaces-pkg}
         FILE "dspaces-targets.cmake")
install (FILES "${CMAKE_CURRENT_BINARY_DIR}/dspaces-config.cmake"
               "${CMAKE_CURRENT_BINARY_DIR}/dspaces-config-version.cmake"
               "../cmake/xpkg-import.cmake"
         DESTINATION ${dspaces-pkg} )
install (FILES "${CMAKE_CURRENT_BINARY_DIR}/dspaces.pc"
		DESTINATION "lib/pkgconfig/")
install (FILES "${CMAKE_CURRENT_BINARY_DIR}/dspaces-server.pc"
        DESTINATION "lib/pkgconfig/")   

---

### tests/CMakeLists.txt (4,129 bytes)

add_executable(dspaces_server server.c)
target_link_libraries(dspaces_server dspaces dspaces-server)

add_executable(test_reader test_reader.c test_get_run.c timer.c)
target_link_libraries(test_reader dspaces)

add_executable(test_writer test_writer.c test_put_run.c timer.c)
target_link_libraries(test_writer dspaces)

add_executable(terminator terminator.c)
target_link_libraries(terminator dspaces)

add_executable(dspaces_ls dspaces_ls.c)
target_link_libraries(dspaces_ls dspaces)

if(DSPACES_HAVE_FORTRAN)
    add_executable(test_writer_f test_writer.f90)
    target_link_libraries(test_writer_f dspaces_fortran)

    add_executable(test_reader_f test_reader.f90)
    target_link_libraries(test_reader_f dspaces_fortran)
endif()

add_executable(test_sub test_sub.c test_sub_run.c timer.c)
target_link_libraries(test_sub dspaces)

add_executable(test_writer_server test_writer_server.c test_put_run.c timer.c)
target_link_libraries(test_writer_server dspaces dspaces-server)

add_executable(test_calc test_calc.c)
target_link_libraries(test_calc dspaces)

install(TARGETS dspaces_server terminator dspaces_ls
  DESTINATION ${CMAKE_INSTALL_BINDIR}
)

configure_file(
  ${PROJECT_SOURCE_DIR}/tests/test_script.sh.in
  ${PROJECT_BINARY_DIR}/tests/test_script.sh
  @ONLY
)

find_program (BASH_PROGRAM bash)

if (BASH_PROGRAM)
  add_test (Test_write ${BASH_PROGRAM} test_script.sh 1)
  set_tests_properties(Test_write PROPERTIES TIMEOUT 30) 
  add_test (Test_write_local ${BASH_PROGRAM} test_script.sh 1 local)
  set_tests_properties(Test_write_local PROPERTIES TIMEOUT 30)
  add_test (Test_read ${BASH_PROGRAM} test_script.sh 2)
  set_tests_properties(Test_read PROPERTIES TIMEOUT 30) 
  add_test (Test_read_data_subset ${BASH_PROGRAM} test_script.sh 3)
  set_tests_properties(Test_read_data_subset PROPERTIES TIMEOUT 30) 
  add_test (Test_read_ts_subset ${BASH_PROGRAM} test_script.sh 4)
  set_tests_properties(Test_read_ts_subset PROPERTIES TIMEOUT 30) 
  add_test (Test_read_early ${BASH_PROGRAM} test_script.sh 5)
  set_tests_properties(Test_read_early PROPERTIES TIMEOUT 30)
  add_test (Test_read_local ${BASH_PROGRAM} test_script.sh 2 local)
  set_tests_properties(Test_read_local PROPERTIES TIMEOUT 30)
  add_test (Test_read_data_subset_local ${BASH_PROGRAM} test_script.sh 3 local)
  set_tests_properties(Test_read_data_subset_local PROPERTIES TIMEOUT 30)
  add_test (Test_read_ts_subset_local ${BASH_PROGRAM} test_script.sh 4 local)
  set_tests_properties(Test_read_ts_subset_local PROPERTIES TIMEOUT 30)
  add_test (Test_read_early_local ${BASH_PROGRAM} test_script.sh 5 local)
  set_tests_properties(Test_read_early_local PROPERTIES TIMEOUT 30)
if(DSPACES_HAVE_FORTRAN)  
    add_test (Test_fortran_binding ${BASH_PROGRAM} test_script.sh 6)
    set_tests_properties(Test_fortran_binding PROPERTIES TIMEOUT 30)
endif()
  add_test (Test_sub ${BASH_PROGRAM} test_script.sh 7)
  set_tests_properties(Test_sub PROPERTIES TIMEOUT 60)
  add_test (Test_read_alloc ${BASH_PROGRAM} test_script.sh 8)
  set_tests_properties(Test_read_alloc PROPERTIES TIMEOUT 30)
  add_test (Test_read_alloc_local ${BASH_PROGRAM} test_script.sh 8 local)
  set_tests_properties(Test_read_alloc_local PROPERTIES TIMEOUT 30)
  add_test (Test_write_server ${BASH_PROGRAM} test_script.sh 9)
  set_tests_properties(Test_write_server PROPERTIES TIMEOUT 30) 
  add_test (Test_write_server_local ${BASH_PROGRAM} test_script.sh 9 local)
  set_tests_properties(Test_write_server_local PROPERTIES TIMEOUT 30)
  add_test (Test_read_server ${BASH_PROGRAM} test_script.sh 10)
  set_tests_properties(Test_read_server PROPERTIES TIMEOUT 30)
  add_test (Test_read_server_local ${BASH_PROGRAM} test_script.sh 10 local)
  set_tests_properties(Test_read_server_local PROPERTIES TIMEOUT 30)
  add_test (Test_read_multi_dht ${BASH_PROGRAM} test_script.sh 11)
  set_tests_properties(Test_read_multi_dht PROPERTIES TIMEOUT 30)
  add_test (Test_calc  ${BASH_PROGRAM} test_script.sh 12)
  set_tests_properties(Test_calc PROPERTIES TIMEOUT 30)
  add_test (Test_ls ${BASH_PROGRAM} test_script.sh 13)
  set_tests_properties(Test_ls PROPERTIES TIMEOUT 30)
endif (BASH_PROGRAM)

---

## Source Files

Source code files are processed separately by the processor.
File list:

- `.gitignore` (25 bytes)
- `docs/Makefile` (580 bytes)
- `examples/Makefile` (244 bytes)
- `examples/ex1_putget/Makefile` (177 bytes)
- `examples/ex2_boundingBox/Makefile` (177 bytes)
- `examples/ex3_minmax/Makefile` (281 bytes)
- `examples/ex4_collective/Makefile` (177 bytes)
- `.readthedocs.yaml` (534 bytes)
- `LICENSE.toml` (1,091 bytes)
- `bindings/fortran/dspaces_f2c.c` (1,869 bytes)
- `bindings/python/__init__.py` (23 bytes)
- `bindings/python/dspaces.py` (9,558 bytes)
- `bindings/python/dspaces_wrapper.c` (21,086 bytes)
- `bindings/python/dspaces_wrapper.h` (2,620 bytes)
- `cmake/FindDRC.cmake` (840 bytes)
- `cmake/FindMPI4Py.cmake` (1,504 bytes)
- `cmake/python_bindings.cmake` (567 bytes)
- `cmake/xpkg-import.cmake` (11,682 bytes)
- `docs/conf.py` (5,490 bytes)
- `examples/ex1_putget/dataspaces.conf` (80 bytes)
- `examples/ex1_putget/get.c` (1,832 bytes)
- `examples/ex1_putget/put.c` (2,222 bytes)
- `examples/ex2_boundingBox/dataspaces.conf` (81 bytes)
- `examples/ex2_boundingBox/get.c` (2,089 bytes)
- `examples/ex2_boundingBox/put.c` (1,861 bytes)
- `examples/ex3_minmax/dataspaces.conf` (82 bytes)
- `examples/ex3_minmax/minmaxavg_reader.c` (3,899 bytes)
- `examples/ex3_minmax/minmaxavg_writer.c` (2,216 bytes)
- `examples/ex4_collective/dataspaces.conf` (82 bytes)
- `examples/ex4_collective/get.c` (3,576 bytes)
- `examples/ex4_collective/put.c` (3,584 bytes)
- `examples/ex5_minmax_python/dataspaces.conf` (82 bytes)
- `examples/ex5_minmax_python/minmaxavg_reader.py` (1,594 bytes)
- `examples/ex5_minmax_python/minmaxavg_writer.py` (1,526 bytes)
- `include/bbox.h` (1,707 bytes)
- `include/dspaces-common.h` (3,709 bytes)
- `include/dspaces-conf.h` (642 bytes)
- `include/dspaces-logging.h` (1,901 bytes)
- `include/dspaces-modules.h` (2,760 bytes)
- `include/dspaces-ops.h` (6,150 bytes)
- `include/dspaces-remote.h` (192 bytes)
- `include/dspaces-server.h` (2,290 bytes)
- `include/dspaces-storage.h` (342 bytes)
- `include/dspaces.h` (18,729 bytes)
- `include/dspacesp.h` (359 bytes)
- `include/gspace.h` (2,875 bytes)
- `include/list.h` (3,229 bytes)
- `include/queue.h` (2,858 bytes)
- `include/sfc.h` (35,994 bytes)
- `include/ss_data.h` (17,382 bytes)
- ... and 32 more files

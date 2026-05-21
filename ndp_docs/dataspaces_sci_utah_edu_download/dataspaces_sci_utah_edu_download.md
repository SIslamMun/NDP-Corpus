[ Skip to content](https://dataspaces.sci.utah.edu/download/#content "Skip to content")
  * [Home](https://dataspaces.sci.utah.edu/)
  * [Overview](https://dataspaces.sci.utah.edu/overview/)
  * [Applications](https://dataspaces.sci.utah.edu/applications/)
  * [News](https://dataspaces.sci.utah.edu/news/)
  * [Research](https://dataspaces.sci.utah.edu/research/)
  * [Download](https://dataspaces.sci.utah.edu/download/)
  * [Publications](https://dataspaces.sci.utah.edu/publications/)
  * [Team](https://dataspaces.sci.utah.edu/team/)
  * [Support](https://dataspaces.sci.utah.edu/support/)Menu Toggle
    * [](https://dataspaces.sci.utah.edu/manual/)
    * [](https://dataspaces.sci.utah.edu/faq/)
  * [Contact](https://dataspaces.sci.utah.edu/contact/)

[ DATASPACES ](https://dataspaces.sci.utah.edu/)
An Extreme Scale Data Management Framework 
[ DATASPACES ](https://dataspaces.sci.utah.edu/)
An Extreme Scale Data Management Framework 
Main Menu
  * [Home](https://dataspaces.sci.utah.edu/)
  * [Overview](https://dataspaces.sci.utah.edu/overview/)
  * [Applications](https://dataspaces.sci.utah.edu/applications/)
  * [News](https://dataspaces.sci.utah.edu/news/)
  * [Research](https://dataspaces.sci.utah.edu/research/)
  * [Download](https://dataspaces.sci.utah.edu/download/)
  * [Publications](https://dataspaces.sci.utah.edu/publications/)
  * [Team](https://dataspaces.sci.utah.edu/team/)
  * [Support](https://dataspaces.sci.utah.edu/support/)Menu Toggle
    * [](https://dataspaces.sci.utah.edu/manual/)
    * [](https://dataspaces.sci.utah.edu/faq/)
  * [Contact](https://dataspaces.sci.utah.edu/contact/)

# Download
### Download Information
The most recent updates, development code, and additional versions can be found on the [GitHub Repo](https://github.com/rdi2dspaces/dspaces)
For additional support and questions, please contact dataspaces@sci.utah.edu
### DataSpaces Releases:
In 2020, DataSpaces transitioned from the DART RPC and bulk transfer library to Mercury. This marked a transition to DataSpaces 2 (dspaces):
Development features (pending release – see master branch on GitHub repo:
  * Python bindings
  * Non-blocking version of dspaces_put()
  * Improved data subscription performance
  * Aries fabric support in dspaces
  * Improved scaling perfomance for dspaces_init()

**[2.1.x](https://github.com/rdi2dspaces/dspaces/archive/refs/tags/v2.1.1.tar.gz)** : Most recent release: March 2021
  * Add streaming metadata put/get interface
  * Add non-blocking data subscription with callbacks
  * Support building as a shared library
  * Add option to allocate data buffer inside dspaces_get()

**[2.0.x](https://github.com/rdi2dspaces/dspaces/archive/refs/tags/v2.0.0rc1.tar.gz)** : Most recent release (candidate): November 2020 (should not be used for new development)
  * Replace DART RPC layer with Mercury
  * Add subscription-based reads (superecedes locking for most use cases)
  * Enable hybrid server/client processes
  * Add experimental asynchronous data draining with index relocation

### Legacy DataSpaces 1.x Releases:
Development code can be found on the DataSpaces 1.x [Github Repo](https://github.com/rdi2dspaces/dataspaces) (no longer in active development and deprecated)
[**1.8.x**](https://github.com/rdi2dspaces/dataspaces/archive/refs/tags/v1.8.1.tar.gz) Most recent release: May 2019
  * Added new metadata support API calls (see header file for usage.)
  * Various bug fixes and performance improvements for InfiniBand transport.

[**1.7.x**](https://github.com/rdi2dspaces/dataspaces/archive/refs/tags/1.7.2.tar.gz) Most recent release: September 2018
  * Added lock type 3

  * Added DataSpaces-as-a-Service (DSaaS) functionality.
  * Added shared-memory based communication for collocated peers.
  * Various performance improvements and bug-fixes.
  * Deprecated and removed DCMF, Portals, and PAMI transport methods.

**[1.6.x](https://github.com/rdi2dspaces/dataspaces/archive/refs/tags/1.6.5.tar.gz)** Most recent release: June 2017
  * Added support for Cray Dynamic RDMA Credentials (DRC)
  * Supports Aries on Cray XC40 systems.
  * Necessary for NERSC’s Cori machine: use –enable-drc with configure
  * Improved support for IBM XL compiler

  * Added network support: Aries for Cray XC30.
  * Updated support for automake-1.12 and above.

  * Added network support: socket for TCP/IP.
  * Added feature: new data deleting API for removing data identified by version, from the staging area.

**Older Release notes for Posterity:**
**1.5.0** Released January 2015
  * Version checking for client/server compatibility.
  * Support for DIMES on InfiniBand.
  * A new set of examples.

**1.4.0** Released June 2014
  * Added network support: PAMI for IBM BlueGene/Q
  * Support for 64bit dimension sizes
  * Support for more than three dimensions

**1.3.0** Released December 2013
  * Optimized memory usage on server side for Gemini to overcome low RDMA memory constrains
  * Distributed client’s registration process, changed file locking mechanism on IB to reduce boot-up time
  * Parallelized DIMES get operation to improve data transfer performance
  * Unified interface for coupled writer/reader testing applications in C and Fortran

**1.2.0** Released May 2013
  * Added network support: DCMF for IBM BlueGene/P
  * Added feature: new data coupling APIs that allow point-to-point data transfers directly between tightly coupled processes by bypassing staging servers
  * Added coupled writer/reader testing applications in C
  * Single codebase for all supported networks

**1.1.0** Released November 2012
  * Added network support: Infiniband
  * Added support for sub-group lock/unlock using application defined MPI communicator

**1.0.0** Released July 2012
  * Network support: Portals for Cray XT series, Gemini for Cray XE/XK series

[](https://www.facebook.com/uusci)[](https://twitter.com/uusci)[](https://www.linkedin.com/groups/1131577/)
Copyright © 2019 - 2025 [Rutgers Discovery Informatics Institute](https://dataspaces.sci.utah.edu/ "Rutgers Discovery Informatics Institute ")
Scroll to Top

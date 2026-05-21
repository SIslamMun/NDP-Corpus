[ Skip to content](https://dataspaces.sci.utah.edu/manual/#content "Skip to content")
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

# Manual
By  [ paul  ](https://dataspaces.sci.utah.edu/author/paul/ "View all posts by paul") /  September 17, 2025 
## DataSpaces 2.x documention:
In progress, to be hosted at [dspaces.readthedocs.io](https://dspaces.readthedocs.io/)
## DataSpaces 1.x documentation (deprecated):
### Overview
DataSpaces is a programming system targeted at current large-scale systems and designed to support dynamic interaction and coordination between scientific applications. DataSpaces essentially provides a semantically specialized shared-space abstraction using a set of staging nodes. This abstraction derives from the tuple-space model and can be associatively accessed by the interacting applications of a simulation workflow. DataSpaces also provides services including distributed in-memory associative object store, scalable messaging, as well as runtime mapping and scheduling of online data analysis operations.
###    
Download and Install DataSpaces
DataSpaces can be downloaded from **[this page](https://dataspaces.sci.utah.edu/download)**. Currently, DataSpaces supports the following platforms: Cray Gemini, IBM DCMF, IBM PAMI and InfiniBand. You can follow these examples to configure DataSpaces on supported architecture. You will need to customize the configure command to your specific system configurations and programming environments
Untar source pre
```
    $ tar zxf dataspaces-1.3.0.tar.gz
    $ ./autogen.sh
```

Cray XE and XK series
####    
1. Setting up the protection domain to use.
Protection domain is a unique communication domain that all the applications in a job can connect to. While installing DataSpaces, a usable protection domain has to be created and used. After a protection domain has been created, a unique (ptag, cookie) pair will be given to define this unique domain. You may either use an existing system protection domain or create a user-defined one for your job.
To check exising usable protection domain information, please run:
```
$ apstat -P
```

You may see the following information.
```
PDomainID        TYPE    Uid        Ptag    Cookie
ADIOS          system      0         250     0x5420000
CCI          system      0         251     0x5430000
```

To create a user-defined protection domain, please run:
```
$ apmgr pdomain -c USER_DEFINED_DOMAIN_NAME 
```

You will see the following information while check usable protection domain information.
```
PDomainID            TYPE        Uid        Ptag    Cookie
ADIOS                system        0         250     0x5420000
CCI                system        0         251     0x5430000
USER_DEFINED_DOMAIN_NAME    user        6444         253    0xec6a0000
```

To release a user-defined protection domain, please run:
```
$ apmgr pdomain -r USER_DEFINED_DOMAIN_NAME 
```

*For more help, please look at man apmgr.
#### 2. Setting up DataSpaces by using <ptag, cookie=””””>pair.</ptag,>
There are two ways of setting <ptag, cookie=””””>pair of a protection domain to DataSpaces. (a) through environment variables; (b) through DataSpaces configuration</ptag,>
Through environment variable: please set environment variables DSPACES_GNI_PTAG and DSPACES_GNI_COOKIE in your job script by using corresponding values of <ptag, cookie=””””>pair. For example, if you are using exising system protection domain ADIOS, then you should set:</ptag,>
```
    export DSPACES_GNI_PTAG=250
    export DSPACES_GNI_COOKIE=0x5420000
```

Through DataSpaces configuration: please configure DataSpaces by using the following options
```
        --with-gni-ptag=ptag         decimal value
        --with-gni-ptag=cookie         hexa value
```

####    
3. Configure DataSpaces.
```
$ ./configure CC=cc FC=ftn
```

Infiniband cluster
```
$ ./configure CC=mpicc FC=mpif90
```

IBM BlueGene/P
```
$ ./configure CC=mpixlc FC=mpixlf90 CFLAGS="-g -O0 -qarch=450 -qtune=450" --with-dcmf="/bgsys/drivers/ppcfloor"
```

IBM BlueGene/Q
```
$ ./configure CC=/bgsys/drivers/ppcfloor/comm/xl/bin/mpixlc_r FC=/bgsys/drivers/ppcfloor/comm/xl/bin/mpixlf90 CFLAGS="-O0 -g -qlanglvl=extc99 -O3 -qarch=qp -qtune=qp -qfullpath"
```

If you have problems configuring and building DataSpaces, please refer to **[this FAQ](https://dataspaces.sci.utah.edu/faq)** or contact us directly.
###    
Building Application with DataSpaces
Let us look at an example of a simple but complete DataSpaces application workflow. In this workflow, there are 2 applications. A writer which puts data and a reader that gets data.
  * dataspaces_sever.c: DataSpaces staging server
  * put.c: Writer application
  * get.c: Reader application

Look inside put.c
```
/* put.c : Example 1: DataSpaces put tutorial 
 * This example will show you the simplest way 
 * to put a 1D array of 3 elements into the DataSpace.
 * */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include "dataspaces.h"
#include "mpi.h"

int main(int argc, char **argv)
{
        int err;
        int nprocs, rank;
        MPI_Comm gcomm;

        MPI_Init(&argc, &argv);
        MPI_Comm_size(MPI_COMM_WORLD, &nprocs);
        MPI_Comm_rank(MPI_COMM_WORLD, &rank);
        MPI_Barrier(MPI_COMM_WORLD);
        gcomm = MPI_COMM_WORLD;

        // Initalize DataSpaces
        // # of Peers, Application ID, ptr MPI comm, additional parameters
        // # Peers: Number of connecting clients to the DS server
        // Application ID: Unique idenitifier (integer) for application
        // Pointer to the MPI Communicator, allows DS Layer to use MPI barrier func
        // Addt'l parameters: Placeholder for future arguments, currently NULL.
        dspaces_init(1, 1, &gcomm, NULL);

        int timestep=0;

        while(timestep<10){
                timestep++;
                sleep(2);
                // DataSpaces: Lock Mechanism
                // Usage: Prevent other process from modifying 
                //        data at the same time as ours
                dspaces_lock_on_write("my_test_lock", &gcomm);

                //Name the Data that will be writen
                char var_name[128];
                sprintf(var_name, "ex1_sample_data");

                // Create integer array, size 3
                int *data = malloc(3*sizeof(int));

                // Initialize Random Number Generator
                srand(time(NULL));

                // Populate data array with random values from 0 to 99
                data[0] = rand()%100;
                data[1] = rand()%100;
                data[2] = rand()%100;

                printf("Timestep %d: put data %d %d %d\n",
                        timestep, data[0], data[1], data[2]);

                // ndim: Dimensions for application data domain
                // In this case, our data array is 1 dimensional
                int ndim = 1;

                // Prepare LOWER and UPPER bound dimensions
                // In this example, we will put all data into a 
                // small box at the origin upper bound = lower bound = (0,0,0)
                // In further examples, we will expand this concept.
                uint64_t lb[3] = {0}, ub[3] = {0};

                // DataSpaces: Put data array into the space
                // Usage: dspaces_put(Name of variable, version num, 
                // size (in bytes of each element), dimensions for bounding box,
                // lower bound coordinates, upper bound coordinates,
                // ptr to data buffer 
                dspaces_put(var_name, timestep, 3*sizeof(int), ndim, lb, ub, data);

                // DataSpaces: Release our lock on the data
                dspaces_unlock_on_write("my_test_lock", &gcomm);
        }

        // DataSpaces: Finalize and clean up DS process
        dspaces_finalize();

        MPI_Barrier(gcomm);
        MPI_Finalize;

        return 0;
}
```

Look inside get.c
```
/* get.c : Example 1: DataSpaces get tutorial
 *  This example will show you the simplest way 
 *  to get a 1D array of 3 elements out of the DataSpace
 *  and store it in a local variable.
 *  */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include "dataspaces.h"
#include "mpi.h"

int main(int argc, char **argv)
{
        int err;
        int nprocs, rank;
        MPI_Comm gcomm;

        MPI_Init(&argc, &argv);
        MPI_Comm_size(MPI_COMM_WORLD, &nprocs);
        MPI_Comm_rank(MPI_COMM_WORLD, &rank);
        MPI_Barrier(MPI_COMM_WORLD);
        gcomm = MPI_COMM_WORLD;

        // DataSpaces: Initalize and identify application
        // Usage: dspaces_init(num_peers, appid, Ptr to MPI comm, parameters)
        // Note: appid for get.c is 2 [for put.c, it was 1]
        dspaces_init(1, 2, &gcomm, NULL);

        int timestep=0;

        while(timestep<10){
                timestep++;

                // DataSpaces: Read-Lock Mechanism
                // Usage: Prevent other processies from changing the 
                //        data while we are working with it
                dspaces_lock_on_read("my_test_lock", &gcomm);

                // Name our data.
                char var_name[128];
                sprintf(var_name, "ex1_sample_data");

                // Create integer array, size 3
                // We will store the data we get out of the DataSpace
                // in this array.
                int *data = malloc(3*sizeof(int));

                // Define the dimensionality of the data to be received 
                int ndim = 1;

                // Prepare LOWER and UPPER bound dimensions
                uint64_t lb[3] = {0}, ub[3] = {0};

                // DataSpaces: Get data array from the space
                // Usage: dspaces_get(Name of variable, version num, 
                // size (in bytes of each element), dimensions for bounding box,
                // lower bound coordinates, upper bound coordinates,
                // ptr to data buffer 
                dspaces_get(var_name, timestep, 3*sizeof(int), ndim,
                            lb, ub, data);

                printf("Timestep %d: get data %d %d %d\n",
                        timestep, data[0], data[1], data[2]);

                // DataSpaces: Release our lock on the data
                dspaces_unlock_on_read("my_test_lock", &gcomm);
        }

        // DataSpaces: Finalize and clean up DS process
        dspaces_finalize();

        MPI_Barrier(gcomm);
        MPI_Finalize;

        return 0;
}
```

Before running DataSpaces staging servers, the user need to create a configuration file dataspaces.conf. Here is an example of a dataspaces.conf file. In this example, we specify a 3D domain with xyz size of 128x128x128. Ten versions of any variables is kept in the staging severs at anytime. Also, only one application can read the data at a time.
```
## Config file for DataSpaces

ndim = 3 
dims = 128,128,128

# 
max_versions = 10
max_readers = 1

# Lock type: 1 - generic, 2 - custom
lock_type = 2

# Hash function used to map the indexing of data domain to servers:
# 1 - Use Hilbert space-filling curve to linearize the data domain, decompose and 
#     map the linearized 1D domain to the servers.
# 2 - Decompose the data domain into 2^ceil(log(n)) regions where n is the number of
#     servers, and map them to the servers.   
hash_version = 1
```

There are two types of lock in DataSpaces.
  * Generic lock: With Generic lock, Producer will not wait for the data to be consumed by Consumer. It will progress at it own pace. Consumer may try to retrive data before the data is produced. It is user’s reponsibility to check whether the data is ready before reading it.
  * Custom lock: Custom lock is a Producer/Consumer type of lock. Consumer will block until Producer put or produce data. Producer will block until Consumber get or consume data. The process is repeated for the next time step.

The DataSpaces server executable has three command line options:
```
  --server, -s    number of server instance/staging nodes
  --cnodes, -c    number of compute nodes
  --conf, -f      path to the configuration file [Optional]
```

The following command runs 1 DataSpaces servers and 2 clients
```
$ ./dataspaces_server -s 1 -c 2
$ ./put
$ ./get 
```

You should see the following output
```
Output 
```

Please visit our **[FAQ page](https://dataspaces.sci.utah.edu/faq)** if you experience problems compiling and running DataSpaces.
[ FAQ ](https://dataspaces.sci.utah.edu/faq/ "FAQ")
[](https://www.facebook.com/uusci)[](https://twitter.com/uusci)[](https://www.linkedin.com/groups/1131577/)
Copyright © 2019 - 2025 [Rutgers Discovery Informatics Institute](https://dataspaces.sci.utah.edu/ "Rutgers Discovery Informatics Institute ")
Scroll to Top

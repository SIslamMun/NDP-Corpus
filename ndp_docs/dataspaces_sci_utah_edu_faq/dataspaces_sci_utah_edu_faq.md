[ Skip to content](https://dataspaces.sci.utah.edu/faq/#content "Skip to content")
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

# FAQ
By  [ paul  ](https://dataspaces.sci.utah.edu/author/paul/ "View all posts by paul") /  September 15, 2025 
For General Questions
**Question:** How to determine the number of servers for a specific application?  
**Answer:** The required number of servers is determined by the number of clients and the runtime data size. Please refer to the README file in the DataSpaces package for details.
**Question:** Is the application ID unique?  
**Answer:** Yes, that is the unique id to distinguish different applications.
**Question:** Is there any detailed documentation available that describe the usage/limitation of the system?  
**Answer:** You can refer to dataspaces.org, as well as documents in the DataSpaces package, such as README. DataSpaces tutorials are also available online for reference.
**Question:** Can DataSpaces support dynamic application join-in and departure?  
**Answer:** No, in the current version of DataSpaces, all applications should start with the server and cannot departure freely. However, DataSpaces will support such feature in the next release (currently under test, will release in two months). For example, you can start the server, then start one instance of 10 clients, then another instance of 30 clients later, and so on…
**Question:** Do I need to specify the number of clients at the start of the dataspaces servers?  
**Answer:** Yes, you have to give the number of clients in advance of the applications. And the number should match the number of clients in the application, because DataSpaces server will wait until all clients connect and register.
###    
For InfiniBand cluster
**Question:** After running configure, InfiniBand is not dected.  
``
```
Infiniband available.
    - INFINIBAND_CFLAGS =  
    - INFINIBAND_CPPFLAGS =  
    - INFINIBAND_LDFLAGS = 
    - INFINIBAND_LIBS =  -libverbs
```

**Answer:** You can force configure in InfiniBand cluster using -DHAVE_INFINIBAND flag and specify infiniband library and header direcotry. For example:
```
$ ./configure CC=mpicc FC=mpif90 CFLAGS="-DHAVE_INFINIBAND -L /opt/ofed/lib64/ -lrdmacm -I /opt/ofed/include/"
```

**Question:** I have the following Connection Route Error:
```
Connection Route Error peer# 0 (192.168.200.204)  to peer# 0 (192.168.200.204).
event is 3 with status -110.
'rpc_connect()': failed with -110.
rpc_connect err -110 in dc_boot.
'dc_boot()': failed with -110.
'dc_alloc()': failed with -110.
'dcg_alloc()': failed with -12.
common_dspaces_init(): failed to initialize.
```

**Answer:** You will need to incrase the default rdma operations timeout. Please reconfigure DataSpaces using –with-infiniband-timeout The default timeout is 100ms.
```
$ ./configure CC=mpicc FC=mpif90 --with-infiniband-timeout=300
```

**Question:** I get this error while running dataspaces_server.
```
rdma_bind_addr -1 in rpc_server_init.
'rpc_server_init()': failed with -1.
'ds_alloc()': failed with 0.
'dsg_alloc()': failed with 0.
```

**Answer:** Please run configure again, and specify the correct infiniband network interface. Please check ifconfig for the list of avaliable infiniband interfaces.
$ ./configure CC=mpicc FC=mpif90 –with-ib-interface=ib0
[Next  Manual ](https://dataspaces.sci.utah.edu/manual/ "Manual")
[](https://www.facebook.com/uusci)[](https://twitter.com/uusci)[](https://www.linkedin.com/groups/1131577/)
Copyright © 2019 - 2025 [Rutgers Discovery Informatics Institute](https://dataspaces.sci.utah.edu/ "Rutgers Discovery Informatics Institute ")
Scroll to Top

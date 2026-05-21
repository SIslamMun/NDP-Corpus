[Skip to content](https://scidx.sci.utah.edu/data-staging/#wp--skip-link--target)
[![](https://scidx.sci.utah.edu/wp-content/uploads/2024/12/ndp_logo.png)](https://nationaldataplatform.org) ![](https://scidx.sci.utah.edu/wp-content/uploads/2024/12/logo-sm.png)
National Data Platform's
# [Science Data Exchange](https://scidx.sci.utah.edu)
* * *
![](https://scidx.sci.utah.edu/wp-content/uploads/2024/12/nsf-logo-150x150.png)
  * [Architecture and Infrastructure](https://scidx.sci.utah.edu/software-architecture/)
  * [Data POPs](https://scidx.sci.utah.edu/data-pops/)
  * [Data Staging](https://scidx.sci.utah.edu/data-staging/)
  * [Data Streaming](https://scidx.sci.utah.edu/data-streaming/)
  * [Use Cases](https://scidx.sci.utah.edu/scidx-use-cases/)
    * [NOAA Data Staging](https://scidx.sci.utah.edu/noaa-data-staging/)
    * [SAGE Data Streaming](https://scidx.sci.utah.edu/sage-data-streaming/)
    * [EarthScope Data Streaming](https://scidx.sci.utah.edu/earthscope-data-streaming/)
    * [On-Demand Fakequakes](https://scidx.sci.utah.edu/on-demand-fakequakes/)
    * [USPTO: AI in Science Workflow](https://scidx.sci.utah.edu/uspto-ai-in-science-workflow/)

![](https://scidx.sci.utah.edu/wp-content/uploads/2024/12/AGU-Stock-Data-Globe-Illustration.jpg)
# Data Staging
SciDX enhances scientific computing workflows through advanced data staging services that optimize data access, preprocessing, and analysis. These services intelligently distribute data reduction, transformation, and analysis across multiple locations, all while considering system resources and user priorities. This approach enables efficient management of data in motion—through filtering, compression, and aggregation—to streamline workflows and minimize data transfer volume. 
Imagine performing ETL-like operations right at the data source, reducing transfer times and system overhead. SciDX makes it possible, allowing you to maximize the efficiency of cyberinfrastructure resources and focus more on deriving insights.
## Distributed Data Staging with DataSpaces
SciDX supports distributed data staging using the powerful [DataSpaces](https://dataspaces.sci.utah.edu/) data management framework. [DataSpaces](https://dataspaces.sci.utah.edu/) is a sophisticated programming system that facilitates dynamic coordination between scientific applications at large scales. It offers a specialized shared-space abstraction for efficient data sharing, bridging the gap between data producers and consumers seamlessly. 
Through [DataSpaces](https://dataspaces.sci.utah.edu/), SciDX provides robust services, including a distributed in-memory associative object store, scalable messaging, and efficient scheduling of data analysis operations. Whether it’s mapping compute jobs to data sources, managing data from cloud storage, or integrating live inputs from scientific instruments, SciDX’s use of [DataSpaces](https://dataspaces.sci.utah.edu/) ensures a seamless interaction among distributed data components.
![](https://scidx.sci.utah.edu/wp-content/uploads/2024/12/Picture7-1024x513.jpg)
## Geographically Distributed Deployments for Converged Data Fabric 
SciDX leverages geographically dispersed deployments to establish a unified data fabric that supports distributed collection and analysis, all coordinated through a centralized directory of data sources. This infrastructure facilitates the efficient integration of diverse data sets, enabling the creation and delivery of valuable data products to users. SciDX’s data staging services take into account system resources, permissions, and user objectives to ensure the most efficient and effective data management solutions for your research needs. 
Discover how SciDX transforms your scientific computing workflows by making data staging efficient, distributed, and ready for the challenges of modern science.
## Optimizing Data Movement for GPU-Based In-Situ Workflow
**Background & Motivation**
  * GPUs are widely adopted by modern HPC clusters and many scientific simulations and analyses have been ported to GPUs.
  * Porting existing in-situ workflow to GPUs is an ongoing effort.
  * Intra-Application GPU communications, e.g. MPI, has leveraged GPUDirect RDMA for I/O optimization.
  * SHAW-Vis Workflow (SNL)

**Scientific Achievement**
We created Dataspaces-GPU, an extension to existing CPU data staging middleware that supports interapplication I/O from/to GPU memory and optimized it by leveraging GPUDirect RDMA (GDR). 
**Significance and Impact**
Dataspaces-GPU works as an interoperable I/O abstraction that reduces the software refactoring cost in the workflow porting process and improves the I/O performance for GPU components. 
**Technical Approach**
  * Apply GDR at both the sender & receiver side.
  * Design a GPU kernel and utilize concurrent kernel launch for data object reassembly
  * R-pulser (link to R-pulser) Streaming now

The National Data Platform and SciDX was funded by [NSF 2333609](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2333609) under CI, CISE Research Resources programs. Any opinions, findings, conclusions, or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the funders.
![](https://scidx.sci.utah.edu/wp-content/uploads/2024/12/sci24-white.png)
72 Central Campus Drive  
SALT LAKE CITY, UT 84112
801-585-1867
  * [Architecture and Infrastructure](https://scidx.sci.utah.edu/software-architecture/)
  * [Data POPs](https://scidx.sci.utah.edu/data-pops/)
  * [Data Staging](https://scidx.sci.utah.edu/data-staging/)
  * [Data Streaming](https://scidx.sci.utah.edu/data-streaming/)
  * [Use Cases](https://scidx.sci.utah.edu/scidx-use-cases/)
    * [NOAA Data Staging](https://scidx.sci.utah.edu/noaa-data-staging/)
    * [SAGE Data Streaming](https://scidx.sci.utah.edu/sage-data-streaming/)
    * [EarthScope Data Streaming](https://scidx.sci.utah.edu/earthscope-data-streaming/)
    * [On-Demand Fakequakes](https://scidx.sci.utah.edu/on-demand-fakequakes/)
    * [USPTO: AI in Science Workflow](https://scidx.sci.utah.edu/uspto-ai-in-science-workflow/)

[SCI Institute](https://www.sci.utah.edu/)
[National Data Platform](https://nationaldataplatform.org/)

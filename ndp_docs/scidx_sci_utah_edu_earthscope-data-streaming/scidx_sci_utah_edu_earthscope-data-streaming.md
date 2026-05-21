[Skip to content](https://scidx.sci.utah.edu/earthscope-data-streaming/#wp--skip-link--target)
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
# EarthScope Data Streaming
## Overview
The EarthScope Consortium ([www.earthscope.org](https://www.earthscope.org/)) streams three-dimensional Global Navigation Satellite System (GNSS) high rate (1hz) position time series from nearly a thousand EarthScope and related GNSS stations. These high precision ground-motion time series are used to study a range of geophysical phenomena including earthquakes, volcanos, tsunamis, hydrologic loads, and glaciers. EarthScope is dedicated to supporting transformative global geophysical research and education through operation of the National Science Foundation’s (NSF) Geodetic GAGE and Seismic SAGE facilities. As part of the National Data Platform (NDP) EarthScope pilot project, the EarthScope GNSS position time series streams are being stored and made available from Data Collaboratory Kafka servers at the University of Utah. This use cases demonstrates tools for access and plotting of sample real time streams and is the foundation for additional services being developed that will facilitate time series analysis including machine learning.
[ Explore the Jupyter Notebook demo for a detailed walkthrough ](https://github.com/national-data-platform/jupyter-notebooks/blob/main/streaming/demo-1-earthscope.ipynb)
## Objective
This use case demonstrate how users can access an process EarthScope’s data streams using SciDx. These data can be processed in real time, or for previous time intervals. 
## Key Features
  * SciDx [data streaming](https://scidx.sci.utah.edu/data-streaming/)
  * Real time data analysis
  * Data set registration

![Flowchart showing how SciDx users can connect to Earthscope streams.](https://scidx.sci.utah.edu/wp-content/uploads/2024/12/earthscope_demo-1024x344.png)
## Challenges
  * High temporal resolution makes downloading all data expensive and impractical
  * Existing data compilations are difficult to find and use
  * Connecting to existing data streams 

## Alignment with NDP
Datasets compiled from EarthScope data, including ongoing data streams, can be registered, shared, and access through NDP’s data POPs. SciDx streaming builds on these data POPs to offer continuous streaming and advanced filtering and data processing. 
## Collaborators
This use case highlights collaboration between the University of Utah, EarthScope Consortium ([www.earthscope.org](http://www.earthscope.org)), and the NSF.
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

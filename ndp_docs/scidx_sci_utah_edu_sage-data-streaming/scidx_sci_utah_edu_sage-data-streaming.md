[Skip to content](https://scidx.sci.utah.edu/sage-data-streaming/#wp--skip-link--target)
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
# SAGE Data Streaming
## Overview
The SAGE cyberinfrastructure ([www.sageplatform.org](http://www.sageplatform.org)) is an advanced software-defined sensor network designed to leverage AI at the edge for real-time data collection and analysis in IoT environments. SAGE supports transformative research by enabling edge-based processing of high-resolution data from diverse sensors, including cameras, air quality monitors, and LIDAR systems. This capability is vital for applications such as environmental monitoring, wildlife tracking, and urban analytics.
As part of the National Data Platform (NDP) initiative, SAGE integrates seamlessly into a robust workflow for data processing and dissemination.
![](https://scidx.sci.utah.edu/wp-content/uploads/2024/12/schema-1024x467.png)
The architecture, illustrated in the figure above, highlights the collaboration of several key components:
  1. **SAGE** : Collects and processes data at the edge, exposing an API for data retrieval
  2. **Data Stream Adapter** : Connects SAGE with the [R-Pulsar Framework](https://rpulsar.sci.utah.edu/), converting data into formats suitable for real-time analysis
  3. **R-Pulsar Framework** : Extends cloud capabilities to IoT devices, enabling local data analysis, decision-making, and transformation in real time
  4. **Data Sink Adapter** : Routes processed data to its destination, such as OSDF Origin, for further use or storage
  5. **Metadata Catalog** : Logs metadata throughout the workflow to ensure data traceability and management
  6. **User & OSDF Origin**: End-users access or subscribe to data streams, while OSDF Origin serves as a repository or platform for processed data.

[ Explore the Jupyter Notebook demo for a detailed walkthrough ](https://github.com/national-data-platform/jupyter-notebooks/blob/main/streaming/demo-2-sage.ipynb)
## Objective
To create a cutting-edge cyberinfrastructure that harnesses artificial intelligence and edge computing to enable real-time data analysis and decision-making. By deploying a network of smart sensors and integrating advanced machine learning, SAGE aims to provide scientists with powerful tools to monitor, understand, and respond to environmental and societal phenomena with unprecedented speed and precision.
## Key Features
  * SciDx [data streaming](https://scidx.sci.utah.edu/data-streaming/)
  * Real time data analysis
  * Data set registration

## Collaborators
This use case highlights collaboration between the University of Utah, Sage Continuum (<https://sagecontinuum.org/>), and the NSF.
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

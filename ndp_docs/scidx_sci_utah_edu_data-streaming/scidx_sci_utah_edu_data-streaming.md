[Skip to content](https://scidx.sci.utah.edu/data-streaming/#wp--skip-link--target)
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
# Data Streaming
## How Streaming Works in SciDX:
![](https://scidx.sci.utah.edu/wp-content/uploads/2024/12/Picture8-1024x341.jpg)
### Step 1: Register Data Sources
SciDX makes it easy to integrate various data sources, including: 
  * Kafka topics
  * URL-based resources like CSV, JSON, TXT, and NetCDF files

When registering a data source, you can specify:
  * Resource Names: Give each source a meaningful identifier.
  * URLs: The location of each resource.
  * File Types: Supported formats (CSV, JSON, TXT, NetCDF).
  * Metadata and Processing Configurations: Optional settings to specify fields and apply processing.

**Mapping** : Choose specific fields to include in your streams, renaming them as needed. If no mapping is specified, all fields are included by default. 
**Processing** : Customize how the data is handled. If left unspecified, SciDX automatically optimizes settings based on the data type, streamlining configuration.
### Step 2: Create Kafka Streams
Once your data sources are registered, you can generate Kafka streams tailored to your needs by
  * **Combining Data Sources:** Merge data from multiple registered sources.
  * **Applying Filters:** Refine streams to include only the information that matters.

SciDX ensures efficient resource management, automatically closing inactive streams and scaling consumers dynamically to save resources. 
### Step 3: Filtering and Data Management
SciDX provides powerful filtering capabilities to manage and refine your data streams based on specific conditions. 
**Filtering Options:**
  * **Column Comparisons:** Compare values across different columns.
  * **Mathematical Operations:** Use mathematical expressions to set filter rules.
  * **Nested Values:** Handle complex, nested data structures such as arrays.
  * **Conditional Logic:** Implement IF-THEN-ELSE workflows to manage data based on dynamic conditions.
  * **Logical Operators:** Use AND/OR operators for compound filters. (Support for parentheses-based conditions is coming soon!)

**Upcoming Feature** : **Window-Based Filtering** Soon, SciDX will support window-based filtering, enabling moving averages, event-based windowing, and other advanced operations, adding a new layer of precision to real-time data processing. 
**Smart Stream Management and Resource Optimization**
Efficiently managing resources is a core feature of SciDX. The platform ensures optimal utilization by:
  * **Closing Idle Consumers:** When consumers are idle, they are closed to prevent unnecessary resource use.
  * **Stopping Unused Streams:** If a stream has no data left to send, it is stopped automatically.

These features lay the groundwork for a fully adaptable, resource-efficient platform that meets the evolving needs of your data workflows. 
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

# jupyter-notebooks


### NASA_ORIGIN/NASA Catalog.ipynb (842,697 bytes)

# NASA Catalog


<div style="display: flex; justify-content: space-between; align-items: flex-start;">
    <div style="flex: 0 0 auto; margin-bottom: 0; margin-top: 10px;">
        <img src="https://www.goes-r.gov/imagesContent/multimedia/goesSeriesLogos/GOES_U_revised/FullColor/GOES-U_logo_small.jpg" alt="NOAA Logo" width="150"/>
    </div>
    <div style="flex: 0 0 auto; margin-left: auto; margin-bottom: 0;">
        <img src="https://www.sci.utah.edu/images/news/2023/sci-30-multi.jpg" alt="Scientific Computing and Imaging Institute Logo" width="100"/>
    </div>
</div>

<h1 style="text-align: center; margin-top: 0;">NOAA Geostationary Operational Environmental Satellites (GOES)</h1>

<h3 style="text-align: center; margin-top: 0;">Real-time Data Streaming and Analysis</h3>

<p style="text-align: center;">NOAA's GOES program plays a critical role in monitoring weather, climate, and environmental phenomena across the Western Hemisphere. The advanced capabilities of the GOES satellites enable real-time data streaming and analysis, providing invaluable information for meteorologists, climate scientists, and emergency response teams.</p>

<div>
    <p>The Geostationary Operational Environmental Satellites (GOES) operated by NOAA are essential for continuous observation of atmospheric conditions, severe weather events, and environmental changes. The GOES satellites provide high-resolution imagery and atmospheric measurements, which are crucial for accurate weather forecasting, climate monitoring, and disaster management. Their geostationary position allows them to monitor the same area continuously, providing real-time data that is vital for tracking the development and movement of storms, hurricanes, and other weather phenomena.</p>
</div>
<div>
    <p> This project focuses on harnessing the real-time data streaming and analysis capabilities of the NOAA GOES satellites. By leveraging advanced data processing techniques and state-of-the-art analytical tools, the project aims to enhance our understanding of weather patterns and environmental changes. This initiative not only supports scientific research but also contributes to public safety by improving the accuracy and timeliness of weather predictions and alerts. The collaboration with the Scientific Computing and Imaging Institute at the University of Utah ensures the integration of cutting-edge computational methods to optimize the use of GOES data for various applications.
    </p>
</div>

<center>
    <div style="text-align: right; padding: 5px;">
        <p style="text-align: right;"><strong>Contact:</strong> Saleem Al-Harir, Systems Engineer, Scientific Computing and Imaging Institute, University of Utah (<a href="mailto:saleem.alharir@utah.edu">saleem.alharir@utah.edu</a>)</p>
    </div>
</center>

<div style="flex: 0 0 auto; margin-right: 0; margin-bottom: 0;">
    <p style="margin-left: 10px; font-size: 10px; margin-top: 10px;">The NOAA GOES project is supported by the National Oceanic and Atmospheric Administration (NOAA). Any opinions, findings, conclusions, or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of NOAA.</p>
</div>

<hr>

## 1. Import and Search for Matching Datasets

In this step, we import the `get_matching_datasets` function from the `nasapy` module. We define the CKAN instance URL and the specific dataset title to search for. The function `get_matching_datasets` retrieves the specified dataset and prints details of datasets that have the same observation start time.

```python
from nasapy import get_matching_datasets

catalog = 'https://ckan.geosciframe.org:8443'
specific_dataset_title = 'OR_ABI-L1b-RadC-M6C01_G18_s20231330001191_e20231330003569_c20231330004026.nc'
get_matching_datasets(catalog, specific_dataset_title)

```python
# example_usage.py

from nasapy import get_matching_datasets

# Define the CKAN instance URL
catalog = 'https://ckan.geosciframe.org:8443'

# Define the specific dataset title to search for
specific_dataset_title = 'OR_ABI-L1b-RadC-M6C01_G18_s20231330001191_e20231330003569_c20231330004026.nc'

# Call the function to get and print matching datasets
get_matching_datasets(catalog, specific_dataset_title)
```



## 2. Filter Datasets by Time Range

We use the `print_filtered_datasets` function to filter datasets within a user-specified time range. This function searches the CKAN instance for datasets and prints details of those that fall within the provided start and end times.

```python
from datetime import datetime
from nasapy import print_filtered_datasets

catalog = 'https://ckan.geosciframe.org:8443'

# First filter attempt (expected to return no results)
user_start_time = datetime(2023, 5, 13, 0, 0, 0)
user_end_time = datetime(2023, 5, 13, 0, 1, 0)
print_filtered_datasets(catalog, user_start_time, user_end_time, query='nasa', rows=1000)

# Second filter attempt (expected to return some results)
user_start_time = datetime(2023, 5, 13, 0, 0, 0)
user_end_time = datetime(2023, 5, 13, 0, 5, 0)
print_filtered_datasets(catalog, user_start_time, user_end_time, query='nasa', rows=1000)

```python
# example_usage.py

from datetime import datetime
from nasapy import print_filtered_datasets

# Define the CKAN instance URL
catalog = 'https://ckan.geosciframe.org:8443'

# Example 1: Filter datasets by time range and print details will return nothing since there are no datasets in the time range
user_start_time = datetime(2023, 5, 13, 0, 0, 0)
user_end_time = datetime(2023, 5, 13, 0, 1, 0)
print("\nFiltering datasets by time range...", user_start_time, user_end_time, "\n")
print_filtered_datasets(catalog, user_start_time, user_end_time, query='nasa', rows=1000)
# Example 2: Filter datasets by time range and print details
user_start_time = datetime(2023, 5, 13, 0, 0, 0)
user_end_time = datetime(2023, 5, 13, 0, 5, 0)
print("\nFiltering datasets by time range...", user_start_time, user_end_time, "\n")
print_filtered_datasets(catalog, user_start_time, user_end_time, query='nasa', rows=1000)
```



## 3. Download Matching Files

Here, we use the `download_matching_files` function to download files that match the specified dataset's observation start time. The function checks for RADC and FDCC files and downloads them from either a Pelican origin link or an S3 link, saving them to the specified download directory.

```python
from nasapy import download_matching_files

download_directory = ''
radc_path, fdcc_path = download_matching_files(catalog, specific_dataset_title, download_directory)
print(f"RADC file downloaded to: {radc_path}")
print(f"FDCC file downloaded to: {fdcc_path}")

```python
from nasapy import download_matching_files
import os

# Get the current working directory
download_directory = os.getcwd()

# Example 3: Download matching files
print("\nDownloading matching files...\n")
radc_path, fdcc_path = download_matching_files(catalog, specific_dataset_title, download_directory)

# Print the paths of the downloaded files
print(f"RADC file downloaded to: {radc_path}")
print(f"FDCC file downloaded to: {fdcc_path}")
```



## 4. Visualize the Data

In this final step, we load the downloaded RADC and FDCC files using the `xarray` library. We convert radiance data to reflectance, apply gamma adjustment, and create a mask for fire pixels. We then visualize the gamma-adjusted reflectance data with a fire detection overlay using `matplotlib`.

```python
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt

Esun_Ch_02 = 663.274497
d2 = 0.3

ds_fdcc = xr.open_dataset(fdcc_path)
ds_radc = xr.open_dataset(radc_path)
radiance = np.array(ds_radc['Rad'])
mask = np.array(ds_fdcc['Mask'])

ref = (radiance * np.pi * d2) / Esun_Ch_02
ref = np.maximum(ref, 0.0)
ref = np.minimum(ref, 1.0)
ref_gamma = np.sqrt(ref)

fire_pixels = np.zeros(radiance.shape)
for i in range(len(mask)):
    for j in range(len(mask[i])):
        if mask[i][j] == 30:
            idx = (slice(2*i, 2*i+40), slice(2*j, 2*j+40))
            fire_pixels[idx] = 0.7
fire_pixels = np.ma.masked_where(fire_pixels == 0, fire_pixels)

fig, ax = plt.subplots(figsize=(10, 10), dpi=200)
im = ax.imshow(ref_gamma, vmin=0.0, vmax=1.0, cmap='Greys_r')
im2 = ax.imshow(fire_pixels, vmin=0.0, vmax=1.0, cmap='Reds', alpha=0.6)
cb = fig.colorbar(im, orientation='horizontal', ax=ax)
cb.set_ticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
cb.set_label('Reflectance')
plt.title("Radiance with Fire Detection Overlay")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()

```python
import os
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt

# Constants needed for the conversion
Esun_Ch_02 = 663.274497
d2 = 0.3


print(f"Loading files: {radc_path} and {fdcc_path}")

try:
    # Load datasets
    ds_fdcc = xr.open_dataset(fdcc_path)
    ds_radc = xr.open_dataset(radc_path)
    
    # Extract data from datasets
    radiance = np.array(ds_radc['Rad'])
    mask = np.array(ds_fdcc['Mask'])
    
    # Apply the formula to convert radiance to reflectance
    ref = (radiance * np.pi * d2) / Esun_Ch_02

    # Make sure all data is in the valid data range
    ref = np.maximum(ref, 0.0)
    ref = np.minimum(ref, 1.0)

    # Apply the formula to adjust reflectance gamma
    ref_gamma = np.sqrt(ref)
    
    # Create a mask for fire pixels
    fire_pixels = np.zeros(radiance.shape)
    for i in range(len(mask)):
        for j in range(len(mask[i])):
            if mask[i][j] == 30:
                idx = (slice(2*i, 2*i+40), slice(2*j, 2*j+40))
                fire_pixels[idx] = 0.7
    fire_pixels = np.ma.masked_where(fire_pixels == 0, fire_pixels)

    # Plot gamma adjusted reflectance with fire detection overlay
    fig, ax = plt.subplots(figsize=(10, 10), dpi=200)
    im = ax.imshow(ref_gamma, vmin=0.0, vmax=1.0, cmap='Greys_r')
    im2 = ax.imshow(fire_pixels, vmin=0.0, vmax=1.0, cmap='Reds', alpha=0.6)
    cb = fig.colorbar(im, orientation='horizontal', ax=ax)
    cb.set_ticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
    cb.set_label('Reflectance')
    plt.title("Radiance with Fire Detection Overlay")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.show()
except Exception as e:
    print(f"Error plotting the file: {str(e)}")
```


### README.md (7,040 bytes)

# NDP Pre-Built JupyterHub Images

***
### Minimal NDP Starter Jupyter Lab
Minimal image with no additional content provided.

***
### NDP Catalog Search
Minimal image with a notebook describing how to search programatically in the NDP catalog.

***
### Physics Guided Machine Learning Starter Code
Next-generation fire models provide the basis to understand fire physics in detail, leading the way for emulators to model potential fire behavior. The Physics Guided Machine Learning (PGML) project uses data from hundreds of coupled fire-atmosphere simulations produced by a physics-based coupled fire-atmospheric modeling model (QUIC-Fire) to develop a reduced-order emulator. Such an emulator can be used to predict the wildfire spread, which can help the fire agencies take necessary steps to reduce the damage. Additionally, the predictions can be utilized to mitigate the risk of controlled fires escalating into wildfires.

This dataset was generated particularly for the Physics Guided Machine Learning (PGML) research and educational tasks. It is an ensemble of prescribed fire simulations generated by the QUIC-Fire coupled fire-atmospheric modeling tool. Each simulation run is represented by a Zarr file, containing the outputs created by QUIC-Fire through the BurnPro3D web interface. To model a burn, users upload the polygon for their burn unit and BurnPro3D uses a 3D fuels model for that location created by FastFuels and an ignition file with a user-defined ignition pattern created in DripTorch. Those files are included here as well. In addition, users define the environmental conditions they would like to model in terms of fuel moisture, wind direction, and wind speed.

***
### SAGE Pilot Streaming Data Starter Code
Streaming Data from SAGE Pilot

***
### EarthScope Consortium Streaming Data Starter Code
The EarthScope Consortium (www.earthscope.org) streams three-dimensional Global Navigation Satellite System (GNSS) high rate (1hz) position time series from nearly a thousand EarthScope and related GNSS stations. These high precision ground-motion time series are used to study a range of geophysical phenomena including earthquakes, volcanos, tsunamis, hydrologic loads, and glaciers. EarthScope is dedicated to supporting transformative global geophysical research and education through operation of the National Science Foundation’s (NSF) Geodetic GAGE and Seismic SAGE facilities. As part of the National Data Platform (NDP) EarthScope pilot project, the EarthScope GNSS position time series streams are being stored and made available from Data Collaboratory Kafka servers at the University of Utah. This Jupyter Notebook provides tools for access and plotting of sample real time streams and is the foundation for additional services being developed that will facilitate time series analysis including machine learning.

***
### NAIRR Pilot - NASA Harmonized Landsat Sentinel-2 (HLS) Starter Code
The Harmonized Landsat and Sentinel-2 (HLS) project is a NASA initiative aiming to produce a seamless surface reflectance record from the Operational Land Imager (OLI) and Multi-Spectral Instrument (MSI) aboard Landsat-8/9 and Sentinel-2A/B remote sensing satellites, respectively.

As part of collection of the collection of resources of the NAIRR Pilot, NASA in partnership with IBM has developed Prithvi-100M, a temporal Vision transformer pre-trained on contiguous HLS data There are 3 examples of finetuning the model for image segmentation using the mmsegmentation library available through HuggingFace: burn scars segmentation, flood mapping, and multi temporal crop classification, with the code used for the experiments available on GitHub.

***
### LLM Training
An LLM, or Large Language Model, is a type of artificial intelligence designed to understand and generate human-like text based on the data it’s been trained on. By adding a vast amount of text from different sources and context’s (web, books, papers, among others) LLM’s are capable to identify the patterns of the human language under different contexts and provide responses to complex questions.

LLM’s posses a huge potential in both research and education, given their capability to quickly process and summarize a vast amount of information. LLM’s can bee seen as a powerful tool to accelerate learning, facilitate the sharing of knowledge, process and generate big amounts of data, generate new hypothesis questions, among other uses.

This image can be used to serve and train LLM with FastChat.

***
### LLM Service Client
This image can be used to query existing LLM deployment.

***
### TLS Fuel-Size Segmentation 2023
The increasing potential for catastrophic wildfires due to climate change and overstocked forests has resulted in increased loss of life, property damage, and ecological damage, particularly in the western U.S. One potential solution is to implement fuel treatments to manage overstocked forests and reduce the potential for wildfire and its severity. Choosing the optimal fuel treatment strategy is critical, and new 3D fire modeling tools are available to help determine the best strategy. Simply put, we need to know the vegetation characteristics within the fire environment to understand what contributes to increased wildfire risk and what needs to be removed.  

In addition, the development of these tools requires access to high-quality data, computational resources, and AI workflows that are essential for generating new knowledge and refining strategies.  

Given that labeled vegetation fuels are a crucial input to fire models, this demo project aims to model the classification of vegetation fuels by effectively segmenting them by category (live and dead) and size class.

***
### NOAA-GOES Analysis
The Geostationary Operational Environmental Satellites (GOES) operated by NOAA are essential for continuous observation of atmospheric conditions, severe weather events, and environmental changes. The GOES satellites provide high-resolution imagery and atmospheric measurements, which are crucial for accurate weather forecasting, climate monitoring, and disaster management. Their geostationary position allows them to monitor the same area continuously, providing real-time data that is vital for tracking the development and movement of storms, hurricanes, and other weather phenomena.

This project focuses on harnessing the real-time data streaming and analysis capabilities of the NOAA GOES satellites. By leveraging advanced data processing techniques and state-of-the-art analytical tools, the project aims to enhance our understanding of weather patterns and environmental changes. This initiative not only supports scientific research but also contributes to public safety by improving the accuracy and timeliness of weather predictions and alerts. The collaboration with the Scientific Computing and Imaging Institute at the University of Utah ensures the integration of cutting-edge computational methods to optimize the use of GOES data for various applications.


### earthscope/final_earthscop.ipynb (10,718 bytes)

# final_earthscop


<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
    <img src="earthscope.png" alt="EarthScope Consortium Logo" style="width: 415px;height: 121px; margin-top: 10px;">
    <div style="flex: 0 0 auto; margin-left: auto; margin-bottom: 0;">
        <img src="https://www.sci.utah.edu/images/news/2023/sci-30-multi.jpg" alt="Scientific Computing and Imaging Institute Logo" width="150"/>
    </div>
</div>

<div style="text-align: center;">
    <h1>NSF National Data Platform (NDP)</h1>
    <h2>Streaming Data from EarthScope Consortium</h2>
</div>

The EarthScope Consortium ([www.earthscope.org](https://www.earthscope.org)) streams three-dimensional Global Navigation Satellite System (GNSS) high rate (1hz) position time series from nearly a thousand EarthScope and related GNSS stations. These high precision ground-motion time series are used to study a range of geophysical phenomena including earthquakes, volcanos, tsunamis, hydrologic loads, and glaciers. EarthScope is dedicated to supporting transformative global geophysical research and education through operation of the National Science Foundation’s (NSF) Geodetic GAGE and Seismic SAGE facilities. As part of the National Data Platform (NDP) EarthScope pilot project, the EarthScope GNSS position time series streams are being stored and made available from Data Collaboratory Kafka servers at the University of Utah. This Jupyter Notebook provides tools for access and plotting of sample real time streams and is the foundation for additional services being developed that will facilitate time series analysis including machine learning. 

#### Users of EarthScope data agree to follow the [EarthScope streaming data policy](https://www.unavco.org/data/policies_forms/data-policy/data-policy-realtime-streaming-gps/data-policy-realtime-streaming-gps.html).

---
<div style="text-align: right; padding: 5px;">
    <p><strong>Contact:</strong> Scientific and Computing Imaging Institute, University of Utah (<a href="mailto:saleem.alharir@utah.edu">saleem.alharir@utah.edu</a>)</p>
</div>

<div style="display: flex; align-items: center; justify-content: flex-start; margin-top: 20px; border-top: 1px solid #ccc; padding-top: 20px;">
    <img src="https://new.nsf.gov/themes/custom/nsf_theme/components/images/logo/logo-desktop.svg" alt="NSF Logo" style="width: 120px; margin-right: 10px;">
    <p style="font-size: 12px;">The National Data Platform was funded by NSF 2333609 under CI, CISE Research Resources programs. Any opinions, findings, conclusions, or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the funders.</p>
</div>

---

This step provides an example of retrieving a streaming dataset, specifying the dataset name with an EarthScope “SNCL” code. For example, "csci_ci_ly__20". The location of the GNSS station corresponding to the SNCL code is plotted on an interactive map.

**SNCL Code Breakdown:**
- `csci`: GNSS station 4-character ID.
- `ci`: Network code indicating Caltech.
- Other sources include `pb` for NOTA/EarthScope, `bk` for U.C. Berkeley, and `pw` for CWU.
- `ly_`: Common for all GNSS streams.
- Last two integers: Processing Package followed by Solution Type.

**Processing Package and Solution Type:**
- There can be more than one processing stream from each GNSS station as indicated by the following processing package and solution type codes.
- Packages used include the CWU server Fastlane (0), Trimble server PIVOT/RTX (1),RTNet server (2), Septentrio on-board (3), Trimble RTX on board (4),and Network solution combining RTNet's RTK and PPPAR, and Trimble RT data (5).
- Solution Types include PPP/AR (0), DIF/RTK (1), PPP/AR COMPLETE (2) and PPP/AR FAST+COMPLETE (3).

```python
from ndpearthscope import process_datasets, plot_station_location
from IPython.display import display 

# Define the list of dataset names you wish to process
dataset_names = ["csci_ci_ly__201"]  # Replace these with actual dataset names

# Process the datasets
datasets_details = process_datasets(dataset_names)

# Initialize an empty list to store file paths
file_paths = []
# Example: Plotting the location of the first dataset
if datasets_details:  # Check if the list is not empty
    first_dataset_details = datasets_details[0]
    latitude = first_dataset_details['latitude']
    longitude = first_dataset_details['longitude']
    station_name = first_dataset_details['dataset_name']
    bootstrap_server = first_dataset_details['bootstrap_server']
    topic = first_dataset_details['topic']
    file_path = first_dataset_details['file_path']
    # Save the file path for later use
    file_paths.append(file_path)   
    # Save the file path for later use
    file_paths.append(file_path)
    # Plot and display the station location in one line
    station_map = plot_station_location(latitude, longitude, station_name)
    display(station_map)
```

## Anomaly Detection in GPS Data

This phase of the analysis involves leveraging a subset of the collected GPS data to identify potential anomalies. Here's what happens:

- **Data Subset**: Utilizes the first 10,000 rows from the downloaded 1Hz dataset.
- **File Path**: `File_path` should be specified as the path to your dataset, which is assumed to be located in the same directory as this notebook.
- **Anomaly Detection**: Implements a One-Class SVM (Support Vector Machine) Anomaly Detection algorithm. This sophisticated technique is designed to detect and highlight outliers within the dataset.
- **Visualization**: Outliers identified by the algorithm are distinctly marked in red on the plot, making it easier to spot any anomalies in the GPS data.

This approach not only facilitates the early detection of irregularities but also aids in understanding the data's underlying patterns and integrity.

---

```python
from ndpearthscope import detect_and_visualize_anomalies
nrows = 10000
nu = 0.01
detect_and_visualize_anomalies(file_path,nrows,nu)
```

## Real-Time Data Streaming and Visualization

This section establishes a connection to the Data Collaboratory Kafka server by creating a Kafka Consumer. It focuses on visualizing geospatial data in real-time, particularly:

- **Three components of displacement** are plotted in real-time.
- **Time Frame**: The visualization covers the last 60 seconds of data.

To control the data flow and visualization, utilize the **Jupyter notebook stop button** to halt the plotting process as needed.

This real-time data streaming and visualization provide valuable insights into the dynamic changes occurring in the monitored geophysical phenomena, facilitating immediate analysis and decision-making.

---

```python
from ndpearthscope import consume_and_plot_kafka_data
consume_and_plot_kafka_data(topic, bootstrap_server)
```

## 3D Real-time GPS Data Visualization

In this segment, we establish a Kafka Consumer to interface with our streaming data infrastructure. This setup enables:

- **3D Visualization**: Leveraging real-time GPS data to render dynamic three-dimensional plots.
- **Interactivity**: Users can initiate or halt the data visualization process at any time using the **Jupyter notebook stop button**.

This approach allows for an immersive exploration of GPS data, providing an intuitive understanding of spatial dynamics as they unfold in real-time.

---

```python
from ndpearthscope import consume_and_plot_kafka_data_3d
consume_and_plot_kafka_data_3d(topic, bootstrap_server)
```


### earthscope/time_query.ipynb (742,841 bytes)

# time_query


**Import Modules**

```python
from scidx.client import sciDXClient, TimeDirection
import numpy as np
import matplotlib.pyplot as plt
```

**API Socket and Credentials**

```python
api_url="https://dataspaces.ndp.utah.edu/pop"
```

**Establish server connection**

```python
# Initialize the client
client = sciDXClient(api_url)
```

**Search Parameters** - parameters that identify the resource or resources being staged. The user provides a `source` dataset (the RadC dataset for the GOES-18 satellite, in this case), a nearest `timestamp` and a direction in time to search (i.e. the nearest available data to `timestamp` in the `PAST` or `FUTURE`).

```python
source = 'goes18-radc'
timestamp = '2024-08-02T00:35:00'
time_direction = TimeDirection.PAST
```

**Subsetting Parameters** - parameters that guide the server-side subsetting of matching data. In this case, the user gives a `var_name`, which specifies the array inside the resource to subset, and lower- and upper- bound indices. These parameters are interpreted by resource type-specific handler module in DataSpaces, which is chosen based on prior registration parameters.

```python
var_name = 'Rad'
lb = (0,2500)
ub = (1499,4999)
```

**Query** - search for resources, do a server-side download and subset, receive the results.

```python
result = client.query_array(source=source,
                       var_name=var_name,
                       lb=lb, 
                       ub=ub, 
                       timestamp=timestamp,
                       time_direction=time_direction)
```

**Handle results** - the return value is a list of tuples, one per found resource.

```python
(radiance, res_tstamp, res_metadata) = result[0]
print(res_tstamp, res_metadata)
```

### Visualize Results

```python
def viz_radiance(radiance):
    # Define some constants needed for the conversion. From the pdf linked above
    Esun_Ch_01 = 726.721072
    Esun_Ch_02 = 663.274497
    Esun_Ch_03 = 441.868715
    d2 = 0.3
    # Apply the formula to convert radiance to reflectance
    ref = (radiance * np.pi * d2) / Esun_Ch_02

    # Make sure all data is in the valid data range
    ref = np.maximum(ref, 0.0)
    ref = np.minimum(ref, 1.0)

    # Apply the formula to adjust reflectance gamma
    ref_gamma = np.sqrt(ref)

    # Plot gamma adjusted reflectance
    fig = plt.figure(figsize=(4,4),dpi=200)
    im = plt.imshow(ref_gamma, vmin=0.0, vmax=1.0, cmap='Greys_r')
    cb = fig.colorbar(im, orientation='horizontal')
    cb.set_ticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
    cb.set_label('Reflectance')
    plt.show()
```

### Generate Visualization
West Coast radiance visualization

```python
viz_radiance(radiance)
```

### Change the time direction
Query with the same `timestamp`, but ask for the next nearest `FUTURE` result.

```python
result = client.query_array(source=source,
                       var_name=var_name,
                       lb=lb, 
                       ub=ub, 
                       timestamp=timestamp,
                       time_direction=TimeDirection.FUTURE)
(radiance, res_tstamp, res_metadata) = result[0]
print(res_tstamp, res_metadata)
```

```python
viz_radiance(radiance)
```

### Query for all the resources within a time range
Query a 15 minute interval

```python
start_time='2024-08-02T00:30:00'
end_time='2024-08-02T00:45:00'
results = client.query_array(source=source,
                       var_name=var_name,
                       lb=lb, 
                       ub=ub, 
                       start_time=start_time,
                       end_time=end_time)
```

```python
for result in results:
    (radiance, res_tstamp, res_metadata) = result
    print(res_tstamp, res_metadata)
```

### Print result metadata
RadC produces data every 5 minutes, so we see three results in our 15 minute interval.


### llm/Local LLM Setup/LLM_setup_localhost.ipynb (13,648 bytes)

# LLM_setup_localhost


<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 40px; margin-top: 0;">
    <div style="flex: 0 0 auto; margin-left: 0; margin-bottom: 0;margin-top: 0;">
        <img src="../pics/NationalDataPlatform_logo.png" alt="WiFire Logo" style="width: 179px; margin-bottom: 0px;">
    </div>    
    <div style="flex: 0 0 auto; margin-left: auto; margin-bottom: 0; margin-top: 0;">
        <img src="../pics/logo_UCSD.png" alt="UCSD Logo" style="width: 179px; margin-bottom: 0px; margin-top: 20px;">
    </div>
    <div style="flex: 0 0 auto; margin-left: auto; margin-bottom: 0; margin-top: 20px;">
        <img src="../pics/sdsclogo-plusname-horiz-red.jpg" alt="San Diego Supercomputer Center Logo" width="300"/>
    </div>
</div>
<h1 style="text-align: center; font-size: 24px; margin-top: 0;">NSF National Data Platform (NDP)</h1>
<h3 style="text-align: center; font-size: 18px; margin-top: 10px;">LLM as a Service Tutorial</h3>
<div style="margin: 20px 0;">
    <p align="justify"> Large Language Models are a powerful AI tool with multiple applications in both research and education, given their capacity to process big amounts of information to generate human-like language.</p>
    <p align="justify"> Understanding today's relevance of LLM's, the National Data Platform (NDP) has developed an LLM service to contribute to the research and education goals of its users.</p>
    <p align="justify"> In this guide, we are covering the use of an LLM as an NDP service. The main purpose of this demo is to showcase how this service works by submitting a series of sample queries, as well as comparing the performance when adding new documentation to a model. The main goal is to allow the user to identify the potential use cases of this service.</p>
</div>

<center>
    <div style="text-align: right; padding: 5px;">
        <p style="text-align: right;"><strong>Contact:</strong><a href="https://docs.google.com/forms/d/e/1FAIpQLSfzjlc0Sw2fTFTKArOZ0ffKNdVcPivf218kLXkBKfobGPbDMw/viewform"> NDP Issue Reporting Form </a></p>
    </div>
</cente


<div style="display: flex; align-items: center; justify-content: flex-start; margin-top: 20px; border-top: 1px solid #ccc; padding-top: 20px;">
    <img src="https://new.nsf.gov/themes/custom/nsf_theme/components/images/logo/logo-desktop.svg" alt="NSF Logo" style="width: 120px; margin-right: 10px;">
    <p style="font-size: 12px;">The National Data Platform was funded by NSF 2333609 under CI, CISE Research Resources programs. Any opinions, findings, conclusions, or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the funders.</p>
</div>
<hr>

### What is an LLM?

An LLM, or Large Language Model, is a type of artificial intelligence designed to understand and generate human-like text based on the data it's been trained on. By adding a vast amount of text from different sources and context's (web, books, papers, among others) LLM's are capable to identify the patterns of the human language under different contexts and provide responses to complex questions. 

LLM's posses a huge potential in both research and education, given their capability to quickly process and summarize a vast amount of information. LLM's can bee seen as a powerful tool to accelerate learning, facilitate the sharing of knowledge, process and generate big amounts of data, generate new hypothesis questions, among other uses.

### ClimateGPT

For this demo, we are using the [ClimateGPT](https://climategpt.ai/) model. Climate GPT was developed by team of researchers at RWTH Aachen University, in collaboration with Erasmus AI and others, for interdisciplinary research focused on climate change. They constructed 7B models from the ground up, utilizing a scientifically-oriented dataset of 300 billion tokens.  

The model was made publicly available through [HuggingFace](https://huggingface.co/eci-io/climategpt-70b) in January 2024. It comes in well-maintained 7B, 13B, and 70B versions, built upon the Llama 2 architecture and leveraging a dataset of 4.2 billion tokens.

### Hands on

We will start using LLM as a service. First, we will make some questions to the vanilla ClimateGPT to see its overall performance. Then, we will extend the chorpus of the model by adding a new document. We expect the model to be able to answer questions based on the new document.

### Local Set Up
This notebook starts all required web servers on localhost (inside this Kubernetes pod).

```python
import os
import subprocess
import threading
import requests

os.environ['HF_HOME']='/srv/starter_content/cache'
```

```python
model = "eci-io/climategpt-7b"
```

## NDP LLM Service Documentation

This Python code snippet is designed to launch various components of a chat service named "FastChat." Each function starts a different part of the service using the `subprocess.run` method to execute shell commands.

### `run_controller()`

Starts the controller for the FastChat service, responsible for managing and coordinating different parts of the service.

```python
def run_controller():
    subprocess.run(["python3", "-m", "fastchat.serve.controller", "--host", "127.0.0.1"])

```python
def run_controller():
    subprocess.run(["python3", "-m", "fastchat.serve.controller", "--host", "127.0.0.1"])
```

## `run_worker`
Initiates a model worker for processing and generating responses based on specified models. Runs the model worker module, specifying the local host and a list of model names for processing requests. The --model-path argument should point to the directory where the models are stored.
```python 
def run_model_worker():
    subprocess.run(["python3", "-m", "fastchat.serve.model_worker", "--host", "127.0.0.1", "--model-names", f"{model},text-embedding-ada-002", "--model-path", model])

```
### `run_api`

Launches an API server that handles API requests to the FastChat service.
Runs the API server module on the local host, acting as an interface between the service and external clients or applications.
```python
def run_api_server():
    subprocess.run(["python3", "-m", "fastchat.serve.openai_api_server", "--host", "127.0.0.1"])
```

```python
def run_model_worker():
    subprocess.run(["python3", "-m", "fastchat.serve.model_worker", "--host", "127.0.0.1", "--model-names", f"{model},text-embedding-ada-002", "--model-path", model])

def run_api_server():
    subprocess.run(["python3", "-m", "fastchat.serve.openai_api_server", "--host", "127.0.0.1"])
def run_ui_server():
    subprocess.run(["python3", "-m", "fastchat.serve.gradio_web_server", "--host", "127.0.0.1"])
```

## Starting the `run_controller` Function in a Separate Thread

To enable the FastChat controller to run concurrently with the main program, the `run_controller` function is executed in a separate thread. This is achieved using Python's `threading` module, which allows for the execution of code in parallel to the main execution flow of the program.

### Code Snippet:

```python
import threading

controller_thread = threading.Thread(target=run_controller)
controller_thread.start()
```

### Note: please wait for the following output line:
```
2024-03-14 20:35:37 | ERROR | stderr | INFO:     Uvicorn running on http://127.0.0.1:21001 (Press CTRL+C to quit)
```

```python
controller_thread = threading.Thread(target=run_controller)
controller_thread.start()
```

## Starting the `run_model_worker` Function in a Separate Thread

To facilitate concurrent execution of the FastChat model worker alongside the main program and potentially other service components, the `run_model_worker` function is executed in a separate thread. This concurrent execution is made possible through the use of Python's `threading` module.

### Code Snippet:

```python
import threading

model_worker_thread = threading.Thread(target=run_model_worker)
model_worker_thread.start()
```


### Note: please wait for the following output line:
```
2024-03-14 20:36:18 | ERROR | stderr | INFO:     Uvicorn running on http://127.0.0.1:21002 (Press CTRL+C to quit)
```

```python
model_worker_thread = threading.Thread(target=run_model_worker)
model_worker_thread.start()
```

## Running the `run_api_server` Function in a Separate Thread

To ensure the API server component of the FastChat service operates concurrently with other parts of the application, the `run_api_server` function is launched in a separate thread. This concurrency is achieved with the help of Python's `threading` module, allowing multiple components to run simultaneously, improving scalability and responsiveness.

### Code Snippet:

```python
import threading

api_server_thread = threading.Thread(target=run_api_server)
api_server_thread.start()

### Note: please wait for the following output line:
```
2024-03-14 20:35:37 | ERROR | stderr | INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

```python
api_server_thread = threading.Thread(target=run_api_server)
api_server_thread.start()
```

## Test that everything works and ready (the response should contain the list of models and other parameters):

```python
requests.get('http://localhost:8000/v1/models').json()
```


### llm/Local LLM Setup/NAIRR_LLM_chat_localhost.ipynb (14,796 bytes)

# NAIRR_LLM_chat_localhost


<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 40px; margin-top: 0;">
    <div style="flex: 0 0 auto; margin-left: 0; margin-bottom: 0;margin-top: 0;">
        <img src="../pics/NationalDataPlatform_logo.png" alt="WiFire Logo" style="width: 179px; margin-bottom: 0px;">
    </div>    
    <div style="flex: 0 0 auto; margin-left: auto; margin-bottom: 0; margin-top: 0;">
        <img src="../pics/logo_UCSD.png" alt="UCSD Logo" style="width: 179px; margin-bottom: 0px; margin-top: 20px;">
    </div>
    <div style="flex: 0 0 auto; margin-left: auto; margin-bottom: 0; margin-top: 20px;">
        <img src="../pics/sdsclogo-plusname-horiz-red.jpg" alt="San Diego Supercomputer Center Logo" width="300"/>
    </div>
</div>
<h1 style="text-align: center; font-size: 24px; margin-top: 0;">NSF National Data Platform (NDP)</h1>
<h3 style="text-align: center; font-size: 18px; margin-top: 10px;">LLM as a Service Tutorial</h3>
<div style="margin: 20px 0;">
    <p align="justify"> Large Language Models are a powerful AI tool with multiple applications in both research and education, given their capacity to process big amounts of information to generate human-like language.</p>
    <p align="justify"> Understanding today's relevance of LLM's, the National Data Platform (NDP) has developed an LLM service to contribute to the research and education goals of its users.</p>
    <p align="justify"> In this guide, we are covering the use of an LLM as an NDP service. The main purpose of this demo is to showcase how this service works by submitting a series of sample queries, as well as comparing the performance when adding new documentation to a model. The main goal is to allow the user to identify the potential use cases of this service.</p>
</div>

<center>
    <div style="text-align: right; padding: 5px;">
        <p style="text-align: right;"><strong>Contact:</strong><a href="https://docs.google.com/forms/d/e/1FAIpQLSfzjlc0Sw2fTFTKArOZ0ffKNdVcPivf218kLXkBKfobGPbDMw/viewform"> NDP Issue Reporting Form </a></p>
    </div>
</cente


<div style="display: flex; align-items: center; justify-content: flex-start; margin-top: 20px; border-top: 1px solid #ccc; padding-top: 20px;">
    <img src="https://new.nsf.gov/themes/custom/nsf_theme/components/images/logo/logo-desktop.svg" alt="NSF Logo" style="width: 120px; margin-right: 10px;">
    <p style="font-size: 12px;">The National Data Platform was funded by NSF 2333609 under CI, CISE Research Resources programs. Any opinions, findings, conclusions, or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the funders.</p>
</div>
<hr>

### What is an LLM?

An LLM, or Large Language Model, is a type of artificial intelligence designed to understand and generate human-like text based on the data it's been trained on. By adding a vast amount of text from different sources and context's (web, books, papers, among others) LLM's are capable to identify the patterns of the human language under different contexts and provide responses to complex questions. 

LLM's posses a huge potential in both research and education, given their capability to quickly process and summarize a vast amount of information. LLM's can bee seen as a powerful tool to accelerate learning, facilitate the sharing of knowledge, process and generate big amounts of data, generate new hypothesis questions, among other uses.

### ClimateGPT

For this demo, we are using the [ClimateGPT](https://climategpt.ai/) model. Climate GPT was developed by team of researchers at RWTH Aachen University, in collaboration with Erasmus AI and others, for interdisciplinary research focused on climate change. They constructed 7B models from the ground up, utilizing a scientifically-oriented dataset of 300 billion tokens.  

The model was made publicly available through [HuggingFace](https://huggingface.co/eci-io/climategpt-70b) in January 2024. It comes in well-maintained 7B, 13B, and 70B versions, built upon the Llama 2 architecture and leveraging a dataset of 4.2 billion tokens.

### Hands on

We will start using LLM as a service. First, we will make some questions to the vanilla ClimateGPT to see its overall performance. Then, we will extend the corpus of the model by adding a new document. We expect the model to be able to answer questions based on the new document.

## Part 1: Explore Q&A using ClimateGPT​

### A. Set Up

We start by importing relevant libraries and functions. Also, we call the model and connect to the server's API.

```python
import requests
import os
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain_community.document_loaders import PyPDFLoader

MODEL = 'eci-io/climategpt-7b' # We specify the model tu use
os.environ['OPENAI_API_BASE'] = 'http://localhost:8000/v1'
os.environ['OPENAI_API_KEY'] = 'EMPTY'
```

### Test that LLM API is up

```python
# Get the response from the API
models = requests.get('http://localhost:8000/v1/models').json()['data']

# Print the model names that are being served 
[x['id'] for x in models]
```

#### Define Conversation Functions

```python
# In the following cell, we define a series of functions to interact with ClimateGPT in a form of a conversation.
def save_conversation_to_file(question, response):
    """
    This function saves questions and responses to text file. 
    :param question: The question (query) string
    :param response: The model's response string 
    :return: None
    """
    with open('conversation.txt', 'a') as file:
        file.write(question+'\n')
        file.write(response+'\n\n')
    

def make_query(question, use_corpus):
    """
    This function makes a call to the API. 
    :param question: The question (query) string
    :param use_corpus: Boolean. If True, the corpus text (from loaded document) will be used to add a context
    :return: question and response
    """
    url = "http://localhost:8000/v1/chat/completions"
    
    headers = {
        "Content-Type": "application/json",
    }
    
    data = {
        "model": MODEL,
        "messages": [{"role": "user", "content": question}],
    }
    
    if use_corpus:
        response = index.query(question, llm=llm)
    else:
        response = requests.post(url, json=data, headers=headers)
        response = response.json()['choices'][0]['message']['content']
    
    print(f"\nResponse: {response}")
    print("----------------------------------------------------------------------------------\n")

    return question, response


def run_conversation(use_corpus=False):
    """
    This function is a driver of the human and model API interaction  
    :param use_corpus: Boolean. If True, the corpus text (from loaded document) will be used to add a context
    :return: None
    """
    response = None
    question = None
    while True:
        user_input = input("Question (q=quit, s=save previous response): ")
        if user_input=='q':
            break
        if user_input=="s" and response:
            save_conversation_to_file(question, response)
            response = None
        else:
            question, response = make_query(user_input, use_corpus)
```

### B. Running the conversation

Now we will start a conversation with ClimateGPT. Some sample questions to begin:

- What AI/ML methods are used for wildfire data analysis?
- Summarize the impact of climate change on wildfires. Include the nature of damages caused by climate-related changes.
- What are the biodiversity impacts of wildfire?

After each question, you can:
- Type a new question
- Type "s" if you want to save your previous question and response
- Type "q" to quit the chat

**NOTE: After typing your question, press ENTER to get your response. Do not press SHIFT+ENTER.**

```python
run_conversation()
```

## Part 2: Add New Document and Compare Q&A Results

### C. Adding new context to ClimateGPT

Now we will extend the capacity of the model by adding new documentation. We will use the following document:

- ["Strengthening and Democratizing the U.S. Artificial Intelligence Innovation Ecosystem: An Implementation Plan for a National Artificial Intelligence Research Resource" (NAIRR-TF-Final-Report-2023.pdf)](https://www.ai.gov/wp-content/uploads/2023/01/NAIRR-TF-Final-Report-2023.pdf)

In the following cell, we will load and embed our document, and index it for retrieval from our Vector Store.

This cell might take a few minutes.

```python
# We load the new document to the model
embedding = OpenAIEmbeddings(model="text-embedding-ada-002")

# To load a different document, please make sure to use the right path
file = '../PDF Documents/NAIRR-TF-Final-Report-2023.pdf'

loader = PyPDFLoader(file)
index = VectorstoreIndexCreator(embedding=embedding).from_loaders([loader])
llm = ChatOpenAI(model=MODEL)
```

Once we have loaded our document, we can start making questions. Some questions that we can use to compare results are the following:

* What task forces are recommended in the report?  
* List the facilities that a NAIRR resource should provide with respect to (a) computing, (b) AI/ML models, and (c) data.  
* What committees does the report refer to?  
* What are NAIRR's goals with respect to human capital?

Let's start with the first question: *What task forces are recommended in the report?* 

1. Run the *PRE-Context* cell and ask the question. You will notice that the model will respond to not possess any knowledge of a report.
2. Type q to close the conversation
3. Go to the next cell *POST*, and repeat the process. Now the model will provide an answer relying on the document.

#### PRE-Context

**NOTE: After typing your question, press ENTER to get your response. Do not press SHIFT+ENTER.**

```python
# PRE - In this cell, we will ask the question without giving any context to ClimateGPT
run_conversation()
```

#### POST-Context

**NOTE: After typing your question, press ENTER to get your response. Do not press SHIFT+ENTER.**

```python
# POST - We add True to indicate the model to make use of the new document
run_conversation(True)
```


### llm/NAIRR_LLM_chat.ipynb (14,802 bytes)

# NAIRR_LLM_chat


<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 40px; margin-top: 0;">
    <div style="flex: 0 0 auto; margin-left: 0; margin-bottom: 0;margin-top: 0;">
        <img src="./pics/NationalDataPlatform_logo.png" alt="WiFire Logo" style="width: 179px; margin-bottom: 0px;">
    </div>    
    <div style="flex: 0 0 auto; margin-left: auto; margin-bottom: 0; margin-top: 0;">
        <img src="./pics/logo_UCSD.png" alt="UCSD Logo" style="width: 179px; margin-bottom: 0px; margin-top: 20px;">
    </div>
    <div style="flex: 0 0 auto; margin-left: auto; margin-bottom: 0; margin-top: 20px;">
        <img src="./pics/sdsclogo-plusname-horiz-red.jpg" alt="San Diego Supercomputer Center Logo" width="300"/>
    </div>
</div>
<h1 style="text-align: center; font-size: 24px; margin-top: 0;">NSF National Data Platform (NDP)</h1>
<h3 style="text-align: center; font-size: 18px; margin-top: 10px;">LLM as a Service Tutorial</h3>
<div style="margin: 20px 0;">
    <p align="justify"> Large Language Models are a powerful AI tool with multiple applications in both research and education, given their capacity to process big amounts of information to generate human-like language.</p>
    <p align="justify"> Understanding today's relevance of LLM's, the National Data Platform (NDP) has developed an LLM service to contribute to the research and education goals of its users.</p>
    <p align="justify"> In this guide, we are covering the use of an LLM as an NDP service. The main purpose of this demo is to showcase how this service works by submitting a series of sample queries, as well as comparing the performance when adding new documentation to a model. The main goal is to allow the user to identify the potential use cases of this service.</p>
</div>

<center>
    <div style="text-align: right; padding: 5px;">
        <p style="text-align: right;"><strong>Contact:</strong><a href="https://docs.google.com/forms/d/e/1FAIpQLSfzjlc0Sw2fTFTKArOZ0ffKNdVcPivf218kLXkBKfobGPbDMw/viewform"> NDP Issue Reporting Form </a></p>
    </div>
</cente


<div style="display: flex; align-items: center; justify-content: flex-start; margin-top: 20px; border-top: 1px solid #ccc; padding-top: 20px;">
    <img src="https://new.nsf.gov/themes/custom/nsf_theme/components/images/logo/logo-desktop.svg" alt="NSF Logo" style="width: 120px; margin-right: 10px;">
    <p style="font-size: 12px;">The National Data Platform was funded by NSF 2333609 under CI, CISE Research Resources programs. Any opinions, findings, conclusions, or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the funders.</p>
</div>
<hr>

### What is an LLM?

An LLM, or Large Language Model, is a type of artificial intelligence designed to understand and generate human-like text based on the data it's been trained on. By adding a vast amount of text from different sources and context's (web, books, papers, among others) LLM's are capable to identify the patterns of the human language under different contexts and provide responses to complex questions. 

LLM's posses a huge potential in both research and education, given their capability to quickly process and summarize a vast amount of information. LLM's can bee seen as a powerful tool to accelerate learning, facilitate the sharing of knowledge, process and generate big amounts of data, generate new hypothesis questions, among other uses.

### ClimateGPT

For this demo, we are using the [ClimateGPT](https://climategpt.ai/) model. Climate GPT was developed by team of researchers at RWTH Aachen University, in collaboration with Erasmus AI and others, for interdisciplinary research focused on climate change. They constructed 7B models from the ground up, utilizing a scientifically-oriented dataset of 300 billion tokens.  

The model was made publicly available through [HuggingFace](https://huggingface.co/eci-io/climategpt-70b) in January 2024. It comes in well-maintained 7B, 13B, and 70B versions, built upon the Llama 2 architecture and leveraging a dataset of 4.2 billion tokens.

### Hands on

We will start using LLM as a service. First, we will make some questions to the vanilla ClimateGPT to see its overall performance. Then, we will extend the corpus of the model by adding a new document. We expect the model to be able to answer questions based on the new document.

## Part 1: Explore Q&A using ClimateGPT​

### A. Set Up

We start by importing relevant libraries and functions. Also, we call the model and connect to the server's API.

```python
import requests
import os
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain_community.document_loaders import PyPDFLoader

MODEL = 'eci-io/climategpt-7b' # We specify the model tu use
os.environ['OPENAI_API_BASE'] = 'http://fc-api-server:8000/v1'
os.environ['OPENAI_API_KEY'] = 'EMPTY'
```

### Test that LLM API is up

```python
# Get the response from the API
models = requests.get('http://fc-api-server:8000/v1/models').json()['data']

# Print the model names that are being served 
[x['id'] for x in models]
```

#### Define Conversation Functions

```python
# In the following cell, we define a series of functions to interact with ClimateGPT in a form of a conversation.
def save_conversation_to_file(question, response):
    """
    This function saves questions and responses to text file. 
    :param question: The question (query) string
    :param response: The model's response string 
    :return: None
    """
    with open('conversation.txt', 'a') as file:
        file.write(question+'\n')
        file.write(response+'\n\n')
    

def make_query(question, use_corpus):
    """
    This function makes a call to the API. 
    :param question: The question (query) string
    :param use_corpus: Boolean. If True, the corpus text (from loaded document) will be used to add a context
    :return: question and response
    """
    url = "http://fc-api-server:8000/v1/chat/completions"
    
    headers = {
        "Content-Type": "application/json",
    }
    
    data = {
        "model": MODEL,
        "messages": [{"role": "user", "content": question}],
    }
    
    if use_corpus:
        response = index.query(question, llm=llm)
    else:
        response = requests.post(url, json=data, headers=headers)
        response = response.json()['choices'][0]['message']['content']
    
    print(f"\nResponse: {response}")
    print("----------------------------------------------------------------------------------\n")

    return question, response


def run_conversation(use_corpus=False):
    """
    This function is a driver of the human and model API interaction  
    :param use_corpus: Boolean. If True, the corpus text (from loaded document) will be used to add a context
    :return: None
    """
    response = None
    question = None
    while True:
        user_input = input("Question (q=quit, s=save previous response): ")
        if user_input=='q':
            break
        if user_input=="s" and response:
            save_conversation_to_file(question, response)
            response = None
        else:
            question, response = make_query(user_input, use_corpus)
```

### B. Running the conversation

Now we will start a conversation with ClimateGPT. Some sample questions to begin:

- What AI/ML methods are used for wildfire data analysis?
- Summarize the impact of climate change on wildfires. Include the nature of damages caused by climate-related changes.
- What are the biodiversity impacts of wildfire?

After each question, you can:
- Type a new question
- Type "s" if you want to save your previous question and response
- Type "q" to quit the chat

**NOTE: After typing your question, press ENTER to get your response. Do not press SHIFT+ENTER.**

```python
run_conversation()
```

## Part 2: Add New Document and Compare Q&A Results

### C. Adding new context to ClimateGPT

Now we will extend the capacity of the model by adding new documentation. We will use the following document:

- ["Strengthening and Democratizing the U.S. Artificial Intelligence Innovation Ecosystem: An Implementation Plan for a National Artificial Intelligence Research Resource" (NAIRR-TF-Final-Report-2023.pdf)](https://www.ai.gov/wp-content/uploads/2023/01/NAIRR-TF-Final-Report-2023.pdf)

In the following cell, we will load and embed our document, and index it for retrieval from our Vector Store.

This cell might take a few minutes.

```python
# We load the new document to the model
embedding = OpenAIEmbeddings(model="text-embedding-ada-002")

# To load a different document, please make sure to use the right path
file = 'PDF Documents/NAIRR-TF-Final-Report-2023.pdf'

loader = PyPDFLoader(file)
index = VectorstoreIndexCreator(embedding=embedding).from_loaders([loader])
llm = ChatOpenAI(model=MODEL)
```

Once we have loaded our document, we can start making questions. Some questions that we can use to compare results are the following:

* What task forces are recommended in the report?  
* List the facilities that a NAIRR resource should provide with respect to (a) computing, (b) AI/ML models, and (c) data.  
* What committees does the report refer to?  
* What are NAIRR's goals with respect to human capital?

Let's start with the first question: *What task forces are recommended in the report?* 

1. Run the *PRE-Context* cell and ask the question. You will notice that the model will respond to not possess any knowledge of a report.
2. Type q to close the conversation
3. Go to the next cell *POST*, and repeat the process. Now the model will provide an answer relying on the document.

#### PRE-Context

**NOTE: After typing your question, press ENTER to get your response. Do not press SHIFT+ENTER.**

```python
# PRE - In this cell, we will ask the question without giving any context to ClimateGPT
run_conversation()
```

#### POST-Context

**NOTE: After typing your question, press ENTER to get your response. Do not press SHIFT+ENTER.**

```python
# POST - We add True to indicate the model to make use of the new document
run_conversation(True)
```


### minimal_starter_content/catalog_search.ipynb (15,021 bytes)

# catalog_search


# Dataset Search Using Catalog API

This notebook demonstrates how to search for datasets in NDP Catalog using the
<a href = "https://github.com/ckan/ckanapi">ckan api </a>. Detailed query syntax examples can be found in the <a href = "https://solr.apache.org/guide/6_6/common-query-parameters.html">SOLR </a> documentation.

```python
import requests
```

```python
# Set catalog API URL
url = 'https://ndp.sdsc.edu/catalog/api/3/action/'
```

### Search Dataset by Organization

```python
# Get organizations list
endpoint = 'organization_list'
requests.get(url+endpoint).json()['result']
```

```python
# Search Datasets by Organization Name
organization='burnpro3d'
endpoint = f'package_search?q=organization:{organization}'
response_result = requests.get(url+endpoint).json()['result']
response_result['count']
```

```python
response_result['results'][1]['name']
```

```python
response_result['results'][1]['resources']
```

### Search Datasets by Tag

```python
# Get tags list
endpoint = 'tag_list'
requests.get(url+endpoint).json()['result'][:10]
```

```python
# Search Datasets by Organization Name
tag='Geodetic'
endpoint = f'package_search?q=tags:{tag}'
response_result = requests.get(url+endpoint).json()['result']
response_result['count']
```

```python
response_result['results'][0]['name']
```

```python
response_result['results'][0]['resources']
```

### Combined Search

```python
organization='burnpro3d'
tag='Quicfire'
endpoint = f'package_search?q=organization:{organization} tags:{tag}'
response_result = requests.get(url+endpoint).json()['result']
response_result['count']
```

```python
response_result['results'][0]['resources']
```


### nairr/exploration.ipynb (4,020,646 bytes)

# exploration


<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 40px; margin-top: 0;">
    <div style="flex: 0 0 auto; margin-left: 0; margin-bottom: 0;margin-top: 0;">
        <img src="./pics/NASA_logo.svg.png" alt="NASA Logo" style="width: 179px; margin-bottom: 0px;">
    </div>    
    <div style="flex: 0 0 auto; margin-left: auto; margin-bottom: 0; margin-top: 0;">
        <img src="./pics/logo_UCSD.png" alt="UCSD Logo" style="width: 179px; margin-bottom: 0px; margin-top: 20px;">
    </div>
    <div style="flex: 0 0 auto; margin-left: auto; margin-bottom: 0; margin-top: 20px;">
        <img src="./pics/sdsclogo-plusname-horiz-red.jpg" alt="San Diego Supercomputer Center Logo" width="300"/>
    </div>
</div>
<h1 style="text-align: center; font-size: 24px; margin-top: 0;">NSF National Data Platform (NDP)</h1>
<h3 style="text-align: center; font-size: 18px; margin-top: 10px;">Harmonized Landsat and Sentinel-2 (HLS) Model Demo</h3>
<div style="margin: 20px 0;">
    <p align="justify"> The <a href="https://hls.gsfc.nasa.gov/">Harmonized Landsat and Sentinel-2 (HLS) </a>project is a NASA initiative aiming to produce a seamless surface reflectance record from the Operational Land Imager (OLI) and Multi-Spectral Instrument (MSI) aboard Landsat-8/9 and Sentinel-2A/B remote sensing satellites, respectively.</p>
    <p align="justify"> As part of collection of the collection of <a href="https://nairrpilot.org/pilot-resources">resources</a> of the NAIRR Pilot, NASA in partnership with IBM has developed <a href="https://huggingface.co/ibm-nasa-geospatial/Prithvi-100M">Prithvi-100M</a>, a temporal Vision transformer pre-trained on contiguous HLS data There are 3 examples of finetuning the model for image segmentation using the mmsegmentation library available through HuggingFace: burn scars segmentation, flood mapping, and multi temporal crop classification, with the code used for the experiments available on GitHub. </p>
    <p align="justify"> In this demo we are covering the use of the model for 3 different use cases:</p>
    <ol>
      <li>An exploration of the raw model, plus a demo for each of the three different fine-tuning cases</li> 
      <li>A replication of the finetuning for the case of the burn-scars data</li>    
      <li>A guidance on how to set-up a finetuning</li>
    </o>
</div>

<div>
<h3 style="text-align: left; font-size: 18px; margin-top: 10px;">Credits</h3>
    <p>
This work builds upon the original <a href="https://github.com/NASA-IMPACT/hls-foundation-os/blob/main/exploration.ipynb">exploration</a> notebook developed by the NASA IMPACT team. For detailed citation information, please refer to the CITATION.cff file in this directory.
    </p>
</div>

<center>
    <div style="text-align: right; padding: 5px;">
        <p style="text-align: right;"><strong>Contact:</strong><a href="https://docs.google.com/forms/d/e/1FAIpQLSfzjlc0Sw2fTFTKArOZ0ffKNdVcPivf218kLXkBKfobGPbDMw/viewform"> NDP Issue Reporting Form </a></p>
    </div>
</center>


<div style="display: flex; align-items: center; justify-content: flex-start; margin-top: 20px; border-top: 1px solid #ccc; padding-top: 20px;">
    <img src="https://new.nsf.gov/themes/custom/nsf_theme/components/images/logo/logo-desktop.svg" alt="NSF Logo" style="width: 120px; margin-right: 10px;">
    <p style="font-size: 12px;">The National Data Platform was funded by NSF 2333609 under CI, CISE Research Resources programs. Any opinions, findings, conclusions, or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the funders.</p>
</div>
<hr>

## Step 1 - Data Acquisition

The HLS Burn Scars data resource was initially identified as part of the available resources within the NAIRR Pilot. After its discovery, the resource was acquired directly from the Huggingface platform.

![Huggingface](pics/huggingface.png)

## Step 2 - Data Registration

With the endpoint of the resource, the resource was registered into NDP's data catalog, along with the finetuned model developed with the dataset, making the discovery of both resources accesible for NDP users. 

![Catalog](pics/catalog.png)

## Step 3 - Data and Model Exploration

To get started, lets add an `__init__.py` file to the `prithvi` directory, so we can treat it as a module and import the `MaskedAutoencoderViT` class from it.
Simply create an empty file inside the `prithvi` directory named `__init__.py` by running the code below

```python
with open("prithvi/__init__.py", "w") as f:
    f.write("")
```

```python
import os
import torch
import matplotlib.pyplot as plt
import numpy as np
import rasterio
import yaml
from prithvi.Prithvi import MaskedAutoencoderViT

NO_DATA = -9999
NO_DATA_FLOAT = 0.0001
PERCENTILES = (0.1, 99.9)
```

#### Define some functions for visualization

```python
def load_raster(path, crop=None):
    with rasterio.open(path) as src:
        img = src.read()

        # load first 6 bands
        img = img[:6]

        img = np.where(img == NO_DATA, NO_DATA_FLOAT, img)
        if crop:
            img = img[:, -crop[0]:, -crop[1]:]
    return img

def enhance_raster_for_visualization(raster, ref_img=None):
    if ref_img is None:
        ref_img = raster
    channels = []
    for channel in range(raster.shape[0]):
        valid_mask = np.ones_like(ref_img[channel], dtype=bool)
        valid_mask[ref_img[channel] == NO_DATA_FLOAT] = False
        mins, maxs = np.percentile(ref_img[channel][valid_mask], PERCENTILES)
        normalized_raster = (raster[channel] - mins) / (maxs - mins)
        normalized_raster[~valid_mask] = 0
        clipped = np.clip(normalized_raster, 0, 1)
        channels.append(clipped)
    clipped = np.stack(channels)
    channels_last = np.moveaxis(clipped, 0, -1)[..., :3]
    rgb = channels_last[..., ::-1]
    return rgb
```

```python
def plot_image_mask_reconstruction(normalized, mask_img, pred_img):
    # Mix visible and predicted patches
    rec_img = normalized.clone()
    rec_img[mask_img == 1] = pred_img[mask_img == 1]  # binary mask: 0 is keep, 1 is remove

    mask_img_np = mask_img.numpy().reshape(6, 224, 224).transpose((1, 2, 0))[..., :3]

    rec_img_np = (rec_img.numpy().reshape(6, 224, 224) * stds) + means
    
    fig, ax = plt.subplots(1, 3, figsize=(15, 6))

    for subplot in ax:
        subplot.axis('off')

    ax[0].imshow(enhance_raster_for_visualization(input_data))
    masked_img_np = enhance_raster_for_visualization(input_data).copy()
    masked_img_np[mask_img_np[..., 0] == 1] = 0
    ax[1].imshow(masked_img_np)
    ax[2].imshow(enhance_raster_for_visualization(rec_img_np, ref_img=input_data))
```

#### Loading the model

```python
# load weights
weights_path = "./prithvi/Prithvi_100M.pt"
checkpoint = torch.load(weights_path, map_location="cuda")

# read model config
model_cfg_path = "./prithvi/Prithvi_100M_config.yaml"
with open(model_cfg_path) as f:
    model_config = yaml.safe_load(f)

model_args, train_args = model_config["model_args"], model_config["train_params"]

# let us use only 1 frame for now (the model was trained on 3 frames)
model_args["num_frames"] = 1

# instantiate model
model = MaskedAutoencoderViT(**model_args)
model.eval()

# load weights into model
# strict=false since we are loading with only 1 frame, but the warning is expected
del checkpoint['pos_embed']
del checkpoint['decoder_pos_embed']
_ = model.load_state_dict(checkpoint, strict=False)
```

### Base Model Exploration

We can access the images directly from the HuggingFace space thanks to rasterio

```python
raster_path = "https://huggingface.co/spaces/ibm-nasa-geospatial/Prithvi-100M-demo/resolve/main/HLS.L30.T13REN.2018013T172747.v2.0.B02.B03.B04.B05.B06.B07_cropped.tif"
input_data = load_raster(raster_path, crop=(224, 224))
print(f"Input data shape is {input_data.shape}")
raster_for_visualization = enhance_raster_for_visualization(input_data)
plt.imshow(raster_for_visualization)
```

We pass:
 - The normalized input image, cropped to size (224, 224)
 - `mask_ratio`: The proportion of pixels that will be masked

The model returns a tuple with:
 - loss
 - reconstructed image
 - mask used

```python
# statistics used to normalize images before passing to the model
means = np.array(train_args["data_mean"]).reshape(-1, 1, 1)
stds = np.array(train_args["data_std"]).reshape(-1, 1, 1)

def preprocess_image(image):
    # normalize image
    normalized = image.copy()
    normalized = ((image - means) / stds)
    normalized = torch.from_numpy(normalized.reshape(1, normalized.shape[0], 1, *normalized.shape[-2:])).to(torch.float32)
    return normalized
```

```python
normalized = preprocess_image(input_data)
with torch.no_grad():
        mask_ratio = 0.5
        _, pred, mask = model(normalized, mask_ratio=mask_ratio)
        mask_img = model.unpatchify(mask.unsqueeze(-1).repeat(1, 1, pred.shape[-1])).detach().cpu()
        pred_img = model.unpatchify(pred).detach().cpu()
```

```python
plot_image_mask_reconstruction(normalized, mask_img, pred_img)
```

### Finetuned Prithvi Exploration

#### Flood Mapping

```python
from mmcv import Config
from mmseg.models import build_segmentor
from mmseg.datasets.pipelines import Compose, LoadImageFromFile
from mmseg.apis import init_segmentor
from model_inference import inference_segmentor, process_test_pipeline
from huggingface_hub import hf_hub_download
import matplotlib
from torch import nn
```

```python
# Grab the config and model weights from huggingface
config_path=hf_hub_download(repo_id="ibm-nasa-geospatial/Prithvi-100M-sen1floods11", filename="sen1floods11_Prithvi_100M.py")
ckpt=hf_hub_download(repo_id="ibm-nasa-geospatial/Prithvi-100M-sen1floods11", filename='sen1floods11_Prithvi_100M.pth')
finetuned_model = init_segmentor(Config.fromfile(config_path), ckpt, device="cuda") # Make sure to replace for "cuda" if you reserved a GPU instance
```

#### Grabbing an image
The following images URL's are valid for exploration. Make sure to use the appropiate file name in the subsequent cells of code.

- `https://huggingface.co/spaces/ibm-nasa-geospatial/Prithvi-100M-sen1floods11-demo/resolve/main/Spain_7370579_S2Hand.tif`
- `https://huggingface.co/spaces/ibm-nasa-geospatial/Prithvi-100M-sen1floods11-demo/resolve/main/USA_430764_S2Hand.tif`
- `https://huggingface.co/spaces/ibm-nasa-geospatial/Prithvi-100M-sen1floods11-demo/resolve/main/India_900498_S2Hand.tif`

```python
!wget https://huggingface.co/spaces/ibm-nasa-geospatial/Prithvi-100M-sen1floods11-demo/resolve/main/Spain_7370579_S2Hand.tif
```

```python
input_data_inference = load_raster("Spain_7370579_S2Hand.tif") # Replace according to the grabbed image
print(f"Image input shape is {input_data_inference.shape}")
raster_for_visualization = enhance_raster_for_visualization(input_data_inference)
plt.axis('off')
plt.imshow(raster_for_visualization)
```

```python
# adapt this pipeline for Tif files with > 3 images
custom_test_pipeline = process_test_pipeline(finetuned_model.cfg.data.test.pipeline)
result = inference_segmentor(finetuned_model, "Spain_7370579_S2Hand.tif", 
                             custom_test_pipeline=custom_test_pipeline) # Replace according to the grabbed image
```

```python
fig, ax = plt.subplots(1, 3, figsize=(15, 10))
input_data_inference = load_raster("Spain_7370579_S2Hand.tif") # Replace according to the grabbed image
norm = matplotlib.colors.Normalize(vmin=0, vmax=2)
ax[0].imshow(enhance_raster_for_visualization(input_data_inference))
ax[1].imshow(result[0], norm=norm, cmap="jet")
ax[2].imshow(enhance_raster_for_visualization(input_data_inference))
ax[2].imshow(result[0], cmap="jet", alpha=0.3, norm=norm)
for subplot in ax:
    subplot.axis('off')
```

#### Burn Scrars Segmentation

```python
# Grab the config and model weights from huggingface
config_path=hf_hub_download(repo_id="ibm-nasa-geospatial/Prithvi-100M-burn-scar", filename="burn_scars_Prithvi_100M.py")
ckpt=hf_hub_download(repo_id="ibm-nasa-geospatial/Prithvi-100M-burn-scar", filename='burn_scars_Prithvi_100M.pth')
finetuned_model = init_segmentor(Config.fromfile(config_path), ckpt, device="cuda") # Make sure to replace for "cuda" if you reserved a GPU instance
```

#### Grabbing an image

The following images URL's are valid for exploration. Make sure to use the appropiate file name in the subsequent cells of code.

- `https://huggingface.co/spaces/ibm-nasa-geospatial/Prithvi-100M-Burn-scars-demo/resolve/main/subsetted_512x512_HLS.S30.T10TGS.2020245.v1.4_merged.tif`
- `https://huggingface.co/spaces/ibm-nasa-geospatial/Prithvi-100M-Burn-scars-demo/resolve/main/subsetted_512x512_HLS.S30.T10TGS.2018285.v1.4_merged.tif`
- `https://huggingface.co/spaces/ibm-nasa-geospatial/Prithvi-100M-Burn-scars-demo/resolve/main/subsetted_512x512_HLS.S30.T10UGV.2020218.v1.4_merged.tif`

```python
!wget https://huggingface.co/spaces/ibm-nasa-geospatial/Prithvi-100M-Burn-scars-demo/resolve/main/subsetted_512x512_HLS.S30.T10TGS.2020245.v1.4_merged.tif
```

```python
input_data_inference = load_raster("subsetted_512x512_HLS.S30.T10TGS.2020245.v1.4_merged.tif") # Replace according to the grabbed image
print(f"Image input shape is {input_data_inference.shape}")
raster_for_visualization = enhance_raster_for_visualization(input_data_inference)
plt.axis('off')
plt.imshow(raster_for_visualization)
```

```python
# adapt this pipeline for Tif files with > 3 images
custom_test_pipeline = process_test_pipeline(finetuned_model.cfg.data.test.pipeline)
result = inference_segmentor(finetuned_model, 
                             "subsetted_512x512_HLS.S30.T10TGS.2020245.v1.4_merged.tif", 
                             custom_test_pipeline=custom_test_pipeline) # Replace according to the grabbed image
```

```python
fig, ax = plt.subplots(1, 3, figsize=(15, 10))
input_data_inference = load_raster("subsetted_512x512_HLS.S30.T10TGS.2020245.v1.4_merged.tif") # Replace according to the grabbed image
norm = matplotlib.colors.Normalize(vmin=0, vmax=2)
ax[0].imshow(enhance_raster_for_visualization(input_data_inference))
ax[1].imshow(result[0], norm=norm, cmap="jet")
ax[2].imshow(enhance_raster_for_visualization(input_data_inference))
ax[2].imshow(result[0], cmap="jet", alpha=0.3, norm=norm)
for subplot in ax:
    subplot.axis('off')
```

#### Multi Temporal Crop Classification

```python
config_path=hf_hub_download(repo_id="ibm-nasa-geospatial/Prithvi-100M-multi-temporal-crop-classification", 
                            filename="multi_temporal_crop_classification_Prithvi_100M.py")
ckpt=hf_hub_download(repo_id="ibm-nasa-geospatial/Prithvi-100M-multi-temporal-crop-classification", 
                     filename='multi_temporal_crop_classification_Prithvi_100M.pth')
finetuned_model = init_segmentor(Config.fromfile(config_path), ckpt, device="cuda")
```

#### Grabbing an image

The following images URL's are valid for exploration. Make sure to use the appropiate file name in the subsequent cells of code.

- https://huggingface.co/spaces/ibm-nasa-geospatial/Prithvi-100M-multi-temporal-crop-classification-demo/resolve/main/chip_102_345_merged.tif
- https://huggingface.co/spaces/ibm-nasa-geospatial/Prithvi-100M-multi-temporal-crop-classification-demo/resolve/main/chip_104_104_merged.tif
- https://huggingface.co/spaces/ibm-nasa-geospatial/Prithvi-100M-multi-temporal-crop-classification-demo/resolve/main/chip_109_421_merged.tif

```python
!wget https://huggingface.co/spaces/ibm-nasa-geospatial/Prithvi-100M-multi-temporal-crop-classification-demo/resolve/main/chip_102_345_merged.tif
```

```python
input_data_inference = load_raster("chip_102_345_merged.tif") # Replace according to the grabbed image
print(f"Image input shape is {input_data_inference.shape}")
raster_for_visualization = enhance_raster_for_visualization(input_data_inference)
plt.axis('off')
plt.imshow(raster_for_visualization)
```

```python
custom_test_pipeline = process_test_pipeline(finetuned_model.cfg.data.test.pipeline)
result = inference_segmentor(finetuned_model, "chip_102_345_merged.tif", 
                             custom_test_pipeline=custom_test_pipeline) # Replace according to the grabbed image
```

```python
fig, ax = plt.subplots(1, 3, figsize=(15, 10))
input_data_inference = load_raster("chip_102_345_merged.tif") # Replace according to the grabbed image
norm = matplotlib.colors.Normalize(vmin=0, vmax=2)
ax[0].imshow(enhance_raster_for_visualization(input_data_inference))
ax[1].imshow(result[0], norm=norm, cmap="jet")
ax[2].imshow(enhance_raster_for_visualization(input_data_inference))
ax[2].imshow(result[0], cmap="jet", alpha=0.3, norm=norm)
for subplot in ax:
    subplot.axis('off')
```

## Step 4 - ML-based Workflow

### Replicating finetuning

We can replicate the finetune process for the burn scars case. First, we need to download the data. The following cell will grab the data, extract the training and validatiton sets, and create a `burn-scars-data` folder to place the extracted files.

```python
import requests
from tqdm.auto import tqdm
import tarfile
import shutil

url = "https://huggingface.co/datasets/ibm-nasa-geospatial/hls_burn_scars/resolve/main/hls_burn_scars.tar.gz"
file_path = "hls_burn_scars.tar.gz"

response = requests.get(url, stream=True) 
with open(file_path, "wb") as f:
    total_length = int(response.headers.get('content-length'))
    for data in tqdm(response.iter_content(chunk_size=4096), total=int(total_length/4096), desc="Downloading"):
        f.write(data)

with tarfile.open(file_path) as tar:
    tar.extractall()

new_dir_path = "burn-scars-data"
os.makedirs(new_dir_path, exist_ok=True)

for folder_name in ['training', 'validation']:
    shutil.move(folder_name, os.path.join(new_dir_path, folder_name))

os.remove(file_path)
```

#### Running the finetuning
With the data downloaded, we can now proceed to finetune the model. It is important to have reserved a GPU instance to be able to run the following cells of code. Take in consideration that it should take between 3-4 hours to complete the finetuning. 

The weights will be saved in the demo folder. To change the parameter specification, or the name of the destination folder, edit `configs/burn_scars.py`.

```python
os.environ['PATH'] = '/opt/conda/envs/myenv/bin:' + os.environ['PATH']
!mim train mmsegmentation configs/burn_scars.py
```

## Step 5 - Product generation

### Finetuning for a different usecase
To finetune, you can now write a PyTorch loop as usual to train on your dataset. Simply extract the backbone from the model with some surgery and run only the model features forward, with no masking!

 In general some reccomendations are:
- At least in the beggining, experiment with freezing the backbone. This will give you much faster iteration through experiments.
- Err on the side of a smaller learning rate
- With an unfrozen encoder, regularization is your friend! (Weight decay, dropout, batchnorm...)

```python
# if going with plain pytorch:
# - remember to normalize images beforehand (find the normalization statistics in the config file)
# - turn off masking by passing mask_ratio = 0
normalized = preprocess_image(input_data)
features, _, _ = model.forward_encoder(normalized, mask_ratio=0)
```

#### What do these features look like?
These are the standard output of a ViT.
- Dim 1: Batch size
- Dim 2: [`cls_token`] + tokens representing flattened image
- Dim 3: embedding dimension

First reshape features into "image-like" shape:
- Drop cls_token
- reshape into HxW shape

```python
print(f"Encoder features have shape {features.shape}")

# drop cls token
reshaped_features = features[:, 1:, :]

# reshape
feature_img_side_length = int(np.sqrt(reshaped_features.shape[1]))
reshaped_features = reshaped_features.view(-1, feature_img_side_length, feature_img_side_length, model_args["embed_dim"])
# channels first
reshaped_features = reshaped_features.permute(0, 3, 1, 2)
print(f"Encoder features have new shape {reshaped_features.shape}")
```

#### Example of a segmentation head
A simple segmentation head can consist of a few upscaling blocks + a final head for classification

```python
num_classes = 2
upscaling_block = lambda in_channels, out_channels: nn.Sequential(nn.Upsample(scale_factor=2), nn.Conv2d(kernel_size=3, in_channels=in_channels, out_channels=out_channels, padding=1), nn.ReLU())
embed_dims = [model_args["embed_dim"] // (2**i) for i in range(5)]
segmentation_head = nn.Sequential(
    *[
    upscaling_block(embed_dims[i], embed_dims[i+1]) for i in range(4)
    ],
    nn.Conv2d(kernel_size=1, in_channels=embed_dims[-1], out_channels=num_classes))
```

### Running features through the segmentation head
We now get an output of shape [batch_size, num_classes, height, width]

```python
segmentation_head(reshaped_features).shape
```

### Finetuning - MMSeg
Alternatively, finetune using the MMSegmentation extension we have opensourced.
- No model surgery required
- No need to write boilerplate training code
- Integrations with Tensorboard, MLFlow, ...
- Segmentation evaluation metrics / losses built in

1. Build your config file. Look [here](./configs/) for examples, the [ReadME](./README.md) for some docs and [MMSeg](https://mmsegmentation.readthedocs.io/en/0.x/tutorials/config.html) for more general tutorials.
2. Collect your dataset in the format determined by MMSeg
3. `mim train mmsegmentation <path to my config>`

This is what the model looks like in the MMSeg configuration code.

All this composition we did above is done for you!
```python
model = dict(
    type="TemporalEncoderDecoder",
    frozen_backbone=False,
    backbone=dict(
        type="TemporalViTEncoder",
        pretrained=pretrained_weights_path,
        img_size=img_size,
        patch_size=patch_size,
        num_frames=num_frames,
        tubelet_size=1,
        in_chans=len(bands),
        embed_dim=embed_dim,
        depth=num_layers,
        num_heads=num_heads,
        mlp_ratio=4.0,
        norm_pix_loss=False,
    ),
    neck=dict(
        type="ConvTransformerTokensToEmbeddingNeck",
        embed_dim=num_frames*embed_dim,
        output_embed_dim=embed_dim,
        drop_cls_token=True,
        Hp=img_size // patch_size,
        Wp=img_size // patch_size,
    ),
    decode_head=dict(
        num_classes=num_classes,
        in_channels=embed_dim,
        type="FCNHead",
        in_index=-1,
        ignore_index=ignore_index,
        channels=256,
        num_convs=1,
        concat_input=False,
        dropout_ratio=0.1,
        norm_cfg=norm_cfg,
        align_corners=False,
        loss_decode=dict(
            type="CrossEntropyLoss",
            use_sigmoid=False,
            loss_weight=1,
            class_weight=ce_weights,
            avg_non_ignore=True
        ),
    ),
    (...)
```


### nasa/NDP_NASA.ipynb (498,689 bytes)

# NDP_NASA


<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
    <img src="https://www.goes-r.gov/imagesContent/multimedia/goesSeriesLogos/goesRLogos/color/small.jpg" alt="EarthScope Consortium Logo" style="width: 150px; margin-top: 10px;">
    <div style="flex: 0 0 auto; margin-left: auto; margin-bottom: 0;">
        <img src="https://www.sci.utah.edu/images/news/2023/sci-30-multi.jpg" alt="Scientific Computing and Imaging Institute Logo" width="100"/>
    </div>
</div>

<h1 style="text-align: center; font-size: 24px; margin-top: 0;">NSF National Data Platform (NDP)</h1>
<h3 style="text-align: center; font-size: 18px; margin-top: 10px;">NASA-GOES R Satellite Data RADC product Visualization</h3>

<div style="margin: 20px 0;">
    <p>NOAA's latest generation of geostationary weather satellites
The Geostationary Operational Environmental Satellite (GOES) – R Series is the nation’s most advanced fleet of geostationary weather satellites. The GOES-R Series significantly improves the detection and observation of environmental phenomena that directly affect public safety, protection of property and our nation’s economic health and prosperity.
The satellites provide advanced imaging with increased spatial resolution and faster coverage for more accurate forecasts, real-time mapping of lightning activity, and improved monitoring of solar activity and space weather.
The GOES-R Series is a four-satellite program (GOES-R/S/T/U) that will extend the availability of the operational GOES satellite system through 2036.</p>
</div>

<center>
    <div style="text-align: right; padding: 5px;">
        <p style="text-align: right;"><strong>Contact:</strong> Scientific and Computing Imaging Institute, University of Utah (<a href="mailto:saleem.alharir@utah.edu">saleem.alharir@utah.edu</a>)</p>
    </div>
</center>

<div style="display: flex; align-items: center; justify-content: flex-start; margin-top: 20px; border-top: 1px solid #ccc; padding-top: 20px;">
    <img src="https://new.nsf.gov/themes/custom/nsf_theme/components/images/logo/logo-desktop.svg" alt="NSF Logo" style="width: 120px; margin-right: 10px;">
    <p style="font-size: 12px;">The National Data Platform was funded by NSF 2333609 under CI, CISE Research Resources programs. Any opinions, findings, conclusions, or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the funders.</p>
</div>

```python
import requests
import io
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import json
```

```python
CKAN_URL = 'http://ckan.geosciframe.org:5000/catalog'

def download_file(url, local_filename):
    response = requests.get(url, stream=True)
    with open(local_filename, 'wb') as output_file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                output_file.write(chunk)
def download_ckan_dataset_files(dataset_name):
    """Get dataset details from CKAN and download files."""
    response = requests.get(f"{CKAN_URL}/api/3/action/package_show", params={"id": dataset_name})
    dataset_details = response.json()
    downloaded_files = []  # Create an empty list to store downloaded file names
    
    if dataset_details['success']:
        resources = dataset_details['result']['resources']
        for resource in resources:
            if resource['format'].lower() in ['netcdf', 'nc']:
                file_url = resource['url']
                print(f"File URL: {file_url}")
                local_filename = file_url.split('/')[-1]
                print(f"Local filename: {local_filename}")
                downloaded_files.append(local_filename)  # Append the file name to the list
                
                print(f"Downloading {local_filename}...")
                download_file(file_url, local_filename)
                
    else:
        print("Failed to get dataset details.")
    
    return downloaded_files  # Return the list of downloaded file names

# Example usage
dataset_name = "abi-l1b-radc_2020_122_00_or_abi-l1b-radc-m6c01_g17_s20201220001177_e20201220003550_c20201220003598"
downloaded_files = download_ckan_dataset_files(dataset_name)
print("Downloaded files:", downloaded_files)
```

### Visualize the data for RADC only for the file retrieved from CKAN

<hr>

```python

try:
    ds_radc = xr.open_dataset(downloaded_files[0])
    radiance = np.array(ds_radc['Rad'])
    # Plot radiance
    plt.figure(figsize=(10, 10))
    plt.imshow(radiance, cmap='gray', vmin=0, vmax=255)
    plt.colorbar(label='Radiance')
    plt.title('RAD Radiance')
    plt.show()
except Exception as e:
    print(f"Error plotting the file: {str(e)}")
```


### pgml/NDP_PGML_EDA.ipynb (1,304,843 bytes)

# NDP_PGML_EDA


<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 40px; margin-top: 0;">
    <div style="flex: 0 0 auto; margin-left: 0; margin-bottom: 0;margin-top: 0;">
        <img src="./pics/WIFIRE_LOGO_Transparent_s_0.png" alt="WiFire Logo" style="width: 179px; margin-bottom: 0px;">
    </div>    
    <div style="flex: 0 0 auto; margin-left: auto; margin-bottom: 0; margin-top: 0;">
        <img src="./pics/logo_UCSD.png" alt="UCSD Logo" style="width: 179px; margin-bottom: 0px; margin-top: 20px;">
    </div>
    <div style="flex: 0 0 auto; margin-left: auto; margin-bottom: 0; margin-top: 20px;">
        <img src="./pics/sdsclogo-plusname-horiz-red.jpg" alt="San Diego Supercomputer Center Logo" width="300"/>
    </div>
</div>

<h1 style="text-align: center; font-size: 24px; margin-top: 0;">NSF National Data Platform (NDP)</h1>
<h3 style="text-align: center; font-size: 18px; margin-top: 10px;"> Physics Guided Machine Learning Project at WIFIRE Lab</h3>

<div style="margin: 20px 0;">
    <p>The <a href="https://wifire.ucsd.edu">WIFIRE Lab</a> is a consortium of UC San Diego organizations and a number of partnerships including the university collaborators, industry partners, fire departments, and state agencies. To meet growing needs in hazard monitoring and response, the WIFIRE Lab is an all-hazards knowledge cyberinfrastructure and a management layer from the data collection to modeling efforts.</p>
    <p>Next-generation fire models provide the basis to understand fire physics in detail, leading the way for emulators to model potential fire behavior. The <b>Physics Guided Machine Learning (PGML)</b> project uses data from hundreds of coupled fire-atmosphere simulations produced by a physics-based coupled fire-atmospheric modeling model (QUIC-Fire) to develop a reduced-order emulator. Such an emulator can be used to predict the wildfire spread, which can help the fire agencies take necessary steps to reduce the damage. Additionally, the predictions can be utilized to mitigate the risk of controlled fires escalating into wildfires.</p>
    <p>This dataset was generated particularly for the Physics Guided Machine Learning (PGML) research and educational tasks. It is an ensemble of prescribed fire simulations generated by the QUIC-Fire coupled fire-atmospheric modeling tool. Each simulation run is represented by a Zarr file, containing the outputs created by QUIC-Fire through the BurnPro3D web interface. To model a burn, users upload the polygon for their burn unit and BurnPro3D uses a 3D fuels model for that location created by FastFuels and an ignition file with a user-defined ignition pattern created in DripTorch. Those files are included here as well. In addition, users define the environmental conditions they would like to model in terms of fuel moisture, wind direction, and wind speed.</p>
</div>

<center>
    <div style="text-align: right; padding: 5px;">
        <p style="text-align: right;"><strong>Contact:</strong> San Diego Supercomputer Center, University of California San Diego (<a href="mailto:saleem.alharir@utah.edu">segurvich@ucsd.edu</a>)</p>
    </div>
</center>


<div style="display: flex; align-items: center; justify-content: flex-start; margin-top: 20px; border-top: 1px solid #ccc; padding-top: 20px;">
    <img src="https://new.nsf.gov/themes/custom/nsf_theme/components/images/logo/logo-desktop.svg" alt="NSF Logo" style="width: 120px; margin-right: 10px;">
    <p style="font-size: 12px;">The National Data Platform was funded by NSF 2333609 under CI, CISE Research Resources programs. Any opinions, findings, conclusions, or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the funders.</p>
</div>

<hr>

## Physics Guided Machine Learning
### Uniform Fuels Idealized Grass Dataset
### Exploratory Data Analysis

#### Imports

```python
import numpy as np
import json
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import Image
from IPython.core.display import HTML 
import zarr
```

#### Load Data

```python
runs_df = pd.read_csv('uniform-pgml-success_list_simulation_runs.csv')
runs_df.head(3)
```

#### Explore how the data look like

```python
# select one simulation run
link = runs_df.loc[0]['link']

# load data from remote location
run_zarr = zarr.open(link)

# select Fuel Density feature
fuels_dens = np.array(run_zarr['fuels-dens'])

# show how the very last 'frame' looks like
fuels_dens[-1]
```

#### Vizualize few frames from the first run

```python
fig, axs = plt.subplots(1, 5,figsize=(15,15))
times=[20,50,150,300,600]
for i, ax in enumerate(axs.flatten()):
    ax.imshow(fuels_dens[times[i],0,:,:],cmap='rainbow',origin="lower")
fig.tight_layout()
plt.show()
```

#### Ensemble info

Let's explore what input features each simulation run has and their unique values:

```python
# input features
runs_df.columns
```

```python
# wind speeds
runs_df['wind_speed'].unique()
```

```python
# wind directions
runs_df['wind_direction'].unique()
```

```python
# surface moisture
runs_df['surface_moisture'].unique()
```

```python
# ignition types
runs_df['ignition_type_metadata'].unique()
```

```python
# overall how many simulation runs
len(runs_df)
```

#### Compare Simulation Runs

Let's explore how the outputs for different simulation runs look like and how they are different based on input parameters. For example, the simulation run with low initial wind speed will be different from similar simulation run with higher wind speed.

```python
# make a simple list of links
runs_list = list(runs_df['link'])
runs_list[:3]
```

```python
# function to produce a set of plots
def plot_runs(feature_to_plot):
    wind_s = runs_df["wind_speed"]
    wind_d = runs_df["wind_direction"]
    surface_m = runs_df["surface_moisture"]
    ignition_t = runs_df["ignition_type_metadata"]
    
    # select just a few samples (simulation runs) to visualize
    run_samples = [0,50,250,300,450,600,750,1153]
    for run_number in run_samples:
        link = runs_list[run_number]
        run_zarr = zarr.open(link)
        fuels_dens = np.array(run_zarr[feature_to_plot])
        fig, axs = plt.subplots(1, 5,figsize=(15,15))
        
        # select just a few samples (frames) to visualize 
        times=[20,50,150,300,600]
        print("Input Parameters:\nWind Speed:",wind_s[run_number],"Wind Direction:",wind_d[run_number],"Surface Moisture:",surface_m[run_number],"Ignition:",ignition_t[run_number],"\n") 
    
        for i, ax in enumerate(axs.flatten()):
            ax.set_title(f"Run #: {run_number}, Time step: t={times[i]}")
            ax.imshow(fuels_dens[times[i],0,:,:],cmap='rainbow',origin="lower")
        fig.tight_layout()
        plt.show()
```

##### Input parameters vs fuel moisture

```python
%matplotlib inline
# make plots for Fuel Moisture feature
plot_runs('fuels-moist')
```

##### Input parameters vs fuel density

```python
%matplotlib inline
# make plots for Fuel Density feature
plot_runs('fuels-dens')
```


### pgml/NGP_PGML_UNet.ipynb (17,273 bytes)

# NGP_PGML_UNet


<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 40px; margin-top: 0;">
    <div style="flex: 0 0 auto; margin-left: 0; margin-bottom: 0;margin-top: 0;">
        <img src="./pics/WIFIRE_LOGO_Transparent_s_0.png" alt="WiFire Logo" style="width: 179px; margin-bottom: 0px;">
    </div>    
    <div style="flex: 0 0 auto; margin-left: auto; margin-bottom: 0; margin-top: 0;">
        <img src="./pics/logo_UCSD.png" alt="UCSD Logo" style="width: 179px; margin-bottom: 0px; margin-top: 20px;">
    </div>
    <div style="flex: 0 0 auto; margin-left: auto; margin-bottom: 0; margin-top: 20px;">
        <img src="./pics/sdsclogo-plusname-horiz-red.jpg" alt="San Diego Supercomputer Center Logo" width="300"/>
    </div>
</div>

<h1 style="text-align: center; font-size: 24px; margin-top: 0;">NSF National Data Platform (NDP)</h1>
<h3 style="text-align: center; font-size: 18px; margin-top: 10px;"> Physics Guided Machine Learning Project at WIFIRE Lab</h3>

<div style="margin: 20px 0;">
    <p>The <a href="https://wifire.ucsd.edu">WIFIRE Lab</a> is a consortium of UC San Diego organizations and a number of partnerships including the university collaborators, industry partners, fire departments, and state agencies. To meet growing needs in hazard monitoring and response, the WIFIRE Lab is an all-hazards knowledge cyberinfrastructure and a management layer from the data collection to modeling efforts.</p>
    <p>Next-generation fire models provide the basis to understand fire physics in detail, leading the way for emulators to model potential fire behavior. The <b>Physics Guided Machine Learning (PGML)</b> project uses data from hundreds of coupled fire-atmosphere simulations produced by a physics-based coupled fire-atmospheric modeling model (QUIC-Fire) to develop a reduced-order emulator. Such an emulator can be used to predict the wildfire spread, which can help the fire agencies take necessary steps to reduce the damage. Additionally, the predictions can be utilized to mitigate the risk of controlled fires escalating into wildfires.</p>
    <p>This dataset was generated particularly for the Physics Guided Machine Learning (PGML) research and educational tasks. It is an ensemble of prescribed fire simulations generated by the QUIC-Fire coupled fire-atmospheric modeling tool. Each simulation run is represented by a Zarr file, containing the outputs created by QUIC-Fire through the BurnPro3D web interface. To model a burn, users upload the polygon for their burn unit and BurnPro3D uses a 3D fuels model for that location created by FastFuels and an ignition file with a user-defined ignition pattern created in DripTorch. Those files are included here as well. In addition, users define the environmental conditions they would like to model in terms of fuel moisture, wind direction, and wind speed.</p>
</div>

<center>
    <div style="text-align: right; padding: 5px;">
        <p style="text-align: right;"><strong>Contact:</strong> San Diego Supercomputer Center, University of California San Diego (<a href="mailto:saleem.alharir@utah.edu">segurvich@ucsd.edu</a>)</p>
    </div>
</center>


<div style="display: flex; align-items: center; justify-content: flex-start; margin-top: 20px; border-top: 1px solid #ccc; padding-top: 20px;">
    <img src="https://new.nsf.gov/themes/custom/nsf_theme/components/images/logo/logo-desktop.svg" alt="NSF Logo" style="width: 120px; margin-right: 10px;">
    <p style="font-size: 12px;">The National Data Platform was funded by NSF 2333609 under CI, CISE Research Resources programs. Any opinions, findings, conclusions, or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the funders.</p>
</div>

<hr>

## Physics Guided Machine Learning
### [UNet Model](https://en.wikipedia.org/wiki/U-Net) Training with Uniform Fuels Idealized Grass Dataset
### [Link to MLFlow Experiments Tracking Dashboard](https://nationaldataplatform.org/mlflow)
_[Link to MLFlow Documentation](https://mlflow.org/docs/latest/getting-started/intro-quickstart/index.html#step-3-train-a-model-and-prepare-metadata-for-logging)_

#### Imports

```python
from __future__ import unicode_literals, print_function, division
import torch
import matplotlib.pyplot as plt
import numpy as np
from torch.utils import data
import time
from unet.unets import U_net
from unet.utils_unet import train_epoch, eval_epoch, test_epoch
from unet.dataset import IdealizedGrasslands
import warnings
import mlflow
import imageio
import datetime
from pathlib import Path
import os
from random import choices
from string import ascii_lowercase, digits
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
warnings.filterwarnings("ignore")
device
```

#### Training

```python
# storage settings
model_type = 'U_Net'
now = datetime.datetime.now().strftime("%Y_%m_%d_%I%M%S%p")
run_name = model_type + '_' + now
pvc_dir = './data'

results_dir=Path(f'{pvc_dir}/results/{run_name}')
graphs_directory = results_dir / 'graphs'
pics_temp_directory = results_dir / 'pics'
movie_directory = pics_temp_directory / 'movie'
graphs_directory.mkdir(parents=True, exist_ok=True)
movie_directory.mkdir(parents=True, exist_ok=True)
model_filename=f"{run_name}_model.pth"
```

```python
# set parameters
min_mse=10
output_length=100
input_length=7
learning_rate=0.001
dropout_rate=0
kernel_size=3
batch_size=1
max_epochs=20

# it is better to shuffle runs to eliminate the structure of the dataset before training
def shuffle_runs(number_of_run_aside=950):
    """
    number_of_run_aside - thin run will have animation after testing is complete. 
    We want to see animation of the same run to be able to compare experiments.
    """
    np.random.seed(42)
    print('Shuffling runs')
    initial_ind = [x for x in range(1155)]
    initial_ind.pop(number_of_run_aside - 1)
    initial_ind = np.array(initial_ind)
    np.random.shuffle(initial_ind)
    train_indices = list(initial_ind[:850])
    valid_indices = list(initial_ind[850:950])
    test_indices = list(initial_ind[950:1155])
    test_indices.insert(0, np.int64(number_of_run_aside))

    return train_indices, valid_indices, test_indices

# assign indices of the simulation runs for training/validation/testing
train_indices, valid_indices, test_indices = shuffle_runs()

# alternatively, split data without shuffling (not recommended)
# train_indices=list(range(0,850))
# valid_indices = list(range(850, 950))
# test_indices = list(range(950, 1155))
```

```python
# create experiment(if not existing) and start new mlflow run
random_suffix = "".join(choices(ascii_lowercase, k=2)+choices(digits, k=3))
mlflow.end_run()  # in case there is active run
suffix = '_' + os.getenv('JUPYTERHUB_USER').split("@")[0]+'_'+random_suffix # experiment name will contain username for uniqueness and random suffix string
experiment_name = model_type+suffix
try:
    mlflow.create_experiment(experiment_name)
except:
    pass
mlflow.set_experiment(experiment_name)
mlflow.start_run(run_name=run_name)
```

```python
# configure model
model=U_net(input_channels = input_length, output_channels = 1, kernel_size = kernel_size,
            dropout_rate = dropout_rate).to(device)
train_set = IdealizedGrasslands(train_indices, input_length , 15, output_length, "train", file='uniform-pgml-success_list_simulation_runs.csv')
valid_set =IdealizedGrasslands(valid_indices, input_length , 15, output_length, "test", file='uniform-pgml-success_list_simulation_runs.csv')
train_loader = data.DataLoader(train_set, batch_size = batch_size, shuffle = True, num_workers = 8)
valid_loader = data.DataLoader(valid_set, batch_size = batch_size, shuffle = False, num_workers = 8)
loss_fun = torch.nn.L1Loss()
optimizer = torch.optim.Adam(model.parameters(), learning_rate, betas = (0.9, 0.999), weight_decay = 4e-4)
scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size = 1, gamma = 0.9)

# log parameters into MLFlow
mlflow.log_param("learning_rate", learning_rate)
mlflow.log_param("batch_size", batch_size)
mlflow.log_param("loss_function", loss_fun)
mlflow.log_param("max_epochs", max_epochs)
mlflow.log_param("optimizer", str(optimizer))
mlflow.log_param("scheduler", str(scheduler))

# start training
train_mse = []
valid_mse = []
test_mse = []

# loop for each epoch of training
for i in range(max_epochs):
    mlflow.log_metric("Current Training Epoch", i + 1)
    print(f'Epoch {i} started')
    start = time.time()
    torch.cuda.empty_cache()
    scheduler.step()
    model.train()
    teacher_force_ratio=np.maximum(0, 1 - i * 0.03)
    train_loss = train_epoch(train_loader, model, optimizer, loss_fun, teacher_force_ratio)
    train_mse.append(train_loss)
    model.eval()
    mse, preds, trues = eval_epoch(valid_loader, model, loss_fun)
    valid_mse.append(mse)

    # send training metrics to MLFlow
    mlflow.log_metric("Epoch Loss", train_loss, step=i)
    mlflow.log_metric("Epoch Validation", mse, step=i)
    
    if valid_mse[-1] < min_mse:
        min_mse = valid_mse[-1]
        best_model = model
        torch.save(best_model, results_dir / model_filename)
    end = time.time()
    if (len(train_mse) > 50 and np.mean(valid_mse[-5:]) >= np.mean(valid_mse[-10:-5])):
            break
    print(train_mse[-1], valid_mse[-1], round((end-start)/60,5))
    print(f'Epoch {i} ended')
```

#### Testing

```python
loss_fun = torch.nn.L1Loss()
best_model = torch.load(results_dir / model_filename)
test_set = IdealizedGrasslands(test_indices, input_length , 15, output_length, 'test', file='uniform-pgml-success_list_simulation_runs.csv')
test_loader = data.DataLoader(test_set, batch_size = batch_size, shuffle = False, num_workers = 8)
loss_curve,preds, trues  = test_epoch(test_loader, best_model, loss_fun)

# send testing metrics to MLFlow
for i, mae_item in enumerate(loss_curve):
    mlflow.log_metric("Test MAE", mae_item, step=i)

# calculate mean MAE for all frames
mean_mae = np.mean(loss_curve)
mlflow.log_metric("Test Avg MAE", mean_mae)

# save testing results
torch.save({"preds": preds[:10],
            "trues": trues[:10],
            "loss_curve": loss_curve},
            results_dir / f"{run_name}_results.pt")
```

#### Produce Visualizations

```python
pt_file = torch.load(results_dir / f"{run_name}_results.pt")

# print the head of the file
y = pt_file['loss_curve']

# create x ticks for plot
x = [str(x) for x in range(len(y))]

# mae over timesteps graph
ax = plt.axes()
ax.plot(x, y)
plt.title(f'{model_type.upper()} Model MAE over the Time Steps')
plt.xlabel('Time Steps')
plt.ylabel('MAE')
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
plt.savefig(graphs_directory / f'{run_name}_mae.png')

# reset plots
plt.clf()
plt.cla()
plt.close()

# plot and save each timestamp picture
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

# generate png for each timestamp containing true and pred
filenames = []
for i in range(len(x)):
    # different models produce different shapes, so trying to support everything
    true = pt_file['trues'][0][i][0] if len(pt_file['trues'].shape) == 5 else pt_file['trues'][0][i]
    pred = pt_file['preds'][0][i][0] if len(pt_file['preds'].shape) == 5 else pt_file['preds'][0][i]
    axs[0].imshow(true, cmap='rainbow', origin="lower")
    axs[1].imshow(pred, cmap='rainbow', origin="lower")
    axs[0].set_title('Ground Truth')
    axs[1].set_title('Prediction')
    axs[0].set_xlabel('x_coord')
    axs[0].set_ylabel('y_coord')
    axs[1].set_xlabel('x_coord')
    axs[1].set_ylabel('y_coord')
    plt.suptitle(f'Time Step {x[i]}')
    plt.savefig(pics_temp_directory / f'{i}.png')
    filenames.append(pics_temp_directory / f'{i}.png')

fig.tight_layout()

# make animation
images = []
for filename in filenames:
    images.append(imageio.imread(filename))
animation_file = f'movie_{run_name}.gif'
imageio.mimsave(movie_directory / animation_file, images)

# reset plots
plt.clf()
plt.cla()
plt.close()
```

#### Upload Model and Visualization Files to MLFlow Storage

```python
# send files to MLFlow
mlflow.log_artifacts(str(movie_directory))
mlflow.log_artifacts(str(graphs_directory))

# send model file to mlflow
mlflow.log_artifact(results_dir / model_filename)

# end run
mlflow.end_run()
```


### sage/NDP_Streaming_SAGE_opt.ipynb (8,859 bytes)

# NDP_Streaming_SAGE_opt


<div style="display: flex; align-items: center;">
    <img src="SAGE_logo.jpeg" alt="SAGE Logo" width="300" height="auto" style="margin-right: 10px; vertical-align: middle;">
    <div style="flex: 0 0 auto; margin-left: auto; margin-bottom: 0;">
        <img src="https://www.sci.utah.edu/images/news/2023/sci-30-multi.jpg" alt="Scientific Computing and Imaging Institute Logo" width="150"/>
    </div>
</div>

    


<h1 style="vertical-align: middle; text-align:center;">NSF National Data Platform (NDP)</h1>
<h3 style="text-align: center; margin-top: 0;">Streaming Data from SAGE Pilot</h3>

![SAGE NDP diagram](schema.png)

The figure you've provided outlines a data processing workflow in an IoT environment, utilizing an architecture that connects several components. Here's what each part appears to do:

1. **SAGE**: Represents a software-defined sensor network designed for AI at the edge, presumably for collecting and processing data at the edge. It appears to have an API through which data can be retrieved.

2. **Data Stream Adapter**: This component acts as an adapter that connects the SAGE platform with the R-Pulsar framework. Its function is to receive data from SAGE and convert it into an appropriate format or protocol for use within the R-Pulsar framework.

3. **R-Pulsar Framework**: It is an IoT Edge Framework that extends cloud capabilities to local devices and provides a programming model to decide what data is collected and processed, when, and where. This framework handles the data in real time, possibly performing analysis and making decisions based on the data received from the Data Stream Adapter.

4. **Data Sink Adapter**: Like the Data Stream Adapter, the Data Sink Adapter likely converts and routes the processed data from R-Pulsar into an appropriate format or destination. This destination could be a storage system or a process requiring data for its operation, depicted here as "OSDF Origin."

5. **Metadata Catalog**: As data flows through the system, relevant metadata is logged in a catalog. This step is crucial for data management, as it provides information on the data's origin, its structure, and how and when it was processed.

6. **User & OSDF Origin**: Represents the end-users and other systems that access the data. Users can subscribe to specific data streams within the data streaming platform, allowing them to receive data or notifications. OSDF Origin could be a data archive system, a database, or any other system that needs to consume processed data.

The general data flow is as follows:
- Data is collected by SAGE and passed through its API to the Data Stream Adapter.
- The Data Stream Adapter sends this data to the R-Pulsar Framework.
- Within the R-Pulsar Framework, data may be analyzed, processed, or transformed in real time.
- Then, the processed data are passed to the Data Sink Adapter, which directs them to the appropriate destination, such as OSDF Origin.
- Throughout this process, metadata are logged for use in the metadata catalog.
- End-users can access the data or subscribe to data streams as needed.

**Contact:** Scientific and Computing Imaging Institute, University of Utah ([ivan.rodero@utah.edu](mailto:ivan.rodero@utah.edu))

<div style="display: flex; align-items: center;">
    <img src="https://new.nsf.gov/themes/custom/nsf_theme/components/images/logo/logo-desktop.svg" alt="NSF Logo" width="120" style="margin-right: 10px; vertical-align: middle;">
    <span style="font-size: 10px; margin-top:10px;">The National Data Platform was funded by NSF 2333609 under CI, CISE Research Resources programs. Any opinions, findings, conclusions, or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the funders.</span>
</div>

```python
from basic_functions import get_and_display_consumer_data, stream_and_visualize_data, fetch_recent_active_consumers
import warnings
from IPython.display import display, HTML
import nest_asyncio
nest_asyncio.apply()
```

```python
display(HTML('<style>.output {max-height: 600px; overflow-y: auto; max-width: 100%; overflow-x: auto;}</style>'))
warnings.filterwarnings("ignore", message="The behavior of DataFrame concatenation with empty or all-NA entries is deprecated")
```

```python
KAFKA_HOST = "155.101.6.194"
KAFKA_PORT = "9092"

consumer_ids = await fetch_recent_active_consumers(KAFKA_HOST, KAFKA_PORT)
```

### Real-Time Data Streaming and Visualization

The `stream_and_visualize_data` function is at the heart of our real-time data analysis and visualization tool. It connects to a Kafka topic as a consumer using a given `consumer_id` and streams data in real time. The function then processes and visualizes this data dynamically, providing insights into trends as they occur.

Key components of this function include:
- **Kafka Consumer Initialization**: Establishes a connection to a Kafka topic to consume messages.
- **Data Processing**: Upon receiving data, it parses the JSON payload, extracts relevant information, and updates the data model.
- **Model Training and Prediction**: Utilizes an incremental model to train on the newly arrived data and makes future predictions based on the model.
- **Dynamic Visualization**: Leverages Plotly to plot real-time data and predictions. The visualization includes both historical data and the latest data points to show trends over time.
- **Saving Option**: Optionally, the visualized data can be saved as an HTML file for offline viewing and shared with others.

This approach enables real-time monitoring and forecasting, making it invaluable for applications requiring up-to-the-minute data analysis, such as environmental monitoring, financial market tracking, or IoT device management.

### Visualizing Real-Time Data for a Selected Consumer

After retrieving and displaying the active consumers, we can focus on a specific consumer to visualize their data in real time. By selecting a consumer ID from the previously obtained array of consumer IDs, we can tailor our data visualization to show trends and predictions related to that particular consumer's data stream.

The code snippet below demonstrates how to select the third consumer from our list (noting that Python uses zero-based indexing) and visualize their real-time data along with future predictions:

```python
wind_sensor_w099 = consumer_ids[4]
await stream_and_visualize_data(KAFKA_HOST, KAFKA_PORT, wind_sensor_w099, predictions=20)
```


### streaming/demo-1-earthscope.ipynb (26,047 bytes)

# demo-1-earthscope


<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
    <div style="flex: 0 0 auto; margin-left: 0; margin-bottom: 0; height: 200px; width: 180px">
        <img src="https://www.earthscope.org/app/uploads/2022/11/generic_governance.jpg" alt="Earthscope Logo"/>
    </div>
    <div style="flex: 0 0 auto; margin-left: auto; margin-bottom: 0;">
        <img src="https://nairrpilot.org/app/site/media/ndp.jpg" alt="NDP Logo" width="200"/>
    </div>
</div>

# SciDX Streaming Capabilities Demonstration 

This demonstration showcases the **SciDX Streaming capabilities**, leveraging both the **SciDX POP Library** for managing data objects and the **Streaming Library** for real-time data streaming and processing. 

## Objectives 

We will: 
1. **Register Earthscope data streams** using the SciDX POP Library (*Data Provider*).
2. **Discover and apply filters** to customize data streams for specific use cases (*Data Consumer*).
3. **Consume and visualize real-time data streams**.
  
## Workflow

Below is a diagram illustrating the interaction between the data provider and consumer in the streaming workflow:

![Data Stream Library](data_stream_library.png) 

### Key Components: 
- **POP Library:** Used to register and discover data objects (acts as the Data Provider). Interacts with the POP API to register and manage data objects.
- **Streaming Library:** Used to create, manage, and consume real-time data streams (acts as the Data Consumer). Manages real-time data streams, including applying filters and consuming messages.

## Step 1: Setting Up the POP (Data Provider) and Streaming (Data Consumer) Clients

In this step, we will:
1. **Import necessary modules** for handling data streams.
2. **Initialize the Point of Presence (POP) client** to manage data registration and discoer*).
3. **Initialize the Streaming client** to manage and consume real-time data stmesses.

```python
import asyncio
import time
from scidx_streaming import StreamingClient
from pointofpresence import APIClient
from earthscope_demo import earthscope_topic_metadata, filters, API_URL, USERNAME, PASSWORD, EARTHSCOPE_USERNAME, EARTHSCOPE_PASSWORD
```

Here, we:
1. Initialize the `APIClient` to handle data registration and discovery.
2. Initialize the `StreamingClient` to handle real-time data streams.

```python
# Initialize the POP client for data registration and discovery
client = APIClient(base_url=API_URL, username=USERNAME, password=PASSWORD)

# Initialize the Streaming client for real-time data streaming
streaming = StreamingClient(client)
print(f"Streaming Client initialized. User ID: {streaming.user_id}")
```

## Step 2: Register an Earthscope Data Stream (Data Provider)

In this step, we will use the **POP client**, and the metadata for accessing an **Earthscope data stream**, to register it into our POP.

```python
# Register the Earthscope data stream with the POP client
client.register_kafka_topic(earthscope_topic_metadata)
```

## Step 3: Search for the Registered Earthscope Data Stream (Data Provider) 

Now that we have registered the data stream, we will: 
1. Use the **POP client** to search for datasets using the `search_datasets` method.
2. Verify that the **Earthscope data stream** is correctly registered by searching for it.

This ensures the dataset is discoverable for use by the Data Consumers.

```python
# Search for the registered Earthscope data stream
search_results = client.search_datasets("earthscope_kafka_gnss_observations")
print(f"Number of datasets found: {len(search_results)}")
```

# Transition: From Data Provider to Data Consumer 

The **POP client** (Data Provider) has completed its role in: 
1. Registering the **Earthscope data stream**.
2. Verifying its discoverability.

We now transition to the **Streaming client** (Data Consumer) to: 
1. Create customized data streams by applying filters.
2. Consume and visualize the real-time data.

## Step 4: Create a Stream with Filtered Data from the Earthscope Topic (Data Consumer) 

In this step, we’ll create a Kafka data stream for the registered **Earthscope topic**. The *filtering capabilities* allow us to refine the data stream by applying conditions, alerts, and transformations.

### Filtering Logic Breakdown: 
- **Station Selection**: Filters data to include specific stations (`SNCL`), ensuring the stream only processes data from:
    - **P505.PW.LY_.00**
    - **DHLG.CI.LY_.20**
    - **P159.PW.LY_.00**
- **Alert System**:
  - **High Quality Data (Blue Alert)**: Activated when `Q > 2,000,000`.
  - **Low Quality Data (Red Alert)**: Triggered when `Q ≤ 2,000,000`.
- **Dynamic Rate Adjustment**:
  - For data flagged with a **Red Alert**, the `rate` field is adjusted with a multiplier of `2`.

These filters allow us to isolate meaningful subsets of the data, trigger alerts dynamically, and transform the data stream for more actionable insights.

Here’s the filtering logic applied in this demonstration:
```python
filters = [ 
    "SNCL IN ['P505.PW.LY_.00', 'DHLG.CI.LY_.20', 'P159.PW.LY_.00']", 
    "IF Q > 2000000 THEN alert = blue", 
    "IF Q <= 2000000 THEN alert = red", 
    "IF alert = 'red' THEN rate = 2" 
]
```

```python
# Create a Kafka stream for Earthscope data with filters applied
stream = await streaming.create_kafka_stream(
    keywords=["earthscope_kafka_gnss_observations"],
    match_all=True,
    filter_semantics=filters,
    username=EARTHSCOPE_USERNAME,
    password=EARTHSCOPE_PASSWORD
)

# Retrieve the stream's topic name
topic = stream.data_stream_id
print(f"Stream created: {topic}")
```

## Step 5: Consuming the Filtered Stream Data 

With the Kafka stream created, we now: 
1. Initialize a **data consumer** using the `consume_kafka_messages` method.
2. Start **real-time consumption** of filtered data.

The consumer continuously listens for incoming messages and populates a dynamic DataFrame. 

**Note**: It may take a few seconds for data to populate due to real-time processing.

```python
# Start consuming the filtered Kafka stream
consumer = streaming.consume_kafka_messages(topic)
```

```python
# Display the first 10 rows of the consumed data
consumer.dataframe.head(10)
```

## Step 6: Stopping Data Consumption and Cleaning Up 

To wrap up, we will: 
1. Stop the data consumer to halt data processing.
2. Delete the created stream from the Kafka topic using the Streaming client.
3. Remove the registered dataset using the POP client.

This ensures all resources and background tasks are properly released.

```python
# Stop the Kafka consumer
consumer.stop()

# Delete the Kafka stream
await streaming.delete_stream(stream)

# Delete the registered dataset from the POP system
client.delete_resource_by_id(search_results[0]["id"])
print("Cleanup completed: Stream and registered dataset deleted.")
```


### streaming/demo-2-sage.ipynb (22,727 bytes)

# demo-2-sage


<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
    <div style="flex: 0 0 auto; margin-left: 0; margin-bottom: 0;">
        <img src="https://naise.northwestern.edu/images/sage-logo-410x410-1-360x200.jpg" alt="SAGE Logo"/>
    </div>
    <div style="flex: 0 0 auto; margin-left: auto; margin-bottom: 0;">
        <img src="https://nairrpilot.org/app/site/media/ndp.jpg" alt="NDP Logo" width="200"/>
    </div>
</div>

# SciDX Streaming Capabilities Demonstration 

This demonstration showcases the **SciDX Streaming capabilities**, leveraging both the **SciDX POP Library** for managing data objects and the **Streaming Library** for real-time data streaming and processing. 

## Objectives 

We will:
1. **Register SAGE sensor data streams** with the SciDX POP Library (*Data Provider*).
2. **Discover and apply filters** to customize data streams for specific use cases (*Data Consumer*).
3. **Consuming and visualizing real-time data streams**.

## Workflow

Below is a diagram illustrating the interaction between the data provider and consumer in the streaming workflow:

![Data Stream Library](data_stream_library.png) 

### Key Components: 
- **POP Library:** Used to register and discover data objects (acts as the Data Provider). Interacts with the POP API to register and manage data objects.
- **Streaming Library:** Used to create, manage, and consume real-time data streams (acts as the Data Consumer). Manages real-time data streams, including applying filters and consuming messages.

## Step 1: Setting Up the POP (Data Provider) and Streaming (Data Consumer) Clients

In this step, we will:
1. **Import necessary modules** for handling data streams.
2. **Initialize the Point of Presence (POP) client** to manage data registration and discovery.
3. **Initialize the Streaming client** to manage and consume real-time data streams.

```python
# Import the sciDX client and demo-specific modules
from scidx_streaming import StreamingClient
from pointofpresence import APIClient
from sage_demo import sensor_data, filters, API_URL, USERNAME, PASSWORD
```

Here, we:
1. Initialize the `APIClient` to handle data registration and discovery.
2. Initialize the `StreamingClient` to handle real-time data streams.

```python
# Initialize the POP client for data registration and discovery
client = APIClient(base_url=API_URL, username=USERNAME, password=PASSWORD)

# Initialize the Streaming client for real-time data streaming
streaming = StreamingClient(client)
print(f"Streaming Client initialized. User ID: {streaming.user_id}")
```

## Step 2: Registering Sensor Data from multiple SAGE nodes (Data Provider)

In this step, we will use the **POP client**, and the metadata for accessing **BME280 sensors data**, to register it into our POP. Each sensor’s data will be registered as a unique resource with its respective URL.

### Data Streams
- **Temperature**
- **Pressure**
- **Humidity**

```python
# Register each sensor data stream from the `sensor_data` list
for sensor in sensor_data:
    client.register_url(sensor)
```

## Step 3: Search for  the Registered BME280 Sensor Data (Data Provider) 

Now that we have registered the BME280 sensor data, we will:
1. Use the **POP client** to search for datasets using the `search_datasets` method.
2. Verify that the **BME280 sensors** are correctly registered by searching them.

This ensures the datasets are discoverable for use by the Data Consumers.

```python
# Search for all registered BME280 sensor datasets
search_results = client.search_datasets("sage_demo_bme280")
print(f"Number of datasets found: {len(search_results)}")
```

## Step 4: Create a Stream with Filtered Data from the SAGE BME280 registered sensors (Data Consumer)

In this step, we’ll create a Kafka data stream on sciDX with filters to select specific data and apply custom alerts. Here’s how the data is filtered and transformed:

- **State Selection**: Filters to only include data from California, Montana, Oregon, North Dakota, Michigan, and Illinois.
- **Data Mapping**: Maps sensor readings to temperature, pressure, and humidity fields.
- **State Assignment**: Associates each sensor with its corresponding state name.
- **Conditional Alerts**:
  - **Heatwave Alert**: Activates if temperature > 35°C or humidity < 25%.
  - **State-Specific Alerts**: Certain states have unique temperature thresholds that will trigger alerts:
    - Montana: Temperature > 40°C
    - Oregon: Temperature > 30°C
  - **Pressure Alert**: Activates if pressure exceeds 101,000 Pa.
- **Pressure Adjustment**: For certain temperature alerts, reduces pressure readings by 5%.

These filters allow us to isolate meaningful subsets of the data, trigger alerts dynamically, and transform the data stream for more actionable insights.

```python
# Create the Kafka stream using sciDXClient with specified filters for SAGE data
stream = await streaming.create_kafka_stream(
    keywords=["sage_demo"],
    match_all=True,
    filter_semantics=filters
)

# Retrieve the stream's topic name
topic = stream.data_stream_id
print(f"Stream created: {topic}")
```

## Step 5: Consuming the Filtered Stream Data 

With the Kafka stream created, we now: 
1. Initialize a **data consumer** using the `consume_kafka_messages` method.
2. Start **real-time consumption** of filtered data.

The consumer continuously listens for incoming messages and populates a dynamic DataFrame. 

**Note**: It may take a few seconds for data to populate due to real-time processing.

```python
# Start consuming Kafka messages from the created topic
consumer = streaming.consume_kafka_messages(topic)
```

```python
# Display the first 10 rows of the consumed data
consumer.dataframe.head(10)
```

## Step 6: Stopping Data Consumption and Cleaning Up 

To wrap up, we will: 
1. Stop the data consumer to halt data processing.
2. Delete the created stream from the Kafka topic using the Streaming client.
3. Remove the registered dataset using the POP client.

This ensures all resources and background tasks are properly released.

```python
# Stop the Kafka consumer
consumer.stop()

# Delete the Kafka stream
await streaming.delete_stream(stream)

# Delete all registered datasets from the POP system
for result in search_results:
    client.delete_resource_by_id(result["id"])
    print(f"Deleted dataset with ID: {result['id']}")

print("Cleanup completed: All registered datasets deleted.")
```


### streaming/streaming-py/README.md (3,068 bytes)

# scidx Streaming

A Python library for managing streaming data using the sciDX platform and a Point of Presence. This library provides easy-to-use methods for creating, consuming, and managing Kafka streams and related resources.


## Table of Contents

- [Installation](https://github.com/sci-ndp/streaming-py/blob/main/README.md#installation)
- [Tutorial](https://github.com/sci-ndp/streaming-py/blob/main/README.md#tutorial)
- [Running Tests](https://github.com/sci-ndp/streaming-py/blob/main/README.md#running-tests)
- [Configuration](https://github.com/sci-ndp/streaming-py/blob/main/README.md#configuration)
- [Contributing](https://github.com/sci-ndp/streaming-py/blob/main/README.md#contributing)
- [License](https://github.com/sci-ndp/streaming-py/blob/main/README.md#license)
- [Contact](https://github.com/sci-ndp/streaming-py/blob/main/README.md#contact)


## Installation

Ensure you have Python 3.7 or higher installed. Using a virtual environment is recommended.

### Option 1: Install from GitHub

1. **Clone the repository:**

   ```bash
   git clone https://github.com/sci-ndp/streaming-py.git
   cd streaming-py
   ```
2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. **Install the package in editable mode:**

   ```bash
   pip install -e .
   ```
4. **Install development dependencies (optional, for testing):**

   ```bash
   pip install -r requirements.txt
   ```

### Option 2: Install via pip

Once the package is published on PyPI, you can install it directly using pip:

```
pip install scidx_streaming
```

## Tutorial

For a step-by-step guide on how to use the `streaming` library, check out our comprehensive tutorial: [10 Minutes for Streaming POP Data](https://github.com/sci-ndp/streaming-py/blob/main/docs/streaming_tutorial.ipynb).


## Running Tests

To run the tests, navigate to the project root and execute:

```bash
pytest
```

## Configuration

To configure the library, you need to set the API URL for your POP API instance. This can be done by initializing the `APIClient` with the appropriate URL:

```python
from streaming import StreamingClient
from pointofpresence import APIClient

API_URL = "http://your-api-url.com"
USERNAME = "placeholder"
USERNAME = "placeholder"

client = APIClient(base_url=API_URL, username=USERNAME, password=PASSWORD)
streaming = StreamingClient(pop_client=client)
```

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the repository**
2. **Create a new branch** (`git checkout -b feature/new-feature`)
3. **Make your changes** and **commit** (`git commit -m 'Add new feature'`)
4. **Push** to the branch (`git push origin feature/new-feature`)
5. **Open a Pull Reques**


## License

This project is licensed under the MIT License. See [LICENSE.md](https://github.com/sci-ndp/streaming-py/blob/main/docs/LICENSE.md) for more details.

## Contact

For any questions or suggestions, please open an [issue](https://github.com/sci-ndp/streaming-py/blob/main/docs/issues.md) on GitHub.


### streaming/streaming-py/docs/streaming_tutorial.ipynb (7,257 bytes)

# streaming_tutorial


# 10 Minutes for Streaming from a POP

Welcome to the **10 Minutes for Streaming from a POP** tutorial! This notebook demonstrates the core functionalities of the `scidx_streaming` library, which allows you to create and interact with streaming data using the sciDX platform and a Point of Presence.

In this tutorial, you will learn how to:
1. Set up the library and authenticate with the API.
2. Create, consume, and manage Kafka streams.
3. Use filter semantics for advanced data processing.


## 1. Setting Up

Ensure you have Python 3.7 or higher installed. Use the following steps to install the library and its dependencies:

### Step 1: Install the Library
```bash
!pip install scidx_streaming
```

Or, if you're working in a virtual environment and have cloned the repository, you can install it by running the following command in the root folder:
```bash
!pip install -e .
!pip install -r requirements.txt
```


### Step 2: Enter API Credentials

To start using the library, configure the `APIClient` with your API URL and credentials. You need either:

1. The base URL where the POP API is hosted, and valid username and password for authentication.
2. A valid token for authentication.

#### Option 1: Username and Password Authentication

Use the following code to configure the client using your username and password:

```python
from getpass import getpass

# Prompt the user for API credentials
api_base_url = input("Enter the POP API base URL (include http:// or https://): ")
api_username = input("Enter your POP API username: ")
api_password = getpass("Enter your POP API password: ")
api_token=None
```

#### Option 2: Token-Based Authentication

If you already have a token, you can use it directly instead of providing a username and password:

```python
# Prompt the user for API credentials
api_base_url = input("Enter the POP API base URL (include http:// or https://): ")
api_token = input("Enter your POP API token: ")
api_username=None
api_password=None
```

## 2. Initializing the Client

Now that you have the required credentials, you can import and configure the `pointofpresence` client and the `scidx_streaming` client with it:

```python
from scidx_streaming.client.init_client import StreamingClient
from pointofpresence import APIClient

# Initialize the API client
client = APIClient(base_url=api_base_url, username=api_username, password=api_password, token=api_token)

# Initialize the Streaming client
streaming = StreamingClient(pop_client=client)
print(f"User ID: {streaming.user_id}")
```


## 3. Creating Kafka Streams

You can create Kafka streams with specific keywords and filter semantics. Filter semantics enable advanced processing of streaming data.

### Example: Create a Kafka Stream
```python
# Define the stream configuration
stream_config = {
    "keywords": ["example_keyword", "CSV"],
    "match_all": True,
    "filter_semantics": [
        "window_filter(5, mean, fixed acidity > 8.7)",
        "residual sugar > 1.5",
        "IF window_filter(9, sum, residual sugar > 20) THEN alert = fixed_acidity * 100 ELSE fixed_acidity = fixed_acidity * 1000",
        "IF alert IN ['blue'] THEN residual_sugar = fixed_acidity * 100"
    ]
}

# Create the stream
result = await streaming.create_kafka_stream(
    keywords=stream_config["keywords"],
    filter_semantics=stream_config["filter_semantics"],
    match_all=stream_config["match_all"]
)

print(f"Stream created: {result['topic']}")
print(f"Involved data objects: {result['involved_streams']}")
```


## 4. Consuming Messages from Kafka Streams

Once a stream is created, you can consume messages in real time.

### Example: Consume Kafka Messages
```python
# Consume messages from the Kafka topic
topic = result["topic"]
consumer = streaming.consume_kafka_messages(topic)

try:
    start_time = time.time()
    while True:
        if time.time() - start_time > 30:
            print("Timeout reached while waiting for messages.")
            break

        if not consumer.dataframe.empty:
            print("Dataframe received:")
            print(consumer.dataframe.head())
            break

        await asyncio.sleep(1)
finally:
    consumer.stop()
```


## 4. Deleting Kafka Streams

You can delete a Kafka stream when it is no longer needed.

### Example: Delete a Kafka Stream
```python
# Delete the Kafka stream
response = await streaming.delete_stream(topic)
print(f"Stream {topic} deleted successfully.")
```


## Running Tests

To validate the library's functionalities, you can run the test suite:

```bash
pytest
```


## Conclusion

You have learned how to:
1. Create Kafka streams with custom configurations.
2. Consume messages from Kafka topics.
3. Delete streams when they are no longer needed.

For more details, check the official documentation and [GitHub repository](https://github.com/sci-ndp/streaming-py).


### streaming/streaming-py/tests/streaming_demo_notebook.ipynb (6,857 bytes)

# streaming_demo_notebook


# Streaming Capabilities Demonstration


This notebook demonstrates how to test the streaming capabilities of the `StreamingClient`. It includes creating Kafka streams, consuming messages, and deleting streams. Sensitive information like usernames and passwords has been replaced with placeholders.

## Setup


Ensure you have the required dependencies installed and a valid API URL. The provided credentials should also be correct for the specific streams you want to test.

```python
# Required Libraries
import asyncio
import logging
from streaming import StreamingClient
from pointofpresence import APIClient
import time

# Constants
API_URL = "http://155.101.6.190:8002"
USERNAME = "placeholder"  # Replace with your username
PASSWORD = "placeholder"  # Replace with your password

# Stream configurations
streams_to_test = [
    {
        "keywords": "pinguintest,CSV",
        "match_all": True,
        "filter_semantics": [
            "window_filter(5, mean, fixed acidity > 8.7)",
            "residual sugar > 1.5",
            "IF window_filter(9, sum, residual sugar > 20) THEN alert = fixed acidity*100 ELSE fixed acidity = fixed acidity*1000",
            "IF alert IN ['blue'] THEN residual sugar = fixed acidity*100"
        ],
    },
    {
        "keywords": "earthscope_kafka_gnss_observations,kafka",
        "match_all": True,
        "filter_semantics": [],
        "username": "<earthscope_username>",  # Replace with the Earthscope stream username
        "password": "<earthscope_password>"   # Replace with the Earthscope stream password
    },
    {
        "keywords": "pokemon",
        "match_all": True,
        "filter_semantics": ["name IN ['sturdy', 'damp', 'limber']", "IF name = 'sturdy' THEN alert = red"]
    }
]
```

## Initialize Clients


Here, we initialize the `APIClient` and `StreamingClient` that will handle the streams.

```python
# Initialize API Client
client = APIClient(base_url=API_URL, username=USERNAME, password=PASSWORD)

# Initialize Streaming Client
streaming = StreamingClient(pop_client=client)
print(f"User ID: {streaming.user_id}")
```

## Test Stream Creation, Consumption, and Deletion


In this section, we:
1. Create Kafka streams.
2. Consume messages from the topics.
3. Delete the streams after processing.

```python

async def test_create_and_consume_multiple_kafka_streams():
    for stream_config in streams_to_test:
        # Step 1: Create the Kafka stream
        result = await streaming.create_kafka_stream(
            keywords=stream_config.get("keywords", "").split(","),
            filter_semantics=stream_config.get("filter_semantics", []),
            match_all=stream_config.get("match_all", True),
            username=stream_config.get("username", None),
            password=stream_config.get("password", None)
        )

        if "error" in result:
            print(f"Error creating stream: {result['error']}")
            continue

        # Extract the topic and involved streams
        topic = result["topic"]
        involved_streams = result["involved_streams"]

        print(f"Stream created: {topic}")
        print(f"Involved streams: {involved_streams}")

        # Step 2: Consume messages from the Kafka topic
        print("\nConsuming messages from the Kafka topic...")
        consumer = streaming.consume_kafka_messages(topic)

        try:
            start_time = time.time()
            while True:
                if time.time() - start_time > 180:
                    print("Timeout reached while waiting for messages.")
                    break

                if not consumer.dataframe.empty:
                    print("Dataframe received:")
                    print(consumer.dataframe.head())
                    break

                await asyncio.sleep(1)
        finally:
            # Stop the consumer
            print("\nStopping the Kafka consumer...")
            consumer.stop()

        # Step 3: Delete the created Kafka stream
        print("\nDeleting the Kafka stream...")
        try:
            response = await streaming.delete_stream(topic)
            print(response["message"])
        except Exception as e:
            print(f"Error deleting stream {topic}: {e}")

        time.sleep(10)  # Wait some seconds to let the consumer clear its data

# Run the test
await test_create_and_consume_multiple_kafka_streams()
```


### utah_demos/Earthscope/final_earthscop.ipynb (12,526 bytes)

# final_earthscop


<div style="display: flex; align-items: center; margin-bottom: 20px;">
    <img src="https://www.earthscope.org/app/uploads/2022/11/EarthScope_Logo-color.png" alt="EarthScope Consortium Logo" style="width: 600px; margin-top: 10px;">
    <img src="NDP logo.png" alt="NDP Logo" style="width: 200px; height: auto; margin-left: auto;">
</div>

# NSF National Data Platform (NDP)

## Streaming Data from EarthScope Consortium and Doing One-Class SVM on data

The EarthScope Consortium ([www.earthscope.org](https://www.earthscope.org)) is dedicated to supporting transformative global geophysical research and education, operating the NSF's Geodetic GAGE and Seismic SAGE facilities. This includes operating a network of nearly a thousand GNSS stations, processing data for a range of geophysical phenomena.

---
<div style="text-align: right; padding: 5px;">
    <p><strong>Contact:</strong> Scientific and Computing Imaging Institute, University of Utah (<a href="mailto:saleem.alharir@utah.edu">saleem.alharir@utah.edu</a>)</p>
</div>

<div style="display: flex; align-items: center; justify-content: flex-start; margin-top: 20px; border-top: 1px solid #ccc; padding-top: 20px;">
    <img src="https://new.nsf.gov/themes/custom/nsf_theme/components/sdc-components/molecules/logo/logo-desktop--white.svg" alt="NSF Logo" style="width: 120px; margin-right: 10px;">
    <p style="font-size: 12px;">The National Data Platform was funded by NSF 2333609 under CI, CISE Research Resources programs. Any opinions, findings, conclusions, or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the funders.</p>
</div>

---
>

<div style="text-align: center;">
    <h1>NSF National Data Platform (NDP)</h1>
    <h2>Streaming Data from EarthScope Consortium</h2>
</div>

The EarthScope Consortium ([www.earthscope.org](https://www.earthscope.org)) streams three-dimensional Global Navigation Satellite System (GNSS) high rate (1hz) position time series from nearly a thousand EarthScope and related GNSS stations. These high precision ground-motion time series are used to study a range of geophysical phenomena including earthquakes, volcanos, tsunamis, hydrologic loads, and glaciers. EarthScope is dedicated to supporting transformative global geophysical research and education through operation of the National Science Foundation’s (NSF) Geodetic GAGE and Seismic SAGE facilities. As part of the National Data Platform (NDP) EarthScope pilot project, the EarthScope GNSS position time series streams are being stored and made available from Data Collaboratory Kafka servers at the University of Utah. This Jupyter Notebook provides tools for access and plotting of sample real time streams and is the foundation for additional services being developed that will facilitate time series analysis including machine learning. 

#### Users of EarthScope data agree to follow the [EarthScope streaming data policy](https://www.unavco.org/data/policies_forms/data-policy/data-policy-realtime-streaming-gps/data-policy-realtime-streaming-gps.html).

---
<div style="text-align: right; padding: 5px;">
    <p><strong>Contact:</strong> Scientific and Computing Imaging Institute, University of Utah (<a href="mailto:saleem.alharir@utah.edu">saleem.alharir@utah.edu</a>)</p>
</div>

<div style="display: flex; align-items: center; justify-content: flex-start; margin-top: 20px; border-top: 1px solid #ccc; padding-top: 20px;">
    <img src="https://new.nsf.gov/themes/custom/nsf_theme/components/sdc-components/molecules/logo/logo-desktop--white.svg" alt="NSF Logo" style="width: 120px; margin-right: 10px;">
    <p style="font-size: 12px;">The National Data Platform was funded by NSF 2333609 under CI, CISE Research Resources programs. Any opinions, findings, conclusions, or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the funders.</p>
</div>

---

This step provides an example of retrieving a streaming dataset, specifying the dataset name with an EarthScope “SNCL” code. For example, "csci_ci_ly__20". The location of the GNSS station corresponding to the SNCL code is plotted on an interactive map.

**SNCL Code Breakdown:**
- `csci`: GNSS station 4-character ID.
- `ci`: Network code indicating Caltech.
- Other sources include `pb` for NOTA/EarthScope, `bk` for U.C. Berkeley, and `pw` for CWU.
- `ly_`: Common for all GNSS streams.
- Last two integers: Processing Package followed by Solution Type.

**Processing Package and Solution Type:**
- There can be more than one processing stream from each GNSS station as indicated by the following processing package and solution type codes.
- Packages used include the CWU server Fastlane (0), Trimble server PIVOT/RTX (1),RTNet server (2), Septentrio on-board (3), Trimble RTX on board (4),and Network solution combining RTNet's RTK and PPPAR, and Trimble RT data (5).
- Solution Types include PPP/AR (0), DIF/RTK (1), PPP/AR COMPLETE (2) and PPP/AR FAST+COMPLETE (3).

```python
from ndpearthscope import process_datasets, plot_station_location
from IPython.display import display 

# Define the list of dataset names you wish to process
dataset_names = ["csci_ci_ly__201"]  # Replace these with actual dataset names

# Process the datasets
datasets_details = process_datasets(dataset_names)

# Initialize an empty list to store file paths
file_paths = []
# Example: Plotting the location of the first dataset
if datasets_details:  # Check if the list is not empty
    first_dataset_details = datasets_details[0]
    latitude = first_dataset_details['latitude']
    longitude = first_dataset_details['longitude']
    station_name = first_dataset_details['dataset_name']
    bootstrap_server = first_dataset_details['bootstrap_server']
    topic = first_dataset_details['topic']
    file_path = first_dataset_details['file_path']
    # Save the file path for later use
    file_paths.append(file_path)   
    # Save the file path for later use
    file_paths.append(file_path)
    # Plot and display the station location in one line
    station_map = plot_station_location(latitude, longitude, station_name)
    display(station_map)
```

## Anomaly Detection in GPS Data

This phase of the analysis involves leveraging a subset of the collected GPS data to identify potential anomalies. Here's what happens:

- **Data Subset**: Utilizes the first 10,000 rows from the downloaded 1Hz dataset.
- **File Path**: `File_path` should be specified as the path to your dataset, which is assumed to be located in the same directory as this notebook.
- **Anomaly Detection**: Implements a One-Class SVM (Support Vector Machine) Anomaly Detection algorithm. This sophisticated technique is designed to detect and highlight outliers within the dataset.
- **Visualization**: Outliers identified by the algorithm are distinctly marked in red on the plot, making it easier to spot any anomalies in the GPS data.

This approach not only facilitates the early detection of irregularities but also aids in understanding the data's underlying patterns and integrity.

---

```python
from ndpearthscope import detect_and_visualize_anomalies
nrows = 10000
nu = 0.01
detect_and_visualize_anomalies(file_path,nrows,nu)
```

## Real-Time Data Streaming and Visualization

This section establishes a connection to the Data Collaboratory Kafka server by creating a Kafka Consumer. It focuses on visualizing geospatial data in real-time, particularly:

- **Three components of displacement** are plotted in real-time.
- **Time Frame**: The visualization covers the last 60 seconds of data.

To control the data flow and visualization, utilize the **Jupyter notebook stop button** to halt the plotting process as needed.

This real-time data streaming and visualization provide valuable insights into the dynamic changes occurring in the monitored geophysical phenomena, facilitating immediate analysis and decision-making.

---

```python
from ndpearthscope import consume_and_plot_kafka_data
consume_and_plot_kafka_data(topic, bootstrap_server)
```

## 3D Real-time GPS Data Visualization

In this segment, we establish a Kafka Consumer to interface with our streaming data infrastructure. This setup enables:

- **3D Visualization**: Leveraging real-time GPS data to render dynamic three-dimensional plots.
- **Interactivity**: Users can initiate or halt the data visualization process at any time using the **Jupyter notebook stop button**.

This approach allows for an immersive exploration of GPS data, providing an intuitive understanding of spatial dynamics as they unfold in real-time.

---

```python
from ndpearthscope import consume_and_plot_kafka_data_3d
consume_and_plot_kafka_data_3d(topic, bootstrap_server)
```


### utah_demos/NOAA/time_query.ipynb (8,542 bytes)

# time_query


![alt text](NOAAWFSlide.png "Title")

**Import Modules**

```python
from scidx.client import sciDXClient, TimeDirection
import numpy as np
import matplotlib.pyplot as plt
```

**API Socket and Credentials**

```python
api_url="https://dataspaces.ndp.utah.edu/pop"
```

**Establish server connection**

```python
# Initialize the client
client = sciDXClient(api_url)
```

**Search Parameters** - parameters that identify the resource or resources being staged. The user provides a `source` dataset (the RadC dataset for the GOES-18 satellite, in this case), a nearest `timestamp` and a direction in time to search (i.e. the nearest available data to `timestamp` in the `PAST` or `FUTURE`).

```python
source = 'goes18-radc'
timestamp = '2024-08-02T00:35:00'
time_direction = TimeDirection.PAST
```

**Subsetting Parameters** - parameters that guide the server-side subsetting of matching data. In this case, the user gives a `var_name`, which specifies the array inside the resource to subset, and lower- and upper- bound indices. These parameters are interpreted by resource type-specific handler module in DataSpaces, which is chosen based on prior registration parameters.

```python
var_name = 'Rad'
lb = (0,2500)
ub = (1499,4999)
```

**Query** - search for resources, do a server-side download and subset, receive the results.

```python
result = client.query_array(source=source,
                       var_name=var_name,
                       lb=lb, 
                       ub=ub, 
                       timestamp=timestamp,
                       time_direction=time_direction)
```

**Handle results** - the return value is a list of tuples, one per found resource.

```python
(radiance, res_tstamp, res_metadata) = result[0]
print(res_tstamp, res_metadata)
```

### Visualize Results

```python
def viz_radiance(radiance):
    # Define some constants needed for the conversion. From the pdf linked above
    Esun_Ch_01 = 726.721072
    Esun_Ch_02 = 663.274497
    Esun_Ch_03 = 441.868715
    d2 = 0.3
    # Apply the formula to convert radiance to reflectance
    ref = (radiance * np.pi * d2) / Esun_Ch_02

    # Make sure all data is in the valid data range
    ref = np.maximum(ref, 0.0)
    ref = np.minimum(ref, 1.0)

    # Apply the formula to adjust reflectance gamma
    ref_gamma = np.sqrt(ref)

    # Plot gamma adjusted reflectance
    fig = plt.figure(figsize=(4,4),dpi=200)
    im = plt.imshow(ref_gamma, vmin=0.0, vmax=1.0, cmap='Greys_r')
    cb = fig.colorbar(im, orientation='horizontal')
    cb.set_ticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
    cb.set_label('Reflectance')
    plt.show()
```

### Generate Visualization
West Coast radiance visualization

```python
viz_radiance(radiance)
```

### Change the time direction
Query with the same `timestamp`, but ask for the next nearest `FUTURE` result.

```python
result = client.query_array(source=source,
                       var_name=var_name,
                       lb=lb, 
                       ub=ub, 
                       timestamp=timestamp,
                       time_direction=TimeDirection.FUTURE)
(radiance, res_tstamp, res_metadata) = result[0]
print(res_tstamp, res_metadata)
```

```python
viz_radiance(radiance)
```

### Query for all the resources within a time range
Query a 15 minute interval

```python
start_time='2024-08-02T00:30:00'
end_time='2024-08-02T00:45:00'
results = client.query_array(source=source,
                       var_name=var_name,
                       lb=lb, 
                       ub=ub, 
                       start_time=start_time,
                       end_time=end_time)
```

```python
for result in results:
    (radiance, res_tstamp, res_metadata) = result
    print(res_tstamp, res_metadata)
```

### Print result metadata
RadC produces data every 5 minutes, so we see three results in our 15 minute interval.


### utah_demos/sage/scidx-sage-streaming.ipynb (11,329 bytes)

# scidx-sage-streaming


<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
    <div style="flex: 0 0 auto; margin-left: 0; margin-bottom: 0; width: 300px; height: 200px; ">
        <img src="https://www.anl.gov/sites/www/files/2020-05/SAGE-image.jpg" alt="SAGE Logo"/>
    </div>
    <div style="flex: 0 0 auto; margin-left: auto; margin-bottom: 0;">
        <img src="https://nairrpilot.org/app/site/media/ndp.jpg" alt="NDP Logo" width="200"/>
    </div>
</div>

# SciDX SAGE Streaming Tutorial

In this tutorial, we will stream and manage data from **SAGE sensors** using the **SciDX platform**. You will learn to how to register, filter, and process real-time data streams efficiently.

This tutorial covers:

1. **Registering SAGE sensor data streams** with the sciDX API.
2. **Applying filters** to customize data streams for specific needs.
3. **Consuming and visualizing real-time data** to analyze sensor data dynamically.

### Initilizing

## Step 1: Setting Up the sciDX Client and Logging In

To start, we’ll import the necessary modules, set up our API URL and credentials, and then initialize the sciDX client. This client will allow us to interact with the sciDX platform for registering and consuming sensor data.

```python
# Import the sciDX client and demo-specific modules
from scidx import sciDXClient
from sage_demo import sensor_data, filters, SageDataProcessing, plot_temp_alerts

# Define URL of the sciDX API
API_URL = "https://vdc-192.chpc.utah.edu/scidx"

# Set user credentials
username = "demo@sage.com"
password = "sage"
```

```python
# Initialize the sciDXClient with the API URL
client = sciDXClient(API_URL)

# Log in to the sciDX platform using the provided username and password
client.login(username, password)
```

## Step 2: Registering BME280 Sensor Data from multiple SAGE nodes

In this step, we’ll register data streams from BME280 sensors, specifically for temperature, pressure, and humidity, into sciDX. Each sensor’s data will be registered as a unique resource with its respective URL.

### Data Streams
- **Temperature**
- **Pressure**
- **Humidity**

```python
# Register each sensor data stream from the `sensor_data` list
for sensor in sensor_data:
    response = client.register_url(
        resource_name=sensor['resource_name'],
        resource_title=sensor['resource_title'],
        owner_org=sensor['owner_org'],
        resource_url=sensor['resource_url'],
        file_type=sensor['file_type']
    )
    print(f"{sensor['resource_title']} registered successfully with ID: {response['id']}")
```

## Step 3: Searching for Registered BME280 Sensor Data

With the BME280 sensor data registered, we can now search for these resources on the sciDX platform. Using the prefix `sage_demo_bme280`, we’ll retrieve all datasets related to this sensor.

```python
# Search for all registered BME280 sensor datasets
search_results = client.search_resource(search_term="sage_demo_bme280")
print(f"Number of datasets found: {len(search_results)}")
```

## Step 4: Creating and Filtering a Data Stream Using sciDX Filtering Capabilities

In this step, we’ll create a Kafka data stream on sciDX with filters to select specific data and apply custom alerts. Here’s how the data is filtered and transformed:

- **State Selection**: Filters to only include data from California, Montana, Oregon, North Dakota, Michigan, and Illinois.
- **Data Mapping**: Maps sensor readings to temperature, pressure, and humidity fields.
- **State Assignment**: Associates each sensor with its corresponding state name.
- **Conditional Alerts**:
  - **Heatwave Alert**: Activates if temperature > 35°C or humidity < 25%.
  - **State-Specific Alerts**: Certain states have unique temperature thresholds that will trigger alerts:
    - Montana: Temperature > 40°C
    - Oregon: Temperature > 30°C
  - **Pressure Alert**: Activates if pressure exceeds 101,000 Pa.
- **Pressure Adjustment**: For certain temperature alerts, reduces pressure readings by 5%.

These filters give us a tailored view of the data, isolating specific conditions and providing custom alerts.

```python
# Create the Kafka stream using sciDXClient with specified filters for SAGE data
stream_response = client.create_kafka_stream(
    keywords=["sage_demo"], 
    filter_semantics=filters
)

print("Stream Created. Topic:", stream_response['topic'])
```

## Step 5: Consuming the Filtered Stream Data

With the Kafka stream created and filters applied, we can now start consuming the filtered data in real time. Our consumer will listen continuously to incoming messages and populate a dynamic DataFrame as new data arrives.

```python
# Start consuming Kafka messages from the created topic
consumer = client.consume_kafka_messages(topic=stream_response['topic'])
```

#### Viewing a Simple Data Summary

We can view a summary of the latest data received, focusing on selected columns. The summary will also show the current total rows and columns.

```python
# Display a summary of the raw received data
consumer.summary(['timestamp', 'state', 'alert', 'temperature', 'humidity', 'pressure'])
```

## Step 6: Processing and Visualizing Data

With data now being consumed, let’s set up a processor to organize and analyze the stream for easy viewing.

```python
# Set up the data processor
processor = SageDataProcessing(consumer)
```

### Viewing Processed Data

Let’s view the latest 5 rows of the processed and aggregated data to see a snapshot of our current data.

```python
processor.get_aggregated_df().tail(5)
```

## Step 7: Stopping Data Consumption and Processing

To wrap up, we’ll stop the data consumer and processor, ending the data flow and background tasks.

```python
# Stop the data consumer and processor
processor.stop()
consumer.stop()
```

#### Cleaning Up Resources

Finally, we’ll delete the registered entries for the SAGE sensors to free up resources on the sciDX platform. This cleanup ensures that no unused resources remain after this tutorial.

```python
# Get the resource IDs from the search results
resource_ids = [result['id'] for result in search_results]

# Delete both resources using the sciDXClient's delete_resource method
for resource_id in resource_ids:
    delete_response = client.delete_resource(resource_id)
    print(f"Deleted resource {resource_id}: {delete_response}")
```

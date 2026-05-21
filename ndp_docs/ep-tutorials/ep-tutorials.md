# ep-tutorials


### README.md (2,237 bytes)

# NDP-EP Tutorials

A comprehensive library of tutorials and demos for the National Data Platform - EndPoint (NDP-EP).

## Overview

NDP-EP is a data management platform that enables researchers and developers to work with datasets, streaming data, and cloud resources through a unified interface. This repository provides hands-on tutorials covering all aspects of the platform.

## What is NDP-EP?

NDP-EP consists of three main components:

- **REST API**: Backend service for managing datasets, organizations, resources (S3, Kafka topics, URLs), and services across CKAN environments
- **Python Library** ([ndp-ep](https://github.com/sci-ndp/ndp-ep-py)): A Python client providing a simplified interface for API interactions
- **Frontend** ([ep-frontend](https://github.com/national-data-platform/ep-frontend)): React-based administrative console for managing NDP-EP instances

## Repository Structure

```
ep-tutorials/
├── api/          # Direct REST API tutorials
├── python/       # Python library (ndp-ep) tutorials
├── frontend/     # Dashboard/UI tutorials
└── examples/     # Complete demo applications
```

## Getting Started

### Prerequisites

- Python 3.8+ (for Python tutorials)
- Access to an NDP-EP API instance
- ndp-ep library: `pip install ndp-ep`

### Quick Links

| Section | Description |
|---------|-------------|
| [API Tutorials](./api/) | Learn to interact directly with the REST API |
| [Python Tutorials](./python/) | Use the ndp-ep library for programmatic access |
| [Frontend Tutorials](./frontend/) | Navigate and use the administrative console |
| [Examples](./examples/) | End-to-end demo applications |

## Related Resources

- [ndp-ep Python Library](https://github.com/sci-ndp/ndp-ep-py)
- [EP Frontend](https://github.com/national-data-platform/ep-frontend)
- [National Data Platform](https://nationaldataplatform.org/)

## Contributing

Contributions are welcome! When adding new tutorials:

1. Place tutorials in the appropriate folder based on topic
2. Include a clear title and objective
3. List prerequisites
4. Provide step-by-step instructions with code examples
5. Show expected outputs/results
6. Add troubleshooting tips when applicable

## License

MIT License


### api/01-getting-started.md (5,187 bytes)

# Getting Started with the NDP-EP REST API

This tutorial covers how to interact directly with the NDP-EP REST API using HTTP requests.

## Prerequisites

- Access to an NDP-EP API instance
- curl, Postman, or any HTTP client
- Valid authentication token (for write operations)

## Base URL

All API requests are made to your NDP-EP instance URL:

```
https://your-api-endpoint.com
```

## Authentication

Most read operations are public, but write operations require authentication using a Bearer token:

```bash
curl -H "Authorization: Bearer YOUR_TOKEN" https://your-api-endpoint.com/endpoint
```

## Read Operations (No Authentication Required)

### Get System Status

Check the API status and configuration:

```bash
curl https://your-api-endpoint.com/status
```

**Response:**
```json
{
  "api_version": "0.4.0",
  "organization": "ORGANIZATION-NAME",
  "ep_name": "EP-NAME",
  "kafka_enabled": true,
  "s3_enabled": true,
  "backend_connected": true
}
```

### List Organizations

Get all available organizations:

```bash
curl https://your-api-endpoint.com/organization
```

**Response:**
```json
["org1", "org2", "org3"]
```

Filter by name:

```bash
curl "https://your-api-endpoint.com/organization?name=nasa"
```

### Search Datasets

Search for datasets by terms:

```bash
curl "https://your-api-endpoint.com/search?terms=climate"
```

Search with multiple terms:

```bash
curl "https://your-api-endpoint.com/search?terms=climate&terms=temperature"
```

**Response:**
```json
[
  {
    "id": "12345678-abcd-efgh-ijkl-1234567890ab",
    "name": "climate_dataset",
    "title": "Climate Dataset",
    "owner_org": "noaa",
    "description": "Climate data from NOAA",
    "resources": [
      {
        "id": "resource-id",
        "url": "https://example.com/data.csv",
        "name": "Main Data",
        "format": "CSV"
      }
    ]
  }
]
```

### Advanced Search (POST)

For more complex searches, use the POST endpoint:

```bash
curl -X POST https://your-api-endpoint.com/search \
  -H "Content-Type: application/json" \
  -d '{
    "dataset_name": "climate",
    "owner_org": "noaa",
    "resource_format": "CSV"
  }'
```

## Write Operations (Authentication Required)

### Create an Organization

```bash
curl -X POST https://your-api-endpoint.com/organization \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "my-organization",
    "title": "My Organization",
    "description": "Organization description"
  }'
```

**Response:**
```json
{
  "id": "305284e6-6338-4e13-b39b-e6efe9f1c45a",
  "message": "Organization created successfully"
}
```

### Register a URL Resource

```bash
curl -X POST https://your-api-endpoint.com/url \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "resource_name": "my-dataset",
    "resource_title": "My Dataset",
    "owner_org": "my-organization",
    "resource_url": "https://example.com/data.csv",
    "file_type": "CSV",
    "notes": "Dataset description"
  }'
```

### Register an S3 Resource

```bash
curl -X POST https://your-api-endpoint.com/s3 \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "resource_name": "s3-dataset",
    "resource_title": "S3 Dataset",
    "owner_org": "my-organization",
    "s3_bucket": "my-bucket",
    "s3_key": "data/file.csv"
  }'
```

### Register a Service

```bash
curl -X POST https://your-api-endpoint.com/services \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "service_name": "my-api",
    "service_title": "My API Service",
    "owner_org": "services",
    "service_url": "https://api.example.com",
    "service_type": "API",
    "notes": "RESTful API service"
  }'
```

## Delete Operations

### Delete a Resource by ID

```bash
curl -X DELETE "https://your-api-endpoint.com/resource/RESOURCE_ID" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

### Delete a Resource by Name

```bash
curl -X DELETE "https://your-api-endpoint.com/resource?name=my-dataset" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

### Delete an Organization

```bash
curl -X DELETE "https://your-api-endpoint.com/organization/my-organization" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

## Error Handling

The API returns standard HTTP status codes:

| Code | Description |
|------|-------------|
| 200 | Success |
| 201 | Created |
| 400 | Bad Request - Invalid parameters |
| 401 | Unauthorized - Invalid or missing token |
| 403 | Forbidden - Insufficient permissions |
| 404 | Not Found |
| 409 | Conflict - Duplicate resource |
| 422 | Validation Error |

**Error Response Format:**
```json
{
  "detail": "Error message describing the problem"
}
```

## API Documentation

For the complete API reference, access the OpenAPI documentation:

- **Swagger UI**: `https://your-api-endpoint.com/docs`
- **OpenAPI JSON**: `https://your-api-endpoint.com/openapi.json`

## Next Steps

- Explore the [Python tutorials](../python/) for a higher-level interface
- Check out the [complete examples](../examples/) for end-to-end workflows

## Related Resources

- [ndp-ep Python Library](https://github.com/sci-ndp/ndp-ep-py)


### api/README.md (610 bytes)

# API Tutorials

This folder contains tutorials for working directly with the NDP-EP REST API.

## Contents

| Tutorial | Description |
|----------|-------------|
| [01 - Getting Started](./01-getting-started.md) | API overview, authentication, and basic operations |

## Prerequisites

- Access to an NDP-EP API instance
- Basic knowledge of REST APIs
- A tool for making HTTP requests (curl, Postman, or similar)

## Topics Covered

- Authentication and authorization
- Dataset management
- Organization management
- Resource registration (URLs, S3, Kafka topics)
- Service management
- Search and filtering


### examples/README.md (1,562 bytes)

# Complete Demo Applications

This folder contains end-to-end example applications demonstrating NDP-EP capabilities.

## Contents

| Example | Description |
|---------|-------------|
| [GOES-18 Utah Satellite](./goes-utah-satellite.ipynb) | Process GOES-18 satellite imagery for Utah region with interactive Folium visualization |
| [EarthScope Seismic Streaming](./earthscope-seismic-streaming.ipynb) | Process EarthScope GNSS station data with regional aggregation |

## Presentations

| Presentation | Description |
|--------------|-------------|
| [GOES-18 Presentation](https://national-data-platform.github.io/ep-tutorials/examples/goes-presentation.html) | Interactive presentation on NDP-EP benefits using GOES-18 satellite data |
| [EarthScope Presentation](https://national-data-platform.github.io/ep-tutorials/examples/earthscope-presentation.html) | Interactive presentation on NDP-EP benefits using EarthScope GNSS data |

## Running Examples

### Google Colab

Most notebooks include an "Open in Colab" badge at the top. Click it to run the notebook directly in Google Colab without local setup.

### Local Execution

1. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install ndp-ep xarray netCDF4 pyproj folium numpy requests pillow
   ```

3. Open Jupyter:
   ```bash
   pip install jupyter
   jupyter notebook
   ```

## Prerequisites

- Access to an NDP-EP API instance
- Valid authentication token
- See each example for specific requirements


### examples/earthscope-seismic-streaming.ipynb (26,503 bytes)

# earthscope-seismic-streaming


# EarthScope GNSS Stations: Data Processing & Analysis

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/national-data-platform/ep-tutorials/blob/main/examples/earthscope-seismic-streaming.ipynb)

## Why NDP-EP?

This example demonstrates the **real advantage** of using NDP-EP for data management:

- **User A** (first time): Downloads raw CSV from NDP catalog, cleans data, processes by region, stores in NDP-EP
- **User B** (later): Finds processed data in NDP-EP, downloads directly - **much faster!**

### Benefits

| Without NDP-EP | With NDP-EP |
|----------------|-------------|
| Download 150 KB raw CSV | Download 5 KB processed JSON |
| Clean malformed headers | Already cleaned |
| Process 1100+ stations | Already aggregated by region |
| ~10 seconds processing | Instant |

## About EarthScope Data

**EarthScope Consortium** provides high-rate (1Hz) GNSS position data from nearly 1,100 stations across the US. This data supports research on:
- Earthquakes and seismic events
- Volcanic activity
- Ground deformation
- Tectonic plate movement

## Prerequisites

- Access to an NDP-EP API instance
- Valid authentication token

## Setup

```python
!pip install ndp-ep pandas matplotlib folium requests -q
```

```python
import json
import time
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import folium
from folium.plugins import MarkerCluster
from ndp_ep import Client
import tempfile
import os
```

## Configuration

```python
# NDP-EP Configuration
API_URL = "http://localhost:8002"  # Change to your API endpoint
TOKEN = "testing_token"            # Change to your token
ORGANIZATION = "earthscope-demo"   # Organization for registering datasets

# Dataset identifiers
DATASET_NAME = "earthscope-stations-processed"
BUCKET_NAME = "seismic-data"
S3_KEY = "earthscope/stations_by_region.json"

# Source data URL (from NDP Global Catalog)
SOURCE_CSV_URL = "https://nationaldataplatform.org/catalog/dataset/811f0bcc-99e5-455c-bcf6-7c63c2634f41/resource/a420cc30-2262-423a-8c63-3ad8d91f2a8f/download/earthscope_converted_data.csv"

# Initialize client
client = Client(base_url=API_URL, token=TOKEN)

# Verify connection
status = client.get_system_status()

print(f"NDP-EP: {status['ep_name']} v{status['api_version']}")
print()
print("Services status:")
print(f"  - Local Catalog: {'✓ Connected' if status.get('backend_connected') else '✗ NOT CONNECTED'}")
print(f"  - S3 Storage:    {'✓ Connected' if status.get('s3_connected') else '✗ NOT CONNECTED'}")

if not status.get('backend_connected'):
    raise RuntimeError("Local catalog is not connected.")
if not status.get('s3_connected'):
    raise RuntimeError("S3 storage is not connected.")

# Ensure organization exists
existing_orgs = client.list_organizations(server="local")
if ORGANIZATION not in existing_orgs:
    print(f"\nCreating organization '{ORGANIZATION}'...")
    client.register_organization({
        "name": ORGANIZATION,
        "title": "EarthScope Demo Organization",
        "description": "Demo organization for EarthScope seismic data"
    })
    print(f"  ✓ Created")

print("\n✓ Ready!")
```

---

# Step 1: Search for Existing Data

Before downloading anything, let's check if someone has already processed EarthScope station data.

```python
# Search for existing processed data
print("Searching for 'earthscope stations' in NDP-EP local catalog...")
print()

results = client.search_datasets(terms=["earthscope", "stations"], server="local")

# Look for our specific processed dataset
found_dataset = None
for dataset in results:
    if dataset.get('name') == DATASET_NAME:
        found_dataset = dataset
        break

if found_dataset:
    print(f"✓ Found existing dataset: {found_dataset['name']}")
    print(f"  Title: {found_dataset.get('title', 'N/A')}")
    print(f"\n→ Skip to USER B section below!")
    DATA_EXISTS = True
else:
    print("✗ No processed EarthScope station data found in local catalog.")
    print("\n→ Continue with USER A workflow to download and process.")
    DATA_EXISTS = False
```

---

# USER A: First-Time Processing

**Scenario**: No one has processed EarthScope station data yet. We need to:
1. Download raw CSV from NDP catalog (150 KB, malformed headers)
2. Clean and parse the data
3. Process: aggregate stations by US region
4. Upload processed JSON to NDP-EP S3
5. Register in local catalog for others to find

```python
# Only run if data doesn't exist
if DATA_EXISTS:
    print("⏭ Data already exists. Skip to USER B section.")
else:
    print("="*60)
    print("USER A: Starting full processing workflow")
    print("="*60)
    
    # Start timing
    user_a_start = time.time()
```

### A.1 Download Raw CSV from NDP Catalog

```python
if not DATA_EXISTS:
    print("Downloading raw CSV from NDP catalog...")
    print(f"Source: {SOURCE_CSV_URL[:60]}...")
    print()
    
    download_start = time.time()
    
    response = requests.get(SOURCE_CSV_URL, timeout=60)
    response.raise_for_status()
    
    download_time = time.time() - download_start
    download_kb = len(response.content) / 1024
    
    print(f"✓ Downloaded {download_kb:.1f} KB in {download_time:.2f}s")
    
    raw_csv = response.text
```

### A.2 Clean and Parse Data

The raw CSV has malformed headers with units embedded. We need to clean it.

```python
if not DATA_EXISTS:
    print("Cleaning and parsing raw data...")
    process_start = time.time()
    
    # Parse raw CSV - headers are malformed
    # Format: Site,Latitude,(deg),Longitude,(deg),EllipElev,(m),X,(m),Y,(m),Z,(m),...
    lines = raw_csv.strip().split('\n')
    
    # Define correct column names
    columns = [
        'site', 'latitude', 'longitude', 'elevation_m',
        'x_m', 'y_m', 'z_m', 'epoch_yr', 'network',
        'status', 'last_update', 'antenna_height_m', 'antenna_type', 'dome'
    ]
    
    # Parse data rows
    data = []
    for line in lines[1:]:  # Skip header
        parts = line.split(',')
        if len(parts) >= 14:
            try:
                row = {
                    'site': parts[0],
                    'latitude': float(parts[1]),
                    'longitude': float(parts[2]),
                    'elevation_m': float(parts[3]),
                    'x_m': float(parts[4]),
                    'y_m': float(parts[5]),
                    'z_m': float(parts[6]),
                    'epoch_yr': float(parts[7]),
                    'network': parts[8],
                    'status': parts[9],
                    'last_update': parts[10],
                    'antenna_height_m': float(parts[11]) if parts[11] else 0,
                    'antenna_type': parts[12],
                    'dome': parts[13]
                }
                data.append(row)
            except (ValueError, IndexError):
                continue
    
    df = pd.DataFrame(data)
    
    print(f"\n✓ Parsed {len(df)} stations")
    print(f"  Columns: {list(df.columns)}")
    print(f"  Networks: {df['network'].nunique()} unique")
    print(f"  Active stations: {len(df[df['status'] == 'ACTIVE'])}")
```

### A.3 Process: Aggregate by US Region

```python
if not DATA_EXISTS:
    print("Processing: Aggregating stations by US region...")
    
    # Define US regions by longitude/latitude
    def get_region(lat, lon):
        if lon > -100:  # East of -100
            if lat > 40:
                return 'Northeast'
            else:
                return 'Southeast'
        else:  # West of -100
            if lat > 45:
                return 'Pacific Northwest'
            elif lat > 35:
                return 'California'
            else:
                return 'Southwest'
    
    # Only include US stations (continental)
    df_us = df[(df['latitude'] > 24) & (df['latitude'] < 50) & 
               (df['longitude'] > -125) & (df['longitude'] < -66)].copy()
    
    df_us['region'] = df_us.apply(lambda r: get_region(r['latitude'], r['longitude']), axis=1)
    
    # Aggregate statistics by region
    region_stats = {}
    for region in df_us['region'].unique():
        region_df = df_us[df_us['region'] == region]
        
        # Only include sample of stations (10 per region) to keep JSON small
        sample_stations = region_df[['site', 'latitude', 'longitude', 'elevation_m', 'network', 'status']].head(10).to_dict('records')
        
        region_stats[region] = {
            'station_count': len(region_df),
            'active_count': len(region_df[region_df['status'] == 'ACTIVE']),
            'networks': region_df['network'].unique().tolist(),
            'avg_elevation_m': round(region_df['elevation_m'].mean(), 2),
            'min_elevation_m': round(region_df['elevation_m'].min(), 2),
            'max_elevation_m': round(region_df['elevation_m'].max(), 2),
            'center_lat': round(region_df['latitude'].mean(), 4),
            'center_lon': round(region_df['longitude'].mean(), 4),
            'sample_stations': sample_stations  # Only 10 samples, not all
        }
    
    # Create processed dataset
    processed_data = {
        'metadata': {
            'source': 'EarthScope Consortium',
            'processed_date': time.strftime('%Y-%m-%d'),
            'total_stations': len(df_us),
            'regions': list(region_stats.keys())
        },
        'regions': region_stats
    }
    
    process_time = time.time() - process_start
    
    print(f"\n✓ Processing complete in {process_time:.2f}s")
    print(f"\nRegion summary:")
    for region, stats in region_stats.items():
        print(f"  {region}: {stats['station_count']} stations ({stats['active_count']} active)")
```

### A.4 Upload to NDP-EP S3

```python
if not DATA_EXISTS:
    print("Uploading processed data to NDP-EP S3...")
    
    # Create bucket
    try:
        client.create_bucket(BUCKET_NAME)
        print(f"  ✓ Created bucket: {BUCKET_NAME}")
    except:
        print(f"  ✓ Bucket exists: {BUCKET_NAME}")
    
    # Convert to JSON and upload
    json_data = json.dumps(processed_data, indent=2)
    processed_kb = len(json_data.encode()) / 1024
    
    upload_start = time.time()
    client.upload_object(BUCKET_NAME, S3_KEY, json_data.encode(), "application/json")
    upload_time = time.time() - upload_start
    
    print(f"  ✓ Uploaded {processed_kb:.1f} KB in {upload_time:.2f}s")
```

### A.5 Register in Catalog

```python
if not DATA_EXISTS:
    print("Registering dataset in NDP-EP catalog...")
    
    result = client.register_s3_link({
        "resource_name": DATASET_NAME,
        "resource_title": "EarthScope GNSS Stations - Processed by Region",
        "owner_org": ORGANIZATION,
        "s3_bucket": BUCKET_NAME,
        "s3_key": S3_KEY,
        "resource_s3": f"{BUCKET_NAME}/{S3_KEY}",
        "notes": "Pre-processed EarthScope GNSS station data aggregated by US region. Includes station counts, elevation statistics, and network information."
    })
    
    print(f"  ✓ Registered: {result}")
    
    # Total time for User A
    user_a_total = time.time() - user_a_start
    
    print("\n" + "="*60)
    print("USER A SUMMARY")
    print("="*60)
    print(f"  Download raw CSV:    {download_time:.2f}s ({download_kb:.1f} KB)")
    print(f"  Clean & Process:     {process_time:.2f}s")
    print(f"  Upload to NDP-EP:    {upload_time:.2f}s ({processed_kb:.1f} KB)")
    print(f"  ─────────────────────────────")
    print(f"  TOTAL TIME:          {user_a_total:.2f}s")
    print(f"  Data downloaded:     {download_kb:.1f} KB")
    print("="*60)
    
    # Store for comparison
    USER_A_TIME = user_a_total
    USER_A_KB = download_kb
```

---

# USER B: Fast Access (Data Already in NDP-EP)

**Scenario**: Another user (or the same user later) needs EarthScope station data by region.

Instead of repeating all the work, they:
1. Search NDP-EP → Find existing processed dataset
2. Download processed JSON directly (only ~5 KB!)
3. Analyze immediately - no cleaning needed

```python
print("="*60)
print("USER B: Fast workflow (data already in NDP-EP)")
print("="*60)

user_b_start = time.time()
```

### B.1 Search Catalog

```python
print("Searching NDP-EP catalog for 'earthscope stations'...")

search_start = time.time()
results = client.search_datasets(terms=["earthscope", "stations"], server="local")
search_time = time.time() - search_start

# Find our dataset
found = None
for dataset in results:
    if dataset.get('name') == DATASET_NAME:
        found = dataset
        break

if found:
    print(f"\n✓ Found in {search_time:.3f}s: {found['name']}")
    print(f"  Title: {found.get('title', 'N/A')}")
else:
    raise RuntimeError("Dataset not found. Run USER A section first.")
```

### B.2 Download from NDP-EP (Fast!)

```python
print("Downloading processed data from NDP-EP S3...")

download_start = time.time()

# Download directly from NDP-EP S3
data = client.download_object(BUCKET_NAME, S3_KEY)

download_time_b = time.time() - download_start
download_kb_b = len(data) / 1024

# Parse JSON
processed_data = json.loads(data.decode())

print(f"\n✓ Downloaded {download_kb_b:.2f} KB in {download_time_b:.3f}s")
print(f"\nDataset info:")
print(f"  Source: {processed_data['metadata']['source']}")
print(f"  Processed: {processed_data['metadata']['processed_date']}")
print(f"  Total stations: {processed_data['metadata']['total_stations']}")
print(f"  Regions: {processed_data['metadata']['regions']}")
```

### B.3 Analyze Immediately (No Processing Needed!)

```python
print("Analyzing regional data...\n")

# Data is already aggregated - just display
print(f"{'Region':<20} {'Stations':<10} {'Active':<10} {'Avg Elev (m)':<15} {'Networks'}")
print("-" * 80)

for region, stats in processed_data['regions'].items():
    networks = ', '.join(stats['networks'][:3])
    if len(stats['networks']) > 3:
        networks += f" +{len(stats['networks'])-3} more"
    print(f"{region:<20} {stats['station_count']:<10} {stats['active_count']:<10} {stats['avg_elevation_m']:<15} {networks}")
```

### B.4 Visualize

```python
print("Creating visualization...")
viz_start = time.time()

# Create map
m = folium.Map(location=[39.0, -98.0], zoom_start=4, tiles='CartoDB positron')

# Color by region
colors = {
    'California': 'red',
    'Pacific Northwest': 'blue',
    'Southwest': 'orange',
    'Northeast': 'green',
    'Southeast': 'purple'
}

# Add stations from processed data
for region, stats in processed_data['regions'].items():
    color = colors.get(region, 'gray')
    
    # Add region center marker
    folium.Marker(
        location=[stats['center_lat'], stats['center_lon']],
        popup=f"<b>{region}</b><br>{stats['station_count']} stations",
        icon=folium.Icon(color=color, icon='info-sign')
    ).add_to(m)
    
    # Add sample station markers
    for station in stats.get('sample_stations', []):
        folium.CircleMarker(
            location=[station['latitude'], station['longitude']],
            radius=3,
            color=color,
            fill=True,
            fillOpacity=0.7,
            popup=f"{station['site']} ({station['network']})"
        ).add_to(m)

# Add legend
legend_html = '''
<div style="position: fixed; bottom: 50px; left: 50px; z-index: 1000; background-color: white; padding: 10px; border-radius: 5px; border: 2px solid gray;">
<b>Regions</b><br>
''' + ''.join([f'<i style="background:{c};width:10px;height:10px;display:inline-block;margin-right:5px;"></i>{r}<br>' for r, c in colors.items()]) + '</div>'

m.get_root().html.add_child(folium.Element(legend_html))

viz_time = time.time() - viz_start
print(f"\n✓ Visualization ready in {viz_time:.2f}s")
```

```python
# Display map
m
```

```python
# User B total time
user_b_total = time.time() - user_b_start

print("\n" + "="*60)
print("USER B SUMMARY")
print("="*60)
print(f"  Search catalog:      {search_time:.3f}s")
print(f"  Download from S3:    {download_time_b:.3f}s ({download_kb_b:.2f} KB)")
print(f"  Visualization:       {viz_time:.2f}s")
print(f"  ─────────────────────────────")
print(f"  TOTAL TIME:          {user_b_total:.2f}s")
print(f"  Data downloaded:     {download_kb_b:.2f} KB")
print("="*60)

USER_B_TIME = user_b_total
USER_B_KB = download_kb_b
```

---

# Comparison: User A vs User B

```python
# Get User A values if available, otherwise use typical values
try:
    ua_time = USER_A_TIME
    ua_kb = USER_A_KB
except:
    ua_time = 8.0   # Typical time
    ua_kb = 149.5   # Typical download size

ub_time = USER_B_TIME
ub_kb = USER_B_KB

print("\n" + "="*60)
print("COMPARISON: NDP-EP BENEFITS")
print("="*60)
print()
print(f"                    USER A          USER B")
print(f"                    (first time)    (with NDP-EP)")
print(f"  ──────────────────────────────────────────────")
print(f"  Time:             {ua_time:>6.2f}s         {ub_time:>6.2f}s")
print(f"  Data downloaded:  {ua_kb:>6.1f} KB       {ub_kb:>6.2f} KB")
print(f"  Processing:       Required        None")
print(f"  Data cleaning:    Required        None")
print(f"  ──────────────────────────────────────────────")
print()
if ua_time > ub_time:
    print(f"  Time saved:      {ua_time - ub_time:.2f}s ({(1 - ub_time/ua_time)*100:.0f}% faster)")
if ua_kb > ub_kb:
    print(f"  Data saved:      {ua_kb - ub_kb:.1f} KB ({(1 - ub_kb/ua_kb)*100:.0f}% less)")
print()
print("="*60)
```

---

## Summary

### Why Use NDP-EP?

**1. Avoid Redundant Work**
- Process data once, use many times
- No need to re-download and re-clean raw data

**2. Faster Access**
- Local S3 is faster than external sources
- Pre-processed data is smaller and cleaner

**3. Data Discovery**
- Search catalog before downloading
- Find datasets others have already prepared

**4. Collaboration**
- Share processed data with your team
- Standard metadata for discovery

## Cleanup (Optional)

```python
# Uncomment to clean up all resources

# client.delete_resource_by_name(DATASET_NAME)
# client.delete_object(BUCKET_NAME, S3_KEY)
# client.delete_bucket(BUCKET_NAME)

print("Done!")
```


### examples/goes-utah-satellite.ipynb (23,862 bytes)

# goes-utah-satellite


# GOES-18 Satellite Imagery: Utah Region

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/national-data-platform/ep-tutorials/blob/main/examples/goes-utah-satellite.ipynb)

## Why NDP-EP?

This example demonstrates the **real advantage** of using NDP-EP for data management:

- **User A** (first time): Downloads from AWS, processes, registers in NDP-EP
- **User B** (later): Finds processed data in NDP-EP, downloads directly - **much faster!**

### Benefits

| Without NDP-EP | With NDP-EP |
|----------------|-------------|
| Download 57 MB from AWS every time | Download 1 MB from local S3 |
| Process data every time | Already processed |
| ~60 seconds | ~2 seconds |

## Prerequisites

- Access to an NDP-EP API instance
- Valid authentication token

## Setup

```python
!pip install ndp-ep xarray netCDF4 pyproj folium numpy requests pillow -q
```

```python
import numpy as np
import xarray as xr
import requests
import folium
from pyproj import CRS, Transformer
from ndp_ep import Client
import tempfile
import os
import time
```

## Configuration

```python
# NDP-EP Configuration
API_URL = "http://localhost:8002"  # Change to your API endpoint
TOKEN = "testing_token"            # Change to your token
ORGANIZATION = "noaa-demo"         # Organization for registering datasets

# Dataset identifiers
DATASET_NAME = "goes18-utah-processed"
BUCKET_NAME = "satellite-data"
S3_KEY = "goes18/utah/goes18_utah_20241125_1800.nc"

# Initialize client
client = Client(base_url=API_URL, token=TOKEN)

# Verify connection
status = client.get_system_status()

print(f"NDP-EP: {status['ep_name']} v{status['api_version']}")
print(f"")
print("Services status:")
print(f"  - Local Catalog: {'✓ Connected' if status.get('backend_connected') else '✗ NOT CONNECTED'}")
print(f"  - S3 Storage:    {'✓ Connected' if status.get('s3_connected') else '✗ NOT CONNECTED'}")

if not status.get('backend_connected'):
    raise RuntimeError("❌ Local catalog is not connected.")
if not status.get('s3_connected'):
    raise RuntimeError("❌ S3 storage is not connected.")

# Ensure organization exists
existing_orgs = client.list_organizations(server="local")
if ORGANIZATION not in existing_orgs:
    print(f"\nCreating organization '{ORGANIZATION}'...")
    client.register_organization({
        "name": ORGANIZATION,
        "title": "NOAA Demo Organization",
        "description": "Demo organization for NOAA satellite data"
    })
    print(f"  ✓ Created")

print("\n✓ Ready!")
```

```python
# Create temporary directory for this session
temp_dir = tempfile.mkdtemp()
print(f"Working directory: {temp_dir}")
```

---

# 🔍 Step 1: Search for Existing Data

Before downloading anything, let's check if someone has already processed GOES-18 data for Utah.

```python
# Search for existing Utah GOES data
print("Searching for 'GOES utah' in NDP-EP catalog...")
print()

results = client.search_datasets(terms=["goes18", "utah"], server="local")

# Look for our specific processed dataset
found_dataset = None
for dataset in results:
    if dataset.get('name') == DATASET_NAME:
        found_dataset = dataset
        break

if found_dataset:
    print(f"✓ Found existing dataset: {found_dataset['name']}")
    print(f"  Title: {found_dataset.get('title', 'N/A')}")
    print(f"\n→ Skip to USER B section below!")
    DATA_EXISTS = True
else:
    print("✗ No processed GOES-18 Utah data found in catalog.")
    print("\n→ Continue with USER A workflow to download and process.")
    DATA_EXISTS = False
```

---

# 👤 USER A: First-Time Processing

**Scenario**: No one has processed Utah GOES data yet. We need to:
1. Download from AWS (slow, 57 MB)
2. Process and crop to Utah
3. Upload to NDP-EP S3
4. Register in catalog for others to find

```python
# Only run if data doesn't exist
if DATA_EXISTS:
    print("⏭ Data already exists. Skip to USER B section.")
else:
    print("="*60)
    print("USER A: Starting full processing workflow")
    print("="*60)
    
    # Start timing
    user_a_start = time.time()
```

### A.1 Download from AWS

```python
if not DATA_EXISTS:
    # GOES-18 file on AWS
    GOES_FILE_URL = "https://noaa-goes18.s3.amazonaws.com/ABI-L2-MCMIPC/2024/330/18/OR_ABI-L2-MCMIPC-M6_G18_s20243301801170_e20243301803543_c20243301804085.nc"
    
    print("Downloading from AWS S3 (NOAA public bucket)...")
    print(f"Source: {GOES_FILE_URL[:60]}...")
    print()
    
    download_start = time.time()
    
    goes_file = os.path.join(temp_dir, "goes18_conus.nc")
    response = requests.get(GOES_FILE_URL, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    
    downloaded_bytes = 0
    with open(goes_file, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
            downloaded_bytes += len(chunk)
            if total_size:
                pct = (downloaded_bytes / total_size) * 100
                print(f"\rDownloading: {downloaded_bytes/1e6:.1f}/{total_size/1e6:.1f} MB ({pct:.0f}%)", end="")
    
    download_time = time.time() - download_start
    download_mb = downloaded_bytes / 1e6
    
    print(f"\n\n✓ Downloaded {download_mb:.1f} MB in {download_time:.1f} seconds")
    print(f"  Speed: {download_mb/download_time:.1f} MB/s")
```

### A.2 Process: Crop to Utah Region

```python
if not DATA_EXISTS:
    process_start = time.time()
    
    # Utah geographic bounds
    UTAH_BOUNDS = {
        'lat_min': 37.0, 'lat_max': 42.0,
        'lon_min': -114.0, 'lon_max': -109.0
    }
    
    print("Processing GOES-18 data...")
    print(f"  Cropping to Utah: {UTAH_BOUNDS}")
    
    # Open and read projection info
    goes_ds = xr.open_dataset(goes_file)
    proj = goes_ds['goes_imager_projection']
    h = proj.attrs['perspective_point_height']
    lon_0 = proj.attrs['longitude_of_projection_origin']
    sweep = proj.attrs.get('sweep_angle_axis', 'x')
    
    # Create coordinate transformation
    goes_crs = CRS.from_cf({
        'grid_mapping_name': 'geostationary',
        'longitude_of_projection_origin': lon_0,
        'perspective_point_height': h,
        'sweep_angle_axis': sweep,
        'semi_major_axis': proj.attrs['semi_major_axis'],
        'semi_minor_axis': proj.attrs['semi_minor_axis'],
    })
    transformer = Transformer.from_crs(goes_crs, "EPSG:4326", always_xy=True)
    
    # Transform coordinates
    x = goes_ds['x'].values * h
    y = goes_ds['y'].values * h
    xx, yy = np.meshgrid(x, y)
    lon, lat = transformer.transform(xx, yy)
    
    # Find Utah region
    utah_mask = (
        (lat >= UTAH_BOUNDS['lat_min']) & (lat <= UTAH_BOUNDS['lat_max']) &
        (lon >= UTAH_BOUNDS['lon_min']) & (lon <= UTAH_BOUNDS['lon_max'])
    )
    utah_indices = np.where(utah_mask)
    y_min, y_max = utah_indices[0].min(), utah_indices[0].max()
    x_min, x_max = utah_indices[1].min(), utah_indices[1].max()
    
    # Extract Utah subset
    cmi_utah = goes_ds['CMI_C02'].values[y_min:y_max, x_min:x_max]
    lat_utah = lat[y_min:y_max, x_min:x_max]
    lon_utah = lon[y_min:y_max, x_min:x_max]
    
    # Save as NetCDF
    utah_file = os.path.join(temp_dir, "goes18_utah.nc")
    utah_ds = xr.Dataset({
        'reflectance': (['y', 'x'], cmi_utah),
        'latitude': (['y', 'x'], lat_utah),
        'longitude': (['y', 'x'], lon_utah),
    })
    utah_ds.attrs = {
        'title': 'GOES-18 Utah Region Subset',
        'source': 'NOAA GOES-18 ABI L2 MCMIPC',
        'band': 'C02 (Red, 0.64 µm)',
        'bounds': str(UTAH_BOUNDS),
    }
    utah_ds.to_netcdf(utah_file)
    
    goes_ds.close()
    
    process_time = time.time() - process_start
    processed_mb = os.path.getsize(utah_file) / 1e6
    
    print(f"\n✓ Processing complete in {process_time:.1f} seconds")
    print(f"  Original: {download_mb:.1f} MB → Processed: {processed_mb:.2f} MB")
    print(f"  Reduction: {(1 - processed_mb/download_mb)*100:.0f}%")
```

### A.3 Upload to NDP-EP S3

```python
if not DATA_EXISTS:
    print("Uploading processed data to NDP-EP S3...")
    
    # Create bucket
    try:
        client.create_bucket(BUCKET_NAME)
        print(f"  ✓ Created bucket: {BUCKET_NAME}")
    except:
        print(f"  ✓ Bucket exists: {BUCKET_NAME}")
    
    # Upload
    upload_start = time.time()
    with open(utah_file, 'rb') as f:
        client.upload_object(BUCKET_NAME, S3_KEY, f.read(), "application/x-netcdf")
    upload_time = time.time() - upload_start
    
    print(f"  ✓ Uploaded {processed_mb:.2f} MB in {upload_time:.1f} seconds")
```

### A.4 Register in Catalog

```python
if not DATA_EXISTS:
    print("Registering dataset in NDP-EP catalog...")
    
    result = client.register_s3_link({
        "resource_name": DATASET_NAME,
        "resource_title": "GOES-18 Utah Region - Visible Band (Processed)",
        "owner_org": ORGANIZATION,
        "s3_bucket": BUCKET_NAME,
        "s3_key": S3_KEY,
        "resource_s3": f"{BUCKET_NAME}/{S3_KEY}",
        "notes": "Pre-processed GOES-18 visible band imagery cropped to Utah region (37-42°N, 109-114°W). Ready for direct visualization."
    })
    
    print(f"  ✓ Registered: {result}")
    
    # Total time for User A
    user_a_total = time.time() - user_a_start
    
    print("\n" + "="*60)
    print("USER A SUMMARY")
    print("="*60)
    print(f"  Download from AWS:  {download_time:.1f}s ({download_mb:.1f} MB)")
    print(f"  Processing:         {process_time:.1f}s")
    print(f"  Upload to NDP-EP:   {upload_time:.1f}s")
    print(f"  ─────────────────────────────")
    print(f"  TOTAL TIME:         {user_a_total:.1f}s")
    print(f"  Data downloaded:    {download_mb:.1f} MB")
    print("="*60)
    
    # Store for comparison
    USER_A_TIME = user_a_total
    USER_A_MB = download_mb
```

---

# 👤 USER B: Fast Access (Data Already in NDP-EP)

**Scenario**: Another user (or the same user later) needs Utah GOES data.

Instead of repeating all the work, they:
1. Search NDP-EP → Find existing dataset
2. Download processed data directly (only 1 MB!)
3. Visualize immediately

```python
print("="*60)
print("USER B: Fast workflow (data already in NDP-EP)")
print("="*60)

user_b_start = time.time()
```

### B.1 Search Catalog

```python
print("Searching NDP-EP catalog for 'GOES utah'...")

search_start = time.time()
results = client.search_datasets(terms=["goes18", "utah"], server="local")
search_time = time.time() - search_start

# Find our dataset
found = None
for dataset in results:
    if dataset.get('name') == DATASET_NAME:
        found = dataset
        break

if found:
    print(f"\n✓ Found in {search_time:.2f}s: {found['name']}")
    print(f"  Title: {found.get('title', 'N/A')}")
else:
    raise RuntimeError("Dataset not found. Run USER A section first.")
```

### B.2 Download from NDP-EP (Fast!)

```python
print("Downloading processed data from NDP-EP S3...")

download_start = time.time()

# Download directly from NDP-EP S3
data = client.download_object(BUCKET_NAME, S3_KEY)

# Save locally
utah_file_b = os.path.join(temp_dir, "goes18_utah_from_ndpep.nc")
with open(utah_file_b, 'wb') as f:
    f.write(data)

download_time_b = time.time() - download_start
download_mb_b = len(data) / 1e6

print(f"\n✓ Downloaded {download_mb_b:.2f} MB in {download_time_b:.2f}s")
print(f"  Speed: {download_mb_b/download_time_b:.1f} MB/s")
```

### B.3 Load and Visualize (No Processing Needed!)

```python
print("Loading data for visualization...")

viz_start = time.time()

# Load the pre-processed data
ds_utah = xr.open_dataset(utah_file_b)

cmi_utah = ds_utah['reflectance'].values
lat_utah = ds_utah['latitude'].values
lon_utah = ds_utah['longitude'].values

print(f"  Shape: {cmi_utah.shape}")
print(f"  Reflectance range: {np.nanmin(cmi_utah):.3f} to {np.nanmax(cmi_utah):.3f}")

ds_utah.close()
```

```python
# Create visualization
from PIL import Image
import base64

# Normalize and apply gamma correction
cmi_normalized = np.nan_to_num(np.clip(cmi_utah, 0, 1), nan=0)
cmi_uint8 = (np.power(cmi_normalized, 0.5) * 255).astype(np.uint8)

# Save PNG
img = Image.fromarray(cmi_uint8, mode='L')
png_file = os.path.join(temp_dir, "utah_satellite_b.png")
img.save(png_file)

# Create Folium map
bounds = [
    [float(np.nanmin(lat_utah)), float(np.nanmin(lon_utah))],
    [float(np.nanmax(lat_utah)), float(np.nanmax(lon_utah))]
]

m = folium.Map(location=[39.5, -111.5], zoom_start=7, tiles='OpenStreetMap')

with open(png_file, 'rb') as f:
    img_data = base64.b64encode(f.read()).decode()

folium.raster_layers.ImageOverlay(
    image=f"data:image/png;base64,{img_data}",
    bounds=bounds,
    opacity=0.7,
    name="GOES-18 Visible Band"
).add_to(m)

folium.LayerControl().add_to(m)

viz_time = time.time() - viz_start

print(f"\n✓ Visualization ready in {viz_time:.2f}s")
```

```python
# Display map
m
```

```python
# User B total time
user_b_total = time.time() - user_b_start

print("\n" + "="*60)
print("USER B SUMMARY")
print("="*60)
print(f"  Search catalog:     {search_time:.2f}s")
print(f"  Download from S3:   {download_time_b:.2f}s ({download_mb_b:.2f} MB)")
print(f"  Visualization:      {viz_time:.2f}s")
print(f"  ─────────────────────────────")
print(f"  TOTAL TIME:         {user_b_total:.1f}s")
print(f"  Data downloaded:    {download_mb_b:.2f} MB")
print("="*60)

USER_B_TIME = user_b_total
USER_B_MB = download_mb_b
```

---

# 📊 Comparison: User A vs User B

```python
# Get User A values if available, otherwise use typical values
try:
    ua_time = USER_A_TIME
    ua_mb = USER_A_MB
except:
    ua_time = 45.0  # Typical time
    ua_mb = 57.3    # Typical download size

ub_time = USER_B_TIME
ub_mb = USER_B_MB

print("\n" + "="*60)
print("📊 COMPARISON: NDP-EP BENEFITS")
print("="*60)
print()
print(f"                    USER A          USER B")
print(f"                    (first time)    (with NDP-EP)")
print(f"  ──────────────────────────────────────────────")
print(f"  Time:             {ua_time:>6.1f}s         {ub_time:>6.1f}s")
print(f"  Data downloaded:  {ua_mb:>6.1f} MB       {ub_mb:>6.2f} MB")
print(f"  Processing:       Required        None")
print(f"  ──────────────────────────────────────────────")
print()
print(f"  ⏱  Time saved:     {ua_time - ub_time:.1f}s ({(1 - ub_time/ua_time)*100:.0f}% faster)")
print(f"  📦 Data saved:     {ua_mb - ub_mb:.1f} MB ({(1 - ub_mb/ua_mb)*100:.0f}% less)")
print()
print("="*60)
```

---

## Summary

### Why Use NDP-EP?

**1. Avoid Redundant Work**
- Process data once, use many times
- No need to re-download from slow external sources

**2. Faster Access**
- Local S3 is faster than AWS public buckets
- Pre-processed data is smaller

**3. Data Discovery**
- Search catalog before downloading
- Find datasets others have already prepared

**4. Collaboration**
- Share processed data with your team
- Standard metadata for discovery

## Cleanup (Optional)

```python
# Uncomment to clean up all resources

# client.delete_resource_by_name(DATASET_NAME)
# client.delete_object(BUCKET_NAME, S3_KEY)
# client.delete_bucket(BUCKET_NAME)

# import shutil
# shutil.rmtree(temp_dir)

print("Done!")
```


### frontend/01-getting-started.md (4,070 bytes)

# Getting Started with the NDP-EP Frontend

This tutorial covers how to access and navigate the NDP-EP administrative console.

## Prerequisites

- Access to an NDP-EP frontend instance
- Valid authentication token
- Modern web browser (Chrome, Firefox, Safari, or Edge)

## Step 1: Accessing the Console

Open your web browser and navigate to your NDP-EP frontend URL:

```
https://your-frontend-url.com
```

You will be presented with the login screen.

![Login Screen](./images/01-login-screen.png)
<!-- SCREENSHOT NEEDED: Login screen showing the token input field and "Enter" button -->

## Step 2: Authentication

The NDP-EP console uses Bearer token authentication. To log in:

1. Obtain your authentication token from your administrator
2. Paste the token into the **Token** input field
3. Click the **Enter** button

![Token Input](./images/01-token-input.png)
<!-- SCREENSHOT NEEDED: Login screen with a token partially visible in the input field (you can blur/hide part of it) -->

If the token is valid, you will be redirected to the Dashboard. If invalid, an error message will appear.

![Login Error](./images/01-login-error.png)
<!-- SCREENSHOT NEEDED: Login screen showing an error message for invalid token (optional - only if easy to reproduce) -->

## Step 3: Dashboard Overview

After successful login, you'll see the main Dashboard. This page provides an overview of your NDP-EP instance status.

![Dashboard Overview](./images/01-dashboard-overview.png)
<!-- SCREENSHOT NEEDED: Full dashboard page showing all status cards and information -->

The Dashboard displays:

### System Information

- **EP Name**: The name of your EndPoint instance
- **Organization**: The organization this instance belongs to
- **API Version**: Current version of the backend API
- **Frontend Version**: Current version of the console

### Connection Status

The Dashboard shows the status of various backend services:

- **Backend**: Connection to the CKAN catalog
- **Kafka**: Streaming data service status
- **S3**: Object storage connection status
- **JupyterLab**: Notebook environment status

Each service shows either:
- **Connected** (green) - Service is available
- **Disabled** (gray) - Service is not configured
- **Error** (red) - Connection problem

## Step 4: Navigation

The main navigation menu is located at the top of the page. It provides access to all console features:

### Available Pages

| Menu Item | Description |
|-----------|-------------|
| **Dashboard** | System status overview |
| **Organizations** | Manage organizations |
| **Datasets** | Create and manage datasets |
| **Kafka Topics** | Register Kafka streaming topics |
| **URL Resources** | Register URL-based resources |
| **S3 Resources** | Register S3 object storage resources |
| **S3 Management** | Browse and manage S3 buckets/objects |
| **Services** | Register and manage microservices |
| **Search** | Search for datasets and services |

## Step 5: User Information

Your authentication status is displayed in the top-right corner of the navigation bar.

This area shows:
- Your user identifier or group
- A **Logout** button to end your session

## Step 6: Logging Out

To log out of the console:

1. Click the **Logout** button in the top-right corner
2. You will be redirected to the login screen
3. Your authentication token will be cleared from the browser

## Common Issues

### Token Expired

If your session expires, you'll see an alert message and be redirected to the login screen. Simply log in again with a valid token.

### API Connection Error

If the Dashboard shows connection errors:

1. Check that the backend API is running
2. Verify your network connection
3. Contact your administrator if the problem persists

## Next Steps

Now that you're familiar with the console, explore these tutorials:

- [Dataset Management](./02-dataset-management.md) - Create and manage datasets
- [Organizations](./03-organizations.md) - Manage organizations
- [Services](./04-services.md) - Register microservices
- [Search](./05-search.md) - Find datasets and services


### frontend/README.md (679 bytes)

# Frontend Tutorials

This folder contains tutorials for using the NDP-EP administrative console (ep-frontend).

## Contents

*No tutorials yet*

## Prerequisites

- Access to an NDP-EP frontend instance
- Web browser (Chrome, Firefox, Safari, or Edge recommended)
- Valid user credentials

## Topics Covered

- Dashboard overview and navigation
- Managing datasets across CKAN environments
- Creating and organizing organizations
- Monitoring system health and connectivity
- Registering and managing microservices
- Bulk operations on Kafka topics and S3 resources

## Related Resources

- [ep-frontend GitHub Repository](https://github.com/national-data-platform/ep-frontend)


### python/01-getting-started.md (1,564 bytes)

# Getting Started with ndp-ep

This guide provides a quick introduction to the `ndp-ep` Python library for interacting with the NDP-EP API.

## Installation

```bash
pip install ndp-ep
```

## Quick Start

### Initialize the Client

```python
from ndp_ep import Client

# Using token authentication
client = Client(
    base_url="https://your-api-endpoint.com",
    token="your-api-token"
)

# Or using username/password
client = Client(
    base_url="https://your-api-endpoint.com",
    username="your-username",
    password="your-password"
)
```

### Basic Operations

```python
# List organizations
organizations = client.list_organizations()

# Search datasets
datasets = client.search_datasets(terms=["climate"])

# Get system status
status = client.get_system_status()
```

## Key Features

The library provides methods for:

- **Authentication**: Token-based and username/password authentication
- **Organizations**: Create, list, and manage organizations
- **Datasets**: Search, register, update, and delete datasets
- **Resources**: Register URL, S3, and Kafka topic resources
- **S3 Operations**: Bucket management, file upload/download, presigned URLs
- **Services**: Register and manage microservices
- **System Info**: Check status, get Kafka details, Jupyter configuration

## Next Steps

After getting familiar with the basics:

1. Learn about [S3 integration](./02-s3-integration.md)
2. Check out the [complete examples](../examples/) in this repository

## Related Resources

- [ndp-ep-py GitHub Repository](https://github.com/sci-ndp/ndp-ep-py)


### python/02-api-reference.md (15,038 bytes)

# NDP-EP Python Library: Complete API Reference

This guide covers all functions available in the `ndp-ep` Python library, organized by category.

## Table of Contents

1. [Connection & Authentication](#1-connection--authentication)
2. [Dataset Registration](#2-dataset-registration)
3. [Dataset Search & Management](#3-dataset-search--management)
4. [Organization Management](#4-organization-management)
5. [Service Management](#5-service-management)
6. [S3 Storage Operations](#6-s3-storage-operations)
7. [Kafka Integration](#7-kafka-integration)
8. [Pelican Federation](#8-pelican-federation)
9. [Jupyter Integration](#9-jupyter-integration)

---

## 1. Connection & Authentication

### Client Initialization

```python
from ndp_ep import Client

# With token authentication
client = Client(base_url="http://localhost:8002", token="your-token")

# With password authentication
client = Client(base_url="http://localhost:8002")
client.get_token(username="user", password="pass")
```

### get_system_status()

Check the system status and available services.

```python
status = client.get_system_status()
print(status)
```

**Returns:**
```python
{
    'api_version': '0.4.0',
    'ep_name': 'EP-DEMO',
    'organization': 'ORGANIZATION-DEMO',
    'backend_connected': True,      # Local catalog (CKAN or other)
    's3_connected': True,           # MinIO/S3 storage
    'kafka_enabled': True,          # Kafka streaming
    'jupyterlab_enabled': True,     # JupyterLab integration
    'is_public': True
}
```

### get_system_metrics()

Retrieve system metrics.

```python
metrics = client.get_system_metrics()
print(metrics)
```

### get_user_info()

Get information about the current authenticated user.

```python
user = client.get_user_info()
print(user)
```

### get_token(username, password)

Obtain an authentication token using username and password.

```python
client = Client(base_url="http://localhost:8002")
client.get_token(username="admin", password="secret")
# Token is now stored in the client
```

---

## 2. Dataset Registration

### register_general_dataset(data, server='local')

Register a new general dataset.

```python
result = client.register_general_dataset({
    "name": "my-dataset",
    "title": "My Dataset Title",
    "owner_org": "my-organization",
    "notes": "Description of the dataset"
})
print(result)
```

**Parameters:**
- `data`: Dictionary with dataset metadata
- `server`: `'local'` (default) or `'global'`

### register_url(data, server='local')

Register a URL resource pointing to external data.

```python
result = client.register_url({
    "resource_name": "external-data",
    "resource_title": "External Data Source",
    "owner_org": "my-organization",
    "resource_url": "https://example.com/data.csv",
    "file_type": "CSV",
    "notes": "Data from external source"
})
print(result)
```

### register_s3_link(data, server='local')

Register a resource linked to S3 storage.

```python
result = client.register_s3_link({
    "resource_name": "s3-data",
    "resource_title": "S3 Stored Data",
    "owner_org": "my-organization",
    "s3_bucket": "my-bucket",
    "s3_key": "path/to/file.nc",
    "resource_s3": "my-bucket/path/to/file.nc",
    "notes": "Data stored in S3"
})
print(result)
```

### register_kafka_topic(data, server='local')

Register a Kafka topic as a streaming data source.

```python
result = client.register_kafka_topic({
    "resource_name": "sensor-stream",
    "resource_title": "Real-time Sensor Data",
    "owner_org": "my-organization",
    "topic": "sensors.temperature",
    "notes": "Live temperature readings"
})
print(result)
```

---

## 3. Dataset Search & Management

### search_datasets(terms, keys=None, server='global')

Search for datasets by terms.

```python
# Simple search
results = client.search_datasets(terms=["temperature"])

# Search with specific keys
results = client.search_datasets(
    terms=["utah", "satellite"],
    keys=["title", "notes"],
    server="local"
)

for ds in results:
    print(f"{ds['name']}: {ds.get('title', 'N/A')}")
```

**Parameters:**
- `terms`: List of search terms
- `keys`: Optional list of fields to search in
- `server`: `'global'` (default) or `'local'`

### advanced_search(search_data)

Perform advanced search with complex queries.

```python
results = client.advanced_search({
    "query": "temperature AND utah",
    "filters": {
        "organization": "noaa"
    },
    "limit": 10,
    "offset": 0
})
```

### update_general_dataset(dataset_id, data, server='local')

Full update of a dataset (replaces all fields).

```python
result = client.update_general_dataset(
    dataset_id="my-dataset-id",
    data={
        "resource_name": "my-dataset",
        "resource_title": "Updated Title",
        "owner_org": "my-organization",
        "notes": "Updated description"
    }
)
```

### patch_general_dataset(dataset_id, data, server='local')

Partial update of a dataset (only specified fields).

```python
result = client.patch_general_dataset(
    dataset_id="my-dataset-id",
    data={
        "notes": "Only updating the description"
    }
)
```

### update_url_resource(resource_id, data, server='local')

Update a URL resource.

```python
result = client.update_url_resource(
    resource_id="resource-id",
    data={
        "resource_url": "https://new-url.com/data.csv"
    }
)
```

### update_s3_resource(resource_id, data, server='local')

Update an S3 resource.

```python
result = client.update_s3_resource(
    resource_id="resource-id",
    data={
        "s3_key": "new/path/to/file.nc"
    }
)
```

### patch_s3_resource(resource_id, data, server='local')

Partial update of an S3 resource.

```python
result = client.patch_s3_resource(
    resource_id="resource-id",
    data={
        "notes": "Updated notes only"
    }
)
```

### patch_dataset_resource(dataset_id, resource_id, data, server='local')

Partial update of a specific resource within a dataset.

```python
result = client.patch_dataset_resource(
    dataset_id="dataset-id",
    resource_id="resource-id",
    data={
        "description": "Updated resource description"
    }
)
```

### delete_resource_by_id(resource_id, server='local')

Delete a resource by its ID.

```python
result = client.delete_resource_by_id(resource_id="resource-id")
```

### delete_resource_by_name(resource_name, server='local')

Delete a resource by its name.

```python
result = client.delete_resource_by_name(resource_name="my-dataset")
```

### delete_dataset_resource(dataset_id, resource_id, server='local')

Delete a specific resource from a dataset.

```python
result = client.delete_dataset_resource(
    dataset_id="dataset-id",
    resource_id="resource-id"
)
```

---

## 4. Organization Management

### list_organizations(name=None, server='global')

List all organizations.

```python
# List all organizations
orgs = client.list_organizations()
for org in orgs:
    print(org)

# Filter by name
orgs = client.list_organizations(name="noaa")

# From local server
orgs = client.list_organizations(server="local")
```

### register_organization(data, server='local')

Register a new organization.

```python
result = client.register_organization({
    "name": "my-org",
    "title": "My Organization",
    "description": "Organization description"
})
```

### delete_organization(organization_name, server='local')

Delete an organization.

```python
result = client.delete_organization(organization_name="my-org")
```

---

## 5. Service Management

### register_service(data, server='local')

Register a new service.

```python
result = client.register_service({
    "name": "data-processing-api",
    "title": "Data Processing API",
    "url": "https://api.example.com",
    "description": "API for processing datasets"
})
```

### update_service(service_id, data, server='local')

Full update of a service.

```python
result = client.update_service(
    service_id="service-id",
    data={
        "name": "data-processing-api",
        "title": "Updated API Title",
        "url": "https://new-api.example.com"
    }
)
```

### patch_service(service_id, data, server='local')

Partial update of a service.

```python
result = client.patch_service(
    service_id="service-id",
    data={
        "description": "Updated description only"
    }
)
```

---

## 6. S3 Storage Operations

### list_buckets()

List all available S3 buckets.

```python
result = client.list_buckets()
for bucket in result['buckets']:
    print(f"{bucket['name']} - Created: {bucket.get('creation_date')}")
```

### create_bucket(bucket_name)

Create a new S3 bucket.

```python
result = client.create_bucket("my-new-bucket")
print(result)
```

### get_bucket_info(bucket_name)

Get information about a specific bucket.

```python
info = client.get_bucket_info("my-bucket")
print(info)
```

### delete_bucket(bucket_name)

Delete an S3 bucket (must be empty).

```python
result = client.delete_bucket("my-bucket")
```

### list_objects(bucket_name, prefix=None)

List objects in a bucket.

```python
# List all objects
result = client.list_objects("my-bucket")
for obj in result['objects']:
    print(f"{obj['key']} - {obj['size']} bytes")

# List with prefix filter
result = client.list_objects("my-bucket", prefix="data/2024/")
```

### upload_object(bucket_name, object_key, file_data, content_type=None)

Upload an object to S3.

```python
# Upload from bytes
with open("local_file.csv", "rb") as f:
    data = f.read()

result = client.upload_object(
    bucket_name="my-bucket",
    object_key="path/to/file.csv",
    file_data=data,
    content_type="text/csv"
)
print(result)
```

### download_object(bucket_name, object_key)

Download an object from S3.

```python
data = client.download_object(
    bucket_name="my-bucket",
    object_key="path/to/file.csv"
)

# Save to local file
with open("downloaded_file.csv", "wb") as f:
    f.write(data)
```

### get_object_metadata(bucket_name, object_key)

Get metadata for an S3 object.

```python
metadata = client.get_object_metadata(
    bucket_name="my-bucket",
    object_key="path/to/file.csv"
)
print(metadata)
```

### delete_object(bucket_name, object_key)

Delete an object from S3.

```python
result = client.delete_object(
    bucket_name="my-bucket",
    object_key="path/to/file.csv"
)
```

### generate_presigned_download_url(bucket_name, object_key, expiration=None)

Generate a temporary URL for downloading an object.

```python
result = client.generate_presigned_download_url(
    bucket_name="my-bucket",
    object_key="path/to/file.csv",
    expiration=3600  # 1 hour in seconds
)
print(f"Download URL: {result['url']}")
```

### generate_presigned_upload_url(bucket_name, object_key, expiration=None)

Generate a temporary URL for uploading an object.

```python
result = client.generate_presigned_upload_url(
    bucket_name="my-bucket",
    object_key="uploads/new-file.csv",
    expiration=3600
)
print(f"Upload URL: {result['url']}")

# Use the URL to upload directly
import requests
with open("local_file.csv", "rb") as f:
    requests.put(result['url'], data=f)
```

---

## 7. Kafka Integration

### get_kafka_details()

Get Kafka connection details.

```python
kafka = client.get_kafka_details()
print(f"Host: {kafka['kafka_host']}")
print(f"Port: {kafka['kafka_port']}")
```

### register_kafka_topic(data, server='local')

Register a Kafka topic (see [Dataset Registration](#2-dataset-registration)).

### update_kafka_topic(dataset_id, data, server='local')

Update a Kafka topic resource.

```python
result = client.update_kafka_topic(
    dataset_id="topic-id",
    data={
        "topic": "new.topic.name",
        "notes": "Updated topic"
    }
)
```

---

## 8. Pelican Federation

Pelican is a federated data distribution system. These functions allow interaction with Pelican namespaces.

### list_federations()

List available Pelican federations.

```python
federations = client.list_federations()
print(federations)
```

### browse_pelican(path, federation='osdf', detail=False)

Browse files in a Pelican namespace.

```python
# Browse a directory
contents = client.browse_pelican(
    path="/osg-htc/public/",
    federation="osdf"
)
for item in contents:
    print(item)

# With detailed information
contents = client.browse_pelican(
    path="/osg-htc/public/",
    federation="osdf",
    detail=True
)
```

### get_pelican_info(path, federation='osdf')

Get metadata for a file without downloading.

```python
info = client.get_pelican_info(
    path="/osg-htc/public/data/file.csv",
    federation="osdf"
)
print(f"Size: {info['size']}")
print(f"Modified: {info['modified']}")
```

### download_pelican(path, federation='osdf', stream=False)

Download a file from Pelican.

```python
# Download entire file
data = client.download_pelican(
    path="/osg-htc/public/data/file.csv",
    federation="osdf"
)

# Stream large files
for chunk in client.download_pelican(
    path="/osg-htc/public/data/large_file.nc",
    federation="osdf",
    stream=True
):
    process(chunk)
```

### import_pelican_metadata(pelican_url, package_id, resource_name=None, resource_description=None)

Import a Pelican file as a resource in the local catalog.

```python
result = client.import_pelican_metadata(
    pelican_url="pelican://osg-htc/public/data/file.csv",
    package_id="my-dataset-id",
    resource_name="pelican-data",
    resource_description="Data imported from Pelican"
)
```

---

## 9. Jupyter Integration

### get_jupyter_details()

Get JupyterLab connection details.

```python
jupyter = client.get_jupyter_details()
print(f"URL: {jupyter['jupyter_url']}")
```

---

## Error Handling

All methods may raise exceptions on errors. Use try/except for robust code:

```python
try:
    result = client.create_bucket("my-bucket")
    print(f"Created: {result}")
except Exception as e:
    print(f"Error: {e}")
```

## Common Patterns

### Check Services Before Operations

```python
status = client.get_system_status()

if not status.get('backend_connected'):
    raise RuntimeError("Local catalog not available")

if not status.get('s3_connected'):
    raise RuntimeError("S3 storage not available")

# Proceed with operations...
```

### Upload and Register Data

```python
# 1. Create bucket
client.create_bucket("data-bucket")

# 2. Upload file
with open("data.csv", "rb") as f:
    client.upload_object(
        bucket_name="data-bucket",
        object_key="datasets/data.csv",
        file_data=f.read(),
        content_type="text/csv"
    )

# 3. Register in catalog
client.register_s3_link({
    "resource_name": "my-csv-data",
    "resource_title": "My CSV Dataset",
    "owner_org": "my-org",
    "s3_bucket": "data-bucket",
    "s3_key": "datasets/data.csv"
})
```

### Search and Download

```python
# Search for datasets
results = client.search_datasets(terms=["temperature"])

# Get first result with S3 data
for ds in results:
    if 's3_bucket' in ds and 's3_key' in ds:
        data = client.download_object(
            bucket_name=ds['s3_bucket'],
            object_key=ds['s3_key']
        )
        break
```


### python/03-s3-integration.md (4,763 bytes)

# S3 Integration with ndp-ep

This tutorial covers how to work with S3-compatible storage using the `ndp-ep` Python library.

## Prerequisites

- `ndp-ep` library installed (`pip install ndp-ep`)
- Access to an NDP-EP API instance with S3 enabled
- Valid authentication token

## Setup

```python
from ndp_ep import Client

# Initialize client with authentication
client = Client(
    base_url="https://your-api-endpoint.com",
    token="your-api-token"
)
```

## Bucket Operations

### List Buckets

```python
# Get all available buckets
result = client.list_buckets()
buckets = result['buckets']

for bucket in buckets:
    print(f"Bucket: {bucket['name']}")
    print(f"  Created: {bucket['creation_date']}")
```

### Create a Bucket

```python
# Create a new bucket
result = client.create_bucket('my-data-bucket')
print(result['message'])  # "Bucket 'my-data-bucket' created successfully"
```

### Get Bucket Info

```python
# Get information about a specific bucket
info = client.get_bucket_info('my-data-bucket')
print(info)
```

### Delete a Bucket

```python
# Delete an empty bucket
result = client.delete_bucket('my-data-bucket')
```

> **Note**: A bucket must be empty before it can be deleted.

## Object Operations

### Upload an Object

```python
# Upload from bytes
data = b'Hello, World!'
result = client.upload_object(
    bucket_name='my-data-bucket',
    object_key='hello.txt',
    file_data=data,
    content_type='text/plain'
)
print(f"Uploaded: {result['key']} ({result['size']} bytes)")
```

```python
# Upload a file from disk
with open('local_file.csv', 'rb') as f:
    file_data = f.read()

result = client.upload_object(
    bucket_name='my-data-bucket',
    object_key='data/my_file.csv',
    file_data=file_data,
    content_type='text/csv'
)
```

### List Objects in a Bucket

```python
# List all objects
result = client.list_objects('my-data-bucket')
objects = result['objects']

for obj in objects:
    print(f"{obj['key']} - {obj['size']} bytes")
```

```python
# List objects with a prefix (like a folder)
result = client.list_objects('my-data-bucket', prefix='data/')
```

### Download an Object

```python
# Download object as bytes
data = client.download_object('my-data-bucket', 'hello.txt')
print(data.decode('utf-8'))  # "Hello, World!"
```

```python
# Download and save to file
data = client.download_object('my-data-bucket', 'data/my_file.csv')
with open('downloaded_file.csv', 'wb') as f:
    f.write(data)
```

### Get Object Metadata

```python
# Get detailed metadata about an object
metadata = client.get_object_metadata('my-data-bucket', 'hello.txt')
print(f"Size: {metadata['size']} bytes")
print(f"Content-Type: {metadata['content_type']}")
print(f"Last Modified: {metadata['last_modified']}")
print(f"ETag: {metadata['etag']}")
```

### Delete an Object

```python
# Delete a single object
result = client.delete_object('my-data-bucket', 'hello.txt')
```

## Presigned URLs

Presigned URLs allow temporary access to objects without sharing credentials.

### Generate Download URL

```python
# Generate a presigned URL for downloading (valid for 1 hour)
result = client.generate_presigned_download_url(
    bucket_name='my-data-bucket',
    object_key='hello.txt',
    expiration=3600  # seconds
)
print(f"Download URL: {result['url']}")
print(f"Expires in: {result['expires_in']} seconds")
```

### Generate Upload URL

```python
# Generate a presigned URL for uploading
result = client.generate_presigned_upload_url(
    bucket_name='my-data-bucket',
    object_key='uploads/new_file.txt',
    expiration=3600
)
print(f"Upload URL: {result['url']}")
```

## Complete Example

Here's a complete workflow example:

```python
from ndp_ep import Client

# Initialize
client = Client(base_url="https://your-api-endpoint.com", token="your-token")

# Create a bucket for our project
client.create_bucket('project-data')

# Upload some data
dataset = b'id,name,value\n1,alpha,100\n2,beta,200\n3,gamma,300'
client.upload_object(
    bucket_name='project-data',
    object_key='datasets/sample.csv',
    file_data=dataset,
    content_type='text/csv'
)

# List what we have
result = client.list_objects('project-data')
for obj in result['objects']:
    print(f"  {obj['key']}")

# Generate a shareable link
url_result = client.generate_presigned_download_url(
    bucket_name='project-data',
    object_key='datasets/sample.csv',
    expiration=86400  # 24 hours
)
print(f"Share this link: {url_result['url']}")

# Cleanup when done
client.delete_object('project-data', 'datasets/sample.csv')
client.delete_bucket('project-data')
```

## Next Steps

- Check out the [complete examples](../examples/) for end-to-end workflows

## Related Resources

- [ndp-ep-py GitHub Repository](https://github.com/sci-ndp/ndp-ep-py)


### python/README.md (994 bytes)

# Python Library Tutorials

This folder contains tutorials for using the `ndp-ep` Python library.

## Contents

| Tutorial | Description |
|----------|-------------|
| [01 - Getting Started](./01-getting-started.md) | Installation, authentication, and basic operations |
| [02 - API Reference](./02-api-reference.md) | Complete reference for all library functions |
| [03 - S3 Integration](./03-s3-integration.md) | Bucket management, upload/download, presigned URLs |

## Prerequisites

- Python 3.8+
- ndp-ep library installed (`pip install ndp-ep`)
- Access to an NDP-EP API instance

## Topics Covered

- Installation and setup
- Authentication (token-based and username/password)
- Dataset search and management
- Organization management
- Resource registration and updates
- S3 integration (bucket management, upload/download, presigned URLs)
- Kafka topic management
- Real-time data streaming

## Related Resources

- [ndp-ep-py GitHub Repository](https://github.com/sci-ndp/ndp-ep-py)

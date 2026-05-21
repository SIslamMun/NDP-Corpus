# ndp_clm_agent_demo


### README.md (5,588 bytes)

# CLM Agents in NDP

AI-powered agents for querying and analyzing California Landscape Metrics (CLM) datasets using natural language. Built with Pydantic AI and FastMCP.

## Overview

This repository provides a Jupyter notebooks demonstrating different capabilities for interacting with CLM datasets:

## Features

- 🔍 **Natural Language Search** - Find datasets using plain English queries
- 💬 **Conversational Interface** - Maintains context across questions
- 📊 **Statistical Analysis** - Compute zonal statistics for California counties
- 🗺️ **Interactive Maps** - Visualize datasets with WMS layers
- 📈 **Distribution Charts** - Compare data distributions across regions
- 🔬 **Threshold Analysis** - Calculate areas above/below specified thresholds
- 📝 **Observability** - Optional Logfire integration for debugging

## Prerequisites

- Python 3.10 or higher
- Jupyter Notebook or JupyterLab
- OpenAI API key (or NRP API key for Qwen3 model)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/national-data-platform/ndp_clm_agent_demo.git
cd ndp_clm_agent_demo
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your API key:
```bash
# For OpenAI
OPENAI_API_KEY=your_openai_api_key

# Or for NRP (optional)
NRP_API_KEY=your_nrp_api_key
```

## Quick Start

Open `enhanced_clm_agent.ipynb` for advanced capabilities including maps and visualizations.

**Example questions:**
- "What is the average carbon turnover time in Los Angeles?"
- "Show me a map of the annual burn probability dataset"
- "Compare the distribution of carbon turnover between San Diego and Orange county"
- "Which county has the highest mean carbon turnover time?"


Full-featured agent with advanced capabilities:
- Statistical analysis (mean, median, min, max, std)
- Threshold-based area calculations
- Interactive WMS map visualization
- Distribution charts and histograms
- Multi-county comparisons
- Ranking and filtering

## Architecture

```
User Question
     ↓
ConversationalAgent (manages history)
     ↓
Pydantic AI Agent (processes with LLM)
     ↓
Tools (search_datasets, compute_stats, etc.)
     ↓
FastMCP Client → CLM-MCP Server
     ↓
GeoServer (WCS/WFS) → Datasets
     ↓
Response (with data/maps/charts)
```

## Available Tools

The enhanced agent includes these tools:

- `search_and_select_dataset` - Find relevant datasets by topic
- `get_county_statistics` - Compute zonal statistics
- `get_area_above_threshold` - Calculate area above a threshold
- `get_area_below_threshold` - Calculate area below a threshold
- `show_map` - Display interactive WMS map
- `get_value_distribution` - Get data distribution for charts

## Model Options

### OpenAI GPT-4o-mini (Default)
- Fast and reliable
- 60 second default timeout
- Requires OpenAI API key

### NRP Qwen3 (Alternative)
- Open-source model
- 180 second default timeout
- Requires NRP API key
- Set `MODEL = "nrp"` in the configuration cell

## Example Queries

### Basic Search
```
"Find datasets about carbon turnover"
"What datasets are available for burn probability?"
```

### Statistical Analysis
```
"What is the average carbon turnover time in Los Angeles?"
"Find the maximum annual burn probability in San Diego county"
"Rank the top 5 counties by mean carbon turnover time"
```

### Threshold Analysis
```
"What percentage of San Diego County has carbon turnover time above 100 years?"
"Show all counties where at least 30% of area has carbon turnover less than 20 years"
```

### Visualization
```
"Show me a map of the carbon turnover dataset"
"Show the data distribution for San Diego and Los Angeles"
"Compare distributions between San Diego, Los Angeles, and Orange county"
```

### Follow-up Questions
```
User: "What is the average carbon turnover in Los Angeles?"
Agent: [provides answer]
User: "How about San Diego?"
Agent: [understands context and provides San Diego statistics]
```

## Configuration

The notebooks connect to:
- **MCP Server**: `https://wenokn.fastmcp.app/mcp`
- **GeoServer**: `https://sparcal.sdsc.edu/geoserver`

These are configured in the `BASE_CONFIG` dictionary and can be modified if needed.

## Troubleshooting

### Timeout Errors
- For complex queries, the agent may timeout
- Try breaking down the question into simpler parts
- Switch to OpenAI model if using NRP
- Increase timeout in `conv_agent.ask(question, timeout=300)`

### Map Not Displaying
- Ensure the dataset has been selected via search first
- Check that WMS URLs are accessible
- Verify internet connection

### Chart Not Showing
- Distribution charts require multiple data points
- Ensure you're querying counties that exist in the dataset
- Check that the distribution tool received data

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Pydantic AI](https://ai.pydantic.dev/)
- Uses [FastMCP](https://github.com/jlowin/fastmcp) for Model Context Protocol
- California Landscape Metrics data from SDSC
- Powered by OpenAI GPT-4o-mini or NRP Qwen3

## Support

For issues or questions:
- Open an issue on GitHub
- Check existing issues for solutions
- Review the example questions in each notebook

## Citation

If you use this work in your research, please cite:

```bibtex
@software{clm_agents_ndp,
  title = {CLM Agents in NDP: AI-powered California Landscape Metrics Analysis},
  year = {2024},
  license = {MIT}
}
```


### enhanced_clm_agent.ipynb (56,643 bytes)

# enhanced_clm_agent


# California Landscape Metrics Analysis - Interactive Chat Interface

This notebook offers an interactive chatbox interface that allows users to query the California Landscape Metrics datasets using the agent.

## Ensure JupyterLab Widget Rendering is Enabled

`jupyterlab_widgets` provides the JupyterLab frontend extension that renders interactive widgets (like the chat interface in this notebook). 

If this package was just installed for the first time, **hard refresh your browser** (`Ctrl+Shift+R` on Windows/Linux, `Cmd+Shift+R` on Mac) before running the chat interface cell, otherwise the widget will not render correctly.

```python
try:
    import jupyterlab_widgets
    print("✓ jupyterlab_widgets already installed")
except ImportError:
    !pip install -q jupyterlab_widgets --user --no-warn-script-location
    print("✓ jupyterlab_widgets installed — please hard refresh your browser (Ctrl+Shift+R)")
```

## Setup and Imports

```python
# Install required packages if needed
!pip -q install ipywidgets pydantic-ai fastmcp openai nest-asyncio folium matplotlib markdown --no-warn-script-location
```

```python
import asyncio
import os
import nest_asyncio
from pydantic_ai import Agent, RunContext
from pydantic_ai.models.openai import OpenAIChatModel
from fastmcp import Client
from typing import Optional
from dataclasses import dataclass
import ipywidgets as widgets
from IPython.display import display, HTML, clear_output
from datetime import datetime

# Enable nested asyncio for Jupyter
nest_asyncio.apply()
print("✓ Imports successful")
```

## Configuration

```python
# Base configuration for GeoServer
BASE_CONFIG = {
    "wcs_base_url": "https://sparcal.sdsc.edu/geoserver",
    "wfs_base_url": "https://sparcal.sdsc.edu/geoserver/boundary/wfs",
    "feature_id": "boundary:ca_counties",
    "filter_column": "name"
}

# Initialize MCP client
mcp_client = Client("https://wenokn.fastmcp.app/mcp")

# Choose your model: "openai" or "nrp"
MODEL = "nrp"  # Change this to "nrp" to use Qwen3

print(f"✓ Configuration set with MODEL={MODEL}")
```

## Set API Keys

```python
from dotenv import load_dotenv
import os

# Load variables from .env file into environment
load_dotenv()

# Check API keys, or Update to your key
openai_key = os.getenv('OPENAI_API_KEY')
nrp_key = os.getenv('NRP_API_KEY')          
# nrp_key = "your-key"
# os.environ['NRP_API_KEY'] = nrp_key

if not openai_key:
    print("⚠️ Warning: OPENAI_API_KEY not set!")
else:
    print("✓ OpenAI API key found")

if not nrp_key:
    print("⚠️ Warning: NRP_API_KEY not set!")
else:
    print("✓ NRP API key found")

if MODEL == "openai":
    print("✓ Using OpenAI GPT-4o-mini")
elif MODEL == "nrp":
    print("✓ Using NRP Qwen3")
```

## Agent Setup

```python
from dataclasses import dataclass
from typing import Optional, List
import asyncio
from pydantic_ai import Agent, RunContext
from fastmcp import Client
import os

@dataclass
class AgentContext:
    """Context to store discovered dataset information."""
    current_coverage_id: Optional[str] = None
    current_dataset_info: Optional[dict] = None

BASE_CONFIG = {
    "wcs_base_url": "https://sparcal.sdsc.edu/geoserver",
    "wfs_base_url": "https://sparcal.sdsc.edu/geoserver/boundary/wfs",
    "feature_id": "boundary:ca_counties",
    "filter_column": "name"
}

def get_model_config(model_name: str = "openai"):
    """Get model configuration based on model name."""
    if model_name == "nrp":
        # Configure for NRP
        os.environ['OPENAI_BASE_URL'] = 'https://ellm.nrp-nautilus.io/v1'
        os.environ['OPENAI_API_KEY'] = os.getenv('NRP_API_KEY', '')
        return 'openai:qwen3'
    else:
        # Configure for OpenAI
        if 'OPENAI_BASE_URL' in os.environ:
            del os.environ['OPENAI_BASE_URL']
        return 'openai:gpt-4o-mini'

def create_internal_agent():
    """Create and configure the Pydantic AI agent."""
    
    agent = Agent(
        model=get_model_config(MODEL),
        deps_type=AgentContext,
        retries=2,
        system_prompt="""You are an expert in analyzing California Landscape Metrics datasets.

The input you receive will be the full conversation history in the format:
User: <question1>
Assistant: <answer1>
User: <question2>
Assistant: <answer2>
...
User: <current question>

Use this history to understand the context for follow-up questions.

You have access to these tools:
1. search_and_select_dataset: Search for the most relevant dataset based on the question
2. get_county_statistics: Compute statistics for one or more counties
3. get_area_above_threshold: Calculate percentage/area above a threshold for one or more counties
4. get_area_below_threshold: Calculate percentage/area below a threshold for one or more counties
5. show_map: Display a map visualization of the current dataset
6. get_value_distribution: Get value distribution for one or more counties (for charts/histograms)

**CRITICAL RULE FOR SEARCH:**
When calling search_and_select_dataset, construct a search query that represents the current user's question.
If the current question is a follow-up (e.g., "How about San Diego?"), incorporate context from the history to make it a standalone query (e.g., "What is the average carbon turnover time in San Diego?").
DO NOT pass vague follow-up phrases directly; always create a meaningful, context-aware query.
DO NOT use the entire history as the query.
When calling search_and_select_dataset, please remove the terms related to statistics like "average" and "mean" and the place names from the question like 'San Diego' or 'Los Angeles'. 
For example, for the question "What is the average carbon turnover time in Los Angeles?", use "carbon turnover time" to call search_and_select_dataset.

**WORKFLOW:**
1. If needed, start by calling search_and_select_dataset with the constructed query.
   - If a similar dataset was used in previous interactions (based on history), you may skip searching if it's clearly the same topic.
2. Once the dataset is selected, use the other tools to answer the question.
3. Include the dataset name and units in your final answer for context.

**For statistical questions:**
- Use get_county_statistics for mean, median, min, max, std
- Pass counties=None to get all counties
- For rankings, get all counties and sort results

**For threshold questions:**
- Use get_area_above_threshold or get_area_below_threshold
- Pass counties=None to get all counties
- For questions about many/all counties, you can use counties=None, but if concerned about timeouts, first get list of counties from get_county_statistics and sample 10-20

**For map visualization requests:**
- When users ask to "show the map", "visualize", "display map", or similar requests, use the show_map tool
- You must have a dataset selected first (via search_and_select_dataset)
- The tool will return a special marker that the interface will use to render the map

**For distribution/histogram requests:**
- When users ask to "show distribution", "show histogram", "compare distributions", "data distribution", or similar requests, use the get_value_distribution tool
- You must have a dataset selected first (via search_and_select_dataset)
- CRITICAL: For comparing distributions between regions, pass ALL county names as a LIST in a SINGLE call to get_value_distribution
  Example: get_value_distribution(counties=["San Diego", "Los Angeles"]) - NOT separate calls
- For single region, pass one county name as a string or single-item list
- For overview of all regions, pass counties=None (but this may be slow for many counties)
- The tool will return distribution data that the interface will visualize as charts
- DO NOT call get_value_distribution multiple times - always use ONE call with a list of counties

**Answer format:**
- Be precise with numbers and include units from the dataset
- Provide clear, concise answers
- Mention the dataset being used
- For distribution requests, briefly describe what the chart shows

""",
    )

    @agent.tool
    async def search_and_select_dataset(
        ctx: RunContext[AgentContext],
        question: str,
        top_k: int = 3
    ) -> dict:
        """Search for and select the most relevant dataset."""
        async with mcp_client:
            result = await mcp_client.call_tool(
                "search_datasets",
                {"query": question, "top_k": top_k}
            )
            
            data = result.data
            if data.get('success') and data.get('datasets'):
                best_dataset = data['datasets'][0]
                ctx.deps.current_coverage_id = best_dataset['wcs_coverage_id']
                ctx.deps.current_dataset_info = best_dataset
                
                return {
                    'success': True,
                    'selected_dataset': best_dataset,
                    'alternatives': data['datasets'][1:] if len(data['datasets']) > 1 else [],
                    'message': f"Selected: {best_dataset['title']}"
                }
            else:
                return {
                    'success': False,
                    'message': 'No suitable datasets found',
                    'error': data.get('error', 'Unknown error')
                }

    @agent.tool
    async def get_county_statistics(
        ctx: RunContext[AgentContext],
        counties: Optional[List[str]] = None,
        stats: List[str] = None
    ) -> dict:
        """Get statistics for one or more counties."""
        if not ctx.deps.current_coverage_id:
            return {
                'success': False,
                'error': 'No dataset selected. Call search_and_select_dataset first.'
            }
        
        if stats is None:
            stats = ["mean", "median", "min", "max", "std"]
        
        async with mcp_client:
            result = await mcp_client.call_tool(
                "compute_zonal_stats",
                {
                    **BASE_CONFIG,
                    "wcs_coverage_id": ctx.deps.current_coverage_id,
                    "filter_value": counties,
                    "stats": stats,
                    "max_workers": 16
                }
            )
            
            response = result.data
            if response.get('success'):
                response['dataset_info'] = {
                    'title': ctx.deps.current_dataset_info.get('title'),
                    'units': ctx.deps.current_dataset_info.get('data_units')
                }
            return response

    @agent.tool
    async def get_area_above_threshold(
        ctx: RunContext[AgentContext],
        counties: Optional[List[str]] = None,
        threshold: float = 100.0
    ) -> dict:
        """Calculate the percentage and area above a threshold for one or more counties."""
        if not ctx.deps.current_coverage_id:
            return {
                'success': False,
                'error': 'No dataset selected. Call search_and_select_dataset first.'
            }
        
        async with mcp_client:
            result = await mcp_client.call_tool(
                "zonal_count",
                {
                    **BASE_CONFIG,
                    "wcs_coverage_id": ctx.deps.current_coverage_id,
                    "filter_value": counties,
                    "threshold": threshold,
                    "max_workers": 16
                }
            )
            
            zonal_data = result.data
            if not zonal_data.get('success'):
                return zonal_data
            
            processed = []
            for stats in zonal_data['data']:
                county_name = stats[BASE_CONFIG['filter_column']]
                valid = stats['valid_pixels']
                above = stats['above_threshold_pixels']
                pixel_area = stats['pixel_area_square_meters']
                
                percentage = (above / valid * 100) if valid > 0 else 0
                area_sq_m = above * pixel_area
                area_sq_km = area_sq_m / 1_000_000
                
                processed.append({
                    'county': county_name,
                    'threshold': threshold,
                    'valid_pixels': valid,
                    'above_threshold_pixels': above,
                    'percentage': percentage,
                    'area_square_meters': area_sq_m,
                    'area_square_km': area_sq_km
                })
            
            return {
                'success': True,
                'data': processed,
                'total_features': zonal_data['total_features'],
                'processed_features': zonal_data['processed_features'],
                'dataset_info': {
                    'title': ctx.deps.current_dataset_info.get('title'),
                    'units': ctx.deps.current_dataset_info.get('data_units')
                }
            }

    @agent.tool
    async def get_area_below_threshold(
        ctx: RunContext[AgentContext],
        counties: Optional[List[str]] = None,
        threshold: float = 100.0
    ) -> dict:
        """Calculate the percentage and area below a threshold for one or more counties."""
        if not ctx.deps.current_coverage_id:
            return {
                'success': False,
                'error': 'No dataset selected. Call search_and_select_dataset first.'
            }
        
        async with mcp_client:
            result = await mcp_client.call_tool(
                "zonal_count",
                {
                    **BASE_CONFIG,
                    "wcs_coverage_id": ctx.deps.current_coverage_id,
                    "filter_value": counties,
                    "threshold": threshold,
                    "max_workers": 16
                }
            )
            
            zonal_data = result.data
            if not zonal_data.get('success'):
                return zonal_data
            
            processed = []
            for stats in zonal_data['data']:
                county_name = stats[BASE_CONFIG['filter_column']]
                valid = stats['valid_pixels']
                above = stats['above_threshold_pixels']
                below = valid - above
                pixel_area = stats['pixel_area_square_meters']
                
                percentage = (below / valid * 100) if valid > 0 else 0
                area_sq_m = below * pixel_area
                area_sq_km = area_sq_m / 1_000_000
                
                processed.append({
                    'county': county_name,
                    'threshold': threshold,
                    'valid_pixels': valid,
                    'below_threshold_pixels': below,
                    'percentage': percentage,
                    'area_square_meters': area_sq_m,
                    'area_square_km': area_sq_km
                })
            
            return {
                'success': True,
                'data': processed,
                'total_features': zonal_data['total_features'],
                'processed_features': zonal_data['processed_features'],
                'dataset_info': {
                    'title': ctx.deps.current_dataset_info.get('title'),
                    'units': ctx.deps.current_dataset_info.get('data_units')
                }
            }
    
    @agent.tool
    async def show_map(ctx: RunContext[AgentContext]) -> dict:
        """Display a map visualization of the current dataset using WMS layer."""
        if not ctx.deps.current_dataset_info:
            return {
                'success': False,
                'error': 'No dataset selected. Call search_and_select_dataset first.'
            }
        
        dataset = ctx.deps.current_dataset_info
        
        # Return map configuration that the interface will use to render
        return {
            'success': True,
            'action': 'show_map',
            'map_data': {
                'wms_base_url': dataset.get('wms_base_url'),
                'wms_layer_name': dataset.get('wms_layer_name'),
                'title': dataset.get('title'),
                'description': dataset.get('description', ''),
                'units': dataset.get('data_units', '')
            },
            'message': f"Displaying map for: {dataset.get('title')}"
        }
    
    @agent.tool
    async def get_value_distribution(
        ctx: RunContext[AgentContext],
        counties: Optional[List[str]] = None,
        num_bins: int = 10
    ) -> dict:
        """Get value distribution for one or more counties to create histograms/charts.
        
        IMPORTANT: To compare multiple counties, pass them ALL in ONE call as a list.
        Example: counties=["San Diego", "Los Angeles", "Orange"]
        DO NOT call this function multiple times for different counties.
        
        Args:
            counties: List of county names, single county, or None for all counties
                     For comparison: ["San Diego", "Los Angeles"] 
                     For single: ["San Diego"] or "San Diego"
                     For all: None
            num_bins: Number of bins for continuous data (default: 10)
        """
        if not ctx.deps.current_coverage_id:
            return {
                'success': False,
                'error': 'No dataset selected. Call search_and_select_dataset first.'
            }
        
        async with mcp_client:
            result = await mcp_client.call_tool(
                "zonal_distribution",
                {
                    **BASE_CONFIG,
                    "wcs_coverage_id": ctx.deps.current_coverage_id,
                    "filter_value": counties,
                    "num_bins": num_bins,
                    "global_bins": True,
                    "categorical_threshold": 20,
                    "max_workers": 16
                }
            )
            
            dist_data = result.data
            if dist_data.get('success'):
                dist_data['dataset_info'] = {
                    'title': ctx.deps.current_dataset_info.get('title'),
                    'units': ctx.deps.current_dataset_info.get('data_units')
                }
                # Add action marker for the interface
                dist_data['action'] = 'show_distribution'
            
            return dist_data
    
    return agent

class HistoryAwareAgent:
    def __init__(self):
        self.internal_agent = create_internal_agent()
        self.history = []
        # Set default timeout based on model
        self.default_timeout = 300 if MODEL == "nrp" else 180

    async def run(self, question: str, timeout: int = None, deps: Optional[AgentContext] = None) -> dict:
        """Run the agent with history-aware input. Returns dict with output and optional map_data/distribution_data."""
        # Use default timeout if not specified
        if timeout is None:
            timeout = self.default_timeout
            
        # Build the full input with history
        full_input = "\n".join(self.history) + (f"\nUser: {question}" if self.history else f"User: {question}")

        try:
            # Pass deps to internal agent's run method
            result = await asyncio.wait_for(
                self.internal_agent.run(full_input, deps=deps),
                timeout=timeout
            )
            output = result.output if hasattr(result, 'output') else str(result)
            
            # Check if any tool result contains map data or distribution data
            map_data = None
            distribution_data = None
            
            if hasattr(result, 'all_messages'):
                for msg in result.all_messages():
                    if hasattr(msg, 'parts'):
                        for part in msg.parts:
                            if hasattr(part, 'content') and isinstance(part.content, dict):
                                if part.content.get('action') == 'show_map':
                                    map_data = part.content.get('map_data')
                                elif part.content.get('action') == 'show_distribution':
                                    # Always use the LAST distribution data (most complete)
                                    # This handles cases where agent makes multiple calls
                                    new_dist = part.content
                                    # Only replace if new data has more records
                                    if distribution_data is None or len(new_dist.get('data', [])) > len(distribution_data.get('data', [])):
                                        distribution_data = new_dist
                                        print(f"Distribution data updated: {len(new_dist.get('data', []))} records")

            # Append to history
            self.history.append(f"User: {question}")
            self.history.append(f"Assistant: {output}")

            return {
                'output': output,
                'map_data': map_data,
                'distribution_data': distribution_data
            }
        except asyncio.TimeoutError:
            return {
                'output': f"Error: Question timed out after {timeout} seconds. This query may be too complex.",
                'map_data': None,
                'distribution_data': None
            }
        except Exception as e:
            return {
                'output': f"Error: {type(e).__name__}: {str(e)[:200]}",
                'map_data': None,
                'distribution_data': None
            }

# Create the agent
agent = HistoryAwareAgent()
print(f"✓ Agent created successfully with {MODEL}!")
```

## Chat Interface

```python
from IPython.display import Javascript, display, clear_output, HTML
import ipywidgets as widgets
from datetime import datetime
import folium
from folium import WmsTileLayer
import json
import matplotlib.pyplot as plt
import io
import base64
import markdown
import html as html_module

class ChatInterface:
    def __init__(self, agent):
        self.agent = agent
        self.messages_container = []
        
        # Output area that takes available space
        self.output_area = widgets.VBox(
            layout=widgets.Layout(
                border='1px solid #ddd',
                height='calc(100vh - 350px)',  # Dynamic height based on viewport
                min_height='400px',
                overflow_y='auto',
                padding='10px',
                margin='0 0 10px 0'
            )
        )
        
        self.input_box = widgets.Textarea(
            placeholder='Ask a question about California Landscape Metrics...',
            layout=widgets.Layout(width='100%', height='100px', margin='10px 0')
        )
        
        self.send_button = widgets.Button(
            description='Send',
            button_style='primary',
            icon='paper-plane',
            layout=widgets.Layout(width='100px', margin='0 5px 0 0')
        )
        
        self.clear_button = widgets.Button(
            description='Clear',
            button_style='warning',
            icon='trash',
            layout=widgets.Layout(width='100px', margin='0 5px 0 0')
        )
        
        self.status_label = widgets.HTML(
            value="✅ Ready",
            layout=widgets.Layout(margin='0 0 0 10px')
        )
        
        # Add button click handlers
        self.send_button.on_click(self.on_send_clicked)
        self.clear_button.on_click(self.on_clear_clicked)
        
        button_box = widgets.HBox([
            self.send_button, 
            self.clear_button, 
            self.status_label
        ])
        
        self.interface = widgets.VBox([
            widgets.HTML(value="<h3>🌲 California Landscape Metrics Chat</h3>"),
            self.output_area,
            self.input_box,
            button_box
        ], layout=widgets.Layout(width='100%', max_width='1200px', margin='0 auto'))
        
        # Add welcome message
        self._add_message(
            "Welcome! Ask me about California landscape metrics.\n\n"
            "Examples:\n"
            "- What is the average carbon turnover time in Los Angeles?\n"
            "- Find the maximum annual burn probability in San Diego county\n"
            "- Show me a map of the carbon turnover dataset\n"
            "- Show me the data distribution for San Diego and Los Angeles",
            "system"
        )
    
    def _get_wms_bounds(self, wms_url, layer_name):
        """Try to get WMS layer bounds from GetCapabilities. Returns California bounds as fallback."""
        # Default California bounds [south, west, north, east]
        california_bounds = [[32.5, -124.5], [42.0, -114.0]]
        
        try:
            import requests
            from xml.etree import ElementTree as ET
            
            # Request GetCapabilities
            params = {
                'service': 'WMS',
                'version': '1.1.0',
                'request': 'GetCapabilities'
            }
            response = requests.get(wms_url + '/wms', params=params, timeout=10)
            
            if response.status_code == 200:
                root = ET.fromstring(response.content)
                # Find the layer
                for layer in root.iter('Layer'):
                    name_elem = layer.find('Name')
                    if name_elem is not None and name_elem.text == layer_name:
                        # Get LatLonBoundingBox
                        bbox = layer.find('LatLonBoundingBox')
                        if bbox is not None:
                            minx = float(bbox.get('minx'))
                            miny = float(bbox.get('miny'))
                            maxx = float(bbox.get('maxx'))
                            maxy = float(bbox.get('maxy'))
                            return [[miny, minx], [maxy, maxx]]
        except:
            pass
        
        return california_bounds
    
    def _get_legend_url(self, wms_url, layer_name, style_name=None):
        """Generate WMS GetLegendGraphic URL."""
        from urllib.parse import urlencode
        
        params = {
            'service': 'WMS',
            'version': '1.1.0',
            'request': 'GetLegendGraphic',
            'layer': layer_name,
            'format': 'image/png',
            'width': '20',
            'height': '20',
            'legend_options': 'fontAntiAliasing:true;fontSize:10;fontName:Arial;dx:5;absoluteMargins:true'
        }
        
        if style_name:
            params['style'] = style_name
        
        return f"{wms_url}/wms?{urlencode(params)}"
    
    def _create_map(self, map_data, style_name=None):
        """Create a Folium map with WMS layer.
        
        Args:
            map_data: Dictionary containing WMS layer information
            style_name: Optional WMS style name to apply (e.g., 'layer_name_std')
        """
        try:
            wms_url = map_data.get('wms_base_url', '')
            layer_name = map_data.get('wms_layer_name', '')
            title = map_data.get('title', 'Dataset')
            
            # Get WMS bounds
            bounds = self._get_wms_bounds(wms_url, layer_name)
            
            # Create map centered on bounds
            center_lat = (bounds[0][0] + bounds[1][0]) / 2
            center_lon = (bounds[0][1] + bounds[1][1]) / 2
            
            m = folium.Map(
                location=[center_lat, center_lon],
                tiles='OpenStreetMap',
                control_scale=True
            )
            
            # Fit bounds to WMS extent
            m.fit_bounds(bounds)
            
            if wms_url and layer_name:
                # Add WMS tile layer with optional style
                wms_params = {
                    'url': wms_url + '/wms',
                    'layers': layer_name,
                    'name': title,
                    'fmt': 'image/png',
                    'transparent': True,
                    'overlay': True,
                    'control': True,
                    'version': '1.1.0'
                }
                
                # Add style if provided
                if style_name:
                    wms_params['styles'] = style_name
                
                wms = WmsTileLayer(**wms_params)
                wms.add_to(m)
                
                # Add layer control
                folium.LayerControl().add_to(m)
                
                # Add legend with unit
                legend_url = self._get_legend_url(wms_url, layer_name, style_name)
                units = map_data.get('units', '')
                unit_text = f'<p style="margin: 5px 0 0 0; font-size: 11px; color: #333; text-align: center;">Units: {units}</p>' if units else ''
                
                legend_html = f'''
                <div style="position: fixed; 
                            top: 10px; 
                            right: 10px; 
                            background-color: white; 
                            z-index: 9999; 
                            padding: 10px; 
                            border: 2px solid grey;
                            border-radius: 5px; 
                            box-shadow: 2px 2px 6px rgba(0,0,0,0.3);">
                    <img src="{legend_url}" alt="Legend" style="display: block;">
                    {unit_text}
                </div>
                '''
                m.get_root().html.add_child(folium.Element(legend_html))
            
            return m
            
        except Exception as e:
            print(f"Error creating map: {e}")
            return None
    
    def _create_distribution_chart(self, distribution_data):
        """Create a matplotlib chart from distribution data.
        
        Args:
            distribution_data: Dictionary containing distribution information
        
        Returns:
            Base64 encoded PNG image string
        """
        try:
            data = distribution_data.get('data', [])
            dist_type = distribution_data.get('distribution_type', 'continuous')
            dataset_info = distribution_data.get('dataset_info', {})
            title = dataset_info.get('title', 'Value Distribution')
            units = dataset_info.get('units', '')
            filter_column = 'name'  # From BASE_CONFIG
            
            if not data:
                return None
            
            # Debug: print data to see what we received
            print(f"Distribution data received: {len(data)} records")
            counties_in_data = list(set([d.get(filter_column) for d in data]))
            print(f"Counties in data: {counties_in_data}")
            
            # Create figure with high DPI for better quality
            fig, ax = plt.subplots(figsize=(10, 5), dpi=100)
            
            # Get unique counties and ensure we have all of them
            counties = sorted(list(set([d.get(filter_column) for d in data if filter_column in d])))
            print(f"Unique counties to plot: {counties}")
            
            if not counties:
                print("No counties found in data!")
                return None
            
            colors = plt.cm.tab10(range(len(counties)))
            
            if dist_type == 'categorical':
                # Categorical distribution - bar chart
                # Group data by county
                import numpy as np
                
                values = sorted(list(set([d['value'] for d in data])))
                x = np.arange(len(values))
                width = 0.8 / len(counties) if len(counties) > 1 else 0.5
                
                for i, county in enumerate(counties):
                    county_data = [d for d in data if d[filter_column] == county]
                    counts = []
                    for val in values:
                        matching = [d['count'] for d in county_data if d['value'] == val]
                        counts.append(matching[0] if matching else 0)
                    
                    offset = (i - len(counties)/2) * width + width/2
                    ax.bar(x + offset, counts, width, label=county, alpha=0.7, color=colors[i])
                
                ax.set_xlabel(f'Value', fontsize=11)
                ax.set_ylabel('Count (pixels)', fontsize=11)
                ax.set_xticks(x)
                ax.set_xticklabels([str(v) for v in values])
                ax.legend(fontsize=10)
                ax.set_title(f'{title}\nCategorical Distribution', fontsize=12, fontweight='bold', pad=10)
                
            else:
                # Continuous distribution - histogram
                bins = distribution_data.get('bins', [])
                bin_labels = distribution_data.get('bin_labels', [])
                
                if not bins:
                    return None
                
                # Calculate bin centers and width
                bin_centers = [(bins[i] + bins[i+1]) / 2 for i in range(len(bins)-1)]
                bin_width = bins[1] - bins[0] if len(bins) > 1 else 1
                width = bin_width * 0.8 / len(counties) if len(counties) > 1 else bin_width * 0.7
                
                for i, county in enumerate(counties):
                    county_data = [d for d in data if d.get(filter_column) == county]
                    # Sort by bin_index to ensure correct order
                    county_data = sorted(county_data, key=lambda x: x.get('bin_index', 0))
                    counts = [d['count'] for d in county_data]
                    
                    print(f"Plotting {county}: {len(counts)} bins")
                    
                    # Calculate offsets for multiple counties
                    if len(counties) > 1:
                        offset = (i - len(counties)/2) * width + width/2
                        positions = [bc + offset for bc in bin_centers]
                    else:
                        positions = bin_centers
                    
                    ax.bar(positions, counts, width, label=county, alpha=0.7, color=colors[i])
                
                xlabel = f'Value Range ({units})' if units else 'Value Range'
                ax.set_xlabel(xlabel, fontsize=11)
                ax.set_ylabel('Count (pixels)', fontsize=11)
                ax.legend(fontsize=10)
                ax.set_title(f'{title}\nValue Distribution', fontsize=12, fontweight='bold', pad=10)
            
            ax.grid(True, alpha=0.3, linestyle='--')
            plt.tight_layout()
            
            # Convert plot to base64 image
            buf = io.BytesIO()
            plt.savefig(buf, format='png', dpi=100, bbox_inches='tight')
            buf.seek(0)
            img_base64 = base64.b64encode(buf.read()).decode('utf-8')
            plt.close(fig)
            
            return img_base64
            
        except Exception as e:
            print(f"Error creating distribution chart: {e}")
            import traceback
            traceback.print_exc()
            return None
    
    def _add_message(self, text, role="user", map_data=None, distribution_data=None):
        """Add a message to the chat interface, optionally with a map or distribution chart."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        if role == "user":
            color = "#007bff"
            icon = "👤"
            label = "You"
            bg_color = "#e7f3ff"
        elif role == "assistant":
            color = "#28a745"
            icon = "🤖"
            label = "Assistant"
            bg_color = "#e8f5e9"
        else:
            color = "#6c757d"
            icon = "ℹ️"
            label = "System"
            bg_color = "#f8f9fa"
        
        # Convert markdown to HTML for assistant messages
        if role == "assistant":
            try:
                # Convert markdown to HTML with extensions
                html_content = markdown.markdown(
                    str(text), 
                    extensions=['extra', 'nl2br', 'sane_lists']
                )
            except:
                # Fallback to escaped text if markdown conversion fails
                html_content = html_module.escape(str(text)).replace('\n', '<br>')
        else:
            # For user and system messages, just escape HTML
            html_content = html_module.escape(str(text)).replace('\n', '<br>')
        
        message_html = widgets.HTML(
            value=f"""
            <div style='margin: 10px 0; padding: 12px; background-color: {bg_color}; 
                        border-radius: 8px; border-left: 4px solid {color}; box-shadow: 0 1px 3px rgba(0,0,0,0.1);
                        position: relative; z-index: 1;'>
                <div style='display: flex; justify-content: space-between; margin-bottom: 8px;'>
                    <strong style='color: {color};'>{icon} {label}</strong>
                    <span style='color: #999; font-size: 0.85em;'>{timestamp}</span>
                </div>
                <div style='line-height: 1.6;'>
                    <style>
                        h1, h2, h3, h4 {{ margin-top: 0.5em; margin-bottom: 0.3em; color: #333; }}
                        h3 {{ font-size: 1.1em; font-weight: 600; }}
                        ul, ol {{ margin: 0.5em 0; padding-left: 1.5em; }}
                        li {{ margin: 0.25em 0; }}
                        p {{ margin: 0.5em 0; }}
                        strong {{ font-weight: 600; }}
                        code {{ background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px; font-family: monospace; }}
                        pre {{ background-color: #f4f4f4; padding: 8px; border-radius: 4px; overflow-x: auto; }}
                    </style>
                    {html_content}
                </div>
            </div>
            """
        )
        
        self.messages_container.append(message_html)
        
        # Add distribution chart if provided (takes priority over map)
        if distribution_data:
            img_base64 = self._create_distribution_chart(distribution_data)
            if img_base64:
                chart_html = f"""
                <div style='width: 98%; margin: 10px 0; clear: both;'>
                    <div style='width: 100%; border: 1px solid #ddd; border-radius: 8px; overflow: hidden; 
                                padding: 10px; background-color: white;'>
                        <img src="data:image/png;base64,{img_base64}" 
                             style="width: 100%; height: auto; display: block;" 
                             alt="Distribution Chart">
                    </div>
                </div>
                """
                chart_widget = widgets.HTML(
                    value=chart_html,
                    layout=widgets.Layout(width='100%')
                )
                self.messages_container.append(chart_widget)
        
        # Add map if provided (and no distribution chart)
        elif map_data:
            # Optionally append '_std' to the layer name for the style
            layer_name = map_data.get('wms_layer_name', '')
            style_name = f"{layer_name}_std" if layer_name else None
            
            folium_map = self._create_map(map_data, style_name=style_name)
            if folium_map:
                # Create a wrapper div to contain and isolate the map
                map_html_content = folium_map._repr_html_()
                wrapped_html = f"""
                <div style='width: 98%; margin: 10px 0; clear: both;'>
                    <div style='width: 100%; height: 300px; border: 1px solid #ddd; border-radius: 8px; overflow: hidden; position: relative;'>
                        <div style='width: 100%; height: 100%;'>
                            {map_html_content}
                        </div>
                    </div>
                </div>
                """
                
                map_widget = widgets.HTML(
                    value=wrapped_html,
                    layout=widgets.Layout(width='100%')
                )
                self.messages_container.append(map_widget)
        
        # Update the output area with all messages
        self.output_area.children = tuple(self.messages_container)
    
    def on_send_clicked(self, button):
        question = self.input_box.value.strip()
        if not question:
            return
        
        self._add_message(question, "user")
        self.input_box.value = ""
        self.send_button.disabled = True
        self.input_box.disabled = True
        self.status_label.value = "<span style='color: orange;'>⏳ Processing...</span>"
        
        try:
            ctx = AgentContext()
            result = asyncio.get_event_loop().run_until_complete(
                asyncio.wait_for(self.agent.run(question, deps=ctx), timeout=180)
            )
            
            # Handle both old string format and new dict format
            if isinstance(result, dict):
                answer = result.get('output', str(result))
                map_data = result.get('map_data')
                distribution_data = result.get('distribution_data')
            else:
                answer = result.output if hasattr(result, 'output') else str(result)
                map_data = None
                distribution_data = None
            
            self._add_message(answer, "assistant", map_data=map_data, distribution_data=distribution_data)
            self.status_label.value = "<span style='color: green;'>✅ Ready</span>"
            
        except asyncio.TimeoutError:
            error_msg = "Request timed out after 3 minutes. Please try a simpler question or try again."
            self._add_message(error_msg, "system")
            self.status_label.value = "<span style='color: red;'>❌ Timeout</span>"
            
        except Exception as e:
            import traceback
            error_msg = f"Error: {str(e)}\n\n{traceback.format_exc()}"
            self._add_message(error_msg, "system")
            self.status_label.value = "<span style='color: red;'>❌ Error</span>"
        
        finally:
            self.send_button.disabled = False
            self.input_box.disabled = False
    
    def on_clear_clicked(self, button):
        self.messages_container = []
        self.output_area.children = tuple(self.messages_container)
        self._add_message(
            "Chat cleared. Ready for new questions!\n\n"
            "Examples:\n"
            "- What is the average carbon turnover time in Los Angeles?\n"
            "- Find the maximum annual burn probability in San Diego county\n"
            "- Show me a map of the carbon turnover dataset\n"
            "- Show me the data distribution for San Diego and Los Angeles",
            "system"
        )
    
    def display(self):
        # Clear any previous output in the cell
        clear_output(wait=True)
        
        # Display the interface
        display(HTML("""
        <style>
            /* Make the cell output area expand */
            .jp-Cell-outputArea {
                max-height: none !important;
            }
            .output_scroll {
                max-height: none !important;
                overflow-y: visible !important;
            }
        </style>
        """))
        
        display(self.interface)


# Create and display chat interface
chat = ChatInterface(agent)
chat.display()
```

## Sample Questions

1. Find the maximum annual burn probability in San Diego county.
2. Could you do the same for Orange county?
3. Los Angeles, Please!
4. Show the data distribution for San Diego, Los Angeles and Orange county.
5. Show me a map of the annual burn probability dataset.
6. Which county has higher average annual burn probability, San Diego or Los Angeles?
7. What percentage of area in San Diego County has carbon turnover time above 100 years?
8. Rank the top 5 counties by mean carbon turnover time.
9. Show all counties where at least 30% of the total area has a carbon turnover time of less than 20 years.

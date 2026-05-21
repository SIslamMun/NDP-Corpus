# ep-api

> NDP Endpoint API

## Documentation Files

### README.md (26,726 bytes)

# National Data Platform - Endpoint API (NDP-EP API)

A REST API that provides **unified access** to dataset management across the [National Data Platform (NDP)](https://nationaldataplatform.org). Users can search the NDP catalog, ingest new datasets, and manage their own data collections through a single, streamlined M2M interface.

## 🌐 About the National Data Platform

The NDP-EP API integrates seamlessly with the National Data Platform ecosystem:

- **🔐 Unified Authentication**: Uses NDP's authentication system - your NDP account works directly with this API
- **📊 Multi-Catalog Management**: Control and access datasets across three different CKAN environments
- **🔍 Centralized Discovery**: Search the main NDP catalog and other connected data sources
- **📥 Streamlined Ingestion**: Simplified workflow for adding new datasets to the platform

## 🏗️ NDP Catalog Architecture

The National Data Platform uses CKAN as its data catalog management software. This API provides access to three different catalog environments, each with specific access levels and purposes:

### 1. **Local Catalog** 🏠 (CKAN or MongoDB)
You can use your own catalog backend for local dataset management, with your choice of storage (see [Adding New Catalog Backends](docs/adding-catalog-backends.md) for custom implementations):

**CKAN Backend** (Traditional):
- Full CKAN compatibility with all extensions
- Ideal if you already have CKAN infrastructure
- Complete administrative access to your catalog

**MongoDB Backend** (Modern NoSQL):
- Lightweight, no CKAN installation required
- Fast document-based storage
- Easy to deploy and scale
- Perfect for new deployments or cloud-native environments

Both options give you:
- **Full Control**: Create, read, update, and delete datasets
- **Use Case**: Personal or organizational data catalogs
- **Flexibility**: Switch between backends via configuration

### 2. **NDP Central Catalog** 🌍
This is the main public catalog of the National Data Platform. Through this API you can:
- **Read-Only Access**: Search and discover publicly available datasets
- **Use Case**: Exploring the official NDP data collection
- **Permissions**: Search and view only - no modifications allowed

### 3. **PreCKAN (Staging Environment)** 🔄
This is a staging environment provided by the NDP for dataset submission and review. Here's how it works:
- **Ingestion Gateway**: Submit new datasets for validation and review
- **Use Case**: Contributing datasets to the NDP central catalog
- **Workflow**: Your datasets are analyzed, validated, and if approved, promoted to the central catalog

## 🚀 Key Features

- **🔐 NDP Authentication Integration**: Seamless login with your National Data Platform credentials
- **🔄 Pluggable Catalog Backends**: Choose between CKAN or MongoDB for your local catalog
- **🔍 Federated Search**: Discover datasets across local, NDP, and staging catalogs
- **🚀 Specialized Ingestion**: Purpose-built endpoints for Kafka topics, S3 resources, web services, and URLs
- **📦 MINIO S3 Storage**: Direct bucket and object management with secure presigned URLs
- **📋 General Dataset Management**: Flexible API for managing datasets with custom metadata
- **🔧 Service Registry**: Register and discover other services (such as microservices, APIs, or apps)
- **🤖 AI Agent Integration**: Model Context Protocol (MCP) support for AI assistants to interact with the API
- **🌐 Pelican Federation**: Access distributed scientific data from OSDF and serve your own data to federations
- **📈 System Monitoring**: Built-in metrics and health monitoring
- **📚 RESTful API**: Comprehensive OpenAPI/Swagger documentation
- **🔌 Extensible Architecture**: Easy to add new catalog backends (Elasticsearch, PostgreSQL, etc.)

## ⚡ Quick Start

Get the NDP-EP API running with Docker in under 5 minutes:

### Prerequisites

Before you begin, ensure you have:

- **Docker**: Container platform for running the API
  - Install from [docker.com](https://www.docker.com/get-started)
  - Verify installation: `docker --version`

- **Docker Compose**: Container orchestration tool
  - Usually included with Docker Desktop
  - Verify installation: `docker-compose --version`

- **CKAN Instance** (Optional):
  - **Required only if**: You want to use local CKAN or PreCKAN features
  - **Not needed if**: You only plan to use NDP Central Catalog (read-only access)
  - Install CKAN following the [official documentation](https://docs.ckan.org/en/latest/maintaining/installing/index.html)

- **S3-Compatible Storage** (Optional):
  - **Required only if**: You want to use S3 object storage features
  - **Not needed if**: You don't plan to use bucket/object management endpoints
  - **Example**: MINIO is a popular S3-compatible service - see [MINIO setup guide](docs/minio-setup.md) for Docker installation instructions

### 1. Configure Environment Variables

Create a `.env` file or prepare environment variables with your configuration:

```bash
# API CONFIGURATION
# API root path prefix (e.g., "/test" or "" for root)
# If empty or not set, the API will be available at the root path
# This is useful when deploying the API behind a reverse proxy at a subpath
ROOT_PATH=

# ORGANIZATION SETTINGS
# Your organization name for identification and metrics
ORGANIZATION="My organization"

# Endpoint name for identification in metrics and monitoring
EP_NAME="EP Name"

# METRICS CONFIGURATION
# Interval in seconds for sending metrics (default: 3300 seconds = 55 minutes)
METRICS_INTERVAL_SECONDS=3300

# AUTHENTICATION CONFIGURATION
# URL for the authentication API to retrieve user information
# This endpoint is used to validate tokens and fetch user details
AUTH_API_URL=https://idp.nationaldataplatform.org/temp/information

# ACCESS CONTROL (Optional)
# Enable group-based access control (True/False)
# When enabled, only users belonging to one of the groups in GROUP_NAMES
# can perform POST, PUT, DELETE operations. Other authenticated users
# will receive 403 Forbidden on write operations.
# GET endpoints remain public regardless of this setting.
ENABLE_GROUP_BASED_ACCESS=False

# Comma-separated list of allowed groups for write operations
# Only used when ENABLE_GROUP_BASED_ACCESS=True
GROUP_NAMES=admins,developers

# LOCAL CATALOG CONFIGURATION
# Choose your local catalog backend: "ckan" or "mongodb"
# Global and Pre-CKAN always use CKAN regardless of this setting
LOCAL_CATALOG_BACKEND=ckan

# LOCAL CKAN CONFIGURATION (if LOCAL_CATALOG_BACKEND=ckan)
# Enable or disable the local CKAN instance (True/False)
# Set to True if you have your own CKAN installation
CKAN_LOCAL_ENABLED=True

# Base URL of your local CKAN instance (Required if CKAN_LOCAL_ENABLED=True)
# Example: http://192.168.1.134:5000/ or https://your-ckan-domain.com/
CKAN_URL=http://XXX.XXX.XXX.XXX:XXXX/

# API Key for CKAN authentication (Required if CKAN_LOCAL_ENABLED=True)
# Get this from your CKAN user profile -> API Tokens
CKAN_API_KEY=

# MONGODB CONFIGURATION (if LOCAL_CATALOG_BACKEND=mongodb)
# MongoDB connection string
MONGODB_CONNECTION_STRING=mongodb://localhost:27017

# MongoDB database name for local catalog
MONGODB_DATABASE=ndp_local_catalog

# PRE-CKAN CONFIGURATION
# Enable or disable the Pre-CKAN instance (True/False)
# Set to True if you want to submit datasets to NDP Central Catalog
PRE_CKAN_ENABLED=True

# URL of the Pre-CKAN staging instance (Required if PRE_CKAN_ENABLED=True)
# This is typically provided by the NDP team
PRE_CKAN_URL=http://XX.XX.XX.XXX:5000/

# API key for Pre-CKAN authentication (Required if PRE_CKAN_ENABLED=True)
# Obtain this from the NDP team or your Pre-CKAN user profile
PRE_CKAN_API_KEY=

# Organization for Pre-CKAN publishing (Optional)
# When set, all datasets published to PRE-CKAN will use this organization,
# regardless of their original owner_org in the local catalog.
# Required when your PRE-CKAN API key is tied to a specific organization.
# Format: ep-XXXXXXXXXXXXXXXXXXXXXXXX (assigned by NDP)
PRE_CKAN_ORGANIZATION=

# STREAMING CONFIGURATION
# Enable or disable Kafka connectivity (True/False)
# Set to True if you want to ingest data from Kafka streams
KAFKA_CONNECTION=False

# Kafka broker hostname or IP address (Required if KAFKA_CONNECTION=True)
KAFKA_HOST=

# Kafka broker port number (Required if KAFKA_CONNECTION=True)
# Default Kafka port is 9092
KAFKA_PORT=9092

# DEVELOPMENT & TESTING
# Test token for development purposes (Optional)
# Leave blank in production environments for security
TEST_TOKEN=testing_token

# EXTERNAL SERVICE INTEGRATIONS
# Enable or disable JupyterLab integration (True/False)
# Set to True if you want to integrate with a JupyterLab instance
USE_JUPYTERLAB=False

# URL to your JupyterLab instance (Required if USE_JUPYTERLAB=True)
# Example: https://jupyter.your-domain.com or http://localhost:8888
JUPYTER_URL=

# S3 STORAGE CONFIGURATION
# Enable or disable S3 storage (True/False)
S3_ENABLED=True

# S3 endpoint (host:port) - use your S3-compatible service endpoint
S3_ENDPOINT=XXX.XXX.XXX.XXX:9000

# S3 access credentials
S3_ACCESS_KEY=minioadmin
S3_SECRET_KEY=minioadmin123

# Use secure connection (True for HTTPS, False for HTTP)
S3_SECURE=False

# Default region
S3_REGION=us-east-1
```

### 2. Run with Docker

1. **Create the .env file** with your configuration (see step 1)

2. **Run the container**:
```bash
docker run -p 8001:8000 --env-file .env rbardaji/ndp-ep-api
```

### 3. Run with Docker Compose (Optional Services)

The `docker-compose.yml` uses **profiles** to let you choose which services to start. By default, only the API starts. Use profiles to add optional services:

**Available Profiles:**
| Profile | Services Included |
|---------|-------------------|
| `mongodb` | MongoDB + Mongo Express |
| `kafka` | Kafka + Zookeeper + Kafka UI |
| `s3` | MinIO (S3-compatible storage) |
| `jupyter` | JupyterLab |
| `pelican` | Pelican Federation (Registry, Director, Origin, Cache) |
| `frontend` | NDP-EP Frontend Web UI |
| `full` | All services |

**Usage Examples:**

```bash
# API only (no additional services)
docker compose up

# API + MongoDB
docker compose --profile mongodb up

# API + MongoDB + Kafka
docker compose --profile mongodb --profile kafka up

# API + all services
docker compose --profile full up
```

**Note:** When using external services (e.g., your own CKAN or Kafka), just run `docker compose up` and configure the external URLs in your `.env` file.

### 4. Verify Installation

Once the container is running, verify everything is working:

- **API Documentation**: http://localhost:8001/docs
- **Health Check**: http://localhost:8001/status/
- **Interactive API Explorer**: Available at the docs URL

### 5. Common Configuration Scenarios

#### Scenario 1: NDP Central Catalog Only (Read-Only)
```bash
# Minimal configuration for read-only access to NDP Central Catalog
ORGANIZATION="Your Organization"
CKAN_LOCAL_ENABLED=False
PRE_CKAN_ENABLED=False
KAFKA_CONNECTION=False
USE_JUPYTERLAB=False
```

#### Scenario 2: Local CKAN Development
```bash
# Configuration for local CKAN development
ORGANIZATION="Your Organization"
LOCAL_CATALOG_BACKEND=ckan
CKAN_LOCAL_ENABLED=True
CKAN_URL=http://localhost:5000/
CKAN_API_KEY=your-local-ckan-api-key
PRE_CKAN_ENABLED=False
TEST_TOKEN=dev_token
```

#### Scenario 3: MongoDB Local Catalog (No CKAN Required)
```bash
# Lightweight setup with MongoDB backend
ORGANIZATION="Your Organization"
LOCAL_CATALOG_BACKEND=mongodb
MONGODB_CONNECTION_STRING=mongodb://localhost:27017
MONGODB_DATABASE=ndp_local_catalog
PRE_CKAN_ENABLED=False
TEST_TOKEN=dev_token
```

#### Scenario 4: Full NDP Integration with CKAN
```bash
# Complete setup with local CKAN and NDP submission capability
ORGANIZATION="Your Organization"
CKAN_LOCAL_ENABLED=True
CKAN_URL=http://your-ckan-instance:5000/
CKAN_API_KEY=your-local-ckan-api-key
PRE_CKAN_ENABLED=True
PRE_CKAN_URL=https://preckan.nationaldataplatform.org
PRE_CKAN_API_KEY=your-ndp-preckan-api-key
PRE_CKAN_ORGANIZATION=ep-your-assigned-org-id
```

## 🔒 Group-Based Access Control

The API supports optional group-based access control to restrict write operations (POST, PUT, DELETE) to users belonging to specific groups.

### How It Works

1. **Authentication**: When a user makes a request with a Bearer token, the API validates the token against the configured `AUTH_API_URL`
2. **Group Retrieval**: The authentication service returns user information including their `groups` array
3. **Authorization**: If `ENABLE_GROUP_BASED_ACCESS=True`, the API checks if any of the user's groups match the allowed groups in `GROUP_NAMES`
4. **Access Decision**:
   - ✅ User belongs to at least one allowed group → Write operation permitted
   - ❌ User doesn't belong to any allowed group → 403 Forbidden

### Configuration

```bash
# Enable group-based access control
ENABLE_GROUP_BASED_ACCESS=True

# Comma-separated list of groups allowed to perform write operations
GROUP_NAMES=admins,developers,data-managers
```

### Behavior

| Setting | Read (GET) | Write (POST/PUT/DELETE) |
|---------|------------|-------------------------|
| `ENABLE_GROUP_BASED_ACCESS=False` | ✅ Public | ✅ Any authenticated user |
| `ENABLE_GROUP_BASED_ACCESS=True` | ✅ Public | ✅ Only users in `GROUP_NAMES` |

### Example

If your authentication service returns:
```json
{
  "sub": "user123",
  "groups": ["researchers", "data-managers"] # from ndp keycloak 
}
```

And your configuration is:
```bash
ENABLE_GROUP_BASED_ACCESS=True
GROUP_NAMES=admins,data-managers
```

The user **will be authorized** because `data-managers` is in both the user's groups and `GROUP_NAMES`.

### Notes

- Group matching is **case-insensitive** (`Admins` matches `admins`)
- GET endpoints remain public regardless of this setting
- If `ENABLE_GROUP_BASED_ACCESS=True` but `GROUP_NAMES` is empty, all write operations will be denied

### Role tiers (viewer / writer / admin)

On top of group membership, the Endpoint enforces three role tiers —
**viewer** (read-only), **writer** (modify catalog content) and **admin**
(everything). See **[Roles and permissions](docs/roles-and-permissions.md)**
for the full model: how roles are named, how they reach the JWT, the AAI
role-management API, and how to grant a tier or introduce a brand-new
permission level. The same reference is available inside the UI from the
**Access Requests → Add more roles** button.

## 📖 Usage Examples

For detailed usage examples and tutorials, please check the documentation in the `/docs` folder.

## 🤖 AI Agent Integration (MCP)

The NDP-EP API includes built-in support for the **Model Context Protocol (MCP)**, enabling AI assistants and agents to interact programmatically with all API endpoints.

### What is MCP?

The Model Context Protocol is an emerging standard that defines how AI agents communicate with applications. It allows AI assistants like Claude, ChatGPT, and custom agents to discover and invoke API operations automatically.

### MCP Endpoint

Once the API is running, the MCP server is automatically available at:

```
http://your-api-host:port/mcp
```

For example, with the default Docker setup:
```
http://localhost:8001/mcp
```

### Key Benefits

- **Zero Configuration**: Automatically exposes all existing API endpoints as MCP tools
- **AI-Friendly**: AI agents can discover available operations and their parameters
- **Schema Preservation**: Maintains all request/response models and validation
- **Secure**: Respects existing authentication mechanisms
- **Standard Protocol**: Compatible with any MCP-compliant AI client

### Use Cases

**Dataset Management with AI Assistants:**
- "Search for oceanography datasets in the NDP catalog"
- "Create a new dataset with these metadata fields"
- "List all my S3 buckets and their contents"

**Automated Workflows:**
- AI agents can orchestrate complex data ingestion pipelines
- Automated catalog synchronization between environments
- Intelligent data discovery and recommendation

**Development & Testing:**
- AI-assisted API testing and validation
- Automatic documentation generation
- Code generation for API clients

### Connecting AI Clients

The MCP endpoint works with any MCP-compatible client. Example clients include:

- **Claude Code**: Anthropic's AI coding assistant
- **Custom MCP Clients**: Using the official MCP SDK
- **AI Automation Tools**: Any tool supporting the MCP protocol

For configuration examples and integration guides, visit the [FastAPI-MCP documentation](https://fastapi-mcp.tadata.com).

## 📊 System Metrics

> **⚠️ CAUTION**: This API automatically collects and logs system metrics (default: every 55 minutes, configurable via `METRICS_INTERVAL_SECONDS`).

The NDP-EP API automatically collects and logs comprehensive system metrics at configurable intervals (default: 55 minutes). These metrics provide visibility into system health, resource usage, catalog statistics, and service connectivity.

### Collected Metrics

**System Information:**
- **Public IP Address**: External IP of the API instance
- **Resource Usage**: Real-time CPU percentage, memory (used/total GB), and disk (used/total GB)
- **API Version**: Current version of the NDP-EP API
- **Organization**: Configured organization name
- **EP Name**: Endpoint identifier name

**Catalog Statistics:**
- **Number of Datasets**: Total datasets in local catalog
- **Number of Services**: Total registered services
- **Services List**: Array of all registered service titles

**Service Registry:**
- **Global CKAN**: NDP central catalog connection details
- **Pre-CKAN**: Staging environment configuration (if enabled)
- **Local CKAN**: Local catalog instance details (if configured)
- **Kafka**: Streaming service configuration (if enabled)
- **JupyterLab**: Notebook service integration (if configured)

### Metrics Output Example

```json
{
  "public_ip": "203.0.113.45",
  "cpu": "5.7%",
  "memory": "4.8GB/30.8GB",
  "disk": "265.4GB/936.8GB",
  "version": "0.3.2",
  "organization": "Your Organization",
  "ep_name": "Your EP",
  "num_datasets": 23,
  "num_services": 5,
  "services": [
    "Service Title 1",
    "Service Title 2",
    "Service Title 3"
  ],
  "timestamp": "2025-10-09T16:48:09.874843Z"
}
```

## 🌐 Pelican Federation Integration

The NDP-EP API integrates with the [Pelican Platform](https://pelicanplatform.org) to enable access to distributed scientific data federations and to serve your own data to the global scientific community.

### What is Pelican?

Pelican is an open-source data federation platform that connects distributed data repositories under a unified architecture. It enables:
- **Federated Data Access**: Browse and download from 20+ PB of scientific data in the Open Science Data Federation (OSDF)
- **Data Sharing**: Serve your MinIO/S3 data to the global scientific federation
- **Distributed Caching**: Automatic caching improves delivery efficiency for popular datasets
- **Unified Namespace**: Access heterogeneous sources (S3, POSIX, HTTP) through a common pelican:// protocol

### Two Integration Approaches

#### 1. Access External Federations (Phase 1)
Use dedicated Pelican endpoints to browse and download from external federations like OSDF:

**Available Endpoints:**
- `GET /pelican/federations` - List available federations (OSDF, PATh-CC, etc.)
- `GET /pelican/browse?path=/ospool/data&federation=osdf` - Browse federation namespaces
- `GET /pelican/info?path=/ospool/file.nc&federation=osdf` - Get file metadata
- `GET /pelican/download?path=/ospool/file.nc&stream=true` - Download/stream files
- `POST /pelican/import-metadata` - Import external file as resource in local catalog

**Example Usage:**
```bash
# List available federations
curl http://localhost:8002/pelican/federations

# Browse OSDF public data
curl "http://localhost:8002/pelican/browse?path=/ospool/uc-shared/public&detail=true"

# Download file from federation
curl "http://localhost:8002/pelican/download?path=/ospool/data/file.nc&stream=true" -o file.nc

# Import external Pelican file into local catalog
curl -X POST http://localhost:8002/pelican/import-metadata \
  -H "Content-Type: application/json" \
  -d '{
    "pelican_url": "pelican://osg-htc.org/ospool/data/temperature.nc",
    "package_id": "my-dataset-id",
    "resource_name": "OSDF Temperature Data"
  }'
```

#### 2. Pelican as Storage Backend (Phase 2)
Use `pelican://` URLs in your resource definitions - the API automatically handles downloads:

```bash
# Register dataset with Pelican URL
curl -X POST http://localhost:8002/services \
  -H "Content-Type: application/json" \
  -d '{
    "name": "osdf-climate-data",
    "title": "Climate Data from OSDF",
    "url": "pelican://osg-htc.org/ospool/climate/dataset.nc"
  }'

# The download handler automatically detects and uses Pelican
# No changes needed to existing endpoints!
```

### Running Your Own Pelican Federation

The included `docker-compose.yml` sets up a complete local Pelican federation with 4 services:

1. **Pelican Registry** (port 8444): Manages namespace registrations
2. **Pelican Director** (port 8445): Routes client requests to appropriate origins/caches
3. **Pelican Origin** (port 8446-8447): Serves MinIO data at federation path `/ndp-demo`
4. **Pelican Cache** (port 8448-8449): Caches popular objects for faster delivery

**Your MinIO data becomes accessible via:**
```
pelican://pelican-origin/ndp-demo/bucket-name/object-key
```

### Configuration

Enable Pelican in your `.env` file:

```bash
# Enable Pelican federation access
PELICAN_ENABLED=True

# Default federation (leave empty for OSDF)
PELICAN_FEDERATION_URL=

# Use caching infrastructure (recommended)
PELICAN_DIRECT_READS=False
```

### Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│                    NDP-EP API                            │
│  ┌──────────────────┐         ┌──────────────────┐     │
│  │ Phase 1 Routes   │         │  Phase 2 Handler │     │
│  │ /pelican/*       │         │  pelican:// URLs │     │
│  └────────┬─────────┘         └─────────┬────────┘     │
│           │                              │               │
│           └──────────┬───────────────────┘               │
│                      │                                   │
│            ┌─────────▼──────────┐                       │
│            │ PelicanRepository  │                       │
│            │   (pelicanfs)      │                       │
│            └─────────┬──────────┘                       │
└──────────────────────┼──────────────────────────────────┘
                       │
        ┌──────────────┼──────────────┐
        │              │               │
   ┌────▼─────┐   ┌───▼────┐    ┌────▼─────┐
   │   OSDF   │   │ PATh-CC│    │  Local   │
   │ Director │   │Director│    │ Director │
   └────┬─────┘   └───┬────┘    └────┬─────┘
        │             │               │
   ┌────▼─────┐  ┌───▼────┐     ┌────▼──────┐
   │  Cache   │  │ Cache  │     │   Cache   │
   └────┬─────┘  └───┬────┘     └────┬──────┘
        │            │                │
   ┌────▼─────┐ ┌───▼────┐      ┌────▼──────┐
   │  Origin  │ │ Origin │      │  Origin   │
   │(20+ PB)  │ │        │      │  (MinIO)  │
   └──────────┘ └────────┘      └───────────┘
```

### Benefits

✅ **Access 20+ PB of Scientific Data**: OSDF provides access to datasets from major research institutions
✅ **Distributed Caching**: Popular datasets are cached closer to compute resources
✅ **Backward Compatible**: Existing endpoints work unchanged with `pelican://` URLs
✅ **Share Your Data**: Expose MinIO datasets to the global scientific federation
✅ **Unified Protocol**: Single API for HTTP, S3, Kafka, and Pelican resources

### Learn More

- **Pelican Platform**: [https://pelicanplatform.org](https://pelicanplatform.org)
- **OSDF Documentation**: [https://osg-htc.org/services/osdf.html](https://osg-htc.org/services/osdf.html)
- **Configuration Guide**: [pelican-origin.yml](pelican-origin.yml)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

For more information about the National Data Platform, visit [nationaldataplatform.org](https://nationaldataplatform.org)

---

### ui/README.md (3,941 bytes)

# National Data Platform - EndPoint Admin Console (NDP-EP Frontend)

A React-based **administrative web interface** for managing and monitoring [NDP-EP API](https://github.com/national-data-platform/ep-api) instances. This console provides system administrators with comprehensive tools to manage datasets, organizations, services, and system health across multiple CKAN environments.

## 🌐 About the NDP-EP Admin Console

The NDP-EP Admin Console is designed specifically for **system administrators** who need to:

- **🔧 Manage API Instances**: Configure and monitor NDP-EP API deployments
- **📊 Administer Catalogs**: Control datasets across Local CKAN, Pre-CKAN, and NDP Central environments  
- **🏢 Organization Management**: Create and manage organizational structures within CKAN instances
- **🔍 System Monitoring**: Monitor API health, connectivity, and service status
- **⚙️ Service Registry**: Register and manage microservices, APIs, and applications
- **🚀 Resource Administration**: Bulk manage Kafka topics, S3 resources, and URL resources
- **☁️ S3 Management**: Direct S3 bucket and object management with presigned URLs (API v0.2.0+)

## ⚡ Quick Start for Administrators

Deploy the admin console for your NDP-EP API instance in under 5 minutes:

### Prerequisites
- Docker (for production deployment)
- Running [NDP-EP API](https://hub.docker.com/r/rbardaji/ndp-ep-api) instance

### Option 1: Docker Hub (Production Ready)

```bash
# Deploy latest version with S3 management features (v0.2.0+)
docker run -p 3000:80 \
  -e NDP_EP_API="https://your-ndp-api.company.com" \
  rbardaji/ndp-ep-frontend:latest

# Or deploy specific version
docker run -p 3000:80 \
  -e NDP_EP_API="https://your-ndp-api.company.com" \
  rbardaji/ndp-ep-frontend:0.2.0
```

**Access the admin console**: http://localhost:3000

### Option 2: Local Development

```bash
# Clone the repository
git clone https://github.com/your-username/ndp-ep-frontend.git
cd ndp-ep-frontend

# Install dependencies
npm install

# Configure API endpoint (optional)
echo "REACT_APP_API_BASE_URL=http://localhost:8003" > .env.local

# Start development server
npm start
```
**Access the admin console**: http://localhost:3000

#### Option 3: Docker Compose (Recommended)
Create a `docker-compose.yml` file:

```yaml
version: '3.8'

services:
  frontend:
    image: rbardaji/ndp-ep-frontend:0.2.0  # Use specific version for S3 features
    ports:
      - "80:80"
    environment:
      - NDP_EP_API=https://api.your-domain.com
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "wget", "--no-verbose", "--tries=1", "--spider", "http://localhost:80/"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
```

Run with:
```bash
docker-compose up -d
```

#### Option 4: Full Stack with Backend
```yaml
version: '3.8'

services:
  frontend:
    image: rbardaji/ndp-ep-frontend:0.2.0  # S3 management features
    ports:
      - "3000:80"
    environment:
      - NDP_EP_API=http://backend:8000
    depends_on:
      - backend
    restart: unless-stopped

  backend:
    image: rbardaji/ndp-ep-api:0.2.0  # Compatible API version for S3 features
    ports:
      - "8001:8000"
    environment:
      - ORGANIZATION=Your Organization
      - CKAN_LOCAL_ENABLED=False
      - PRE_CKAN_ENABLED=True
      - PRE_CKAN_URL=https://preckan.nationaldataplatform.org
      - PRE_CKAN_API_KEY=your-api-key
    restart: unless-stopped
```

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Default | Example |
|----------|-------------|---------|---------|
| `NDP_EP_API` | Backend API URL | `http://localhost:8003` | `https://api.example.com` |

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

For more information about the National Data Platform, visit [nationaldataplatform.org](https://nationaldataplatform.org)

---

### CHANGELOG.md (58,583 bytes)

# Changelog

All notable changes to the NDP-EP API project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.29.0] - 2026-05-19

### Added
- `docs/roles-and-permissions.md`: operator/support reference for the role model. Covers the three tiers and what each can do, the `ndp_{tier}` and `group:{AFFINITIES_EP_UUID}:{tier}` naming convention (and the legacy `{uuid}_admin` form), how `effective_role` is derived and where that code lives, how realm roles reach the JWT through the client's protocol mapper (with the empirically-verified note that newly created realm roles need no per-role client change), the AAI API surface for role/group management with exact request shapes, the "editor (AAI) vs writer (EP)" gotcha, and step-by-step guidance for the two "I need more roles" scenarios (reuse an existing tier in another group = config only, vs. a new permission level = Endpoint code change) plus when to escalate to NDP support.
- The same role reference is now reachable three ways:
  - **UI**: a new `/roles-help` page renders the guide in-app. The Access Requests page gained an **"Add more roles"** button next to Refresh that opens it, and the page links out to the full markdown reference on GitHub.
  - **Swagger**: the `POST /user/access-requests/{id}/approve` endpoint description now explains all three tiers (plus the deprecated `member` alias), the role naming convention, and points to `docs/roles-and-permissions.md`.
  - **README**: a "Role tiers" subsection under Group-Based Access Control links the doc and mentions the in-UI button.

### Backwards compatibility
- Additive only: one new UI route, one new button, an expanded Swagger description, a README link. No API behavior, request/response shapes or existing routes change.

## [0.28.0] - 2026-05-18

### Added
- Three explicit role tiers — Viewer (read-only), Writer (modify catalog content) and Admin (everything) — recognised in two flavours each, mirroring how the admin role already worked:
  - **Admin**: `ndp_admin` (global, already supported), plus per-endpoint `group:{AFFINITIES_EP_UUID}:admin` (the form Keycloak actually emits). The legacy form `{AFFINITIES_EP_UUID}_admin` is also still accepted for compatibility — we added matchers, we did not replace them.
  - **Writer**: `ndp_writer` (global) and `group:{AFFINITIES_EP_UUID}:writer` (per-EP). New.
  - **Viewer**: `ndp_viewer` (global) and `group:{AFFINITIES_EP_UUID}:viewer` (per-EP). New.
  - Implicit ordering: admin can do everything a writer can; writer can do everything a viewer can. A user only needs the highest tier they want — three separate role assignments are not required.
- New auth helpers exported from `api.services.auth_services`: `is_writer`, `is_viewer`, `effective_role`, `endpoint_group_role_name`, `get_user_for_read_operation`. The existing `is_admin` and `get_user_for_write_operation` are updated; the existing `get_user_for_endpoint_access` is unchanged.
- `GET /user/info` carries a new `effective_role` field (`admin`, `writer`, `viewer` or `none`). The UI uses it to decide which actions to expose without re-implementing the role-tier logic in the browser.
- UI gates write actions on the user's effective role:
  - The "+ New" menu in the navigation bar is hidden for viewers and users without a role.
  - The Delete action on owned organization, dataset and service cards in Search is hidden for viewers and users without a role.
  - The Publish action on owned dataset cards is hidden for viewers and users without a role.
  - Read paths (browsing Search results, expanding details) are unchanged.

### Changed
- `get_user_for_write_operation` now adds a role gate on top of the existing group-based-access gate. After group membership has been verified, the user must also carry at least the writer tier; otherwise the request is rejected with `403` and a friendly message asking an administrator to grant them the writer or admin role.
- The "Access Requests" approval flow now exposes three radios (Viewer / Writer / Admin) instead of the previous two (Member / Admin). The `POST /user/access-requests/{id}/approve` request body's `grant_type` accepts `viewer`, `writer` and `admin`; the legacy `member` value keeps working as an alias for `viewer` so existing API clients are unaffected. Approving as `writer` or `admin` adds the user to the EP group and then assigns the per-EP role on top via the AAI; approving as `viewer` only adds the user to the group (the AAI defaults the per-group role to viewer on join).
- `aai_client.assign_role` now takes a `group_name` argument and a bare tier name (`"admin"` / `"writer"`) — the AAI expects the per-group role to be specified as `(group_name, tier)` and builds the full `group:{group_name}:{tier}` name server-side. The previous signature was passing the already-prefixed string and got `"Missing token or group"` back from the AAI; tests had been mocking around it so the bug only surfaced once the UI actually exercised the approve-as-admin path on real data.

### Backwards compatibility
- **Strict default**: users that today belong to the EP group but have no role assigned were implicitly writers before this release; they now become "none" and lose write access until an administrator assigns them a role. The flow that adds approved users to the EP group via the AAI already assigns the `viewer` role automatically, so newly approved users land as viewers and have to be upgraded explicitly to writers.
- The legacy `{AFFINITIES_EP_UUID}_admin` role keeps working — we did not remove the old matcher.
- No request/response payload shapes change. The only addition on `/user/info` is `effective_role`, which clients that ignore unknown keys can safely ignore.
- The new realm roles (`ndp_writer`, `ndp_viewer`, the per-EP `group:{uuid}:writer` and `group:{uuid}:viewer` forms) have to be created in Keycloak before they can be assigned. The EP does not expose role creation; that step happens in the realm's admin console.

## [0.27.4] - 2026-05-14

### Added
- Dashboard: the group whose identifier matches the deployment's `AFFINITIES_EP_UUID` env value is now rendered in bold in the user's Groups list, so the user can tell at a glance which of their Keycloak groups ties them to this Endpoint. A hover tooltip explains the highlight. Matching covers all the shapes the auth service returns (plain string, or object with id/name/path, with any leading "/" stripped). Other groups render exactly as before.

### Changed
- `entrypoint.sh` now also exposes `AFFINITIES_EP_UUID` to the React UI through the runtime `config.js` (already used to expose `rootPath`). The new field is `window.__EP_CONFIG__.affinitiesEpUuid`. When the env var is not set, the field is an empty string and the Dashboard highlight is a no-op.

### Backwards compatibility
- UI-only feature plus a small entrypoint addition. The shape of `window.__EP_CONFIG__` only grows (new field, existing field unchanged), so any consumer that ignores unknown keys keeps working.
- When `AFFINITIES_EP_UUID` is not configured or the user has no matching group, the Dashboard renders exactly as before.

## [0.27.3] - 2026-05-14

### Changed
- The `service_type` field on the `POST /services` request model now carries a multi-line description (rendered as markdown in Swagger UI) explaining each of the three canonical service types — API, UI, Trigger — and noting that any other free-text value is accepted up to 50 characters. Single source of truth for the same definitions the registration form exposes.
- "+ New > Service" form: added a "What's this?" expandable block under the Service type select, collapsed by default. When opened, it lists the three canonical types with the same definitions used in the Swagger docs.

### Backwards compatibility
- Prose-only change. No code paths, no API contracts, no payload shapes are altered. Existing `service_type` values keep working.

## [0.27.2] - 2026-05-14

### Changed
- "+ New > Service" form: the "Service type" field is now a select with three canonical options (API, UI, Trigger) plus an Other option that reveals a free-text input. Picking a canonical option submits its exact label as `service_type`; choosing Other submits the value typed into the text input. Leaving the field on "(none)" omits `service_type` from the request, preserving the previous "blank type is fine" behavior.

### Backwards compatibility
- UI-only change. The backend contract for `POST /services` is unchanged — `service_type` is still an optional string up to 50 characters.

## [0.27.1] - 2026-05-14

### Changed
- Search page: the result-scoping toggle is now labelled "My assets" instead of "Only mine". The tooltip on hover ("Show only assets I created") was adjusted to match the new wording. Behaviour is unchanged — the same client-side and server-side filters are still applied.

## [0.27.0] - 2026-05-14

### Added
- "+ New > Dataset" form gains a "Publish to the global catalog after creation" checkbox. When checked, the form first registers the dataset on the local catalog and then chains a publish call to `POST /dataset/{id}/publish`. A helper line below the checkbox tells the user the dataset will not appear in the global catalog until an administrator approves the submission.
- The success banner after submission reflects what actually happened: it mentions both registration and the pending approval when publish was requested, and surfaces any warning returned by the publish endpoint (for example, a name collision that caused PRE-CKAN to publish the dataset under a timestamped variant).
- If registration succeeds but the publish call fails, the form surfaces a non-fatal yellow warning instead of a destructive error: the local dataset is kept and the user is told they can retry from the Search page.

### Backwards compatibility
- All changes are UI-only and additive. No backend changes.
- When the checkbox is left unchecked, the form behaves exactly as it did in 0.26.0 — single registration call against the local catalog.

## [0.26.0] - 2026-05-13

### Added
- Navigation: the "+ New" menu now hosts a "Dataset" entry between "Organization" and "Service", replacing the dedicated "Datasets" entry inside the "Resources" dropdown.
- Search page: dataset result cards whose persisted creator hash matches the authenticated user now expose a "Yours" badge plus two inline actions:
  - **Delete** — opens an inline confirmation panel on the same card; on success the card disappears immediately, on failure a friendly, actionable message is shown.
  - **Publish** — only shown when the dataset has not yet been published (no `extras.status` on the dataset). Opens an inline confirmation panel; on success the card updates to reflect the new status (`submitted`) and the Publish button disappears, on failure a friendly message is shown.
- A shared inline confirmation panel renders both delete and publish flows, with action-specific copy and palette (red for destructive, teal for publish) and a single processing/error path. Only one action can be pending per card at a time.

### Changed
- The Datasets page is now a single-purpose "register a new dataset" form, mirroring the simplified Organizations and Services creation pages. Listing moved to the Search page; deletion and publishing now happen on the dataset result cards (new in this release). Editing, tag/group/license/version inputs and the filter-by-organization controls are dropped from the page; we can revisit them as Search-card actions if it becomes a real ask. The route stays at `/datasets` so deep links keep working.
- The "Datasets" entry has been removed from the "Resources" navigation dropdown; the page is now reached exclusively from "+ New > Dataset".

### Backwards compatibility
- No new public API surface. Dataset deletion goes through the existing `DELETE /resource?resource_id=...` endpoint (datasets are CKAN packages). Dataset publishing goes through the existing `POST /dataset/{id}/publish` endpoint, unchanged since 0.19.0.
- The `/datasets` UI route still exists and still creates datasets; the page only drops the listing/edit/delete/publish features that became redundant once Search took over.
- Datasets registered before the creator-hash feature do not appear under "Only mine" and never expose Delete or Publish actions on Search; no migration is performed.

## [0.25.0] - 2026-05-13

### Added
- Navigation: the "+ New" menu now hosts a "Service" entry next to the existing "Organization" entry, replacing the dedicated "Services" top-level link.
- Search page: service result cards whose persisted creator hash matches the authenticated user expose a "Yours" badge and a "Delete" action. Clicking Delete opens an inline confirmation panel on the same card (no `window.confirm`, no full-screen modal). On success the card disappears immediately; on failure the panel surfaces a friendly, actionable message instead of the raw backend string.

### Changed
- The Services page is now a single-purpose "register a new service" form, mirroring the simplified Organizations creation page. Listing, editing and deletion have moved to the Search page (listing was already there; deletion is new with this release). The route stays at `/services` so deep links keep working.
- The "Services" entry has been removed from the navigation bar; the page is now reached exclusively from "+ New > Service".

### Backwards compatibility
- No new API surface: service deletion goes through the existing dataset-deletion endpoint (services are CKAN packages under the `services` organization).
- The `/services` UI route still exists and still creates services; the page only drops the listing/edit/delete features that became redundant once Search took over.
- Services registered before the creator-hash feature simply do not appear under "Only mine" and never expose a Delete action on Search; no migration is performed.

## [0.24.0] - 2026-05-13

### Added
- Navigation: new "+ New" dropdown replaces the old "Organizations" entry. It currently contains a single "Organization" item that takes the user to the simplified organization-creation page; the menu is wired so adding more entries (Dataset, Service, etc.) later is a single-line change.
- Search page: organization result cards that belong to the authenticated user now show a "Delete" action and a "Yours" badge. Clicking Delete opens an in-line confirmation panel on the card itself (no `window.confirm`, no full-screen modal). On success the card disappears immediately; on failure the panel shows a friendly, actionable error message rather than the raw backend string.
- `DELETE /organization/{name}` accepts a new optional `cascade` query parameter (default `true`, the legacy behavior). When `cascade=false`, the endpoint deletes only the organization and refuses with `409 Conflict` if the organization still owns datasets. The error payload includes the dataset count so callers can render a helpful message. The Search UI always passes `cascade=false`, so users never lose datasets by clicking Delete.

### Changed
- The Organizations page is now a focused "create a new organization" form. The list-and-delete role it played before moved to the Search page (listing was already there; deletion is new). The route stays at `/organizations` so the "+ New > Organization" item lands there.
- The Organizations entry has been removed from the navigation bar; the page is now reached exclusively from "+ New > Organization".

### Backwards compatibility
- The new `cascade` parameter defaults to `true`, matching the legacy "delete the organization and every dataset it owns" behavior. Existing API clients are unaffected.
- The HTTP path and response shape of `DELETE /organization/{name}` are unchanged; `cascade=false` introduces a new `409` response code in addition to the existing `200/400/404`.
- The `/organizations` UI route still exists and still creates organizations; the create-only redesign drops listing/delete features that are now duplicated on Search.

## [0.23.0] - 2026-05-13

### Added
- Search page has a new "Only mine" toggle alongside the existing scope/server filters. When active, every result group (datasets, services and organizations) is restricted to items whose persisted creator hash matches the authenticated user. The toggle relies on the one-way hash that the EP already stores; no PII is involved.
- `GET /organization` accepts a new optional `mine=true` query parameter. When set, the response is filtered server-side to organizations whose `ndp_user_id` extra (CKAN) or top-level `ndp_user_id` field (MongoDB) matches the requester's hash. The response shape stays `List[str]`. Requires a Bearer token; the endpoint stays anonymous-friendly when `mine` is not used.
- `GET /user/info` now also returns the requesting user's own `ndp_user_id` (the same hash that the EP persists alongside resources). The UI uses this so it can filter datasets/services client-side without re-deriving the hash in the browser. Upstream payloads that already carry an `ndp_user_id` are preserved as-is.

### Backwards compatibility
- All changes are additive. No required parameters, no fields removed, no type changes.
- `GET /organization` keeps working without authentication when `mine` is not passed; the response shape is unchanged.
- `GET /user/info` keeps every field the auth service was returning and only adds `ndp_user_id` on top. Clients that ignore unknown fields are unaffected.
- Items registered before the corresponding creator-hash feature simply do not appear under "Only mine"; no migration is performed.

## [0.22.0] - 2026-05-12

### Added
- Organizations created through `POST /organization` now persist the same one-way creator hashes (`ndp_user_id` and `ndp_creator_md5`) that datasets, services, URL, S3 and Kafka registrations already store via `inject_ndp_metadata`:
  - The route used to capture the authenticated `user_info` only to satisfy the auth dependency and then discarded it; it now forwards it to the `create_organization` service, which derives the hashes with the existing helpers (`hash_user_id`/`calculate_md5`).
  - The MongoDB backend persists `ndp_user_id` and `ndp_creator_md5` as top-level fields on the organization document when the request was authenticated.
  - The CKAN backend turns those same hashes into standard CKAN organization extras (so CKAN never receives unknown top-level fields). Any caller-provided extras are preserved and the creator extras are appended.
  - No PII is stored. Only the same hash family already used for datasets — the raw user identity is never persisted.
  - Organizations created before this version stay valid and simply keep no attribution; no migration is performed.

### Changed
- `hash_user_id` and `calculate_md5` are now re-exported from `api.services.metadata_services`, so services other than `inject_ndp_metadata` can reuse them without reaching into the submodule.

## [0.21.0] - 2026-05-12

### Added
- Search page can now also find organizations alongside datasets and services:
  - The mode selector gained a third scope, `Organizations`, in addition to `Datasets` and `Services`
  - The default `All` mode runs the dataset search, the service search and the organization search in parallel, and renders the three result groups together so the user does not need to switch modes and re-run the same query to also see matching organizations
  - Organization cards expose a `View datasets in this org →` action that re-runs the search scoped to that organization (using the existing POST `/search` `owner_org` filter) and switches the mode to `Datasets`, so the user can drill down without leaving the page
  - When the org filter is active, a removable chip ("Filtered by org: X (×)") is shown right under the search bar so the user always sees which scope is applied and can clear it with one click
  - Clicking the chip's clear button restores the unfiltered behavior and keeps the typed term (re-running the broader search if a term is present, or just clearing the page otherwise)
- The search term is now optional when the mode is `Organizations` (the EP's `GET /organization` endpoint already lists every organization on the server when no `name` filter is provided), so the user can browse the full list of organizations without typing anything

### Changed
- Search hero title now reads "Find datasets, services and organizations"
- Results summary now mentions the active organization scope when one is applied

## [0.20.0] - 2026-05-11

### Changed
- The UI landing page is now the Search page instead of the Dashboard. Regular users land directly on the search experience, which matches what they actually need to do on the EP (find datasets and services) without first navigating through a Dashboard that is primarily useful for administrators
- The Dashboard is still available, but its nav entry has been moved to the end of the navigation bar (just before "Access Requests") and is only shown to administrators — the same gate that already controls the "Access Requests" entry
- The "Search" nav entry now points to `/` (the new landing route); `/search` still works as before for backwards compatibility, and `/dashboard` is the new path for the Dashboard view
- Search page redesigned to be cleaner and more complete:
  - Pre-search layout is a centered hero with a large rounded search bar, an inline clear button and an autofocused input, so the page reads as a search experience from the first second
  - After running a search, the hero collapses and the bar moves up so the results take the visible area
  - Mode selector now has three options instead of two: "All" (default — runs the dataset search and the service search in parallel and shows the two result groups), "Datasets" and "Services". This removes the need to switch tabs and run the query twice when looking for "everything matching a term"
  - Results are grouped by type with a section header that shows the count, and each result card uses badges (type, organization, service type) plus a collapsible "Show details" block for resources/endpoints and extras — instead of always rendering the full payload inline
  - The old static "Search Tips" block was removed; its contents were not actionable and competed with the actual results for screen space
  - Error messages no longer abort a multi-mode search: when "All" is selected, a failure in one of the two queries is silently dropped and the other group is still rendered; the page only surfaces an error when every requested query fails

## [0.19.5] - 2026-04-30

### Changed
- Services Registry table: the "Access Service" link no longer points straight at the registered `service_url`. It now goes through the EP API's existing redirect proxy at `/services/redirect/{service_name}`, so every consumption of the registered service stays inside the EP boundary (consistent logging, headers, future auth handling) and the UI no longer hardcodes external URLs in `<a href>` attributes:
  - `BASE_URL` is now exported from the shared API client and consumed in the Services page so the proxy URL is built from the same `rootPath` the axios client uses
  - The link is rendered only when the service has both a usable `service_url` and a `name` (the CKAN-style name is the identifier the backend's `get_service_url` matches against)
  - The hover tooltip now reads "Proxied through <redirect-url> → <service-url>" so the user can see at a glance that the click goes through the EP API and where it ends up
- The Documentation link is intentionally left untouched: documentation typically lives on a different host than the service URL, and the redirect proxy is not designed to forward to arbitrary external URLs

## [0.19.4] - 2026-04-30

### Changed
- Services Registry form: the "Additional Metadata" input no longer requires the user to write JSON
  - Default editor is a guided list of key/value rows with Add/Remove controls, mirroring the "Extras" editor already exposed on the Dataset Management form so the two forms feel like one
  - An "Advanced (JSON)" toggle still exposes the raw textarea for metadata that needs nested or non-text values
  - When editing an existing service, the editor defaults to guided fields if the service's extras (with the service-specific reserved keys already stripped) form a flat primitive map; nested shapes load straight into JSON mode so nothing is dropped
  - Switching back from JSON to simple fields is blocked with an inline message when the JSON is invalid, is not an object, or contains nested/non-primitive values, so the user is never silently downgraded

## [0.19.3] - 2026-04-30

### Fixed
- Services Registry page: dropped the leftover "Controls" card wrapper, the static "Local Server Only" badge and the Refresh button so the layout now mirrors the other resource management pages — the page header is followed directly by the primary "Register Service" button (Dataset Management, Kafka Topics, URL Resources and S3 Resources had already been cleaned up in 0.17.1; Services was missed back then)
- Resource management pages (Dataset Management, Kafka Topics, URL Resources, Services, S3 Resources): the outer primary button used to toggle its label between "Create …" / "Register …" and "Cancel" depending on whether the create form was open, which made two separate "Cancel" buttons visible at once (the outer toggle and the one inside the form's card header). The outer button is now only rendered while the form is closed, so the form's own Cancel button stays as the single way to dismiss the form

## [0.19.2] - 2026-04-30

### Added
- Dataset Management page: a new "Organization" select on the right side of the datasets card header now filters the visible rows by the organization that owns them. The filter runs client-side on the data the page already fetches, so no extra API call is needed:
  - Default value is "All organizations", which keeps the current behavior of showing every dataset
  - When a filter is active, the dataset count next to the title becomes "Datasets (X of Y)" so the user knows how many were hidden
  - When the filter matches no rows, the empty-state copy suggests trying a different organization or going back to the full list, instead of nudging the user to create a new dataset
  - The select reuses the organization name strings the page already fetches for the create/edit form, so the dropdown values match the strings rendered in the table's "Organization" column

## [0.19.1] - 2026-04-30

### Fixed
- Top header: when an admin session showed the "Access Requests" link, the row no longer fit horizontally — "Access Requests" wrapped onto a second line and the Logout button on the right ended up looking misaligned. The header now stays on a single row regardless of which nav items are visible:
  - Every nav link/button label uses `white-space: nowrap` so labels never wrap mid-word
  - Nav and right-cluster gaps tightened from 1.5rem to 1rem; link padding from 0.75rem 1rem to 0.5rem 0.75rem; Logout button padding from 0.75rem 1.5rem to 0.5rem 1rem
  - Inner container max width raised from 1200px to 1400px so the header has more horizontal room before falling back on the tighter sizes

## [0.19.0] - 2026-04-30

### Added
- Dataset Management page: each row whose `extras.status` is not "submitted" now exposes a primary "Publish" action button before the Edit/Delete buttons, so a user can push a local dataset to PRE-CKAN directly from the table without leaving the page (no more Swagger or curl round-trip):
  - The button calls `POST /dataset/{dataset_id}/publish` through a new `generalDatasetAPI.publish` client method
  - Per-row publishing state disables the button and switches its label to "Publishing…" while the request is in flight, so double-clicks cannot fire the publish twice
  - On success the datasets list is refetched and the status icon flips from Home to Clock automatically
  - When the backend had to auto-rename the dataset (because its `name` was already in use in PRE-CKAN), the response's `warning` field is surfaced via the yellow warning banner instead of the green success banner, so the user notices that the published name/title differ from theirs
  - Once a dataset is already submitted the button is hidden, preventing a re-publish that would just create a renamed duplicate

## [0.18.2] - 2026-04-30

### Added
- Dataset Management page: a new "Status" column on the datasets table surfaces each dataset's submission state at a glance, using a small icon instead of the raw status string so the table stays compact:
  - Amber Clock when the dataset has been published to PRE-CKAN (`extras.status === "submitted"`) and is awaiting review
  - Gray Home when the dataset has no status entry (local-only, never published)
  - Gray AlertCircle for any unrecognized status, with the raw value still exposed via the hover tooltip so the row never silently hides state
- Each icon is wrapped in a `title`-bearing span so hovering reveals the underlying status text without cluttering the table

## [0.18.1] - 2026-04-30

### Removed
- Repository root: orphaned `package.json` and `package-lock.json` (legacy `pop-api-frontend` v1.3.0-alpha.2). The actual frontend lives under `ui/` (`ndp-ep-frontend`) and is the only one consumed by the Docker build, so the root-level files were unused and only added confusion about which is the real frontend

## [0.18.0] - 2026-04-29

### Changed
- `POST /dataset/{dataset_id}/publish` no longer fails when the dataset's `name` is already in use in PRE-CKAN. The publish is retried automatically with a timestamp suffix on both `name` and `title`, mirroring the auto-rename behavior of `POST /dataset`:
  - `name` becomes `<original>-<YYYYMMDDHHMMSS>` so it still satisfies CKAN's slug constraint (`^[a-z0-9_-]+$`)
  - `title` becomes `<original> (YYYY-MM-DD HH:MM:SS)` so the rename is obvious to humans
  - The response keeps a `201 Created` status and now also returns the final `name`, `title` and a `warning` field describing the rename (or `null` when no rename happened)
  - The local dataset's `status=submitted` mirror is still applied after the (possibly renamed) publish succeeds, so the originating Endpoint can still tell which datasets are pending review
- Other publish failures (PRE-CKAN disabled, dataset not found locally, organization missing in PRE-CKAN, transport errors) keep their existing semantics and do not trigger the auto-rename retry

## [0.17.3] - 2026-04-29

### Changed
- UI footer: the displayed version is now read at runtime from the backend's OpenAPI document (`info.version` exposed at `/openapi.json`), so it always matches the deployed API and no longer needs a manual bump on every release. While the version is being fetched, or if the request fails, the footer renders a neutral placeholder

### Removed
- UI footer: the "© <year> National Data Platform. All rights reserved." line has been removed; the version row now only shows the "NDP EndPoint" label and the live version badge

## [0.17.2] - 2026-04-29

### Removed
- Dataset Management page: the "Type" column on the datasets table has been removed. The page already filters out URL / S3 / Kafka / Service datasets, so by construction every row was labeled "General" and the column carried no useful signal

## [0.17.1] - 2026-04-29

### Removed
- Dataset Management, Kafka Topics, URL Resources and S3 Resources pages: the "Controls" card that wrapped the create / refresh buttons (and showed a static "📍 Local Server Only" badge) has been removed. The page header now flows directly into the action buttons, which removes visual weight that was not carrying any function

## [0.17.0] - 2026-04-29

### Changed
- `POST /dataset` no longer rejects requests whose `name` (or its derived URL) is already in use. Instead, the dataset is created with an automatic timestamp suffix and the response keeps a `201 Created` status while including a `warning` field that explains the rename:
  - `name` becomes `<original>-<YYYYMMDDHHMMSS>` so it still satisfies CKAN's slug constraint (`^[a-z0-9_-]+$`)
  - `title` becomes `<original> (YYYY-MM-DD HH:MM:SS)` so the rename is obvious to humans
  - The response body now also returns the final `name` and `title` so any consumer (UI, CURL, scripts) can detect and surface the rename
- The previous `409 Conflict` response with a structured `detail` object has been removed from this endpoint, since the duplicate-name case is now handled transparently
- Dataset Management page: when the backend renames a duplicate dataset, the create form now shows a dedicated yellow warning banner prefixed with "WARNING:" instead of the green success banner, so the user immediately notices that the stored `name` and `title` differ from the ones they submitted

### Fixed
- Dataset Management page: creating a dataset that triggered a backend error with a structured `detail` payload used to display the meaningless string "Failed to create dataset: [object Object]". A new helper now flattens structured detail objects into a readable message before showing them to the user

## [0.16.0] - 2026-04-26

### Changed
- Dataset Management page: the "Resources" input on the Create/Edit dataset form no longer requires the user to write JSON
  - Default editor is a guided list of resource cards with URL, Name, Format and Description inputs and Add/Remove controls, mirroring the field set already exposed by the inline resource editor on the dataset detail row
  - An "Advanced (JSON)" toggle still exposes the raw textarea for resources that need fields the simple editor does not show (mimetype, size, …)
  - When editing an existing dataset, each resource is loaded into a card and any non-canonical fields it carries are preserved on save, so a fields-mode round-trip never silently drops data
  - Switching back from JSON to fields is blocked with an inline message when the JSON is invalid, is not an array, or contains non-object items, so the user is never silently downgraded

## [0.15.1] - 2026-04-26

### Fixed
- `example.env` now documents `CKAN_VERIFY_SSL` and `PRE_CKAN_VERIFY_SSL`, the existing settings that toggle TLS certificate verification for the local CKAN and Pre-CKAN instances. Both default to `True` in code, so behavior is unchanged; this only makes the option discoverable for operators running against a self-signed CKAN.

## [0.15.0] - 2026-04-26

### Changed
- Dataset Management page: the "Extras" input on the Create/Edit dataset form no longer requires the user to write JSON
  - Default editor is a guided list of key/value rows with Add/Remove controls, so users unfamiliar with JSON can still attach metadata
  - An "Advanced (JSON)" toggle still exposes the raw textarea for nested or non-text values that the simple fields cannot represent
  - When editing an existing dataset whose extras are a flat primitive map, the editor opens in the guided fields mode pre-populated with the current pairs; nested or non-text values open in the advanced JSON mode instead
  - Switching back from JSON to fields is blocked with an inline message when the JSON is invalid or contains nested/non-text values, so the user is never silently downgraded

### Removed
- UI dead code: the unused client-side `handleSendToPreCkan` flow and the unused `getDatasetTypeBadge` helper in `DatasetManagement` were removed; the Pre-CKAN publish workflow is fully driven from the backend (see 0.14.0)

### Fixed
- Outstanding ESLint warnings in the UI build (`Navigation`, `S3ObjectManager`, `S3Resources`, `Organizations`) were cleaned up so the production build now compiles without warnings

## [0.14.0] - 2026-04-26

### Changed
- `POST /dataset/{dataset_id}/publish` now marks both the local dataset and the Pre-CKAN copy with a `status=submitted` entry in their `extras`, so an Endpoint can tell which of its datasets are pending review and Pre-CKAN reviewers can identify newly submitted datasets in their queue
  - The status is stored as a CKAN-style extra (`{"key": "status", "value": "submitted"}`) alongside any existing extras (`ndp_user_id`, `ndp_group_id`, `ndp_creator_md5`, user-provided extras)
  - Re-publishing a dataset that already had a `status` entry (for example `approved` or `rejected`) replaces it with `submitted`, since this represents a fresh submission to the review queue
  - If creating the dataset in Pre-CKAN fails, the local dataset is left untouched
  - If the local update fails after a successful Pre-CKAN creation, the failure is logged as a warning and the publish still returns success — the Pre-CKAN copy is the source of truth for the review workflow

## [0.13.0] - 2026-04-23

### Added
- Access-request workflow, end-to-end (backend + UI)
  - New `ENABLE_ACCESS_REQUESTS` flag (off by default) so deployments without MongoDB boot unchanged
  - `POST /user/access-requests` lets an authenticated user submit a request with an optional justification; duplicates (existing pending request for the same user) are rejected with 409
  - `GET /user/access-requests` lists pending requests for administrators, with `?status=pending|approved|rejected|all` filter
  - `POST /user/access-requests/{id}/approve` performs the IDP grant using the administrator's own bearer token — either adding the requester to the endpoint group (`grant_type=member`) or also assigning the endpoint admin role (`grant_type=admin`) — and records the decision
  - `POST /user/access-requests/{id}/reject` marks the request as rejected without touching the IDP
  - A new `require_admin` dependency that admits users with either the `ndp_admin` role or the endpoint-specific `{AFFINITIES_EP_UUID}_admin` role
  - A thin client for the NDP AAI API (`add_user_to_group`, `assign_role`, `list_group_members`) so the grant step reuses the administrator's session and no service account is introduced
  - MongoDB-backed persistence in the `access_requests` collection, with the connection string and database name reused from `CatalogSettings` (no new env vars)
  - UI: the AuthGuard 403 screen now offers a "Request access to this Endpoint" button with an optional justification, replaced by a success confirmation once the request is submitted. The user's bearer token is held in memory only for this single call and never persisted to `localStorage`.
  - UI: a new "Access Requests" page, visible in the top nav only to users with the `ndp_admin` or endpoint-scoped `{UUID}_admin` role, lists pending/approved/rejected requests and lets administrators approve (choosing between `member` or `admin` grant, with optional notes) or reject (with optional notes).

## [0.12.0] - 2026-04-22

### Changed
- `ENABLE_GROUP_BASED_ACCESS` now authorizes a user when **any** of the following is true:
  1. The user belongs to one of the groups listed in `GROUP_NAMES` (existing behavior)
  2. The user has the role `ndp_admin`
  3. The user belongs to the group whose name matches `AFFINITIES_EP_UUID`
- When group-based access is disabled the behavior is unchanged — any authenticated user is allowed
- The 403 response body now shows a short user-friendly message ("You do not have permission to access this Endpoint. Please contact the administrator." / "You do not have permission to perform this operation. Please contact the administrator."). The technical details (required role, endpoint group UUID, configured `GROUP_NAMES`) are logged as a backend warning instead of being returned to the user
- `GET /user/info` is now gated by the same authorization rule. When `ENABLE_GROUP_BASED_ACCESS=True`, users that do not satisfy any of the three paths receive 403 Forbidden instead of their profile data, which prevents the UI's AuthGuard from letting them into the app
- The UI credentials login flow now validates the returned token against `/user/info` before storing it, so authorization errors are surfaced at login time rather than after entering the app
- The UI login screen now shows the backend's 403 detail (e.g. "Access forbidden: access to this Endpoint requires …") when the user is not allowed to enter the Endpoint

## [0.11.0] - 2026-04-22

### Added
- Username and password login option on the UI authentication screen
  - New `POST /user/login` endpoint proxies credentials to the configured identity provider and returns the access token plus profile data
  - `AuthGuard` now includes a link below the "Authenticate" button labeled "or use your login / password" that switches the screen to a credentials form (username, password, show/hide toggle); a reciprocal link returns to the access token form
  - On successful login the token is stored in `localStorage` so subsequent requests are authenticated automatically
  - Invalid credentials surface as 401 with the IDP message, IDP outages as 502

## [0.10.11] - 2026-04-13

### Fixed
- `/resources/search` crashed with `AttributeError: 'NoneType' object has no attribute 'lower'` when any resource had `None` values in fields used for filtering (`name`, `url`, `description`, `format`)
  - `dict.get("key", "")` returns the default only when the key is missing; when the key exists with value `None` it returns `None`, breaking the subsequent `.lower()` call
  - Replaced `resource.get("key", "")` with `(resource.get("key") or "")` in all filter branches of `DataCatalogRepository.resource_search`
  - Added regression test covering resources with `None` values across all searchable fields

## [0.10.10] - 2026-04-08

### Fixed
- React asset paths in `index.html` were not rewritten with `ROOT_PATH` prefix
  - Assets like favicon, JS bundles, CSS, and manifest were still referenced as `/ui/...` instead of `{ROOT_PATH}/ui/...`
  - `entrypoint.sh` now rewrites all `"/ui/` references in the built `index.html` at startup
  - Ensures the page loads correctly behind a reverse proxy with any path prefix

## [0.10.9] - 2026-04-08

### Fixed
- Nginx inside the container did not use `ROOT_PATH` for location prefixes
  - `entrypoint.sh` now generates `nginx.conf` dynamically with `ROOT_PATH`-prefixed locations
  - Locations `/ui/`, `/api/`, and `/` become `{ROOT_PATH}/ui/`, `{ROOT_PATH}/api/`, `{ROOT_PATH}/`
  - Also updates the `config.js` script path in the built `index.html` at startup
  - When `ROOT_PATH` is empty, behavior is identical to the previous static config

## [0.10.8] - 2026-04-08

### Fixed
- UI did not use `ROOT_PATH` for API calls when deployed behind a reverse proxy
  - Added `entrypoint.sh` that generates a runtime `config.js` with the `ROOT_PATH` value
  - UI now reads the API base URL from `window.__EP_CONFIG__` instead of build-time env var
  - No rebuild required — just change `ROOT_PATH` in `.env` and restart the container

## [0.10.7] - 2026-04-03

### Fixed
- UI was calling `/general-dataset` endpoint which does not exist in the API
  - Changed UI API client to use the correct `/dataset` path for create, update, and partial update operations
  - Fixes "Failed to create dataset: Not Found" error on the Dataset Management page

## [0.10.6] - 2026-04-03

### Fixed
- JupyterLab Status "Disabled" style now matches Streaming Status style
  - Changed from red error style (`AlertCircle`) to warning style (`MinusCircle`)
  - "Disabled" is not an error — it means the feature is intentionally turned off

## [0.10.5] - 2026-04-03

### Fixed
- Streaming Status card on Dashboard always showed "Connected" even when Kafka is disabled
  - The UI only checked if the API responded, without inspecting the `kafka_connection` field
  - When `KAFKA_CONNECTION=False`, the card now correctly displays "Disabled"
  - Fixed field name mismatch (`host`/`port` vs `kafka_host`/`kafka_port`) that caused "undefined:undefined"

## [0.10.4] - 2026-04-03

### Fixed
- Catalog Status card on Dashboard was permanently stuck on "Checking..." instead of showing "Connected"
  - Status endpoints were incorrectly listed as public, so requests were sent without the auth token
  - The backend requires authentication, causing silent 401 errors that left the status unresolved
  - Removed status endpoints from the public endpoints list so the Bearer token is always sent

## [0.10.3] - 2026-04-02

### Fixed
- Test token now returns a human-readable username ("Test User") in the Dashboard's Current User section
- Test token user no longer includes placeholder groups, matching a realistic no-groups scenario

## [0.10.2] - 2026-04-02

### Removed
- Removed API Connection Status panel from the login screen
  - No longer shows API version, frontend version, or compatibility checks
  - Login screen now displays only the token input form for a cleaner experience
  - Removed version comparison logic and related constants from AuthGuard

## [0.10.1] - 2026-04-02

### Fixed
- Logout now redirects to `/ui/` instead of `/` so the AuthGuard login screen is shown correctly
  - Fixed redirect in `AuthStatus.js` and `Navigation.js`
  - Previously, logout sent users to the server root instead of the UI login screen

## [0.10.0] - 2026-03-30

### Added
- Integrated React frontend (NDP-EP Admin Console) into the monorepo under `ui/`
  - Dashboard, Organizations, Datasets, Services, Search pages
  - S3 bucket/object management
  - Kafka topics and URL resources management
  - AuthGuard with JWT token validation and API version check
- Multi-stage `Dockerfile.allinone` for all-in-one deployment
  - Stage 1: Node 18 builds the React frontend
  - Stage 2: Python 3.13 + nginx + supervisord serves both API and UI
- `nginx.conf` reverse proxy configuration
  - UI served at `/ui/` as static files with SPA routing
  - API accessible at `/` and `/api/` via proxy to uvicorn

### Changed
- `docker-compose.yml` now uses `Dockerfile.allinone` by default
- Removed dependency on external `rbardaji/ndp-ep-frontend` Docker image

## [0.9.0] - 2026-03-12

### Added
- Add `ndp_creator_md5` field for catalog alignment with official NDP catalog

## [0.8.0] - 2026-03-03

### Added
- New endpoint `POST /dataset/{dataset_id}/publish` to copy datasets from local catalog to PRE-CKAN
  - Copies dataset metadata and all associated resources
  - Proper error handling for disabled PRE-CKAN and duplicate names
  - Unit tests for all scenarios
- New `PRE_CKAN_ORGANIZATION` environment variable
  - When set, overrides the owner_org when publishing to PRE-CKAN
  - Required when PRE-CKAN API credentials are tied to a specific organization
  - Local catalog can use any organization; PRE-CKAN uses the configured one

## [0.7.2] - 2026-02-23

### Added
- Create affinity triples when registering datasets and services
  - New `create_affinity_triple()` method in AffinitiesClient
  - Automatic POST to `/affinities` endpoint after dataset registration
  - Automatic POST to `/affinities` endpoint after service registration
  - Creates triples linking datasets/services with their hosting endpoint

## [0.7.1] - 2026-02-19

### Added
- Store Affinities UUID in dataset extras (`ndp_affinity_uuid`) after registration
- Store Affinities UUID in service extras (`ndp_affinity_uuid`) after registration
- UUIDs enable cross-referencing between local catalog and Affinities API

## [0.7.0] - 2026-02-18

### Added
- NDP Affinities integration for automatic registration of datasets and services
  - New configuration: `AFFINITIES_ENABLED`, `AFFINITIES_URL`, `AFFINITIES_EP_UUID`, `AFFINITIES_TIMEOUT`
  - AffinitiesClient module for async HTTP communication with Affinities API
  - Automatic dataset registration in Affinities on `POST /dataset`
  - Automatic service registration in Affinities on `POST /services`
  - Automatic endpoint relationships created for datasets and services
  - Non-blocking integration: Affinities errors don't affect main operations
  - Documentation: `docs/affinities-integration.md`

## [0.6.1] - 2026-02-12

### Changed
- Version bump for Docker image release

## [0.6.0] - 2026-02-02

### Added
- MongoDB full-text search with text indexes
  - Text index on `title`, `tags`, and `notes` fields with weighted relevance (title: 10, tags: 5, notes: 1)
  - Uses MongoDB `$text` operator for efficient full-text search
  - Relevance-based sorting using `$meta: "textScore"`
  - 10-100x performance improvement over regex-based search for large datasets
  - Built-in stemming, stop words, and case-insensitive matching
  - Backward compatible with Solr-style field queries (`field:value`)
- Comprehensive test suite for MongoDB full-text search functionality

### Changed
- MongoDB `package_search` now uses `$text` operator for simple text queries instead of regex
- Search results are sorted by relevance score when using full-text search

## [0.5.3] - 2025-12-27

### Changed
- Renamed `ENABLE_ORGANIZATION_BASED_ACCESS` to `ENABLE_GROUP_BASED_ACCESS`
- Added `GROUP_NAMES` environment variable for comma-separated list of allowed groups
- Authorization now checks if user belongs to any group in `GROUP_NAMES` instead of single organization
- Backward compatibility maintained with function aliases

## [0.5.2] - 2025-12-22

### Added
- Installation script (`install.sh`) for fresh Ubuntu systems
  - Interactive configuration prompts
  - Automatic Docker installation
  - Environment file generation with overwrite protection
- Infrastructure services reporting to federation metrics
  - `jupyterlab_enabled` + `jupyterlab_url`
  - `kafka_enabled` + `kafka_host` + `kafka_port`
  - `s3_enabled`
  - `pre_ckan_enabled`
- Docker Compose profiles for optional services
  - `mongodb`: MongoDB + Mongo Express
  - `kafka`: Kafka + Zookeeper + Kafka UI
  - `s3`: MinIO
  - `jupyter`: JupyterLab
  - `pelican`: Pelican Federation services
  - `frontend`: NDP-EP Frontend
  - `full`: All services

### Changed
- Docker Compose now starts only the API by default
- Healthcheck endpoint changed from `/status/` to `/` (status requires auth)

## [0.5.1] - 2025-12-22

### Fixed
- Added authentication requirement to all `/status` endpoints
- Fixed tests for `resource_patch` method in base repository
- Fixed SSL verification test to use explicit configuration

## [0.5.0] - 2025-12-08

### Added
- Resource management endpoints by ID only (no dataset_id required)
  - `GET /resource/{resource_id}` - Get resource by ID
  - `PATCH /resource/{resource_id}` - Update resource by ID
  - `DELETE /resource/{resource_id}` - Delete resource by ID
- Resource search endpoint with filtering capabilities
  - `GET /resources/search` - Search resources across all datasets
  - Supports filters: `q` (general), `name`, `url`, `format`, `description`
  - Pagination with `limit` and `offset` parameters
  - Results include parent dataset context (dataset_id, dataset_name, dataset_title)
- MongoDB-optimized `resource_search` implementation in repository layer

## [0.4.1] - 2025-12-07

### Added
- SSL verification toggle for CKAN connections
  - `CKAN_VERIFY_SSL` environment variable (default: True)
  - `PRE_CKAN_VERIFY_SSL` environment variable (default: True)
  - Allows disabling SSL certificate verification for self-signed certificates
  - Fixes SSL errors when connecting to CKAN instances with self-signed certs

### Changed
- Refactored URL normalization into `_normalize_url` helper method in ckan_settings

## [0.4.0] - 2025-11-27

### Added
- New endpoint to delete individual resources from a dataset
  - `DELETE /dataset/{dataset_id}/resource/{resource_id}` removes a single resource
  - Dataset and other resources remain intact
  - Supports both local and pre_ckan server parameters
  - New service function `delete_resource()` in dataset_services
- New endpoint to partially update individual resources (PATCH)
  - `PATCH /dataset/{dataset_id}/resource/{resource_id}` updates only specified fields
  - Supports updating name, url, description, format
  - New `resource_patch` method in repositories (CKAN and MongoDB)
  - New service function `patch_resource()` in dataset_services

### Fixed
- ROOT_PATH now properly propagates to Swagger UI requests (fixes #23)
  - Added servers configuration to OpenAPI schema when ROOT_PATH is set

### Documentation
- Added link to "Adding New Catalog Backends" documentation in README (fixes #22)

## [0.3.4] - 2025-11-27

### Fixed
- Use purge instead of delete for CKAN datasets and organizations
  - Changed `package_delete` to use `dataset_purge` for permanent deletion
  - Changed `organization_delete` to use `organization_purge` for permanent deletion
  - CKAN's soft-delete left datasets in database, preventing organization deletion
  - Now datasets and organizations are completely removed, enabling proper cleanup

## [0.3.3] - 2025-11-27

### Fixed
- Fixed AttributeError in service routes when using CKAN backend
  - Service routes accessed `repository.ckan_instance` but CKANRepository stores client as `self.ckan`
  - Affected endpoints: POST /services, PUT /services/{id}, PATCH /services/{id}

## [0.3.2] - 2025-11-12

### Fixed
- **Critical: MongoDB organization search compatibility** - Fixed search by organization name in MongoDB backend
  - MongoDB stores `owner_org` as UUID, but CKAN allows searching by organization name
  - Added automatic organization name → UUID resolution in all search paths (q, fq, fq_list)
  - Ensures `{"owner_org": "services"}` searches work identically in MongoDB and CKAN backends
  - Maintains full backward compatibility with existing code

## [0.3.1] - 2025-11-12

### Fixed
- Fixed MongoDB repository `owner_org` expansion issue where services and datasets showed `owner_org: null` in search results
  - Added automatic expansion of `owner_org` UUID to full `organization` object in `package_search` method
  - Maintains CKAN API compatibility by providing organization details (id, name, title, description) in search results
  - All services now correctly display their associated organization

### Added
- Sample data seeding script (`seed_sample_data.py`) for development and demo purposes
  - Creates 4 organizations (services, marine-research, climate-monitoring, biodiversity-lab)
  - Seeds 5 real public API services (Dog Breed, Cat Facts, JSONPlaceholder, Public Holidays, Open-Meteo Weather)
  - Creates S3 buckets and uploads sample data files with real content
  - Includes cleanup functionality to avoid duplicates
- CHANGELOG.md to track all project changes following Keep a Changelog format

## [0.3.0] - 2025-01-10

### Added
- Pelican federation integration for data discovery across federated origins
  - New Pelican repository (`api/repositories/pelican_repository.py`) for federation access
  - Pelican service layer for federation operations
  - Pelican API endpoints for federated dataset discovery
  - Unified download helper with Pelican support
  - Pelican configuration variables and conditional route integration
  - Pelican Origin configuration file
  - Docker Compose services for Pelican federation (origin, cache, director)
- Comprehensive test suite for Pelican routes
- Pelican federation integration documentation

### Changed
- Docker Compose stack now includes Pelican services (optional)
- Enhanced metrics payload with catalog data and configurable interval
- Added `ep_name` and `metrics_interval` to status endpoint
- Updated metrics format for better observability

### Fixed
- Implemented repository pattern for search functions to support MongoDB
- Ensured `LOCAL_CATALOG_BACKEND` is respected in service routes
- Ensured 'services' organization exists on startup

## [0.2.0] - 2024-12-15

### Added
- FastAPI-MCP integration for AI agent communication
  - MCP (Model Context Protocol) server mounted at `/mcp` endpoint
  - AI agents can discover and invoke all API operations automatically
  - Full API surface exposed as MCP tools
- AI agent integration documentation
- Complete Docker Compose stack with web interfaces
  - MongoDB Express for database management
  - Kafka UI for stream monitoring
  - MinIO Console for S3 storage management
  - JupyterLab for interactive data analysis
- Background metrics task with configurable interval
  - System metrics (CPU, memory, disk, public IP)
  - Catalog statistics (dataset count, service count)
  - Service registry information
  - Automatic posting to federation metrics endpoint

### Changed
- Updated Python base image from 3.9 to 3.13
- Improved metrics task with enhanced payload structure
- Updated README with new configuration and metrics information
- Added configurable API root path for flexible deployment

### Fixed
- Full metrics handler updated to support new system metrics format

## [0.1.0] - 2024-11-01

### Added
- Initial release of NDP-EP API
- Repository pattern architecture for catalog abstraction
  - Abstract base repository (`DataCatalogRepository`)
  - CKAN repository implementation
  - MongoDB repository implementation
  - Factory pattern for runtime backend selection
- Three catalog types support:
  - Local catalog (configurable: CKAN or MongoDB)
  - Global catalog (CKAN, read-only)
  - PreCKAN catalog (CKAN staging)
- Core API functionality:
  - Dataset management (CRUD operations)
  - Resource management (URL, S3, Kafka)
  - Organization management
  - Service registry
  - Federated search across catalogs
- S3 integration with MinIO
  - Bucket management
  - Object upload/download
  - Presigned URLs
  - Metadata operations
- Kafka integration
  - Topic-based dataset ingestion
  - Stream metadata management
- Authentication and authorization
  - Bearer token authentication
  - Organization-based access control
  - User information endpoints
- Health checks and status endpoints
- Comprehensive API documentation (OpenAPI/Swagger)
- Docker support with multi-stage builds
- Logging with rotation
- Environment-based configuration

### Infrastructure
- Docker Compose setup for local development
- MongoDB backend for local catalog
- MinIO for S3-compatible storage
- Apache Kafka for streaming data
- Zookeeper for Kafka coordination

---

## Version Schema

This project uses [Semantic Versioning](https://semver.org/):
- **MAJOR** version: Incompatible API changes
- **MINOR** version: New functionality in a backwards compatible manner
- **PATCH** version: Backwards compatible bug fixes

## Categories

Changes are grouped into the following categories:
- **Added**: New features
- **Changed**: Changes in existing functionality
- **Deprecated**: Soon-to-be removed features
- **Removed**: Removed features
- **Fixed**: Bug fixes
- **Security**: Security vulnerability fixes

---

### requirements.txt (544 bytes)

pydantic_settings
uvicorn
fastapi
ckanapi
python-multipart
jinja2
flake8
pytest
httpx
pytest-mock
trio
pytest-asyncio
psutil
requests>=2.25.0
fastapi-utils
pytest-cov
requests
jupyter>=1.0.0
minio==7.2.16
pymongo>=4.0.0
mongomock>=4.1.0
fastapi-mcp
pelicanfs>=0.1.0
# OpenTelemetry (optional - for distributed tracing)
opentelemetry-api>=1.20.0
opentelemetry-sdk>=1.20.0
opentelemetry-instrumentation-fastapi>=0.41b0
opentelemetry-instrumentation-httpx>=0.41b0
opentelemetry-instrumentation-requests>=0.41b0
opentelemetry-exporter-otlp>=1.20.0

---

### DOCKERHUB_README.md (21,201 bytes)

# NDP Endpoint API

Unified REST API for dataset management and discovery across the National Data Platform (NDP) ecosystem. Built with FastAPI, it provides a single interface to manage datasets across multiple catalog backends (CKAN, MongoDB), stream data through Kafka, store objects in S3-compatible storage (MinIO), and access distributed scientific data via Pelican Federation.

## Features

- **Dataset Management** - Full CRUD operations for datasets across multiple catalog environments (local, NDP Central, Pre-CKAN staging)
- **Federated Search** - Search datasets across local catalog, NDP Central Catalog, and Pre-CKAN staging
- **Streaming Data** - Register and manage Kafka topics for real-time data ingestion
- **Object Storage** - S3-compatible bucket and object management (create buckets, upload/download files, presigned URLs)
- **Pelican Federation** - Browse and download files from distributed scientific data federations (OSDF and others)
- **Service Registry** - Register external services with dynamic routing and proxy capabilities
- **AI Agent Integration** - Built-in Model Context Protocol (MCP) server for AI assistant integration
- **OpenTelemetry** - Distributed tracing and observability with configurable exporters
- **Group-Based Access Control** - Optional role-based write permissions using Bearer token authentication
- **Automatic Metrics** - Background task that reports system metrics (CPU, memory, disk) to federation
- **Dataset Publishing** - Publish datasets from local catalog to Pre-CKAN staging environment
- **NDP Affinities** - Automatic registration of datasets and services in the NDP Affinities system
- **Remote Execution** - Integration with deployment APIs for remote code execution

## Quick Start

### Using Docker Compose (Recommended)

Create a `docker-compose.yml` with the API and the optional services you need. The API always starts; additional services are organized into **profiles** that you activate with `--profile`.

```yaml
services:
  # ==============================================
  # API Service (always starts)
  # ==============================================
  api:
    image: rbardaji/ndp-ep-api
    container_name: ndp-ep-api
    ports:
      - "8002:8000"
    env_file:
      - .env
    networks:
      - ndp-network
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s

  # ==============================================
  # MongoDB - Local Catalog Backend
  # Activate with: --profile mongodb
  # ==============================================
  mongodb:
    image: mongo:7
    container_name: ndp-mongodb
    profiles: ["mongodb", "full"]
    ports:
      - "27018:27017"
    environment:
      MONGO_INITDB_ROOT_USERNAME: admin
      MONGO_INITDB_ROOT_PASSWORD: admin123
      MONGO_INITDB_DATABASE: ndp_local_catalog
    volumes:
      - mongodb_data:/data/db
      - mongodb_config:/data/configdb
    networks:
      - ndp-network
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "mongosh", "--eval", "db.adminCommand('ping')"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 20s

  # ==============================================
  # Mongo Express - MongoDB Web UI
  # Activate with: --profile mongodb
  # ==============================================
  mongo-express:
    image: mongo-express:latest
    container_name: ndp-mongo-express
    profiles: ["mongodb", "full"]
    ports:
      - "8082:8081"
    environment:
      ME_CONFIG_MONGODB_ADMINUSERNAME: admin
      ME_CONFIG_MONGODB_ADMINPASSWORD: admin123
      ME_CONFIG_MONGODB_URL: mongodb://admin:admin123@mongodb:27017/
      ME_CONFIG_BASICAUTH_USERNAME: admin
      ME_CONFIG_BASICAUTH_PASSWORD: admin123
      ME_CONFIG_MONGODB_ENABLE_ADMIN: 'true'
    networks:
      - ndp-network
    depends_on:
      mongodb:
        condition: service_healthy
    restart: unless-stopped

  # ==============================================
  # MinIO - S3-Compatible Object Storage
  # Activate with: --profile s3
  # ==============================================
  minio:
    image: minio/minio:latest
    container_name: ndp-minio
    profiles: ["s3", "full"]
    ports:
      - "9002:9000"      # API port
      - "9003:9001"      # Console UI
    environment:
      MINIO_ROOT_USER: minioadmin
      MINIO_ROOT_PASSWORD: minioadmin123
    command: server /data --console-address ":9001"
    volumes:
      - minio_data:/data
    networks:
      - ndp-network
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "mc", "ready", "local"]
      interval: 10s
      timeout: 5s
      retries: 5

  # ==============================================
  # Zookeeper - Required for Kafka
  # Activate with: --profile kafka
  # ==============================================
  zookeeper:
    image: confluentinc/cp-zookeeper:7.6.0
    container_name: ndp-zookeeper
    profiles: ["kafka", "full"]
    environment:
      ZOOKEEPER_CLIENT_PORT: 2181
      ZOOKEEPER_TICK_TIME: 2000
      ZOOKEEPER_LOG4J_ROOT_LOGLEVEL: WARN
    volumes:
      - zookeeper_data:/var/lib/zookeeper/data
      - zookeeper_log:/var/lib/zookeeper/log
    networks:
      - ndp-network
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "nc", "-z", "localhost", "2181"]
      interval: 10s
      timeout: 5s
      retries: 5

  # ==============================================
  # Kafka - Streaming Platform
  # Activate with: --profile kafka
  # ==============================================
  kafka:
    image: confluentinc/cp-kafka:7.6.0
    container_name: ndp-kafka
    profiles: ["kafka", "full"]
    ports:
      - "9094:9092"      # External access
      - "9095:9093"      # Internal access
    environment:
      KAFKA_BROKER_ID: 1
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://kafka:9093,PLAINTEXT_HOST://localhost:9092
      KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: PLAINTEXT:PLAINTEXT,PLAINTEXT_HOST:PLAINTEXT
      KAFKA_INTER_BROKER_LISTENER_NAME: PLAINTEXT
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
      KAFKA_TRANSACTION_STATE_LOG_MIN_ISR: 1
      KAFKA_TRANSACTION_STATE_LOG_REPLICATION_FACTOR: 1
      KAFKA_LOG4J_ROOT_LOGLEVEL: WARN
      KAFKA_TOOLS_LOG4J_LOGLEVEL: ERROR
    volumes:
      - kafka_data:/var/lib/kafka/data
    networks:
      - ndp-network
    depends_on:
      zookeeper:
        condition: service_healthy
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "kafka-broker-api-versions", "--bootstrap-server", "localhost:9093"]
      interval: 10s
      timeout: 10s
      retries: 5
      start_period: 30s

  # ==============================================
  # Kafka UI - Web Interface for Kafka Management
  # Activate with: --profile kafka
  # ==============================================
  kafka-ui:
    image: provectuslabs/kafka-ui:latest
    container_name: ndp-kafka-ui
    profiles: ["kafka", "full"]
    ports:
      - "8081:8080"
    environment:
      KAFKA_CLUSTERS_0_NAME: ndp-demo
      KAFKA_CLUSTERS_0_BOOTSTRAPSERVERS: kafka:9093
      KAFKA_CLUSTERS_0_ZOOKEEPER: zookeeper:2181
      DYNAMIC_CONFIG_ENABLED: 'true'
    networks:
      - ndp-network
    depends_on:
      kafka:
        condition: service_healthy
    restart: unless-stopped

  # ==============================================
  # JupyterLab - Interactive Development Environment
  # Activate with: --profile jupyter
  # ==============================================
  jupyterlab:
    image: jupyter/scipy-notebook:latest
    container_name: ndp-jupyterlab
    profiles: ["jupyter", "full"]
    ports:
      - "8888:8888"
    environment:
      JUPYTER_ENABLE_LAB: 'yes'
      JUPYTER_TOKEN: testing_token
    volumes:
      - jupyterlab_data:/home/jovyan/work
    networks:
      - ndp-network
    restart: unless-stopped
    command: start-notebook.sh --NotebookApp.token='testing_token' --NotebookApp.password=''

  # ==============================================
  # NDP-EP Frontend - Web Interface
  # Activate with: --profile frontend
  # ==============================================
  frontend:
    image: rbardaji/ndp-ep-frontend:latest
    container_name: ndp-frontend
    profiles: ["frontend", "full"]
    ports:
      - "3000:80"
    environment:
      NDP_EP_API: http://ndp-ep-api:8000
    networks:
      - ndp-network
    depends_on:
      api:
        condition: service_healthy
    restart: unless-stopped

volumes:
  mongodb_data:
  mongodb_config:
  minio_data:
  zookeeper_data:
  zookeeper_log:
  kafka_data:
  jupyterlab_data:

networks:
  ndp-network:
    driver: bridge
```

Create a `.env` file (see below) and run:

```bash
# Start API + MongoDB only (minimal setup)
docker compose --profile mongodb up -d

# Start API + MongoDB + Kafka + S3
docker compose --profile mongodb --profile kafka --profile s3 up -d

# Start everything (all profiles)
docker compose --profile full up -d
```

The API will be available at `http://localhost:8002`.

### Using Docker Run

If you only need the API and already have a MongoDB instance running:

```bash
docker run -d -p 8000:8000 \
  -e LOCAL_CATALOG_BACKEND="mongodb" \
  -e CKAN_LOCAL_ENABLED="True" \
  -e MONGODB_CONNECTION_STRING="mongodb://admin:admin123@your-mongodb-host:27017" \
  -e MONGODB_DATABASE="ndp_local_catalog" \
  -e ORGANIZATION="my-organization" \
  -e EP_NAME="my-endpoint" \
  rbardaji/ndp-ep-api:latest
```

## Available Profiles

| Profile | Services | Description |
|---------|----------|-------------|
| `mongodb` | MongoDB + Mongo Express | Local catalog database. Mongo Express available at `http://localhost:8082` (login: `admin` / `admin123`) |
| `kafka` | Zookeeper + Kafka + Kafka UI | Streaming data platform. Kafka UI available at `http://localhost:8081` |
| `s3` | MinIO | S3-compatible object storage. Console at `http://localhost:9003` (login: `minioadmin` / `minioadmin123`) |
| `jupyter` | JupyterLab | Interactive notebooks. Available at `http://localhost:8888` (token: `testing_token`) |
| `frontend` | NDP-EP Web UI | Web interface at `http://localhost:3000` |
| `full` | All of the above | Starts all optional services |

## Routes

| Path | Description |
|------|-------------|
| `/` | List all datasources (also acts as health check) |
| `/search` | Search datasets by terms with optional filters |
| `/health` | Liveness probe |
| `/ready` | Readiness probe (checks dependencies) |
| `/status/` | API status, configuration, and service details (requires auth) |
| `/status/jupyter` | JupyterLab availability check |
| `/status/kafka` | Kafka connection details |
| `/status/rexec-api` | Remote execution service status |
| `/dataset` | Dataset CRUD operations |
| `/dataset/{id}/publish` | Publish a dataset from local catalog to Pre-CKAN |
| `/organization` | Organization management |
| `/resources/` | Resource search and management |
| `/url` | Register/update URL-based resources |
| `/s3` | Register/update S3 object resources |
| `/kafka` | Register/update Kafka topic resources |
| `/services` | Service registry and management |
| `/buckets` | S3 bucket management (create, list, delete) |
| `/objects/{bucket}` | S3 object management (upload, download, delete) |
| `/pelican/*` | Pelican federation (browse, download, import) |
| `/user/info` | Current user information |
| `/mcp` | Model Context Protocol server for AI agents |
| `/docs` | Swagger API documentation |
| `/redoc` | ReDoc API documentation |

## Environment Variables

### API Configuration

| Variable | Description | Default |
|----------|-------------|---------|
| `ROOT_PATH` | Root path prefix for reverse proxy deployment (e.g., `/api`). Useful when the API runs behind a reverse proxy at a subpath | _(empty)_ |
| `ORGANIZATION` | Organization name for this endpoint, used in metrics and identification | `Unknown Organization` |
| `EP_NAME` | Unique name for this endpoint instance, used in metrics and status | `Unknown EP` |

### Metrics Configuration

The API runs a background task that periodically sends system metrics (CPU, memory, disk, catalog stats) to the configured federation endpoint.

| Variable | Description | Default |
|----------|-------------|---------|
| `METRICS_INTERVAL_SECONDS` | Interval in seconds for background metrics reporting | `3300` (55 min) |
| `METRICS_ENDPOINT` | URL where metrics are sent periodically. Typically points to the NDP Federation metrics endpoint | `https://federation.ndp.utah.edu/metrics/` |

### Access Control

The API supports Bearer token authentication. When a user makes a request with a token, the API validates it against the configured auth endpoint and retrieves user details. Optionally, write operations can be restricted to users belonging to specific groups.

| Variable | Description | Default |
|----------|-------------|---------|
| `AUTH_API_URL` | URL for token validation and user information retrieval. The API sends the Bearer token to this endpoint to authenticate users | `https://idp.nationaldataplatform.org/temp/information` |
| `ENABLE_GROUP_BASED_ACCESS` | When `True`, write operations (POST, PUT, DELETE) are restricted to users belonging to specific groups. GET endpoints remain public | `False` |
| `GROUP_NAMES` | Comma-separated list of groups allowed for write operations (e.g., `admins,developers,data-managers`). Group matching is case-insensitive. If empty and `ENABLE_GROUP_BASED_ACCESS=True`, all write operations will be denied | _(empty)_ |
| `TEST_TOKEN` | Token for development/testing purposes. Leave blank in production | `testing_token` |

### Local Catalog Backend

The API uses a local catalog to store datasets, resources, and organizations. You can choose between CKAN or MongoDB as the backend. The Global Catalog and Pre-CKAN always use CKAN regardless of this setting.

| Variable | Description | Default |
|----------|-------------|---------|
| `LOCAL_CATALOG_BACKEND` | Backend type for the local catalog: `ckan` or `mongodb` | `ckan` |
| `CKAN_LOCAL_ENABLED` | Enable or disable local catalog write operations (POST, PUT, DELETE). Set to `False` for read-only mode. Note: the variable name contains "CKAN" for historical reasons, but it applies to all backends (CKAN, MongoDB, etc.) | `False` |

### MongoDB Configuration

Required when `LOCAL_CATALOG_BACKEND=mongodb`.

| Variable | Description | Default |
|----------|-------------|---------|
| `MONGODB_CONNECTION_STRING` | Full MongoDB connection URI. For Docker Compose use the service name (e.g., `mongodb://admin:admin123@mongodb:27017`). For local development use `localhost` | `mongodb://localhost:27017` |
| `MONGODB_DATABASE` | MongoDB database name for the local catalog | `ndp_local_catalog` |

### CKAN Configuration

Required when `LOCAL_CATALOG_BACKEND=ckan`.

| Variable | Description | Default |
|----------|-------------|---------|
| `CKAN_URL` | Base URL of your local CKAN instance (e.g., `http://ckan:5000`) | `http://localhost:5000` |
| `CKAN_API_KEY` | API key for CKAN authentication. Get it from your CKAN user profile | _(none)_ |
| `CKAN_VERIFY_SSL` | Verify SSL certificates when connecting to CKAN. Set to `False` for self-signed certificates | `True` |

### Pre-CKAN Staging

Pre-CKAN is a staging environment where datasets are reviewed before they appear in the NDP Central Catalog. When enabled, you can publish datasets from your local catalog to Pre-CKAN using the `POST /dataset/{id}/publish` endpoint.

| Variable | Description | Default |
|----------|-------------|---------|
| `PRE_CKAN_ENABLED` | Enable or disable Pre-CKAN integration | `False` |
| `PRE_CKAN_URL` | URL of the Pre-CKAN instance | _(empty)_ |
| `PRE_CKAN_API_KEY` | API key for Pre-CKAN authentication | _(empty)_ |
| `PRE_CKAN_ORGANIZATION` | Organization name in Pre-CKAN. When set, overrides the original `owner_org` when publishing. Required when your Pre-CKAN credentials are tied to a specific organization | _(empty)_ |

### Kafka Streaming

Enable Kafka to register streaming data topics as dataset resources. Requires the `kafka` profile in Docker Compose (or an external Kafka broker).

| Variable | Description | Default |
|----------|-------------|---------|
| `KAFKA_CONNECTION` | Enable or disable Kafka connectivity | `False` |
| `KAFKA_HOST` | Kafka broker hostname. For Docker Compose use the service name `kafka`. For local development use `localhost` | `localhost` |
| `KAFKA_PORT` | Kafka broker port. Use `9093` for internal Docker network, `9092` for external access | `9092` |

### S3/MinIO Object Storage

Enable S3-compatible storage for managing buckets and objects. Requires the `s3` profile in Docker Compose (or an external S3/MinIO service).

| Variable | Description | Default |
|----------|-------------|---------|
| `S3_ENABLED` | Enable or disable S3 storage integration | `False` |
| `S3_ENDPOINT` | S3 endpoint in `host:port` format. For Docker Compose use `minio:9000`. For local development use `localhost:9000` | `localhost:9000` |
| `S3_ACCESS_KEY` | S3 access key for authentication | `minioadmin` |
| `S3_SECRET_KEY` | S3 secret key for authentication | `minioadmin123` |
| `S3_SECURE` | Use HTTPS for S3 connections. Set to `True` for production environments with SSL | `False` |
| `S3_REGION` | AWS region or S3-compatible region | `us-east-1` |

### Pelican Federation

Enable access to distributed scientific data through the Pelican Federation (OSDF and others). When enabled, adds endpoints for browsing, downloading, and importing external federated datasets.

| Variable | Description | Default |
|----------|-------------|---------|
| `PELICAN_ENABLED` | Enable Pelican federation support | `False` |
| `PELICAN_FEDERATION_URL` | Default Pelican federation URL. Leave empty to use OSDF (Open Science Data Federation). Format: `pelican://federation-host` | _(empty, uses OSDF)_ |
| `PELICAN_DIRECT_READS` | Enable direct reads from Origins, bypassing caches. Set to `False` to use caching infrastructure for better performance | `False` |

### JupyterLab Integration

Requires the `jupyter` profile in Docker Compose (or an external JupyterLab instance).

| Variable | Description | Default |
|----------|-------------|---------|
| `USE_JUPYTERLAB` | Enable JupyterLab integration. Adds JupyterLab status to the `/status/jupyter` endpoint | `False` |
| `JUPYTER_URL` | URL of your JupyterLab instance. For Docker Compose use `http://jupyterlab:8888` | `https://jupyter.org/try-jupyter/lab/` |

### NDP Affinities Integration

When enabled, datasets and services created in this endpoint are automatically registered in the NDP Affinities system, creating relationships between resources across the platform.

| Variable | Description | Default |
|----------|-------------|---------|
| `AFFINITIES_ENABLED` | Enable automatic registration of datasets and services in Affinities | `False` |
| `AFFINITIES_URL` | Base URL of the Affinities API (e.g., `http://affinities-api:8000`) | _(empty)_ |
| `AFFINITIES_EP_UUID` | UUID of this endpoint in the Affinities system. Obtained when you register this endpoint via `POST /endpoints` on the Affinities API | _(empty)_ |
| `AFFINITIES_TIMEOUT` | Request timeout in seconds for Affinities API calls | `30` |

### Remote Execution (Rexec)

| Variable | Description | Default |
|----------|-------------|---------|
| `REXEC_CONNECTION` | Enable or disable Remote Execution Deployment API connectivity | `False` |
| `REXEC_DEPLOYMENT_API_URL` | URL of the Remote Execution Deployment API | _(empty)_ |

## `.env` Example

Below is a complete `.env` file with all available configuration options. See the Environment Variables section above for detailed descriptions of each variable.

```env
# API Configuration
ROOT_PATH=
ORGANIZATION=my-organization
EP_NAME=my-endpoint

# Metrics
METRICS_INTERVAL_SECONDS=3300
METRICS_ENDPOINT=https://federation.ndp.utah.edu/metrics/

# Access Control
ENABLE_GROUP_BASED_ACCESS=False
GROUP_NAMES=

# Authentication
AUTH_API_URL=https://idp.nationaldataplatform.org/temp/information
TEST_TOKEN=

# Local Catalog Backend ("ckan" or "mongodb")
LOCAL_CATALOG_BACKEND=mongodb
CKAN_LOCAL_ENABLED=True

# CKAN (only if LOCAL_CATALOG_BACKEND=ckan)
CKAN_URL=
CKAN_API_KEY=

# MongoDB (only if LOCAL_CATALOG_BACKEND=mongodb)
MONGODB_CONNECTION_STRING=mongodb://admin:admin123@mongodb:27017
MONGODB_DATABASE=ndp_local_catalog

# Pre-CKAN Staging
PRE_CKAN_ENABLED=False
PRE_CKAN_URL=
PRE_CKAN_API_KEY=
PRE_CKAN_ORGANIZATION=

# Kafka Streaming
KAFKA_CONNECTION=True
KAFKA_HOST=kafka
KAFKA_PORT=9093

# S3/MinIO Storage
S3_ENABLED=True
S3_ENDPOINT=minio:9000
S3_ACCESS_KEY=minioadmin
S3_SECRET_KEY=minioadmin123
S3_SECURE=False
S3_REGION=us-east-1

# Pelican Federation
PELICAN_ENABLED=False
PELICAN_FEDERATION_URL=
PELICAN_DIRECT_READS=False

# JupyterLab
USE_JUPYTERLAB=True
JUPYTER_URL=http://jupyterlab:8888

# Affinities
AFFINITIES_ENABLED=False
AFFINITIES_URL=
AFFINITIES_EP_UUID=
AFFINITIES_TIMEOUT=30

# Remote Execution
REXEC_CONNECTION=False
REXEC_DEPLOYMENT_API_URL=
```

## Source Code

GitHub: [https://github.com/national-data-platform/ep-api](https://github.com/national-data-platform/ep-api)

---

### docs/adding-catalog-backends.md (21,129 bytes)

# Adding New Catalog Backend Implementations

This guide explains how to add support for new catalog backend systems (e.g., Elasticsearch, PostgreSQL, or any other storage system) to the NDP-EP API.

## Table of Contents

1. [Overview](#overview)
2. [Architecture](#architecture)
3. [Step-by-Step Implementation](#step-by-step-implementation)
4. [Example: Adding Elasticsearch Backend](#example-adding-elasticsearch-backend)
5. [Testing Your Implementation](#testing-your-implementation)
6. [Best Practices](#best-practices)

## Overview

The NDP-EP API uses the **Repository Pattern** to abstract catalog operations. This allows you to swap out the underlying storage system (CKAN, MongoDB, etc.) without changing any business logic or API endpoints.

### Current Supported Backends

- **CKAN**: Traditional CKAN catalog system (default)
- **MongoDB**: NoSQL document database

### What You Can Add

Any system that can store and retrieve datasets, resources, and organizations can be implemented as a catalog backend:

- **Elasticsearch**: Full-text search engine
- **PostgreSQL**: Relational database
- **SQLite**: Lightweight file-based database
- **Neo4j**: Graph database
- **Redis**: In-memory data store
- **Custom REST API**: Any external catalog service

## Architecture

```
┌─────────────────────────────────────────┐
│     FastAPI Routes                      │
│     (No changes needed)                 │
└──────────────┬──────────────────────────┘
               │
┌──────────────▼──────────────────────────┐
│     Service Layer                       │
│     (No changes needed)                 │
└──────────────┬──────────────────────────┘
               │
┌──────────────▼──────────────────────────┐
│   CatalogSettings (Factory)             │
│   - Selects repository based on config  │
└──────────────┬──────────────────────────┘
               │
┌──────────────▼──────────────────────────┐
│   DataCatalogRepository Interface       │
│   (Abstract base class)                 │
└──────────────┬──────────────────────────┘
               │
       ┌───────┴────────┬──────────────────┐
       │                │                  │
┌──────▼──────┐  ┌──────▼────────┐  ┌─────▼──────────┐
│  CKAN       │  │  MongoDB      │  │  Your New      │
│  Repository │  │  Repository   │  │  Repository    │
└─────────────┘  └───────────────┘  └────────────────┘
```

## Step-by-Step Implementation

### Step 1: Create Your Repository Class

Create a new file in `api/repositories/` for your backend implementation:

```bash
touch api/repositories/your_backend_repository.py
```

### Step 2: Implement the DataCatalogRepository Interface

Your class must inherit from `DataCatalogRepository` and implement all abstract methods:

```python
# api/repositories/your_backend_repository.py
from typing import Any, Dict, List
from api.repositories.base_repository import DataCatalogRepository

class YourBackendRepository(DataCatalogRepository):
    """
    Your backend implementation of the catalog repository.

    Parameters
    ----------
    connection_params : dict
        Connection parameters specific to your backend
    """

    def __init__(self, connection_params: dict):
        self.client = YourBackendClient(**connection_params)
        # Initialize your connection here

    def package_create(self, **kwargs) -> Dict[str, Any]:
        """Create a package in your backend."""
        # Your implementation here
        # Must return dict with at least {"id": "...", "name": "..."}
        pass

    def package_show(self, id: str) -> Dict[str, Any]:
        """Retrieve a package from your backend."""
        # Your implementation here
        pass

    def package_update(self, **kwargs) -> Dict[str, Any]:
        """Update a package in your backend."""
        # Your implementation here
        pass

    def package_patch(self, **kwargs) -> Dict[str, Any]:
        """Partially update a package in your backend."""
        # Your implementation here
        pass

    def package_delete(self, id: str) -> None:
        """Delete a package from your backend."""
        # Your implementation here
        pass

    def package_search(
        self,
        q: str = "*:*",
        fq: str = "",
        rows: int = 10,
        start: int = 0,
        sort: str = "score desc, metadata_modified desc",
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Search packages in your backend.

        Must return dict with {"count": int, "results": []}
        """
        # Your implementation here
        pass

    def resource_create(self, **kwargs) -> Dict[str, Any]:
        """Create a resource in your backend."""
        # Your implementation here
        pass

    def resource_show(self, id: str) -> Dict[str, Any]:
        """Retrieve a resource from your backend."""
        # Your implementation here
        pass

    def resource_delete(self, id: str) -> None:
        """Delete a resource from your backend."""
        # Your implementation here
        pass

    def organization_create(self, **kwargs) -> Dict[str, Any]:
        """Create an organization in your backend."""
        # Your implementation here
        pass

    def organization_show(self, id: str) -> Dict[str, Any]:
        """Retrieve an organization from your backend."""
        # Your implementation here
        pass

    def organization_list(
        self, all_fields: bool = False, **kwargs
    ) -> List[Dict[str, Any]]:
        """List organizations from your backend."""
        # Your implementation here
        pass

    def organization_delete(self, id: str) -> None:
        """Delete an organization from your backend."""
        # Your implementation here
        pass
```

### Step 3: Register Your Repository in the Module

Update `api/repositories/__init__.py` to export your new repository:

```python
# api/repositories/__init__.py
from api.repositories.base_repository import DataCatalogRepository
from api.repositories.ckan_repository import CKANRepository
from api.repositories.mongodb_repository import MongoDBRepository
from api.repositories.your_backend_repository import YourBackendRepository  # Add this

__all__ = [
    "DataCatalogRepository",
    "CKANRepository",
    "MongoDBRepository",
    "YourBackendRepository",  # Add this
]
```

### Step 4: Add Configuration Settings

Update `api/config/catalog_settings.py` to support your new backend:

```python
# api/config/catalog_settings.py
from api.repositories.your_backend_repository import YourBackendRepository

class CatalogSettings(BaseSettings):
    # Existing settings...
    local_catalog_backend: str = "ckan"

    # Add your backend settings
    your_backend_connection_string: str = "your-default-connection"
    your_backend_param1: str = "default-value"
    your_backend_param2: int = 5432

    @property
    def local_catalog(self) -> DataCatalogRepository:
        backend = self.local_catalog_backend.lower()

        if backend == "your_backend":
            return YourBackendRepository(
                connection_params={
                    "connection_string": self.your_backend_connection_string,
                    "param1": self.your_backend_param1,
                    "param2": self.your_backend_param2,
                }
            )
        elif backend == "mongodb":
            return MongoDBRepository(...)
        elif backend == "ckan":
            return CKANRepository(...)
        else:
            raise ValueError(
                f"Unsupported catalog backend: {backend}. "
                f"Supported backends: 'ckan', 'mongodb', 'your_backend'"
            )
```

### Step 5: Update Environment Configuration

Add your backend configuration to `example.env`:

```bash
# LOCAL CATALOG CONFIGURATION

# Backend for local catalog: "ckan", "mongodb", or "your_backend"
LOCAL_CATALOG_BACKEND=ckan

# ... existing CKAN and MongoDB config ...

# Your Backend Configuration (if LOCAL_CATALOG_BACKEND=your_backend)

YOUR_BACKEND_CONNECTION_STRING=your-connection-string-here
YOUR_BACKEND_PARAM1=value1
YOUR_BACKEND_PARAM2=5432
```

### Step 6: Add Dependencies

If your backend requires additional Python packages, add them to `requirements.txt`:

```txt
# requirements.txt
...existing packages...
your-backend-client>=1.0.0
```

## Example: Adding Elasticsearch Backend

Here's a complete example of adding Elasticsearch as a catalog backend:

### 1. Create Elasticsearch Repository

```python
# api/repositories/elasticsearch_repository.py
from typing import Any, Dict, List
from datetime import datetime
from elasticsearch import Elasticsearch
from api.repositories.base_repository import DataCatalogRepository

class ElasticsearchRepository(DataCatalogRepository):
    """Elasticsearch implementation of catalog repository."""

    def __init__(self, hosts: List[str], index_prefix: str = "ndp"):
        self.es = Elasticsearch(hosts=hosts)
        self.index_prefix = index_prefix
        self.packages_index = f"{index_prefix}_packages"
        self.resources_index = f"{index_prefix}_resources"
        self.orgs_index = f"{index_prefix}_organizations"

        # Create indices if they don't exist
        self._create_indices()

    def _create_indices(self):
        """Create Elasticsearch indices with mappings."""
        package_mapping = {
            "mappings": {
                "properties": {
                    "id": {"type": "keyword"},
                    "name": {"type": "keyword"},
                    "title": {"type": "text"},
                    "notes": {"type": "text"},
                    "owner_org": {"type": "keyword"},
                    "extras": {"type": "object"},
                    "resources": {"type": "nested"},
                    "metadata_created": {"type": "date"},
                    "metadata_modified": {"type": "date"},
                }
            }
        }

        if not self.es.indices.exists(index=self.packages_index):
            self.es.indices.create(index=self.packages_index, body=package_mapping)

        # Similar for resources and organizations...

    def package_create(self, **kwargs) -> Dict[str, Any]:
        """Create a package in Elasticsearch."""
        import uuid

        package_id = str(uuid.uuid4())
        now = datetime.utcnow().isoformat()

        doc = {
            "id": package_id,
            "name": kwargs.get("name"),
            "title": kwargs.get("title", ""),
            "owner_org": kwargs.get("owner_org"),
            "notes": kwargs.get("notes", ""),
            "extras": kwargs.get("extras", []),
            "resources": [],
            "metadata_created": now,
            "metadata_modified": now,
            "state": "active",
        }

        self.es.index(
            index=self.packages_index,
            id=package_id,
            document=doc,
            refresh=True  # Make immediately searchable
        )

        return doc

    def package_show(self, id: str) -> Dict[str, Any]:
        """Retrieve a package from Elasticsearch."""
        try:
            result = self.es.get(index=self.packages_index, id=id)
            return result["_source"]
        except Exception as e:
            raise Exception(f"Package '{id}' not found: {str(e)}")

    def package_search(
        self,
        q: str = "*:*",
        fq: str = "",
        rows: int = 10,
        start: int = 0,
        sort: str = "score desc, metadata_modified desc",
        **kwargs,
    ) -> Dict[str, Any]:
        """Search packages using Elasticsearch query DSL."""
        query = {
            "query": {
                "query_string": {
                    "query": q if q != "*:*" else "*",
                    "fields": ["title^2", "notes", "name"]
                }
            },
            "from": start,
            "size": rows,
        }

        # Add filters if provided
        if fq:
            # Parse fq and add to query
            pass

        result = self.es.search(index=self.packages_index, body=query)

        return {
            "count": result["hits"]["total"]["value"],
            "results": [hit["_source"] for hit in result["hits"]["hits"]]
        }

    # Implement other methods...
    def package_update(self, **kwargs) -> Dict[str, Any]:
        package_id = kwargs.get("id")
        kwargs["metadata_modified"] = datetime.utcnow().isoformat()

        self.es.update(
            index=self.packages_index,
            id=package_id,
            doc=kwargs,
            refresh=True
        )

        return self.package_show(package_id)

    def package_delete(self, id: str) -> None:
        self.es.delete(index=self.packages_index, id=id, refresh=True)

    # ... implement remaining methods
```

### 2. Register in Catalog Settings

```python
# api/config/catalog_settings.py
from api.repositories.elasticsearch_repository import ElasticsearchRepository

class CatalogSettings(BaseSettings):
    local_catalog_backend: str = "ckan"

    # Elasticsearch settings
    elasticsearch_hosts: List[str] = ["http://localhost:9200"]
    elasticsearch_index_prefix: str = "ndp"

    @property
    def local_catalog(self) -> DataCatalogRepository:
        backend = self.local_catalog_backend.lower()

        if backend == "elasticsearch":
            return ElasticsearchRepository(
                hosts=self.elasticsearch_hosts,
                index_prefix=self.elasticsearch_index_prefix
            )
        # ... other backends
```

### 3. Update Configuration Files

```bash
# example.env
LOCAL_CATALOG_BACKEND=elasticsearch

# Elasticsearch Configuration
ELASTICSEARCH_HOSTS=["http://localhost:9200"]
ELASTICSEARCH_INDEX_PREFIX=ndp
```

```txt
# requirements.txt
elasticsearch>=8.0.0
```

## Testing Your Implementation

### 1. Unit Tests

Create unit tests for your repository:

```python
# tests/test_your_backend_repository.py
import pytest
from api.repositories.your_backend_repository import YourBackendRepository

@pytest.fixture
def repository():
    return YourBackendRepository(connection_params={...})

def test_package_create(repository):
    package = repository.package_create(
        name="test-package",
        title="Test Package",
        owner_org="test-org",
        notes="Test description"
    )

    assert "id" in package
    assert package["name"] == "test-package"

def test_package_show(repository):
    # Create a package first
    created = repository.package_create(name="test", title="Test", owner_org="org")

    # Retrieve it
    retrieved = repository.package_show(created["id"])

    assert retrieved["id"] == created["id"]
    assert retrieved["name"] == "test"

# Add more tests...
```

### 2. Integration Tests

Test the full stack with your backend:

```python
# tests/test_integration_your_backend.py
from fastapi.testclient import TestClient
from api.main import app
import os

# Set environment to use your backend
os.environ["LOCAL_CATALOG_BACKEND"] = "your_backend"

client = TestClient(app)

def test_create_s3_resource_with_your_backend():
    response = client.post(
        "/s3",
        json={
            "resource_name": "test-s3",
            "resource_title": "Test S3 Resource",
            "owner_org": "test-org",
            "resource_s3": "s3://bucket/key"
        }
    )

    assert response.status_code == 200
    assert "id" in response.json()
```

## Best Practices

### 1. **Match CKAN's Response Format**

To ensure compatibility, your responses should match CKAN's structure:

```python
# Package response example
{
    "id": "uuid-string",
    "name": "package-name",
    "title": "Package Title",
    "owner_org": "org-id",
    "notes": "Description",
    "extras": [{"key": "k1", "value": "v1"}],
    "resources": [...],
    "metadata_created": "2024-01-01T00:00:00",
    "metadata_modified": "2024-01-01T00:00:00",
    "state": "active"
}
```

### 2. **Handle Errors Gracefully**

Always raise descriptive exceptions:

```python
def package_show(self, id: str) -> Dict[str, Any]:
    try:
        result = self.backend.get(id)
        if not result:
            raise Exception(f"Package '{id}' not found")
        return result
    except ConnectionError as e:
        raise Exception(f"Backend connection error: {str(e)}")
    except Exception as e:
        raise Exception(f"Error retrieving package: {str(e)}")
```

### 3. **Implement Efficient Indexing**

Create indexes for commonly queried fields:

```python
def _create_indexes(self):
    # For MongoDB
    self.packages.create_index("name", unique=True)
    self.packages.create_index("owner_org")
    self.packages.create_index([("title", "text"), ("notes", "text")])
```

### 4. **Support Transactions (if possible)**

For backends that support transactions, use them for multi-step operations:

```python
def package_delete(self, id: str) -> None:
    with self.backend.transaction():
        # Delete resources first
        self.resources.delete_many({"package_id": id})
        # Then delete package
        self.packages.delete_one({"id": id})
```

### 5. **Document Your Implementation**

Add comprehensive docstrings:

```python
class YourBackendRepository(DataCatalogRepository):
    """
    Your Backend implementation of the catalog repository.

    This repository uses YourBackend to store catalog data,
    providing [specific features/advantages].

    Connection Parameters
    ---------------------
    param1 : str
        Description of param1
    param2 : int
        Description of param2

    Examples
    --------
    >>> repo = YourBackendRepository(param1="value", param2=42)
    >>> package = repo.package_create(name="test", title="Test", owner_org="org")

    Notes
    -----
    - [Important note 1]
    - [Important note 2]
    """
```

### 6. **Optimize for Your Backend's Strengths**

Take advantage of your backend's unique features:

- **Elasticsearch**: Use full-text search capabilities
- **PostgreSQL**: Use SQL joins for complex queries
- **Neo4j**: Use graph traversals for relationships
- **Redis**: Use pub/sub for real-time updates

### 7. **Handle Extras/Metadata Properly**

Extras can contain any user-defined metadata:

```python
def package_create(self, **kwargs) -> Dict[str, Any]:
    extras = kwargs.get("extras", [])

    # Convert extras list to dict for easier handling
    extras_dict = {e["key"]: e["value"] for e in extras}

    # Store in your backend's preferred format
    # Convert back to list format when returning
    return {
        "id": package_id,
        "extras": [{"key": k, "value": v} for k, v in extras_dict.items()]
    }
```

## Troubleshooting

### Common Issues

1. **Import Errors**
   - Make sure to add your repository to `__init__.py`
   - Check that all dependencies are in `requirements.txt`

2. **Configuration Not Loading**
   - Verify environment variables are set correctly
   - Check `pydantic_settings` is reading from `.env`

3. **Type Mismatches**
   - Ensure your return types match the interface
   - Use `typing` hints consistently

4. **Tests Failing**
   - Mock external dependencies in unit tests
   - Use test containers for integration tests
   - Clean up test data between tests

## Contributing Your Backend

If you've implemented a backend that others might find useful, consider contributing it to the project:

1. Ensure all tests pass
2. Add comprehensive documentation
3. Update the main README.md
4. Submit a pull request with your implementation

## Resources

- [Repository Pattern Explained](https://martinfowler.com/eaaCatalog/repository.html)
- [CKAN API Documentation](https://docs.ckan.org/en/latest/api/index.html)
- [Python Abstract Base Classes](https://docs.python.org/3/library/abc.html)
- [Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)

---

For questions or support, please open an issue on the GitHub repository.

---

### docs/affinities-integration.md (3,641 bytes)

# Affinities Integration

This document describes how to configure and use the NDP Affinities integration in NDP-EP.

## Overview

NDP Affinities is a service that tracks relationships between datasets, services, and endpoints across the NDP ecosystem. When enabled, NDP-EP automatically registers datasets and services in Affinities, creating a federated view of all data assets.

## Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `AFFINITIES_ENABLED` | `False` | Enable/disable Affinities integration |
| `AFFINITIES_URL` | - | Base URL of the Affinities API |
| `AFFINITIES_EP_UUID` | - | UUID of this endpoint in Affinities |
| `AFFINITIES_TIMEOUT` | `30` | Request timeout in seconds |

### Setup Steps

1. **Register your endpoint in Affinities**

   First, manually register your NDP-EP instance in the Affinities system:

   ```bash
   curl -X POST "https://your-affinities-api/endpoints/" \
     -H "Content-Type: application/json" \
     -d '{
       "kind": "ndp-ep",
       "url": "https://your-ndp-ep-url",
       "metadata": {
         "name": "My NDP Endpoint",
         "organization": "My Organization"
       }
     }'
   ```

   This returns a response with a `uid` field - save this UUID.

2. **Configure NDP-EP**

   Add the following to your `.env` file:

   ```env
   AFFINITIES_ENABLED=True
   AFFINITIES_URL=https://your-affinities-api
   AFFINITIES_EP_UUID=550e8400-e29b-41d4-a716-446655440000
   ```

3. **Restart NDP-EP**

   After updating the configuration, restart your NDP-EP instance.

## How It Works

When Affinities integration is enabled:

### Dataset Registration

When you create a dataset via `POST /dataset`:

1. The dataset is created in the local catalog (CKAN or MongoDB)
2. NDP-EP registers the dataset in Affinities (`POST /datasets/`)
3. A relationship is created between the dataset and this endpoint (`POST /dataset-endpoints/`)

### Service Registration

When you register a service via `POST /services`:

1. The service is created in the local catalog
2. NDP-EP registers the service in Affinities (`POST /services/`)
3. A relationship is created between the service and this endpoint (`POST /service-endpoints/`)

## Error Handling

The Affinities integration is **non-blocking**:

- If Affinities is unreachable or returns an error, the main operation (dataset/service creation) still succeeds
- Errors are logged as warnings but do not affect the API response
- This ensures that Affinities availability does not impact NDP-EP functionality

## Metadata Stored in Affinities

### For Datasets

```json
{
  "title": "Dataset title",
  "source_ep": "your-ep-uuid",
  "metadata": {
    "name": "dataset_name",
    "owner_org": "organization",
    "local_id": "local-catalog-id",
    "notes": "Description",
    "tags": ["tag1", "tag2"]
  }
}
```

### For Services

```json
{
  "type": "service_type",
  "openapi_url": "documentation_url",
  "source_ep": "your-ep-uuid",
  "metadata": {
    "service_name": "my_service",
    "service_title": "My Service",
    "service_url": "https://service-url",
    "local_id": "local-catalog-id",
    "notes": "Description"
  }
}
```

## Troubleshooting

### Integration Not Working

1. Check that `AFFINITIES_ENABLED=True`
2. Verify `AFFINITIES_URL` is correct and accessible
3. Confirm `AFFINITIES_EP_UUID` is a valid UUID from Affinities
4. Check the NDP-EP logs for warning messages

### Testing the Connection

You can verify the Affinities API is accessible:

```bash
curl -X GET "https://your-affinities-api/endpoints/"
```

This should return a list of registered endpoints.

---

### docs/api-usage-guide.md (14,822 bytes)

# NDP EP API Usage Guide

This guide provides comprehensive documentation for using the NDP Entry Point (EP) API with curl examples, response formats, and common use cases.

## Table of Contents

- [Authentication](#authentication)
- [API Base URL](#api-base-url)
- [Server Selection](#server-selection)
- [Status Endpoints](#status-endpoints)
- [Organizations](#organizations)
- [Datasets](#datasets)
- [Services](#services)
- [URL Resources](#url-resources)
- [S3 Resources](#s3-resources)
- [Kafka Resources](#kafka-resources)
- [Search](#search)
- [Resource Management](#resource-management)
- [Error Handling](#error-handling)

---

## Authentication

The API uses Bearer token authentication. Include the `Authorization` header in your requests:

```bash
curl -H "Authorization: Bearer YOUR_TOKEN" https://api.example.com/endpoint
```

### Get User Information

```bash
curl -s http://localhost:8002/user/info \
  -H "Authorization: Bearer testing_token"
```

**Response:**
```json
{
  "roles": ["admin", "user"],
  "groups": ["test_group", "developers"],
  "sub": "test_user",
  "username": "test_user"
}
```

---

## API Base URL

Replace `http://localhost:8002` with your actual API endpoint:

- **Local Development:** `http://localhost:8002`
- **Production:** `https://your-api-domain.com`

### Root Endpoint

```bash
curl -s http://localhost:8002/
```

**Response:**
```json
"API is running successfully."
```

---

## Server Selection

Most endpoints support a `server` query parameter:

| Server | Description |
|--------|-------------|
| `local` | Default. Uses the local catalog backend (MongoDB or CKAN) |
| `pre_ckan` | Uses the pre-production CKAN instance (if enabled) |
| `global` | For search operations across all instances |

Example:
```bash
curl "http://localhost:8002/search?terms=test&server=local"
```

---

## Status Endpoints

### Get API Status

Returns comprehensive information about the API configuration and connected services.

```bash
curl -s http://localhost:8002/status/ \
  -H "Authorization: Bearer testing_token"
```

**Response:**
```json
{
  "api_version": "0.5.0",
  "organization": "Test Organization",
  "ep_name": "test_ep",
  "organization_based_access": false,
  "local_catalog_backend": "mongodb",
  "backend_connected": true,
  "pre_ckan_enabled": true,
  "kafka_enabled": false,
  "jupyterlab_enabled": true,
  "s3_enabled": true,
  "auth_api_url": "https://idp.example.com/information",
  "is_public": true,
  "pre_ckan_connected": true,
  "s3_connected": false
}
```

---

## Organizations

### List Organizations

```bash
curl -s "http://localhost:8002/organization?server=local"
```

**Response:**
```json
["services", "research_group", "test_org"]
```

### Filter Organizations by Name

```bash
curl -s "http://localhost:8002/organization?name=test&server=local"
```

### Create Organization

```bash
curl -s -X POST "http://localhost:8002/organization?server=local" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{
    "name": "research_team",
    "title": "Research Team",
    "description": "Organization for research projects"
  }'
```

**Response:**
```json
{
  "id": "911f00d5-8e99-4d92-9187-5cb8d011c19b",
  "message": "Organization created successfully"
}
```

### Delete Organization

```bash
curl -s -X DELETE "http://localhost:8002/organization/research_team?server=local" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

---

## Datasets

### Create General Dataset

```bash
curl -s -X POST "http://localhost:8002/dataset?server=local" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{
    "name": "climate_research_2024",
    "title": "Climate Research Dataset 2024",
    "owner_org": "research_team",
    "notes": "Comprehensive climate data from 2024 research project",
    "tags": ["climate", "research", "2024"],
    "extras": {
      "source": "field_observations",
      "project": "climate_study"
    }
  }'
```

**Response:**
```json
{
  "id": "cf248952-0f9d-4abe-8df2-fbae0b699f4d"
}
```

> **Note:** Some keys are reserved and cannot be used in `extras`: `version`, `ndp_group_id`, `ndp_user_id`

### Update Dataset (Full Update)

```bash
curl -s -X PUT "http://localhost:8002/dataset/DATASET_ID?server=local" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{
    "name": "climate_research_2024_updated",
    "title": "Climate Research Dataset 2024 - Updated",
    "owner_org": "research_team",
    "notes": "Updated comprehensive climate data"
  }'
```

### Partial Update Dataset (PATCH)

Update only specific fields without affecting others:

```bash
curl -s -X PATCH "http://localhost:8002/dataset/DATASET_ID?server=local" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{
    "notes": "Updated description for the dataset"
  }'
```

**Response:**
```json
{
  "message": "Dataset updated successfully"
}
```

---

## Services

Services are registered under the `services` organization.

### Register a New Service

```bash
curl -s -X POST "http://localhost:8002/services?server=local" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{
    "service_name": "weather_api",
    "service_title": "Weather API Service",
    "owner_org": "services",
    "service_url": "https://api.weather.example.com",
    "service_type": "REST API",
    "notes": "Weather data API providing real-time and forecast data",
    "health_check_url": "https://api.weather.example.com/health",
    "documentation_url": "https://docs.weather.example.com"
  }'
```

**Response:**
```json
{
  "id": "f5a319f9-c306-4f39-b7a3-add0dd654ab9"
}
```

### Update Service (PUT)

```bash
curl -s -X PUT "http://localhost:8002/services/SERVICE_ID?server=local" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{
    "service_name": "weather_api",
    "service_title": "Weather API Service - Updated",
    "owner_org": "services",
    "service_url": "https://api.weather.example.com/v2",
    "service_type": "REST API"
  }'
```

### Partial Update Service (PATCH)

```bash
curl -s -X PATCH "http://localhost:8002/services/SERVICE_ID?server=local" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{
    "notes": "Updated service description"
  }'
```

---

## URL Resources

### Create URL Resource

```bash
curl -s -X POST "http://localhost:8002/url?server=local" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{
    "resource_name": "temperature_data",
    "resource_title": "Temperature Dataset",
    "owner_org": "research_team",
    "resource_url": "https://data.example.com/temperature.csv",
    "file_type": "CSV",
    "notes": "Daily temperature readings",
    "processing": {
      "delimiter": ",",
      "header_line": 1,
      "start_line": 2
    }
  }'
```

**Response:**
```json
{
  "id": "a5918817-48a0-4974-8acd-2a582aa090f6"
}
```

### Supported File Types

| File Type | Description |
|-----------|-------------|
| `CSV` | Comma-separated values |
| `JSON` | JSON data files |
| `TXT` | Plain text files |
| `NetCDF` | Network Common Data Form |
| `stream` | Real-time data streams |

### Update URL Resource

```bash
curl -s -X PUT "http://localhost:8002/url/RESOURCE_ID?server=local" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{
    "resource_name": "temperature_data",
    "resource_title": "Temperature Dataset - Updated",
    "owner_org": "research_team",
    "resource_url": "https://data.example.com/temperature_v2.csv",
    "file_type": "CSV"
  }'
```

---

## S3 Resources

### Create S3 Resource

```bash
curl -s -X POST "http://localhost:8002/s3?server=local" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{
    "resource_name": "satellite_images",
    "resource_title": "Satellite Image Archive",
    "owner_org": "research_team",
    "s3_bucket": "research-data",
    "s3_key": "satellite/2024/",
    "file_type": "archive",
    "notes": "Satellite imagery for 2024"
  }'
```

### S3 Bucket Operations

#### List Buckets

```bash
curl -s "http://localhost:8002/s3/buckets/" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

#### Create Bucket

```bash
curl -s -X POST "http://localhost:8002/s3/buckets/new-bucket-name" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

#### List Objects in Bucket

```bash
curl -s "http://localhost:8002/s3/objects/bucket-name" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

#### Get Presigned Download URL

```bash
curl -s "http://localhost:8002/s3/objects/bucket-name/object-key/presigned-download" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

#### Get Presigned Upload URL

```bash
curl -s "http://localhost:8002/s3/objects/bucket-name/object-key/presigned-upload" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

---

## Kafka Resources

### Create Kafka Dataset

```bash
curl -s -X POST "http://localhost:8002/kafka?server=local" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{
    "dataset_name": "sensor_stream",
    "dataset_title": "Sensor Data Stream",
    "owner_org": "research_team",
    "kafka_topic": "sensors.temperature",
    "kafka_host": "kafka.example.com",
    "kafka_port": "9092",
    "dataset_description": "Real-time sensor data stream",
    "mapping": {
      "timestamp": "event_time",
      "value": "temperature"
    },
    "processing": {
      "data_key": "data",
      "info_key": "metadata"
    }
  }'
```

### Update Kafka Dataset

```bash
curl -s -X PUT "http://localhost:8002/kafka/DATASET_ID?server=local" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{
    "kafka_topic": "sensors.temperature.v2",
    "kafka_port": "9093"
  }'
```

### Partial Update Kafka Dataset

```bash
curl -s -X PATCH "http://localhost:8002/kafka/DATASET_ID?server=local" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{
    "kafka_host": "new-kafka.example.com"
  }'
```

---

## Search

### Simple GET Search

Search by terms across all fields:

```bash
curl -s "http://localhost:8002/search?terms=climate,temperature&server=local" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

**Response:**
```json
[
  {
    "id": "cf248952-0f9d-4abe-8df2-fbae0b699f4d",
    "name": "climate_research_2024",
    "title": "Climate Research Dataset 2024",
    "owner_org": "research_team",
    "notes": "Comprehensive climate data",
    "resources": [...],
    "extras": {...}
  }
]
```

### Search with Specific Keys

```bash
curl -s "http://localhost:8002/search?terms=research&keys=name&server=local" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

### Advanced POST Search

```bash
curl -s -X POST "http://localhost:8002/search" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{
    "owner_org": "services",
    "server": "local"
  }'
```

### Search by Multiple Criteria

```bash
curl -s -X POST "http://localhost:8002/search" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{
    "search_term": "weather,api",
    "resource_format": "service",
    "server": "local"
  }'
```

### Search with Filter List

```bash
curl -s -X POST "http://localhost:8002/search" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{
    "filter_list": ["service_type:REST API", "owner_org:services"],
    "server": "local"
  }'
```

---

## Resource Management

### Search Resources

Search for specific resources across datasets:

```bash
curl -s "http://localhost:8002/resources/search?name=temperature&server=local" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

**Response:**
```json
{
  "count": 1,
  "results": [
    {
      "id": "5b191c17-153e-4513-83aa-3167de17a317",
      "package_id": "a5918817-48a0-4974-8acd-2a582aa090f6",
      "name": "temperature_data",
      "url": "https://data.example.com/temperature.csv",
      "format": "url",
      "dataset_name": "temperature_data",
      "dataset_title": "Temperature Dataset"
    }
  ]
}
```

### Get Resource by ID

```bash
curl -s "http://localhost:8002/resource/RESOURCE_ID?server=local" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

### Update Resource within Dataset

```bash
curl -s -X PATCH "http://localhost:8002/dataset/DATASET_ID/resource/RESOURCE_ID?server=local" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{
    "name": "updated_resource_name",
    "description": "Updated resource description"
  }'
```

### Delete Resource from Dataset

```bash
curl -s -X DELETE "http://localhost:8002/dataset/DATASET_ID/resource/RESOURCE_ID?server=local" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

---

## Error Handling

### Common HTTP Status Codes

| Code | Description |
|------|-------------|
| `200` | Success |
| `201` | Created |
| `400` | Bad Request - Invalid input |
| `401` | Unauthorized - Missing or invalid token |
| `403` | Forbidden - Insufficient permissions |
| `404` | Not Found - Resource doesn't exist |
| `409` | Conflict - Duplicate resource |
| `422` | Validation Error - Invalid data format |

### Error Response Format

```json
{
  "detail": "Error message describing what went wrong"
}
```

### Duplicate Resource Error

```json
{
  "detail": {
    "error": "Duplicate Dataset",
    "detail": "A dataset with the given name already exists."
  }
}
```

### Validation Error

```json
{
  "detail": [
    {
      "loc": ["body", "name"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

### Reserved Key Error

```json
{
  "detail": "Reserved key error: \"Extras contain reserved keys: {'version'}\""
}
```

---

## Best Practices

1. **Always include authentication** - All write operations require a valid Bearer token.

2. **Use appropriate HTTP methods**:
   - `GET` for reading data
   - `POST` for creating new resources
   - `PUT` for full updates
   - `PATCH` for partial updates
   - `DELETE` for removing resources

3. **Handle errors gracefully** - Check the response status code and parse error messages.

4. **Use server parameter** - Specify `server=local` or `server=pre_ckan` based on your environment.

5. **Avoid reserved keys** - Don't use `version`, `ndp_group_id`, or `ndp_user_id` in extras.

---

## Swagger UI

Interactive API documentation is available at:

```
http://localhost:8002/docs
```

The OpenAPI specification can be accessed at:

```
http://localhost:8002/openapi.json
```

---

## Support

For issues and feature requests, please visit:
- GitHub Issues: [national-data-platform/ep-api/issues](https://github.com/national-data-platform/ep-api/issues)

---

### docs/architecture-diagrams.md (27,607 bytes)

# Architecture Diagrams and Visual References

This document provides visual diagrams to complement the Repository Pattern Architecture documentation.

## 1. Overall System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Client Applications                       │
│              (Web UI, Mobile Apps, Scripts)                 │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       │ HTTP/REST API
                       │
┌──────────────────────▼──────────────────────────────────────┐
│                   FastAPI Application                        │
│  ┌─────────────────────────────────────────────────────┐   │
│  │              Authentication & Authorization          │   │
│  └─────────────────────────────────────────────────────┘   │
└──────────────────────┬──────────────────────────────────────┘
                       │
        ┌──────────────┼──────────────┐
        │              │              │
┌───────▼────┐  ┌─────▼──────┐  ┌───▼────────┐
│  Register  │  │   Search   │  │   Update   │
│   Routes   │  │   Routes   │  │   Routes   │
└───────┬────┘  └─────┬──────┘  └───┬────────┘
        │             │             │
        └─────────────┼─────────────┘
                      │
                      │ Delegate to Services
                      │
┌─────────────────────▼──────────────────────────────────────┐
│                    Service Layer                            │
│  ┌──────────────────┐  ┌──────────────────────────┐        │
│  │ Organization     │  │ Datasource/Search        │        │
│  │ Services         │  │ Services                 │        │
│  └────────┬─────────┘  └──────────┬───────────────┘        │
│           │                       │                         │
│  ┌────────▼──────────────────────▼──────────┐             │
│  │      Dataset Services                    │             │
│  └────────┬──────────────────────────────────┘             │
│           │                                                 │
└───────────┼─────────────────────────────────────────────────┘
            │
            │ Use Repository Interface
            │
┌───────────▼──────────────────────────────────────────────────┐
│           Repository Abstraction Layer                        │
│  ┌──────────────────────────────────────────────────────┐   │
│  │       DataCatalogRepository (Abstract)               │   │
│  │  - package_*() methods                              │   │
│  │  - resource_*() methods                             │   │
│  │  - organization_*() methods                         │   │
│  │  - check_health()                                   │   │
│  └──────────────────────────────────────────────────────┘   │
└───┬──────────────────┬──────────────────┬──────────────────┘
    │                  │                  │
┌───▼────────┐  ┌──────▼──────┐  ┌──────▼──────┐
│    CKAN    │  │   MongoDB   │  │  Future     │
│ Repository │  │ Repository  │  │ Repository  │
└───┬────────┘  └──────┬──────┘  └──────┬──────┘
    │                  │                │
┌───▼────────┐  ┌──────▼──────┐  ┌──────▼──────┐
│  CKAN API  │  │  MongoDB    │  │  Custom     │
│   Client   │  │  Connection │  │  Backend    │
└─────────────  └─────────────┘  └─────────────┘
```

## 2. Request Flow: Create Dataset

```
┌─────────────────────────────────────────────────────────────┐
│  POST /dataset                                              │
│  Body: {name, title, owner_org, resources, extras}         │
└──────────────────┬──────────────────────────────────────────┘
                   │
       ┌───────────▼──────────────┐
       │  Authentication Check    │
       │  Authorization Check     │
       └───────────┬──────────────┘
                   │
       ┌───────────▼────────────────────────┐
       │  post_general_dataset_endpoint()   │
       │  - Extract server parameter        │
       │  - Get repository from settings    │
       └───────────┬────────────────────────┘
                   │
       ┌───────────▼──────────────────────┐
       │ catalog_settings factory         │
       │ (Choose backend)                  │
       └───────┬───────────────────────────┘
               │
       ┌───────┴──────────┐
       │                  │
   ┌───▼───┐          ┌───▼────┐
   │CKAN?  │          │MongoDB?│
   └───┬───┘          └───┬────┘
       │                  │
   ┌───▼───────┐      ┌───▼──────────┐
   │CKANRepos- │      │MongoDBRepos- │
   │itory     │      │itory         │
   └───┬───────┘      └───┬──────────┘
       │                  │
       └─────────┬────────┘
                 │
       ┌─────────▼──────────────────┐
       │ create_general_dataset()   │
       │ (Service layer)             │
       │ - Validate input            │
       │ - Inject NDP metadata      │
       │ - Call repository methods   │
       └─────────┬──────────────────┘
                 │
       ┌─────────▼──────────────────────┐
       │ repository.package_create()     │
       │ Create package/dataset          │
       └─────────┬──────────────────────┘
                 │
       ┌─────────▼──────────────────────┐
       │ repository.resource_create()    │
       │ Create resource for each item   │
       └─────────┬──────────────────────┘
                 │
       ┌─────────▼──────────────────┐
       │ Response: {id: dataset_id} │
       └─────────────────────────────┘
```

## 3. Request Flow: Search Datasources

```
┌────────────────────────────────────────────────────┐
│  POST /search                                      │
│  Body: {search_term, dataset_name, server: local} │
└─────────────┬────────────────────────────────────┘
              │
   ┌──────────▼────────────────┐
   │  search_datasource()      │
   │  (Route)                   │
   └──────────┬─────────────────┘
              │
   ┌──────────▼──────────────────────┐
   │ catalog_settings factory        │
   │ (Get repository by server)      │
   │ server="local" →                │
   │ local_catalog property          │
   └──────────┬──────────────────────┘
              │
        ┌─────┴──────────┐
        │                │
    ┌───▼────┐       ┌───▼─────┐
    │ CKAN   │       │ MongoDB  │
    │enabled?│       │enabled?  │
    └───┬────┘       └───┬──────┘
        │                │
   ┌────▼────┐      ┌────▼────────┐
   │CKANRepo │      │MongoDBRepo  │
   └────┬────┘      └────┬────────┘
        │                │
        └────┬───────────┘
             │
   ┌─────────▼────────────────────────────┐
   │ datasource_services.search_datasource│
   │ (Service layer)                       │
   │ - Build query string                 │
   │ - Apply filters                      │
   │ - Call repository.package_search()   │
   └─────────┬────────────────────────────┘
             │
   ┌─────────▼──────────────────┐
   │ repository.package_search()│
   │                            │
   │ If CKAN:                   │
   │  - Solr query              │
   │  - Full-text search        │
   │                            │
   │ If MongoDB:                │
   │  - Regex search            │
   │  - Filter queries          │
   └─────────┬──────────────────┘
             │
   ┌─────────▼────────────────────┐
   │ Transform results            │
   │ (DataSourceResponse model)   │
   └─────────┬────────────────────┘
             │
   ┌─────────▼────────────────────┐
   │ Return: List[DataSourceResp] │
   └────────────────────────────┘
```

## 4. Repository Pattern: Backend Switching

```
                   Service Layer
                        │
                        │ repository.package_search(q="climate")
                        │
                ┌───────▼──────────┐
                │ Repository       │
                │ Interface        │
                └───────┬──────────┘
                        │
           ┌────────────┼────────────┐
           │            │            │
      ┌────▼─────┐  ┌───▼────┐  ┌──▼────────┐
      │ CKAN     │  │MongoDB │  │ Future    │
      │Repo      │  │Repo    │  │ Repo      │
      └────┬─────┘  └───┬────┘  └──┬────────┘
           │            │         │
      ┌────▼─────┐  ┌───▼────┐  ┌──▼────────┐
      │ CKAN API │  │MongoDB │  │ Custom    │
      │ (Solr)   │  │Driver  │  │ Backend   │
      └──────────┘  └────────┘  └───────────┘

Same Service Code → Different Backends
Different Implementations → Same Response Format
```

## 5. Data Model: Package Structure

```
Package (Dataset)
├── id (UUID)
├── name (unique)
├── title
├── owner_org (organization ID)
├── notes (description)
├── state ("active")
├── type ("dataset")
├── metadata_created (ISO timestamp)
├── metadata_modified (ISO timestamp)
│
├── resources (array)
│  └── Resource
│     ├── id (UUID)
│     ├── package_id (parent package)
│     ├── name
│     ├── url
│     ├── description
│     ├── format (CSV, S3, Kafka, URL, etc.)
│     ├── created (ISO timestamp)
│     └── last_modified (ISO timestamp)
│
├── extras (array)
│  └── Extra
│     ├── key (field name)
│     └── value (field value)
│
├── tags (array)
│  └── Tag
│     ├── id (UUID)
│     ├── name
│     └── vocabulary_id
│
└── organization (nested object)
   ├── id
   ├── name
   └── title
```

## 6. Three-Catalog Architecture

```
┌──────────────────────────────────────────────────────────┐
│                    NDP-EP Application                     │
└──────────────────────────────────────────────────────────┘
                        │
    ┌───────────────────┼───────────────────┐
    │                   │                   │
    
┌───▼──────────┐  ┌─────▼──────┐  ┌────────▼───┐
│   LOCAL      │  │   GLOBAL   │  │  PRE-CKAN  │
│  CATALOG     │  │  CATALOG   │  │  CATALOG   │
├──────────────┤  ├────────────┤  ├────────────┤
│              │  │            │  │            │
│ Mutable      │  │ Read-only  │  │ Staging    │
│ Configurable│  │ Reference  │  │ Testing    │
│ Backend:    │  │            │  │            │
│             │  │ Always CKAN│  │ Always CKAN│
│ CKAN        │  │            │  │            │
│  or         │  │ Global NDP │  │ Pre-release│
│ MongoDB     │  │ Data Hub   │  │ Environment│
│             │  │            │  │            │
└────┬────────┘  └──────┬─────┘  └────┬───────┘
     │                  │             │
     │                  │             │
├─────────────┐  ┌──────────────┐  ┌──────────┐
│ Organization│  │  Read-only   │  │ Promote  │
│'s data      │  │  references  │  │ datasets │
│             │  │  for global  │  │ to global│
│ Write:      │  │  integration │  │ from pre │
│ Datasets    │  │              │  │          │
│ Resources   │  │ Use for:     │  │ Validate │
│ Orgs        │  │ - Integration│  │ before   │
│             │  │ - Metrics    │  │ going    │
│ Read:       │  │ - Analytics  │  │ global   │
│ View own    │  │              │  │          │
│ data        │  │ Do NOT write │  │ Do NOT   │
│             │  │              │  │ write    │
└─────────────┘  └──────────────┘  └──────────┘
```

## 7. Configuration & Factory Pattern

```
┌─────────────────────────────────┐
│  Environment Variables           │
│  .env file                       │
├─────────────────────────────────┤
│                                 │
│ LOCAL_CATALOG_BACKEND=mongodb   │
│ MONGODB_CONNECTION_STRING=...   │
│ MONGODB_DATABASE=ndp_local      │
│                                 │
│ (+ CKAN configs for all)        │
│                                 │
└────────────┬────────────────────┘
             │
     ┌───────▼────────────┐
     │ CatalogSettings    │
     │ (Configuration     │
     │  class)            │
     └───────┬────────────┘
             │
     ┌───────┴─────────────────┐
     │                         │
 ┌───▼────┐  ┌────────────┐  ┌─▼────────┐
 │ local  │  │  global    │  │   pre    │
 │_cat    │  │_cat        │  │_cat      │
 │alog()  │  │alog()      │  │alog()    │
 └───┬────┘  └──────┬─────┘  └─┬────────┘
     │              │         │
 ┌───▼────┐     ┌───▼──┐  ┌──▼──────┐
 │Factory │     │CKAN  │  │ CKAN    │
 │Selection   │ │Repo  │  │ Repo    │
 │Based on │  │      │  │         │
 │CONFIG  │  │      │  │         │
 └────────┘  └──────┘  └─────────┘
     │
  ┌──┴──────────────────┐
  │                     │
┌─▼───────────┐  ┌──────▼────┐
│ CKAN Repo   │  │MongoDB Repo│
│ (if CKAN)   │  │(if MongoDB)│
└─────────────┘  └───────────┘
```

## 8. Search Flow: Query Processing

### CKAN Backend
```
Service: package_search(q="climate change")
    ↓
CKANRepository.package_search()
    ↓
ckan.action.package_search(
    q="climate change",
    fq_list=["organization:research"],
    rows=100
)
    ↓
Solr Search Engine
    ├─ Full-text search on indexed fields
    ├─ Scoring and ranking
    ├─ Filter by organization
    └─ Pagination
    ↓
CKAN Response:
{
    "count": 42,
    "results": [
        {
            "id": "...",
            "name": "...",
            "title": "Climate Study",
            "resources": [...],
            "organization": {...}
        },
        ...
    ]
}
    ↓
Service: Transform to DataSourceResponse
    ↓
Route: Return to Client
```

### MongoDB Backend
```
Service: package_search(q="climate change")
    ↓
MongoDBRepository.package_search()
    ↓
Parse query and filters
    ├─ q="climate change" 
    │  → MongoDB query with $or on regex
    └─ fq_list=["organization:research"]
       → Add to query: {"organization": "research"}
    ↓
MongoDB Query:
db.packages.find({
    "$or": [
        {"title": {"$regex": "climate change", "$options": "i"}},
        {"notes": {"$regex": "climate change", "$options": "i"}},
        {"name": {"$regex": "climate change", "$options": "i"}}
    ],
    "organization": "research"
})
    ↓
Apply sorting, skip, limit
    ↓
MongoDB Response:
{
    "count": 12,
    "results": [
        {
            "id": "...",
            "name": "...",
            "title": "Climate Change Data",
            "resources": [...],
            "organization": {...}
        },
        ...
    ]
}
    ↓
Service: Transform to DataSourceResponse
    ↓
Route: Return to Client
```

## 9. Service Layer Patterns

### Pattern 1: Direct Repository Usage
```python
def get_organization(org_id: str, server: str = "local"):
    repository = catalog_settings.get_repository_by_name(server)
    return repository.organization_show(id=org_id)
```

### Pattern 2: Complex Business Logic
```python
def create_dataset_with_validation(data: DatasetRequest):
    repository = catalog_settings.local_catalog
    
    # Validate organization exists
    try:
        repository.organization_show(id=data.owner_org)
    except:
        raise ValueError("Organization not found")
    
    # Create package
    package = repository.package_create(**data.dict())
    
    # Create resources
    for resource in data.resources:
        repository.resource_create(
            package_id=package["id"],
            **resource.dict()
        )
    
    return package["id"]
```

### Pattern 3: Multi-Backend Search
```python
async def search_across_servers(query: str):
    results = {}
    
    for server in ["local", "global"]:
        repo = catalog_settings.get_repository_by_name(server)
        results[server] = repo.package_search(q=query, rows=100)
    
    return results
```

## 10. Error Handling Flow

```
┌─────────────┐
│HTTP Request │
└──────┬──────┘
       │
    ┌──▼────────────────┐
    │ Try Block         │
    ├──────────────────┤
    │ 1. Get Repository│
    │ 2. Call Service  │
    │ 3. Return Result │
    └──┬─────────────┬──┘
       │             │
       │ ┌──────────▼──────────┐
       │ │ Exception Occurs    │
       │ │ (in service/repo)   │
       │ └──────────┬──────────┘
       │            │
    ┌──▼────────────▼──────────┐
    │ Except Handlers           │
    ├───────────────────────────┤
    │ ValueError → 400 Bad Req  │
    │ NotFound → 404 Not Found  │
    │ ValidationError → 409     │
    │ Generic → 500 Server Err  │
    └──────────┬────────────────┘
               │
    ┌──────────▼──────────┐
    │ HTTPException       │
    │ (with status_code & │
    │  detail message)    │
    └──────────┬──────────┘
               │
    ┌──────────▼────────────┐
    │ JSON Error Response   │
    │ {                     │
    │  "detail": "message"  │
    │ }                     │
    └───────────────────────┘
```

## 11. Index Strategy

### CKAN (Solr)
```
Solr Index:
- Full-text fields: title, notes, name
- Exact match fields: id, name, owner_org
- Facet fields: organization, tags, format
- Sorting: score, metadata_modified
- Real-time indexing
```

### MongoDB
```
Indexes Created:
- packages.name (unique)
- packages.owner_org
- packages.title + packages.notes (text index)
- resources.package_id
- organizations.name (unique)
```

## 12. Deployment Scenarios

### Scenario 1: Development Setup
```
┌─────────────┐
│  Docker Dev │
├─────────────┤
│             │
│ FastAPI App │──────┐
│             │      │
└─────────────┘      │
                     │
                  ┌──▼──────┐
                  │ MongoDB  │
                  │(embedded)│
                  └──────────┘
                  
Configuration:
LOCAL_CATALOG_BACKEND=mongodb
Minimal infrastructure needed
```

### Scenario 2: Production Setup
```
┌──────────────┐
│  K8s Cluster │
├──────────────┤
│              │
│ FastAPI Pods │──────┐
│  (replicas)  │      │
│              │      │
└──────────────┘      │
                   ┌──▼───────┐
                   │ CKAN      │
                   ├───────────┤
                   │ Solr      │
                   ├───────────┤
                   │ PostgreSQL│
                   └───────────┘
                   
Configuration:
LOCAL_CATALOG_BACKEND=ckan
HA setup with replicas
Separate search (Solr)
Persistent storage
```

---

This document provides visual references for understanding the architecture. Refer to `repository-pattern-architecture.md` for detailed explanations.

---

### docs/minio-setup.md (5,755 bytes)

# S3-Compatible Storage Setup Guide (MINIO Example)

This guide explains how to set up S3-compatible object storage for use with the NDP-EP API, using MINIO as an example.

## What is MINIO?

MINIO is a popular, high-performance S3-compatible object storage system that can be used as an example for S3 storage setup. It supports:
- **File Storage**: Store and manage files, documents, images, and data
- **Backup Storage**: Create backup repositories for datasets
- **Data Archiving**: Long-term storage of infrequently accessed data
- **API Integration**: Direct S3-compatible API access for applications

## Quick Setup with Docker

### Option 1: Standalone Container

Run MINIO as a single Docker container:

```bash
docker run -d \
  --name ndp-minio \
  -p 9000:9000 \
  -p 9001:9001 \
  -e MINIO_ROOT_USER=minioadmin \
  -e MINIO_ROOT_PASSWORD=minioadmin123 \
  -v minio_data:/data \
  minio/minio:latest server /data --console-address ":9001"
```

> **📝 Note**: If you get a "port already allocated" error, make sure no other services are using ports 9000 or 9001. You can check with `docker ps` and stop any conflicting containers.

### Option 2: Using Docker Compose

Create a `docker-compose.yml` file:

```yaml
services:
  minio:
    image: minio/minio:latest
    container_name: ndp-minio
    ports:
      - "9000:9000"
      - "9001:9001"
    environment:
      MINIO_ROOT_USER: minioadmin
      MINIO_ROOT_PASSWORD: minioadmin123
    command: server /data --console-address ":9001"
    volumes:
      - minio_data:/data
    networks:
      - backend

volumes:
  minio_data:
    driver: local

networks:
  backend:
    driver: bridge
```

Run with:
```bash
# Modern Docker Compose (recommended)
docker compose up -d

# Or legacy docker-compose if available
docker-compose up -d
```

> **📝 Note**: The `version` field is obsolete in modern Docker Compose and will show a warning if included.

## Access Points

Once MINIO is running, you can access:

- **MINIO API**: `http://localhost:9000` (or `http://YOUR_SERVER_IP:9000`)
  - Used by the NDP-EP API for programmatic access
  - S3-compatible REST API endpoint

- **MINIO Console**: `http://localhost:9001` (or `http://YOUR_SERVER_IP:9001`)
  - Web-based management interface
  - Create buckets, upload files, manage users

> **🔧 Replace `localhost`**: If running on a remote server, replace `localhost` with your server's IP address (e.g., `192.168.1.100`).

## Default Credentials

- **Username**: `minioadmin`
- **Password**: `minioadmin123`

> **⚠️ Security Warning**: Change the default credentials in production environments!

## Configure NDP-EP API

Update your `.env` file to connect the API to your S3-compatible storage (using MINIO as example):

```bash
# Enable S3 storage integration
S3_ENABLED=True

# S3 endpoint (replace YOUR_SERVER_IP with your actual server IP)
S3_ENDPOINT=YOUR_SERVER_IP:9000

# S3 credentials (match your S3 service setup)
S3_ACCESS_KEY=minioadmin
S3_SECRET_KEY=minioadmin123

# Connection security
S3_SECURE=False  # Set to True if using HTTPS

# Default region
S3_REGION=us-east-1
```

## Verify Installation

### 1. Check Container Status
```bash
docker ps | grep minio
```

> **✅ Expected result**: You should see a running container with ports `9000-9001->9000-9001/tcp`

Example output:
```
12b831bae9ca   minio/minio:latest   "/usr/bin/docker-ent…"   8 seconds ago   Up 7 seconds   0.0.0.0:9000-9001->9000-9001/tcp   ndp-minio
```

### 2. Test API Connection
```bash
# Replace localhost with your server IP if running remotely
curl http://localhost:9000/minio/health/ready
```

> **✅ Expected result**: HTTP 200 response means MINIO API is working correctly.

### 3. Access Web Console
Open `http://localhost:9001` in your browser (replace `localhost` with your server IP if running remotely) and log in with:
- **Username**: `minioadmin`
- **Password**: `minioadmin123`

### 4. Test NDP-EP API Integration
Once both MINIO and the NDP-EP API are running, test the integration:

```bash
# List buckets via NDP-EP API (replace YOUR_API_TOKEN with your actual token)
curl -H "Authorization: Bearer YOUR_API_TOKEN" \
     http://localhost:8001/s3/buckets

# Create a test bucket (replace YOUR_API_TOKEN with your actual token)
curl -X POST \
     -H "Authorization: Bearer YOUR_API_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"name": "test-bucket"}' \
     http://localhost:8001/s3/buckets
```

> **🔑 Get API Token**: You can use `testing_token` for development, or get a real token from the NDP authentication system.

## Troubleshooting

### MINIO Container Won't Start
- Check if ports 9000 and 9001 are available
- Verify Docker has permissions to create volumes
- Check container logs: `docker logs ndp-minio`

### Connection Refused from NDP-EP API
- Verify MINIO container is running and accessible
- Check firewall settings for ports 9000/9001
- Ensure MINIO_ENDPOINT in `.env` matches your server IP
- Verify credentials match between MINIO and API configuration

### Permission Denied Errors
- Check MINIO credentials are correct
- Verify the API key has sufficient permissions
- Review MINIO access policies in the web console

## Advanced Configuration

### Multi-Node Setup
For high-availability deployments, refer to the [MINIO distributed setup documentation](https://docs.min.io/docs/distributed-minio-quickstart-guide.html).

### Backup and Recovery
Configure regular backups of your MINIO data directory and consider using MINIO's built-in replication features.

### Monitoring
MINIO provides Prometheus metrics at `http://your-server:9000/minio/v2/metrics/cluster` for monitoring integration.

---

For more information about MINIO, visit the [official documentation](https://docs.min.io/).

---

### docs/repository-pattern-architecture.md (22,119 bytes)

# Repository Pattern Architecture

## Overview

The NDP-EP (National Data Platform - Enterprise Platform) implements a **Repository Pattern** for abstracting data catalog backend operations. This architecture enables seamless switching between different catalog implementations (CKAN, MongoDB, or future backends) without changing application code.

## Key Concepts

### What is the Repository Pattern?

The Repository Pattern is a design pattern that abstracts data access logic by creating an intermediary layer between business logic and data sources. Instead of directly accessing databases or external APIs, application code communicates with repositories that provide a consistent interface.

**Benefits:**
- Backend independence: Switch databases/services without code changes
- Testability: Easy to mock repositories for unit tests
- Consistency: Uniform API across different implementations
- Maintainability: Data access logic centralized in one place

---

## Architecture Layers

```
┌─────────────────────────────────┐
│     FastAPI Routes/Endpoints    │  HTTP interface
└────────────┬────────────────────┘
             │
┌────────────▼────────────────────┐
│    Service/Business Logic       │  Domain-specific operations
└────────────┬────────────────────┘
             │
┌────────────▼────────────────────┐
│  Repository Abstraction Layer   │  Uniform interface for data access
└────────────┬────────────────────┘
             │
    ┌────────┴─────────┬──────────┐
    │                  │          │
┌───▼────┐    ┌────────▼──┐  ┌───▼────┐
│ CKAN   │    │ MongoDB    │  │ Future │
│ API    │    │ Database   │  │Backends│
└────────┘    └────────────┘  └────────┘
```

---

## 1. Repository Layer

### Base Repository (`api/repositories/base_repository.py`)

The `DataCatalogRepository` is an abstract base class (ABC) that defines the interface all backends must implement.

**Key Methods:**

#### Package Management
```python
package_create(**kwargs) -> Dict[str, Any]
package_show(id: str) -> Dict[str, Any]
package_update(**kwargs) -> Dict[str, Any]
package_patch(**kwargs) -> Dict[str, Any]
package_delete(id: str) -> None
package_search(q: str, fq: str, rows: int, start: int, sort: str, **kwargs) -> Dict[str, Any]
```

#### Resource Management
```python
resource_create(**kwargs) -> Dict[str, Any]
resource_show(id: str) -> Dict[str, Any]
resource_delete(id: str) -> None
```

#### Organization Management
```python
organization_create(**kwargs) -> Dict[str, Any]
organization_show(id: str) -> Dict[str, Any]
organization_list(all_fields: bool) -> List[Dict[str, Any]]
organization_delete(id: str) -> None
```

#### Health Monitoring
```python
check_health() -> bool
```

### CKAN Repository (`api/repositories/ckan_repository.py`)

Implements the repository interface for **CKAN** (Comprehensive Knowledge Archive Network).

**How it works:**
- Wraps a `ckanapi.RemoteCKAN` client instance
- Delegates all operations to CKAN's action API
- Returns responses in CKAN's standard format

**Example:**
```python
class CKANRepository(DataCatalogRepository):
    def __init__(self, ckan_instance):
        self.ckan = ckan_instance  # RemoteCKAN client
    
    def package_create(self, **kwargs) -> Dict[str, Any]:
        return self.ckan.action.package_create(**kwargs)
    
    def package_search(self, q: str = "*:*", fq: str = "", rows: int = 10, 
                      start: int = 0, sort: str = "score desc, metadata_modified desc",
                      **kwargs) -> Dict[str, Any]:
        return self.ckan.action.package_search(
            q=q, fq=fq, rows=rows, start=start, sort=sort, **kwargs
        )
```

**Characteristics:**
- Direct wrapper around CKAN API
- Minimal transformation needed (CKAN responses already match interface)
- Supports Solr-style full-text search

### MongoDB Repository (`api/repositories/mongodb_repository.py`)

Implements the repository interface for **MongoDB**, allowing it to serve as a drop-in replacement for CKAN.

**Architecture:**
- Collections: `packages`, `resources`, `organizations`
- Each collection has appropriate indexes for performance
- Mimics CKAN's response structure for compatibility

**Key Implementation Details:**

#### Document Structure
```python
# Package document
{
    "id": "uuid",
    "name": "unique_name",
    "title": "Human Title",
    "owner_org": "org_id",
    "notes": "description",
    "resources": [],
    "extras": [{"key": "...", "value": "..."}],
    "metadata_created": "ISO timestamp",
    "metadata_modified": "ISO timestamp",
    "state": "active",
    "type": "dataset"
}

# Resource document
{
    "id": "uuid",
    "package_id": "parent_package_id",
    "name": "resource_name",
    "url": "resource_url",
    "description": "resource_description",
    "format": "CSV|S3|Kafka|...",
    "created": "ISO timestamp",
    "last_modified": "ISO timestamp"
}

# Organization document
{
    "id": "uuid",
    "name": "unique_org_name",
    "title": "Organization Title",
    "description": "org_description",
    "created": "ISO timestamp",
    "state": "active",
    "type": "organization"
}
```

#### Search Implementation
```python
def package_search(self, q: str = "*:*", fq: str = "", fq_list: Optional[List[str]] = None,
                  rows: int = 10, start: int = 0, 
                  sort: str = "score desc, metadata_modified desc",
                  **kwargs) -> Dict[str, Any]:
    # Text search using regex on title, notes, name
    if q and q != "*:*":
        query["$or"] = [
            {"title": {"$regex": re.escape(q), "$options": "i"}},
            {"notes": {"$regex": re.escape(q), "$options": "i"}},
            {"name": {"$regex": re.escape(q), "$options": "i"}},
        ]
    
    # Filter queries (field:value format)
    for filter_item in fq_list:
        field, value = filter_item.split(":", 1)
        query[field] = value.strip('"')
    
    # Execute with pagination and sorting
    return {"count": total_count, "results": results}
```

**Characteristics:**
- Uses MongoDB's native text search capabilities
- Simpler but less feature-rich than Solr
- Supports pagination and filtering
- Perfect for development/testing environments

---

## 2. Configuration & Factory Pattern

### Catalog Settings (`api/config/catalog_settings.py`)

Central configuration module that manages repository instantiation based on environment variables.

```python
class CatalogSettings(BaseSettings):
    # Backend selection for LOCAL catalog only
    local_catalog_backend: str = "ckan"  # "ckan" or "mongodb"
    
    # MongoDB configuration
    mongodb_connection_string: str = "mongodb://localhost:27017"
    mongodb_database: str = "ndp_local_catalog"
    
    @property
    def local_catalog(self) -> DataCatalogRepository:
        """Get repository for local catalog"""
        if self.local_catalog_backend == "mongodb":
            return MongoDBRepository(
                connection_string=self.mongodb_connection_string,
                database_name=self.mongodb_database,
            )
        else:  # "ckan"
            return CKANRepository(ckan_settings.ckan)
    
    @property
    def global_catalog(self) -> DataCatalogRepository:
        """Always returns CKAN for global catalog"""
        return CKANRepository(ckan_settings.ckan_global)
    
    @property
    def pre_catalog(self) -> DataCatalogRepository:
        """Always returns CKAN for PreCKAN staging"""
        return CKANRepository(ckan_settings.pre_ckan)
```

**Key Points:**
- **LOCAL catalog**: Can be CKAN or MongoDB (configurable via `LOCAL_CATALOG_BACKEND`)
- **GLOBAL catalog**: Always CKAN (global NDP instance, read-only)
- **PRE catalog**: Always CKAN (PreCKAN staging environment)
- Factory method pattern enables runtime backend selection

**Environment Variables:**
```bash
LOCAL_CATALOG_BACKEND=mongodb         # "ckan" or "mongodb"
MONGODB_CONNECTION_STRING=mongodb://localhost:27017
MONGODB_DATABASE=ndp_local_catalog
```

---

## 3. Service Layer

Services contain business logic and use repositories for data access. They abstract domain-specific operations.

### Pattern: Service → Repository

**Example: Search Datasource Service**

```python
# api/services/datasource_services/search_datasource.py

async def search_datasource(
    dataset_name: Optional[str] = None,
    dataset_title: Optional[str] = None,
    owner_org: Optional[str] = None,
    resource_format: Optional[str] = None,
    search_term: Optional[str] = None,
    server: Optional[str] = "local",  # "local", "global", or "pre_ckan"
) -> List[DataSourceResponse]:
    """
    Search datasources across different backends.
    """
    
    # Step 1: Get appropriate repository based on server parameter
    if server == "local":
        repository = catalog_settings.local_catalog  # Could be CKAN or MongoDB
    elif server == "global":
        repository = catalog_settings.global_catalog  # Always CKAN
    else:  # "pre_ckan"
        repository = catalog_settings.pre_catalog    # Always CKAN
    
    # Step 2: Build search query
    search_params = []
    if dataset_name:
        search_params.append(f"name:{dataset_name}")
    if dataset_title:
        search_params.append(f"title:{dataset_title}")
    # ... more conditions
    
    query_string = " AND ".join(search_params) if search_params else "*:*"
    
    # Step 3: Execute search (works with any backend)
    results = repository.package_search(
        q=query_string,
        fq_list=fq_list,
        rows=rows,
        start=start,
    )
    
    # Step 4: Transform results to domain model
    processed_results = []
    for dataset in results["results"]:
        # Filter resources based on criteria
        matching_resources = [
            res for res in dataset.get("resources", [])
            if (not resource_format or res.get("format").lower() == resource_format.lower())
        ]
        
        if matching_resources:
            processed_results.append(DataSourceResponse(
                id=dataset["id"],
                name=dataset["name"],
                title=dataset["title"],
                resources=resources_list,
            ))
    
    return processed_results
```

**Key Characteristics:**
- Receives `server` parameter to select catalog
- Uses `catalog_settings` to get appropriate repository
- Doesn't care about backend implementation
- Transforms CKAN/MongoDB response to domain model
- Single code path works for all backends

### Pattern: Organization Management Service

```python
# api/services/organization_services/create_organization.py

def create_organization(
    name: str,
    title: str,
    description: Optional[str] = None,
    server: Literal["local", "pre_ckan"] = "local",
) -> str:
    """Create organization in specified catalog."""
    
    # Get repository based on server
    if server == "pre_ckan":
        repository = catalog_settings.pre_catalog
    else:
        repository = catalog_settings.local_catalog  # CKAN or MongoDB
    
    # Call repository (same code works for both CKAN and MongoDB)
    organization = repository.organization_create(
        name=name,
        title=title,
        description=description
    )
    
    return organization["id"]
```

---

## 4. Routes/Endpoints Layer

Routes receive HTTP requests and delegate to services.

### Pattern: Route → Service → Repository

**Example: Create Dataset Endpoint**

```python
# api/routes/register_routes/post_general_dataset.py

@router.post("/dataset", status_code=status.HTTP_201_CREATED)
async def create_general_dataset_endpoint(
    data: GeneralDatasetRequest,
    server: Literal["local", "pre_ckan"] = Query("local"),
    user_info: Dict[str, Any] = Depends(get_user_for_write_operation),
):
    """
    Create a new general dataset.
    """
    try:
        # Step 1: Determine which repository to use
        if server == "pre_ckan":
            repository = CKANRepository(ckan_settings.pre_ckan)
        else:
            repository = catalog_settings.local_catalog  # Smart selection
        
        # Step 2: Delegate to service
        dataset_id = create_general_dataset(
            name=data.name,
            title=data.title,
            owner_org=data.owner_org,
            notes=data.notes,
            tags=data.tags,
            extras=data.extras,
            resources=resources,
            repository=repository,  # Pass repository to service
            user_info=user_info,
        )
        
        return {"id": dataset_id}
    
    except Exception as exc:
        # Handle errors consistently
        raise HTTPException(status_code=400, detail=str(exc))
```

**Request Flow:**
```
HTTP Request
    ↓
FastAPI Route Handler
    ↓
Get Repository (catalog_settings or explicit)
    ↓
Call Service with Repository
    ↓
Service Uses Repository Methods
    ↓
Repository Executes on CKAN or MongoDB
    ↓
Transform & Return Response
    ↓
HTTP Response
```

---

## 5. How Search Works Across Backends

### Unified Search Interface

Both CKAN and MongoDB implement `package_search()` with the same signature:

```python
def package_search(
    self,
    q: str = "*:*",              # Query string
    fq: str = "",                # Filter query (single string)
    fq_list: Optional[List[str]] = None,  # Filter list
    rows: int = 10,              # Results per page
    start: int = 0,              # Pagination offset
    sort: str = "...",           # Sort specification
    **kwargs
) -> Dict[str, Any]:
    """Returns: {"count": int, "results": [...]}"
```

### CKAN Search
```
Query String: "title:climate AND organization:research"
↓
Solr Full-Text Search Engine
↓
Results sorted by score + metadata_modified
↓
CKAN Response Format
```

### MongoDB Search
```
Query String: "title:climate AND organization:research"
↓
Parse to filters: {"title": "climate", "organization": "research"}
↓
MongoDB find() with regex on text fields
↓
Sort and paginate with MongoDB
↓
Transform to CKAN-compatible format
```

### Service Example: Search with Multiple Backends

```python
async def search_datasource(
    search_term: Optional[str] = None,
    server: Optional[str] = "local",
) -> List[DataSourceResponse]:
    
    # Get appropriate repository
    repository = {
        "local": catalog_settings.local_catalog,      # CKAN or MongoDB
        "global": catalog_settings.global_catalog,    # Always CKAN
        "pre_ckan": catalog_settings.pre_catalog      # Always CKAN
    }[server]
    
    # Same code works whether repository is CKAN or MongoDB
    results = repository.package_search(
        q=search_term,
        rows=1000
    )
    
    # Both backends return data in same format
    # Services don't need to care which backend is used
    for dataset in results["results"]:
        # Process consistently
        ...
```

---

## 6. Backend Comparison

| Feature | CKAN | MongoDB |
|---------|------|---------|
| **Use Case** | Production, complex queries | Development, quick prototyping |
| **Full-Text Search** | Solr-based, advanced | Regex-based, simple |
| **Scalability** | Distributed via Solr | Limited, single instance |
| **Query Language** | Solr syntax | MongoDB filters + regex |
| **Organization Sync** | Real-time | Via application |
| **Performance** | Excellent for complex search | Good for simple queries |
| **Configuration** | Required external Solr | Only MongoDB needed |
| **Best For** | Production deployments | Testing, development, demos |

---

## 7. Adding a New Backend

To add a new catalog backend (e.g., PostgreSQL, Elasticsearch):

### Step 1: Implement the Interface

```python
# api/repositories/custom_repository.py

from api.repositories.base_repository import DataCatalogRepository

class CustomRepository(DataCatalogRepository):
    """Your custom backend implementation."""
    
    def __init__(self, connection_config):
        self.config = connection_config
    
    def package_create(self, **kwargs) -> Dict[str, Any]:
        # Implement using your backend
        pass
    
    def package_search(self, q: str = "*:*", fq: str = "", ...) -> Dict[str, Any]:
        # Implement search in your backend
        # IMPORTANT: Return {"count": int, "results": [...]}
        pass
    
    # ... implement all abstract methods
```

### Step 2: Register in Factory

```python
# api/config/catalog_settings.py

@property
def local_catalog(self) -> DataCatalogRepository:
    backend = self.local_catalog_backend.lower()
    
    if backend == "mongodb":
        return MongoDBRepository(...)
    elif backend == "ckan":
        return CKANRepository(...)
    elif backend == "custom":  # NEW
        return CustomRepository(...)
    else:
        raise ValueError(f"Unsupported backend: {backend}")
```

### Step 3: Update Configuration

```bash
# .env
LOCAL_CATALOG_BACKEND=custom
CUSTOM_CONNECTION_STRING=your_config_here
```

### Step 4: No Service/Route Changes Needed!

All existing services and routes work automatically with the new backend because they use the repository interface.

---

## 8. Key Architectural Decisions

### Why Abstract the Repository?

1. **Flexibility**: Run MongoDB for development, CKAN for production
2. **Testing**: Mock repositories in unit tests without external services
3. **Migration**: Switch backends without code changes
4. **Future-proofing**: Easy to add new backends as requirements evolve

### Why Three Catalogs?

- **Local**: Mutable, organization's own data (CKAN or MongoDB)
- **Global**: Read-only, global NDP catalog (always CKAN)
- **PreCKAN**: Staging environment (always CKAN)

This separation ensures:
- Local catalog can be changed without affecting global
- Users can work in staging before promoting to global
- Different backends can be used for different purposes

### Why MongoDB for Local?

MongoDB is useful when:
- CKAN/Solr infrastructure isn't available
- Fast prototyping is needed
- Full-text search complexity isn't required
- Running in resource-constrained environments

---

## 9. Data Flow Examples

### Example 1: Create Dataset

```
Client: POST /dataset
    ↓
Route: create_general_dataset_endpoint
    ↓ (get repository)
catalog_settings.local_catalog  ← Selects CKAN or MongoDB
    ↓
Service: create_general_dataset
    ↓
Repository: package_create()
    ├─ If CKAN: ckan_instance.action.package_create()
    └─ If MongoDB: insert into packages collection
    ↓
Service: create_resource()
    ↓
Repository: resource_create()
    ├─ If CKAN: ckan_instance.action.resource_create()
    └─ If MongoDB: insert into resources collection
    ↓
Response: {"id": "dataset_uuid"}
```

### Example 2: Search Across Catalogs

```
Client: POST /search with server="local"
    ↓
Route: search_datasource
    ↓ (get repository)
catalog_settings.local_catalog
    ↓
Service: search_datasource
    ├─ Build query: "title:climate"
    ├─ Execute: repository.package_search(q="title:climate")
    │
    ├─ If CKAN backend:
    │  └─ Solr search with full-text scoring
    │
    └─ If MongoDB backend:
       └─ Regex search on title field
    ↓
Transform results to DataSourceResponse
    ↓
Return: List[DataSourceResponse]
```

---

## 10. File Structure Reference

```
api/
├── config/
│   ├── catalog_settings.py      # Repository factory
│   ├── ckan_settings.py         # CKAN configuration
│   └── ...
├── repositories/
│   ├── base_repository.py       # Abstract interface
│   ├── ckan_repository.py       # CKAN implementation
│   ├── mongodb_repository.py    # MongoDB implementation
│   └── __init__.py
├── services/
│   ├── datasource_services/
│   │   ├── search_datasource.py        # Uses repository
│   │   └── add_datasource.py           # Uses repository
│   ├── organization_services/
│   │   ├── create_organization.py      # Uses repository
│   │   ├── list_organization.py        # Uses repository
│   │   └── ...
│   ├── dataset_services/
│   │   ├── general_dataset.py          # Uses repository
│   │   └── ...
│   └── ...
└── routes/
    ├── register_routes/
    │   ├── post_general_dataset.py     # Gets repository, calls service
    │   ├── post_organization.py
    │   └── ...
    ├── search_routes/
    │   ├── post_search_datasource_route.py  # Gets repository, calls service
    │   └── ...
    ├── delete_routes/
    │   └── delete_dataset.py
    └── ...
```

---

## Summary

The **Repository Pattern** in NDP-EP provides:

1. **Abstraction**: Services and routes don't know about backend implementation
2. **Flexibility**: Switch between CKAN and MongoDB with a single environment variable
3. **Consistency**: All backends conform to the same interface
4. **Testability**: Easy to mock repositories in tests
5. **Extensibility**: Adding new backends requires only implementing the interface

The architecture enables:
- **Local catalog** to use CKAN (production) or MongoDB (development)
- **Global catalog** to always use CKAN (global NDP instance)
- **Services** to work transparently across any backend
- **Routes** to route requests without caring about implementation details

This design has proven essential for the project's flexibility and ease of deployment in different environments.

---

### docs/repository-quick-reference.md (10,370 bytes)

# Repository Pattern - Quick Reference Guide

## TL;DR - Key Points

1. **Abstract Interface** (`base_repository.py`): Defines what all backends must implement
2. **Two Implementations**: CKAN wrapper, MongoDB native implementation
3. **Factory Pattern** (`catalog_settings.py`): Creates the right repository based on config
4. **Single Code Path**: Services and routes work with any backend
5. **Three Catalogs**: Local (configurable), Global (always CKAN), PreCKAN (always CKAN)

---

## File Quick Map

```
api/repositories/
├── base_repository.py          ← Abstract interface (DataCatalogRepository)
├── ckan_repository.py          ← CKAN implementation
├── mongodb_repository.py       ← MongoDB implementation
└── __init__.py                 ← Exports all implementations

api/config/
└── catalog_settings.py         ← Factory (creates repositories)

api/services/
├── datasource_services/        ← Uses catalog_settings.local_catalog
├── organization_services/      ← Uses catalog_settings.local_catalog
└── dataset_services/           ← Uses provided repository

api/routes/
├── register_routes/
├── search_routes/
└── delete_routes/
```

---

## How to Use Repositories

### In a Service Function

```python
from api.config.catalog_settings import catalog_settings

def create_dataset(name, title, owner_org):
    # Get repository (CKAN or MongoDB, depending on config)
    repository = catalog_settings.local_catalog
    
    # Call repository method - works with any backend
    dataset = repository.package_create(
        name=name,
        title=title,
        owner_org=owner_org
    )
    
    return dataset["id"]
```

### Supporting Multiple Servers

```python
def search_datasets(query, server="local"):
    # Get appropriate repository
    if server == "global":
        repo = catalog_settings.global_catalog
    elif server == "pre_ckan":
        repo = catalog_settings.pre_catalog
    else:  # "local"
        repo = catalog_settings.local_catalog
    
    # Same code works for all
    return repo.package_search(q=query, rows=100)
```

### In a Route Handler

```python
from fastapi import APIRouter, Query
from api.config import catalog_settings, ckan_settings
from api.repositories import CKANRepository

@router.post("/dataset")
def create_dataset_endpoint(data, server: str = Query("local")):
    if server == "pre_ckan":
        repository = CKANRepository(ckan_settings.pre_ckan)
    else:
        repository = catalog_settings.local_catalog
    
    # Pass to service or use directly
    return create_dataset(
        name=data.name,
        title=data.title,
        owner_org=data.owner_org,
        repository=repository
    )
```

---

## Core Methods Reference

### Package (Dataset) Methods

```python
# Create
package = repo.package_create(
    name="my_dataset",
    title="My Dataset",
    owner_org="organization_id",
    notes="Description",
    extras=[{"key": "custom_field", "value": "value"}]
)
# Returns: {"id": "uuid", "name": "my_dataset", ...}

# Retrieve
package = repo.package_show(id="uuid_or_name")
# Returns: {"id": "uuid", ...}

# Update (full)
package = repo.package_update(
    id="uuid",
    title="New Title",
    notes="New Description"
)
# Returns: updated package dict

# Update (partial)
package = repo.package_patch(
    id="uuid",
    title="Only Update Title"
)
# Returns: updated package dict

# Delete
repo.package_delete(id="uuid")

# Search
results = repo.package_search(
    q="search term",           # Text query
    fq_list=["org:my_org"],    # Filters
    rows=50,                   # Page size
    start=0,                   # Offset
    sort="metadata_modified desc"
)
# Returns: {"count": 100, "results": [...]}
```

### Resource Methods

```python
# Create
resource = repo.resource_create(
    package_id="dataset_uuid",
    name="Resource Name",
    url="http://example.com/data.csv",
    format="CSV",
    description="Resource Description"
)
# Returns: {"id": "uuid", ...}

# Retrieve
resource = repo.resource_show(id="uuid")
# Returns: {"id": "uuid", ...}

# Delete
repo.resource_delete(id="uuid")
```

### Organization Methods

```python
# Create
org = repo.organization_create(
    name="my_org",
    title="My Organization",
    description="Org Description"
)
# Returns: {"id": "uuid", "name": "my_org", ...}

# Retrieve
org = repo.organization_show(id="uuid_or_name")
# Returns: {"id": "uuid", ...}

# List
orgs = repo.organization_list(all_fields=True)
# Returns: [{"id": "uuid", "name": "org1"}, ...]

# Delete
repo.organization_delete(id="uuid")
```

### Health Check

```python
is_healthy = repo.check_health()
# Returns: True or False
```

---

## Configuration

### Environment Variables

```bash
# Backend selection for LOCAL catalog
LOCAL_CATALOG_BACKEND=mongodb  # or "ckan"

# MongoDB configuration (if LOCAL_CATALOG_BACKEND=mongodb)
MONGODB_CONNECTION_STRING=mongodb://localhost:27017
MONGODB_DATABASE=ndp_local_catalog

# CKAN configuration (for all catalogs)
CKAN_SITE_URL=http://localhost:5000
CKAN_API_TOKEN=your_api_token
CKAN_GLOBAL_URL=http://global-ckan.example.com
CKAN_GLOBAL_API_TOKEN=token
PRE_CKAN_URL=http://pre-ckan.example.com
PRE_CKAN_API_TOKEN=token
```

### In Code

```python
from api.config.catalog_settings import catalog_settings

# Access repositories
local_repo = catalog_settings.local_catalog    # CKAN or MongoDB
global_repo = catalog_settings.global_catalog  # Always CKAN
pre_repo = catalog_settings.pre_catalog        # Always CKAN

# Get by name
repo = catalog_settings.get_repository_by_name("local")
```

---

## Common Patterns

### Pattern 1: Simple CRUD on Local Catalog

```python
def manage_dataset(dataset_id, title):
    repo = catalog_settings.local_catalog
    
    # Show
    dataset = repo.package_show(id=dataset_id)
    print(f"Current title: {dataset['title']}")
    
    # Update
    updated = repo.package_update(id=dataset_id, title=title)
    return updated["id"]
```

### Pattern 2: Search with Filters

```python
def search_org_datasets(org_name, format="csv"):
    repo = catalog_settings.local_catalog
    
    results = repo.package_search(
        q="*:*",  # All packages
        fq_list=[
            f"owner_org:{org_name}",
            f"resource_format:{format}"
        ],
        rows=100
    )
    
    return results["results"]
```

### Pattern 3: Create Dataset with Resources

```python
def create_full_dataset(dataset_data, resources_data):
    repo = catalog_settings.local_catalog
    
    # Create package
    package = repo.package_create(**dataset_data)
    package_id = package["id"]
    
    # Create resources
    for resource in resources_data:
        repo.resource_create(
            package_id=package_id,
            **resource
        )
    
    return package_id
```

### Pattern 4: Multi-Server Comparison

```python
def compare_datasets(query):
    results = {}
    
    for server_name in ["local", "global"]:
        repo = catalog_settings.get_repository_by_name(server_name)
        results[server_name] = repo.package_search(q=query, rows=10)
    
    return results
```

---

## Testing with Mock Repositories

```python
from unittest.mock import Mock
from api.repositories import DataCatalogRepository

# Create mock repository
mock_repo = Mock(spec=DataCatalogRepository)
mock_repo.package_search.return_value = {
    "count": 1,
    "results": [{"id": "test_id", "name": "test"}]
}

# Use in test
def test_search(mock_repo):
    results = search_datasets(query="test", repo=mock_repo)
    assert len(results["results"]) == 1
    mock_repo.package_search.assert_called_once()
```

---

## CKAN vs MongoDB Quick Comparison

| Feature | CKAN | MongoDB |
|---------|------|---------|
| **Search** | Solr full-text (fast) | Regex on fields (simple) |
| **Setup** | Requires Solr, PostgreSQL | Single DB connection |
| **For** | Production | Development/Testing |
| **Complex Queries** | Yes | Limited |
| **Scaling** | Yes (via Solr) | Limited |

---

## Troubleshooting

### "Organization does not exist" Error

**Cause**: Creating dataset with invalid `owner_org`

**Solution**: 
```python
# Ensure organization exists first
repo = catalog_settings.local_catalog
orgs = repo.organization_list()
assert "my_org" in orgs

# Then create dataset
repo.package_create(owner_org="my_org", ...)
```

### "Package with name X already exists"

**Cause**: Duplicate package name (names must be unique)

**Solution**:
```python
# Use UUID or timestamp in name
import uuid
package_name = f"dataset_{uuid.uuid4().hex[:8]}"
```

### Search returns no results with MongoDB

**Cause**: MongoDB regex search is simpler than Solr

**Solution**:
- Keep search terms simple
- Check exact field names
- Use `fq_list` for precise filtering

### "No scheme supplied" error

**Cause**: CKAN server not configured or unreachable

**Solution**:
```bash
# Check configuration
echo $CKAN_SITE_URL
# Should be http://... or https://...

# Check server is running
curl http://localhost:5000/api/3/action/status_show
```

---

## Adding a New Backend

1. **Create implementation**:
```python
# api/repositories/custom_repository.py
from api.repositories.base_repository import DataCatalogRepository

class CustomRepository(DataCatalogRepository):
    def package_create(self, **kwargs): ...
    def package_search(self, q, fq, ...): ...
    # ... all other methods
```

2. **Register in factory**:
```python
# api/config/catalog_settings.py
@property
def local_catalog(self) -> DataCatalogRepository:
    if self.local_catalog_backend == "custom":
        return CustomRepository(...)
    # ...
```

3. **Update .env**:
```bash
LOCAL_CATALOG_BACKEND=custom
```

4. **No other changes needed!** Services and routes work automatically.

---

## Key Takeaways

1. **Always get repository from `catalog_settings`** (except pre_ckan in routes)
2. **Same interface for all backends** - code is backend-agnostic
3. **Three catalogs serve different purposes** - don't mix them up
4. **Services should accept optional repository parameter** - enables testing
5. **Routes determine backend** - services use what they're given

---

For detailed information, see:
- `repository-pattern-architecture.md` - Full documentation
- `architecture-diagrams.md` - Visual references
- `adding-catalog-backends.md` - Extending with new backends

---

### docs/roles-and-permissions.md (10,048 bytes)

# Roles and permissions

This document explains the role model the Endpoint (EP) enforces, how a
user's roles travel from Keycloak into the JWT, and the exact steps to
grant access or introduce a new role. It is aimed at deployment
operators and at NDP support.

> TL;DR
> - The EP understands three tiers: **viewer** (read), **writer**
>   (modify catalog content) and **admin** (everything).
> - Roles are Keycloak **realm roles** named either `ndp_{tier}`
>   (platform-wide) or `group:{AFFINITIES_EP_UUID}:{tier}` (per-EP).
> - Assigning an existing tier to a user is **configuration only** (AAI
>   API or the Access Requests screen). A genuinely new permission level
>   requires an **Endpoint code change** (see
>   [Scenario B](#scenario-b-a-brand-new-permission-level)).

---

## 1. The three tiers

| Tier   | Can do | Implied lower tiers |
| ------ | ------ | ------------------- |
| viewer | Read / browse only (Search, view details). | — |
| writer | Everything a viewer can, plus create / edit / delete / publish catalog content. | viewer |
| admin  | Everything a writer can, plus manage access requests and admin-only pages. | writer, viewer |

The tiers are hierarchical: an **admin** does not also need the writer
and viewer roles, and a **writer** does not also need viewer. The
Endpoint resolves the highest tier the user holds.

**Strict default:** a user who is a member of the EP group but holds
**no** recognised role is treated as `none` and cannot perform any write
operation. They can still authenticate and read.

---

## 2. Role naming convention

Every recognised role is a Keycloak **realm role**. Two forms are
accepted for each tier:

| Tier   | Platform-wide (any EP) | Per-endpoint                                |
| ------ | ---------------------- | ------------------------------------------- |
| admin  | `ndp_admin`            | `group:{AFFINITIES_EP_UUID}:admin`          |
| writer | `ndp_writer`           | `group:{AFFINITIES_EP_UUID}:writer`         |
| viewer | `ndp_viewer`           | `group:{AFFINITIES_EP_UUID}:viewer`         |

`{AFFINITIES_EP_UUID}` is the value of the `AFFINITIES_EP_UUID`
environment variable for this deployment (it is also the name of the
endpoint's Keycloak group). Example for the dev EP whose UUID is
`96207a63-ee21-40c8-a492-31d680002330`:

```
group:96207a63-ee21-40c8-a492-31d680002330:writer
```

The legacy per-EP admin form `{AFFINITIES_EP_UUID}_admin` (no `group:`
prefix, underscore before `admin`) is **also** still accepted for admin,
for backwards compatibility. New deployments should prefer the
`group:{uuid}:admin` form.

> **Gotcha — "editor" vs "writer".** The AAI's own group model uses the
> default role names `admin` / `editor` / `viewer`. The Endpoint, by
> contrast, recognises `admin` / `writer` / `viewer`. Assigning the
> AAI's `editor` role does **not** grant write access on the EP — you
> must assign `writer`. Only `admin`, `writer` and `viewer` are mapped
> to EP permissions.

---

## 3. How the Endpoint sees roles

When a user authenticates, the AAI returns their realm roles in the
`roles` claim. `GET /user/info` exposes them, plus a derived
`effective_role` field that is the single value the UI and API gating
rely on:

```jsonc
GET /user/info
{
  "username": "raul",
  "sub": "6bfaa6c3-…",
  "roles": ["ndp_admin", "group:96207a63-…:admin", "default-roles-ndp"],
  "effective_role": "admin"      // admin | writer | viewer | none
}
```

The matching logic lives in
[`api/services/auth_services/authorization_service.py`](../api/services/auth_services/authorization_service.py):

- `is_admin`, `is_writer`, `is_viewer` — tier checks (each implies the
  lower tiers).
- `effective_role` — returns the highest tier as a string.
- `get_user_for_write_operation` — the FastAPI dependency guarding every
  `POST`/`PUT`/`PATCH`/`DELETE`; rejects callers below writer with `403`.
- `get_user_for_read_operation` — viewer-or-above dependency, available
  for future read endpoints.

Any realm role that does not match one of the six names in the table
above is carried in the token but **ignored** by the EP for permission
purposes (it will not raise `effective_role` above what the recognised
roles grant).

---

## 4. How roles reach the JWT (the "Keycloak client" question)

Roles are emitted into the token by a **protocol mapper** on the
Keycloak client (`oidc-usermodel-realm-role-mapper`, claim name
`roles`). This mapper is configured once, when the client is created by
the AAI (see `create_client` in the AAI's
`services/direct_keycloak/client_service.py`).

**You do not need to touch the Keycloak client when you add a new realm
role.** Because the mapper emits the user's realm roles wholesale, a
newly created `group:{uuid}:…` role appears in the token as soon as it
is assigned — no per-role client change, no client-scope edit.

This was verified empirically: creating a brand-new realm role
`group:{uuid}:probe-doc`, assigning it to a user, and re-reading
`GET /user/info` showed the role present in `roles` immediately, with no
client modification. (`effective_role` stayed `viewer` because
`probe-doc` is not a recognised tier — see
[Scenario B](#scenario-b-a-brand-new-permission-level).)

The only situation where the client *would* matter is a deployment whose
client was created **without** the realm-roles mapper, or one relying on
client-specific roles (`resource_access.{client}.roles`) instead of
realm roles. The standard AAI-provisioned client already includes the
mapper, so this is not a concern for normal deployments.

---

## 5. AAI API for role and group management

The AAI API (base URL = `AUTH_API_URL` host) is authoritative for group
and role writes; it wraps the Keycloak Admin API and enforces that the
caller is a group admin/editor. All calls take the caller's own Bearer
token.

| Action | Endpoint | Body | Notes |
| ------ | -------- | ---- | ----- |
| Create a custom role in a group | `POST /role/create` | `{groupName, roleName, users?:[]}` | `roleName` is the bare tier (e.g. `writer`); the AAI builds `group:{groupName}:{roleName}`. The names `admin`/`editor`/`viewer` are reserved and cannot be created. Caller must be group editor. |
| Assign a role to user(s) | `POST /role/assign` | `{groupName, roleName, username \| users:[]}` | `roleName` is the **bare** tier — do **not** pass the fully-qualified `group:…:writer` string (it double-prefixes). Assigning `admin` requires the caller to be a group admin. |
| Remove a role from user(s) | `DELETE /role/remove` | `{groupName, roleName, username \| users:[]}` | |
| Delete a custom role | `DELETE /role/delete` | `{groupName, roleName}` | Cannot delete `admin`/`editor`/`viewer`. Caller must be group admin. |
| Add user to a group | `POST /group/add-user` | `{group_name, username}` | The AAI assigns the `viewer` role automatically on join. |
| List group members | `GET /group/members?group_name=…` | — | |

The Endpoint's own thin wrapper around these lives in
[`api/services/auth_services/aai_client.py`](../api/services/auth_services/aai_client.py)
(`assign_role`, `add_user_to_group`, `list_group_members`).

---

## 6. Common tasks

### Grant an existing tier to a user

**Via the UI (preferred).** When a user requests access, an admin
approves the request on the **Access Requests** page and picks the tier
(Viewer / Writer / Admin). This adds the user to the EP group and
assigns the chosen per-EP role.

**Via the AAI API.** Add the user to the group (this gives them
`viewer`), then assign a higher tier if needed:

```bash
TOKEN=$(curl -s -X POST "$AAI/user/login" \
  -H 'Content-Type: application/json' \
  -d '{"username":"<admin>","password":"<pass>"}' | jq -r .access_token)

# join the group (auto-assigns viewer)
curl -s -X POST "$AAI/group/add-user" \
  -H "Authorization: Bearer $TOKEN" -H 'Content-Type: application/json' \
  -d '{"group_name":"<EP_UUID>","username":"<user>"}'

# upgrade to writer (bare tier name + groupName)
curl -s -X POST "$AAI/role/assign" \
  -H "Authorization: Bearer $TOKEN" -H 'Content-Type: application/json' \
  -d '{"groupName":"<EP_UUID>","roleName":"writer","username":"<user>"}'
```

The user must **re-login** afterwards: their old JWT was issued before
the grant and will not contain the new role until a fresh token is
minted.

### Scenario A: reuse an existing tier in another group

Nothing in the Endpoint changes. Create/assign the
`group:{OTHER_UUID}:viewer|writer|admin` roles for that group. The
Endpoint only ever evaluates roles for **its own** `AFFINITIES_EP_UUID`,
so per-group roles for other endpoints are naturally isolated.

### Scenario B: a brand-new permission level

If you need a tier that is **not** viewer/writer/admin (say, a
`publisher` that can publish but not delete), two things are required:

1. **Create the role** in Keycloak / via the AAI as usual
   (`group:{uuid}:publisher`). It will appear in the token automatically
   (Section 4).
2. **Teach the Endpoint about it** — a code change in
   [`authorization_service.py`](../api/services/auth_services/authorization_service.py):
   add a matcher (e.g. `is_publisher`), fold it into `effective_role`,
   and gate the relevant routes/dependencies. Without this step the role
   rides in the token but grants nothing (`effective_role` ignores it).

Step 2 is the part that "request to NDP support" covers when an operator
cannot change the Endpoint code themselves.

---

## 7. When to request NDP support

Open a request with NDP support when you need something that is not a
plain assignment of an existing tier:

- A new permission level that the Endpoint must enforce (Scenario B).
- Changes to the Keycloak client itself (new protocol mappers, switching
  to client roles) — only relevant for non-standard clients (Section 4).
- Realm-level changes you do not have admin rights for.

For everything else — granting viewer/writer/admin to a user, creating a
per-group custom role, listing members — use the Access Requests screen
or the AAI API directly.

---


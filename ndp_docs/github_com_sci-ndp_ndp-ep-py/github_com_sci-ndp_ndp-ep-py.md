# ndp-ep-py

## Documentation Files

### README.md (6,258 bytes)

# ndp-ep

[![CI](https://github.com/sci-ndp/ndp-ep-py/workflows/CI/badge.svg)](https://github.com/sci-ndp/ndp-ep-py/actions)
[![codecov](https://codecov.io/gh/sci-ndp/ndp-ep-py/branch/main/graph/badge.svg)](https://codecov.io/gh/sci-ndp/ndp-ep-py)
[![PyPI version](https://badge.fury.io/py/ndp-ep.svg)](https://badge.fury.io/py/ndp-ep)
[![Python versions](https://img.shields.io/pypi/pyversions/ndp-ep.svg)](https://pypi.org/project/ndp-ep/)

A Python client library for interacting with the NDP EP API. This library provides a simple and intuitive interface for managing datasets, organizations, resources, and services through the API.

## Features

- **Complete API Coverage**: Support for all API endpoints including Kafka topics, S3 resources, URL resources, organizations, and services
- **Authentication**: Token-based and username/password authentication
- **Search Functionality**: Advanced search capabilities across datasets and resources
- **Error Handling**: Comprehensive error handling with meaningful error messages
- **Type Hints**: Full type hint support for better IDE integration
- **Testing**: Extensive test coverage (>70%) with unit and integration tests

## Installation

```bash
pip install ndp-ep
```

## Quick Start

```python
from ndp_ep import APIClient

# Initialize client with token
client = APIClient(
    base_url="https://your-api-endpoint.com",
    token="your-access-token"
)

# List organizations
organizations = client.list_organizations()
print(organizations)

# Search datasets
results = client.search_datasets(
    terms=["climate", "temperature"],
    server="global"
)

# Register a new organization
org_data = {
    "name": "my_organization",
    "title": "My Organization",
    "description": "A sample organization"
}
response = client.register_organization(org_data)

# Register a service
service_data = {
    "service_name": "user_auth_api",
    "service_title": "User Authentication API",
    "owner_org": "services",
    "service_url": "https://api.example.com/auth",
    "service_type": "API",
    "notes": "RESTful API for user authentication"
}
response = client.register_service(service_data)

# S3 Management Examples
buckets = client.list_buckets()
client.create_bucket("my-data-bucket")

# Upload and download files
with open("data.csv", "rb") as f:
    client.upload_object("my-data-bucket", "datasets/data.csv", f)

file_content = client.download_object("my-data-bucket", "datasets/data.csv")

# Generate presigned URLs for secure file sharing
upload_url = client.generate_presigned_upload_url("my-data-bucket", "new-file.txt")
download_url = client.generate_presigned_download_url("my-data-bucket", "data.csv")
```

### More Examples

For comprehensive examples and use cases, check out our:
- **📓 [Quick start](docs/source/tutorials/getting_started.ipynb)** 
- **📓 [Bulk Resource Management](docs/source/tutorials/bulk_resource_management.ipynb)** 

## API Coverage

### Authentication
- Token-based authentication
- Username/password authentication

### Organizations
- `list_organizations()` - List all organizations
- `register_organization()` - Create new organization
- `delete_organization()` - Delete organization

### Datasets and Resources
- `search_datasets()` - Search datasets with advanced filters
- `advanced_search()` - Advanced search with POST method
- `register_url()` - Register URL resources
- `register_s3_link()` - Register S3 resources
- `register_kafka_topic()` - Register Kafka topics
- `register_general_dataset()` - Register general datasets
- `update_url_resource()` - Update URL resources
- `update_s3_resource()` - Update S3 resources
- `update_kafka_topic()` - Update Kafka topics
- `update_general_dataset()` - Update general datasets (PUT)
- `patch_general_dataset()` - Partially update general datasets (PATCH)
- `delete_resource_by_id()` - Delete resource by ID
- `delete_resource_by_name()` - Delete resource by name

### Services
- `register_service()` - Register new services

### S3 Management
- `list_buckets()` - List all S3 buckets
- `create_bucket()` - Create new S3 bucket
- `get_bucket_info()` - Get S3 bucket information
- `delete_bucket()` - Delete S3 bucket
- `list_objects()` - List objects in S3 bucket
- `upload_object()` - Upload object to S3 bucket
- `download_object()` - Download object from S3 bucket
- `delete_object()` - Delete object from S3 bucket
- `get_object_metadata()` - Get S3 object metadata
- `generate_presigned_upload_url()` - Generate presigned upload URL
- `generate_presigned_download_url()` - Generate presigned download URL

### System Information
- `get_kafka_details()` - Get Kafka connection details
- `get_system_status()` - Check system status
- `get_system_metrics()` - Get system metrics
- `get_jupyter_details()` - Get Jupyter connection details

## Development

### Setting up development environment

```bash
# Clone the repository
git clone https://github.com/sci-ndp/ndp-ep-py.git
cd ndp-ep-py

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -e .
pip install -r requirements-dev.txt
```

### Running tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=ndp_ep --cov-report=html

# Run specific test categories
pytest -m unit          # Unit tests only
pytest -m integration   # Integration tests only
```

### Code formatting and linting

```bash
# Format code
black ndp_ep tests

# Lint code
flake8 ndp_ep

# Type checking
mypy ndp_ep
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests for your changes
5. Ensure all tests pass and coverage is maintained
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Changelog

### v0.1.0
- Initial release
- Complete API coverage for all endpoints
- Authentication support (token and username/password)
- Search functionality
- Resource management (URL, S3, Kafka)
- Organization management
- Comprehensive testing suite

---

### docs/README.md (8,811 bytes)

# NDP EP Documentation

This directory contains the complete documentation for the ndp-ep Python client library, built with Sphinx.

## 📁 Structure

```
docs/
├── source/                     # Sphinx source files
│   ├── conf.py                # Sphinx configuration
│   ├── index.rst              # Main documentation page
│   ├── installation.rst       # Installation guide
│   ├── quickstart.rst         # Quick start guide
│   ├── authentication.rst     # Authentication guide
│   ├── api_reference.rst      # Complete API reference
│   ├── user_guide/           # Detailed user guides
│   │   ├── organizations.rst  # Working with organizations
│   │   ├── resources.rst      # Managing resources
│   │   ├── search.rst         # Search functionality
│   │   └── system_info.rst    # System information
│   ├── tutorials/            # Interactive tutorials
│   │   ├── getting_started.ipynb        # Main tutorial
│   │   ├── data_management_workflow.ipynb
│   │   └── advanced_search.ipynb
│   ├── _static/              # Static files (CSS, images)
│   └── _templates/           # Custom templates
├── build/                    # Generated documentation (gitignored)
├── requirements.txt          # Documentation dependencies
├── Makefile                 # Build commands
└── README.md               # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip or conda

### Installation

1. **Install documentation dependencies:**

   ```bash
   cd docs
   pip install -r requirements.txt
   ```

   Or using the Makefile:

   ```bash
   make install
   ```

2. **Build the documentation:**

   ```bash
   make html
   ```

3. **View the documentation:**

   ```bash
   make serve
   ```

   This will build the docs and open them in your default browser.

## 🔧 Building Documentation

### Available Make Targets

```bash
# Install dependencies
make install

# Build HTML documentation
make html

# Build and open in browser
make serve

# Clean build directory
make clean

# Live reload during development
make live
```

### Manual Build

If you prefer not to use Make:

```bash
# Install dependencies
pip install -r requirements.txt

# Build documentation
sphinx-build -M html source build

# Clean build
sphinx-build -M clean source build
```

## 📝 Writing Documentation

### Adding New Pages

1. Create a new `.rst` file in the appropriate directory:
   - `source/` for main pages
   - `source/user_guide/` for user guides
   - `source/tutorials/` for tutorials

2. Add the file to the appropriate `toctree` directive in `index.rst` or parent page

3. Rebuild the documentation

### RST Syntax

The documentation uses reStructuredText (RST) format. Key syntax:

```rst
Page Title
==========

Section
-------

Subsection
~~~~~~~~~~

**Bold text**
*Italic text*
``Code text``

.. code-block:: python

   # Python code example
   from ndp_ep import APIClient
   client = APIClient(base_url="...")

.. note::
   This is a note box

.. warning::
   This is a warning box

`Link text <https://example.com>`_
```

### Code Examples

Always include working code examples:

```rst
.. code-block:: python

   from ndp_ep import APIClient

   # Initialize client
   client = APIClient(
       base_url="http://155.101.6.191:8003",
       token="your-token"
   )

   # List organizations
   organizations = client.list_organizations()
   print(f"Found {len(organizations)} organizations")
```

### API Documentation

API documentation is auto-generated from docstrings. To add new API documentation:

1. Ensure your Python code has proper docstrings
2. Add autoclass/automodule directives in `api_reference.rst`:

```rst
.. autoclass:: YourNewClass
   :members:
   :show-inheritance:
```

## 📓 Jupyter Notebooks

### Creating Tutorial Notebooks

1. Create notebooks in `source/tutorials/`
2. Include Colab and Binder badges at the top:

```markdown
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sci-ndp/ndp-ep-py/blob/main/docs/source/tutorials/your_notebook.ipynb)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sci-ndp/ndp-ep-py/main?filepath=docs%2Fsource%2Ftutorials%2Fyour_notebook.ipynb)
```

3. Test notebooks work in both Colab and Binder
4. Add notebook to `index.rst` toctree

### Notebook Guidelines

- Start with library installation: `!pip install ndp-ep`
- Include comprehensive examples and explanations
- Add error handling and troubleshooting
- Test with and without authentication
- Use markdown cells for explanations

## 🎨 Customization

### Theme Configuration

The documentation uses the Read the Docs theme. Customize in `source/conf.py`:

```python
html_theme_options = {
    'canonical_url': '',
    'analytics_id': '',
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'style_nav_header_background': '#2980B9',
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}
```

### Custom CSS

Add custom styles in `source/_static/custom.css`:

```css
/* Custom styles */
.wy-nav-content {
    max-width: 1200px;
}

.highlight-python .highlight {
    background: #f8f8f8;
}
```

### Custom Templates

Override templates by creating files in `source/_templates/`:

- `layout.html` - Main layout
- `navigation.html` - Navigation menu
- `searchbox.html` - Search box

## 🚀 Deployment

### GitHub Pages

To deploy to GitHub Pages:

1. Build documentation: `make html`
2. Copy `build/html/*` to your gh-pages branch
3. Push to GitHub

### Read the Docs

1. Connect your GitHub repository to Read the Docs
2. Configure build settings:
   - Python version: 3.8+
   - Requirements file: `docs/requirements.txt`
   - Documentation type: Sphinx

### Manual Deployment

Deploy to any web server by uploading the `build/html/` directory.

## 🔍 Troubleshooting

### Common Issues

**"No module named 'ndp_ep'"**

Install the package in development mode:

```bash
pip install -e .
```

**"Extension error"**

Check that all Sphinx extensions are installed:

```bash
pip install -r docs/requirements.txt
```

**"Notebook execution failed"**

Notebooks are set to `nbsphinx_execute = 'never'` by default. To execute during build:

```python
# In conf.py
nbsphinx_execute = 'always'
```

**"Theme not found"**

Install the theme:

```bash
pip install sphinx-rtd-theme
```

### Build Debugging

Enable verbose output:

```bash
sphinx-build -v -M html source build
```

Check for warnings:

```bash
sphinx-build -W -M html source build
```

### Live Development

For continuous rebuilding during development:

```bash
pip install sphinx-autobuild
sphinx-autobuild source build/html --open-browser
```

## 🤝 Contributing

### Documentation Guidelines

1. **Clarity**: Write for beginners and experts alike
2. **Examples**: Include working code examples
3. **Testing**: Test all examples and links
4. **Consistency**: Use consistent formatting and style
5. **Updates**: Keep documentation in sync with code changes

### Review Process

1. Create documentation changes in a feature branch
2. Test builds locally: `make html`
3. Test notebooks in Colab/Binder
4. Submit PR with documentation changes
5. Ensure CI passes and documentation builds

### Style Guide

- Use present tense: "The client connects..." not "The client will connect..."
- Use active voice: "You can configure..." not "Configuration can be..."
- Use "you" to address the reader
- Keep sentences concise and clear
- Use code examples liberally
- Add screenshots for UI elements (if any)

## 📊 Analytics

### Tracking Documentation Usage

If you want to track documentation usage, add Google Analytics:

```python
# In conf.py
html_theme_options = {
    'analytics_id': 'G-XXXXXXXXXX',  # Your GA4 tracking ID
}
```

### Feedback Collection

Consider adding feedback mechanisms:

- GitHub Issues for documentation bugs
- Discussion forums for questions
- Survey links for user feedback

## 🆘 Getting Help

If you need help with the documentation:

1. **Check existing issues**: [GitHub Issues](https://github.com/sci-ndp/ndp-ep-py/issues)
2. **Sphinx documentation**: [Sphinx Docs](https://www.sphinx-doc.org/)
3. **RST guide**: [RST Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
4. **RTD theme docs**: [Read the Docs Theme](https://sphinx-rtd-theme.readthedocs.io/)

---

## 📄 License

This documentation is part of the ndp-ep project and is licensed under the MIT License.

---

*Last updated: 2025-01-06*

---

### CHANGELOG.md (4,408 bytes)

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.8.0] - 2026-04-11

### Changed
- Version check no longer emits a `UserWarning` when the `/status/` endpoint does not return version information. Instead, an informational message is logged via Python's `logging` module, reducing noise for users whose API server does not yet expose version data.

### Fixed
- Handle `None` response from `set_environment` method

## [0.6.0] - 2026-01-10

### Added
- Remote execution (rexec) support using scidx-rexec
  - `setup_rexec_environment(requirements, token)` - Provision remote execution environments
  - `remote_func` decorator re-exported from scidx-rexec
- Optional dependency `[rexec]` for remote execution features
- PyJWT dependency for token handling

## [0.5.0] - 2025-12-22

### Fixed
- `_check_api_version()` now uses authenticated session for API version check
- Fixes compatibility with API deployments that require authentication for `/status/` endpoint

## [0.4.0] - 2025-12-08

### Added
- Resource operations by ID without requiring dataset_id:
  - `get_resource(resource_id)` - GET /resource/{id}
  - `patch_resource(resource_id, ...)` - PATCH /resource/{id}
  - `delete_resource(resource_id)` - DELETE /resource/{id}
  - `search_resources(q, name, url, format, ...)` - GET /resources/search
- Resource Management tutorial (`docs/source/tutorials/resource_management.ipynb`)

### Features
- Search resources by query, name, url, format, or description
- Pagination support with limit/offset for resource search
- Results include parent dataset context (dataset_id, dataset_name, dataset_title)

## [0.3.0] - 2025-12-01

### Added
- Pelican Federation methods for browsing and downloading from external federations:
  - `list_federations()` - GET /pelican/federations
  - `browse_pelican(path, federation, detail)` - GET /pelican/browse
  - `get_pelican_info(path, federation)` - GET /pelican/info
  - `download_pelican(path, federation, stream)` - GET /pelican/download
  - `import_pelican_metadata(pelican_url, package_id, ...)` - POST /pelican/import-metadata
- Pelican Federation tutorial (`docs/source/tutorials/pelican_federation.ipynb`)

### Fixed
- `create_bucket()` now uses correct API field name (`name` instead of `bucket_name`)

## [0.1.0] - 2025-07-03

### Added
- Initial release of ndp-ep Python client library
- Complete API coverage for all NDP EP endpoints
- Authentication support (token-based and username/password)
- Organization management (create, list, delete)
- Resource registration for multiple types:
  - Kafka topics
  - S3 resources  
  - URL resources
  - Services
  - General datasets
- Resource update functionality (PUT and PATCH operations)
- Resource deletion (by ID and name)
- Search functionality (simple and advanced)
- System information retrieval:
  - System status and health checks
  - System metrics
  - Kafka connection details
  - Jupyter connection details
- Comprehensive error handling with meaningful error messages
- Type hints throughout the codebase
- Extensive test suite with 89% code coverage
- CI/CD pipeline with GitHub Actions
- Automatic PyPI publishing on main branch
- Complete documentation and examples

### Technical Details
- Python 3.8+ support
- Built with requests library for HTTP operations
- Follows PEP 8 coding standards
- Modular architecture with mixin classes
- Comprehensive error handling and validation
- Mock-based testing with requests-mock
- Coverage reporting with pytest-cov
- Code formatting with black
- Linting with flake8
- Type checking with mypy

### API Endpoints Covered
- `/token` - Authentication
- `/organization` - Organization management
- `/kafka` - Kafka topic management
- `/s3` - S3 resource management
- `/url` - URL resource management
- `/services` - Service registration
- `/dataset` - General dataset management
- `/search` - Search functionality
- `/status/*` - System information
- `/resource` - Resource deletion

### Dependencies
- requests >= 2.25.0
- urllib3 >= 1.26.0

### Development Dependencies
- pytest >= 7.0.0
- pytest-cov >= 4.0.0
- pytest-mock >= 3.10.0
- requests-mock >= 1.9.0
- black >= 22.0.0
- flake8 >= 5.0.0
- mypy >= 1.0.0
- twine >= 4.0.0
- build >= 0.10.0

---

### LICENSE (1,067 bytes)

MIT License

Copyright (c) 2024 NDP EP Team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

### docs/requirements.txt (291 bytes)

# Core Sphinx and theme
sphinx>=5.0.0,<9.0.0
sphinx-rtd-theme>=1.2.0

# Optional extensions (commented out to avoid dependency issues)
# sphinx-autodoc-typehints>=1.19.0
# sphinx-copybutton>=0.5.0

# Ensure we have the base dependencies from the main package
requests>=2.25.0
urllib3>=1.26.0

---

### docs/source/requirements.txt (180 bytes)

sphinx>=5.0.0
sphinx-rtd-theme>=1.2.0
nbsphinx>=0.8.0
myst-parser>=0.18.0
sphinx-autodoc-typehints>=1.19.0
sphinx-copybutton>=0.5.0
ipykernel>=6.0.0
jupyter>=1.0.0
requests>=2.25.0

---

### requirements.txt (154 bytes)

 requests>=2.25.0
urllib3>=1.26.0
PyJWT>=2.8.0

# Jupyter notebook dependencies for tutorial execution
jupyter>=1.1.0
ipykernel>=6.30.0
nbconvert>=7.16.0

---

### docs/source/api_reference.rst (3,594 bytes)

API Reference
=============

This section provides detailed documentation for all classes and methods in the ndp-ep library.

.. currentmodule:: ndp_ep

Main Client
-----------

.. autoclass:: APIClient
   :members:
   :inherited-members:
   :show-inheritance:

The main APIClient class provides access to all NDP EP functionality.

Example usage::

    from ndp_ep import APIClient
    
    client = APIClient(
        base_url="http://155.101.6.191:8003",
        token="your-token"
    )

Base Classes
------------

.. autoclass:: APIClientBase
   :members:
   :show-inheritance:

Organization Management
-----------------------

.. autoclass:: ndp_ep.register_organization_method.APIClientOrganizationRegister
   :members:
   :show-inheritance:

.. autoclass:: ndp_ep.list_organization_method.APIClientOrganizationList
   :members:
   :show-inheritance:

.. autoclass:: ndp_ep.delete_organization_method.APIClientOrganizationDelete
   :members:
   :show-inheritance:

Resource Registration
---------------------

.. autoclass:: ndp_ep.register_kafka_method.APIClientKafkaRegister
   :members:
   :show-inheritance:

.. autoclass:: ndp_ep.register_s3_method.APIClientS3Register
   :members:
   :show-inheritance:

.. autoclass:: ndp_ep.register_url_method.APIClientURLRegister
   :members:
   :show-inheritance:

.. autoclass:: ndp_ep.register_service_method.APIClientServiceRegister
   :members:
   :show-inheritance:

.. autoclass:: ndp_ep.register_dataset_method.APIClientDatasetRegister
   :members:
   :show-inheritance:

Resource Updates
----------------

.. autoclass:: ndp_ep.update_kafka_method.APIClientKafkaUpdate
   :members:
   :show-inheritance:

.. autoclass:: ndp_ep.update_s3_method.APIClientS3Update
   :members:
   :show-inheritance:

.. autoclass:: ndp_ep.update_url_method.APIClientURLUpdate
   :members:
   :show-inheritance:

.. autoclass:: ndp_ep.update_dataset_method.APIClientDatasetUpdate
   :members:
   :show-inheritance:

Search Functionality
--------------------

.. autoclass:: ndp_ep.search_method.APIClientSearch
   :members:
   :show-inheritance:

System Information
------------------

.. autoclass:: ndp_ep.get_kafka_details_method.APIClientKafkaDetails
   :members:
   :show-inheritance:

.. autoclass:: ndp_ep.get_system_status_method.APIClientSystemStatus
   :members:
   :show-inheritance:

Constants and Version
---------------------

.. autodata:: ndp_ep.__version__

.. autodata:: ndp_ep.__description__

Common Parameters
-----------------

Server Options
~~~~~~~~~~~~~~

Most methods accept a ``server`` parameter with these options:

- ``"local"``: Local CKAN instance
- ``"global"``: Global CKAN instance (default for searches)
- ``"pre_ckan"``: Pre-production CKAN instance

Authentication
~~~~~~~~~~~~~~

The client supports two authentication methods:

**Token-based (recommended)**::

    client = APIClient(base_url="...", token="your-token")

**Username/Password**::

    client = APIClient(base_url="...", username="user", password="pass")

Error Handling
--------------

All methods may raise ``ValueError`` with descriptive error messages for:

- Authentication failures
- Network connectivity issues  
- API validation errors
- Resource not found errors
- Server configuration errors

Example error handling::

    try:
        result = client.register_organization(org_data)
    except ValueError as e:
        if "already exists" in str(e):
            print("Organization name is taken")
        elif "Authentication failed" in str(e):
            print("Check your credentials")
        else:
            print(f"API error: {e}")

---

### docs/source/authentication.rst (8,686 bytes)

Authentication Guide
====================

The ndp-ep library supports multiple authentication methods to connect to the NDP EP API. This guide covers all available options and best practices.

Getting Your Credentials
-------------------------

Before you can authenticate, you need to obtain credentials from the National Data Platform:

1. Visit https://nationaldataplatform.org/
2. Create an account or log in to your existing account
3. Navigate to your user profile or settings
4. Find the API token section
5. Generate or copy your API token

.. note::
   Keep your API token secure and never share it publicly or commit it to version control.

Authentication Methods
----------------------

Token-Based Authentication (Recommended)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The preferred method for authentication is using an API token:

.. code-block:: python

   from ndp_ep import APIClient

   client = APIClient(
       base_url="http://155.101.6.191:8003",
       token="your-api-token-here"
   )

**Advantages:**
- More secure than username/password
- Can be easily rotated
- Doesn't require storing passwords
- Better for automated scripts

Username/Password Authentication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can also authenticate using your username and password:

.. code-block:: python

   from ndp_ep import APIClient

   client = APIClient(
       base_url="http://155.101.6.191:8003",
       username="your-username",
       password="your-password"
   )

**When to use:**
- For interactive sessions
- When tokens are not available
- For testing purposes

.. warning::
   Username/password authentication requires the client to obtain a token from the server on initialization. This adds a network call during setup.

Environment Variables (Best Practice)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For production applications, store credentials in environment variables:

.. code-block:: python

   import os
   from ndp_ep import APIClient

   client = APIClient(
       base_url=os.getenv("NDP_API_URL", "http://155.101.6.191:8003"),
       token=os.getenv("NDP_API_TOKEN")
   )

Set your environment variables:

.. code-block:: bash

   # Linux/macOS
   export NDP_API_URL="http://155.101.6.191:8003"
   export NDP_API_TOKEN="your-token-here"

   # Windows
   set NDP_API_URL=http://155.101.6.191:8003
   set NDP_API_TOKEN=your-token-here

Using .env Files
~~~~~~~~~~~~~~~~

For local development, use a `.env` file with python-dotenv:

.. code-block:: bash

   pip install python-dotenv

Create a `.env` file:

.. code-block:: text

   NDP_API_URL=http://155.101.6.191:8003
   NDP_API_TOKEN=your-token-here

Load in your Python code:

.. code-block:: python

   import os
   from dotenv import load_dotenv
   from ndp_ep import APIClient

   # Load environment variables from .env file
   load_dotenv()

   client = APIClient(
       base_url=os.getenv("NDP_API_URL"),
       token=os.getenv("NDP_API_TOKEN")
   )

No Authentication (Limited Access)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some endpoints may work without authentication:

.. code-block:: python

   from ndp_ep import APIClient

   # This will work for public read-only endpoints
   client = APIClient(base_url="http://155.101.6.191:8003")

   # You can still perform searches and view public data
   results = client.search_datasets(["climate"], server="global")

Security Best Practices
------------------------

Token Management
~~~~~~~~~~~~~~~~

1. **Rotate tokens regularly**: Change your API tokens periodically
2. **Use different tokens for different environments**: Separate tokens for dev, staging, and production
3. **Revoke unused tokens**: Remove tokens that are no longer needed
4. **Monitor token usage**: Check for unauthorized access

Secure Storage
~~~~~~~~~~~~~~

.. code-block:: python

   # ✅ Good: Using environment variables
   token = os.getenv("NDP_API_TOKEN")
   
   # ✅ Good: Using secure configuration management
   from your_config_manager import get_secret
   token = get_secret("ndp_api_token")
   
   # ❌ Bad: Hardcoding in source code
   token = "abc123def456"  # Never do this!
   
   # ❌ Bad: Storing in plain text files
   with open("token.txt") as f:
       token = f.read()  # Avoid this

Network Security
~~~~~~~~~~~~~~~~

1. **Use HTTPS in production**: Always use secure connections
2. **Validate certificates**: Don't disable SSL verification
3. **Use VPNs for sensitive data**: Consider additional network security
4. **Monitor API access**: Log and monitor API usage

Error Handling
--------------

Handle authentication errors gracefully:

.. code-block:: python

   from ndp_ep import APIClient

   def create_authenticated_client():
       """Create an authenticated client with error handling."""
       try:
           client = APIClient(
               base_url=os.getenv("NDP_API_URL"),
               token=os.getenv("NDP_API_TOKEN")
           )
           
           # Test the connection
           status = client.get_system_status()
           print("✅ Authentication successful")
           return client
           
       except ValueError as e:
           if "Invalid username or password" in str(e):
               print("❌ Authentication failed: Invalid credentials")
           elif "No access token received" in str(e):
               print("❌ Authentication failed: No token received")
           else:
               print(f"❌ Authentication error: {e}")
           return None
           
       except ConnectionError:
           print("❌ Network error: Could not connect to API")
           return None
           
       except Exception as e:
           print(f"❌ Unexpected error: {e}")
           return None

   # Usage
   client = create_authenticated_client()
   if client:
       # Proceed with API operations
       pass

Troubleshooting
---------------

Common Authentication Issues
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**"Authentication failed: Invalid username or password"**

- Check your username and password are correct
- Verify your account is active on the NDP platform
- Try logging in to the web interface first

**"Failed to connect to the API"**

- Check the API URL is correct and accessible
- Verify network connectivity
- Check firewall settings

**"No access token received"**

- The server response didn't include a token
- Check if your account has API access enabled
- Contact support if the issue persists

**Token-related errors**

- Verify the token is valid and not expired
- Check the token has the correct permissions
- Try generating a new token

Testing Authentication
~~~~~~~~~~~~~~~~~~~~~~

You can test your authentication setup:

.. code-block:: python

   def test_authentication():
       """Test different authentication methods."""
       
       # Test 1: Token authentication
       try:
           client = APIClient(
               base_url="http://155.101.6.191:8003",
               token=os.getenv("NDP_API_TOKEN")
           )
           client.get_system_status()
           print("✅ Token authentication: SUCCESS")
       except Exception as e:
           print(f"❌ Token authentication: FAILED - {e}")
       
       # Test 2: Search without authentication
       try:
           client = APIClient(base_url="http://155.101.6.191:8003")
           results = client.search_datasets(["test"], server="global")
           print(f"✅ Public access: SUCCESS - Found {len(results)} results")
       except Exception as e:
           print(f"❌ Public access: FAILED - {e}")

   test_authentication()

Configuration Examples
----------------------

Development Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # config/development.py
   import os
   from ndp_ep import APIClient

   def get_dev_client():
       return APIClient(
           base_url="http://155.101.6.191:8003",
           token=os.getenv("NDP_DEV_TOKEN")
       )

Production Configuration
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # config/production.py
   import os
   from ndp_ep import APIClient

   def get_prod_client():
       return APIClient(
           base_url=os.getenv("NDP_PROD_URL"),
           token=os.getenv("NDP_PROD_TOKEN")
       )

Docker Configuration
~~~~~~~~~~~~~~~~~~~~

.. code-block:: dockerfile

   FROM python:3.11-slim

   WORKDIR /app

   # Install dependencies
   RUN pip install ndp-ep

   # Environment variables will be passed at runtime
   ENV NDP_API_URL=""
   ENV NDP_API_TOKEN=""

   COPY app.py .

   CMD ["python", "app.py"]

Run with environment variables:

.. code-block:: bash

   docker run -e NDP_API_URL="http://155.101.6.191:8003" \
              -e NDP_API_TOKEN="your-token" \
              your-app:latest

---

### docs/source/index.rst (7,237 bytes)

NDP EP Python Client Library
=============================

**ndp-ep** is a Python client library for interacting with the National Data Platform (NDP) EP API.

🚀 Quick Start
--------------

**Try our interactive tutorials first!**

.. raw:: html

   <p>
   <a href="https://colab.research.google.com/github/sci-ndp/ndp-ep-py/blob/main/docs/source/tutorials/getting_started.ipynb" target="_blank">
   <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
   </a>
   <a href="https://mybinder.org/v2/gh/sci-ndp/ndp-ep-py/main?filepath=docs%2Fsource%2Ftutorials%2Fgetting_started.ipynb" target="_blank">
   <img src="https://mybinder.org/badge_logo.svg" alt="Binder"/>
   </a>
   </p>

The tutorial includes:

* 🔧 **Client setup and authentication** - Secure token configuration
* 🏢 **Working with organizations** - Create and manage data containers
* 🔍 **Searching datasets** - Simple and advanced search techniques  
* 📊 **Registering resources** - URL, S3, and Kafka topic registration
* 🛡️ **Error handling** - Best practices for robust applications
* 🎯 **Complete workflows** - End-to-end examples

Install and Basic Usage
-----------------------

Install the library:

.. code-block:: bash

   pip install ndp-ep

Basic usage:

.. code-block:: python

   from ndp_ep import APIClient

   # Initialize client with token
   client = APIClient(
       base_url="http://155.101.6.191:8003",
       token="your-access-token"
   )

   # List organizations
   organizations = client.list_organizations()
   print(organizations)

   # Search datasets
   results = client.search_datasets(
       terms=["climate", "temperature"],
       server="global"
   )

Features
--------

* **Complete API Coverage**: Support for all API endpoints including Kafka topics, S3 resources, URL resources, organizations, and services
* **Authentication**: Token-based and username/password authentication  
* **Search Functionality**: Advanced search capabilities across datasets and resources
* **Error Handling**: Comprehensive error handling with meaningful error messages
* **Type Hints**: Full type hint support for better IDE integration
* **Testing**: Extensive test coverage (>89%) with unit and integration tests

Documentation
-------------

.. toctree::
   :maxdepth: 2
   :caption: Getting Started

   installation
   quickstart
   authentication

.. toctree::
   :maxdepth: 2
   :caption: Interactive Tutorials
   
   tutorials/getting_started
   tutorials/bulk_resource_management

.. toctree::
   :maxdepth: 2
   :caption: User Guide

   user_guide/organizations

.. toctree::
   :maxdepth: 2
   :caption: API Reference

   api_reference

Learning Path
-------------

For the best learning experience, we recommend this path:

1. **📓 Start with the Interactive Tutorial** (:doc:`tutorials/getting_started`)
   
   * Run it in `Google Colab <https://colab.research.google.com/github/sci-ndp/ndp-ep-py/blob/main/docs/source/tutorials/getting_started.ipynb>`_ or `Binder <https://mybinder.org/v2/gh/sci-ndp/ndp-ep-py/main?filepath=docs%2Fsource%2Ftutorials%2Fgetting_started.ipynb>`_
   * Hands-on experience with live examples
   * Learn authentication and basic operations

2. **🔐 Set up Authentication** (:doc:`authentication`)
   
   * Get your API token
   * Configure secure authentication
   * Learn best practices

3. **🏢 Master Organizations** (:doc:`user_guide/organizations`)
   
   * Create and manage organizations
   * Learn naming conventions
   * Understand data organization

4. **📋 Explore the API Reference** (:doc:`api_reference`)
   
   * Complete method documentation
   * Advanced features and options
   * Error handling details

Advanced Tutorials
------------------

Ready for more? Explore advanced patterns and real-world scenarios:

**🚀 Bulk Resource Management** (:doc:`tutorials/bulk_resource_management`)

.. raw:: html

   <p>
   <a href="https://colab.research.google.com/github/sci-ndp/ndp-ep-py/blob/main/docs/source/tutorials/bulk_resource_management.ipynb" target="_blank">
   <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
   </a>
   <a href="https://mybinder.org/v2/gh/sci-ndp/ndp-ep-py/main?filepath=docs%2Fsource%2Ftutorials%2Fbulk_resource_management.ipynb" target="_blank">
   <img src="https://mybinder.org/badge_logo.svg" alt="Binder"/>
   </a>
   </p>

* Learn bulk operations, progress tracking, and complete cleanup workflows
* Create and manage hundreds of resources efficiently  
* Perfect for data migration, system setup, and testing environments
* Includes comprehensive error handling and performance monitoring

Quick Examples
--------------

**Search for datasets:**

.. code-block:: python

   # Simple search
   results = client.search_datasets(["climate"], server="global")
   
   # Advanced search with filters
   results = client.advanced_search({
       "search_term": "temperature,precipitation", 
       "filter_list": ["format:CSV"],
       "server": "global"
   })

**Create an organization:**

.. code-block:: python

   org_data = {
       "name": "my_research_lab",
       "title": "My Research Laboratory",
       "description": "Climate research data repository"
   }
   result = client.register_organization(org_data)

**Register a dataset:**

.. code-block:: python

   # URL resource
   url_data = {
       "resource_name": "climate_data_csv",
       "resource_title": "Climate Data",
       "owner_org": "my_research_lab",
       "resource_url": "https://example.com/climate.csv",
       "file_type": "CSV"
   }
   result = client.register_url(url_data)
   
   # S3 resource
   s3_data = {
       "resource_name": "large_dataset", 
       "resource_title": "Large Climate Dataset",
       "owner_org": "my_research_lab",
       "resource_s3": "s3://my-bucket/climate-data.parquet"
   }
   result = client.register_s3_link(s3_data)

**Bulk operations:**

.. code-block:: python

   # Create multiple services efficiently
   for i in range(1, 101):
       service_data = {
           "service_name": f"test_service_{i:03d}",
           "service_title": f"Test Service {i:03d}",
           "owner_org": "services",
           "service_url": f"https://api.example.com/service_{i:03d}",
           "service_type": "REST API"
       }
       result = client.register_service(service_data)
   
   # With progress tracking and cleanup
   # See the bulk management tutorial for complete examples

Community and Support
---------------------

* **📚 Documentation**: Complete guides and API reference
* **💻 GitHub**: `Source code and issues <https://github.com/sci-ndp/ndp-ep-py>`_
* **📦 PyPI**: `Package distribution <https://pypi.org/project/ndp-ep/>`_
* **🎓 Tutorials**: Interactive learning with live examples

Contributing
------------

We welcome contributions! See our `GitHub repository <https://github.com/sci-ndp/ndp-ep-py>`_ for:

* **🐛 Bug reports and feature requests** - Use GitHub Issues
* **🔧 Development setup** - Complete development guide  
* **🧪 Testing** - Comprehensive test suite
* **📝 Documentation** - Help improve our docs

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

---

### docs/source/installation.rst (3,739 bytes)

Installation Guide
==================

Requirements
------------

* Python 3.8 or higher
* requests >= 2.25.0
* urllib3 >= 1.26.0

Installing from PyPI
---------------------

The easiest way to install ndp-ep is from PyPI using pip:

.. code-block:: bash

   pip install ndp-ep

Installing from Source
-----------------------

You can also install directly from the GitHub repository:

.. code-block:: bash

   pip install git+https://github.com/sci-ndp/ndp-ep-py.git

For development purposes, clone the repository and install in editable mode:

.. code-block:: bash

   git clone https://github.com/sci-ndp/ndp-ep-py.git
   cd ndp-ep-py
   pip install -e .

Development Installation
------------------------

If you want to contribute to the project, install the development dependencies:

.. code-block:: bash

   git clone https://github.com/sci-ndp/ndp-ep-py.git
   cd ndp-ep-py
   
   # Create virtual environment (recommended)
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
   # Install package and development dependencies
   pip install -e .
   pip install -r requirements-dev.txt

Verifying Installation
----------------------

After installation, you can verify that the library is working correctly:

.. code-block:: python

   import ndp_ep
   print(ndp_ep.__version__)
   
   # Basic connection test (replace with actual API URL)
   from ndp_ep import APIClient
   
   try:
       client = APIClient(base_url="http://155.101.6.191:8003")
       print("✓ Connection successful")
   except Exception as e:
       print(f"✗ Connection failed: {e}")

Docker Installation
-------------------

If you prefer using Docker, you can create a container with the library pre-installed:

.. code-block:: dockerfile

   FROM python:3.11-slim
   
   WORKDIR /app
   
   # Install ndp-ep
   RUN pip install ndp-ep
   
   # Copy your scripts
   COPY . .
   
   CMD ["python", "your_script.py"]

Jupyter Notebook Installation
-----------------------------

For interactive development and tutorials, install Jupyter:

.. code-block:: bash

   pip install ndp-ep jupyter
   
   # Start Jupyter
   jupyter notebook

Then create a new notebook and test the installation:

.. code-block:: python

   import ndp_ep
   from ndp_ep import APIClient
   
   print(f"ndp-ep version: {ndp_ep.__version__}")

Troubleshooting
---------------

Common Issues
~~~~~~~~~~~~~

**ImportError: No module named 'ndp_ep'**

Make sure you have installed the package correctly:

.. code-block:: bash

   pip list | grep ndp-ep

**Connection Errors**

If you encounter connection errors, check:

1. Network connectivity to the API endpoint
2. Firewall settings
3. API endpoint URL (ensure it's correct and accessible)

**Authentication Issues**

For authentication problems:

1. Verify your API token is valid
2. Check token expiration
3. Ensure proper permissions for your account

Getting Help
~~~~~~~~~~~~

If you encounter issues not covered here:

1. Check the `GitHub Issues <https://github.com/sci-ndp/ndp-ep-py/issues>`_
2. Review the API documentation
3. Create a new issue with:
   - Python version
   - ndp-ep version
   - Complete error message
   - Minimal code example reproducing the issue

Virtual Environment Recommendations
-----------------------------------

It's strongly recommended to use a virtual environment:

**Using venv (Python 3.3+):**

.. code-block:: bash

   python -m venv ndp-env
   source ndp-env/bin/activate  # On Windows: ndp-env\Scripts\activate
   pip install ndp-ep

**Using conda:**

.. code-block:: bash

   conda create -n ndp-env python=3.11
   conda activate ndp-env
   pip install ndp-ep

**Using pipenv:**

.. code-block:: bash

   pipenv install ndp-ep
   pipenv shell

---

### docs/source/quickstart.rst (10,969 bytes)

Quick Start Guide
=================

This guide will help you get started with the ndp-ep library in just a few minutes.

🎯 Recommended: Interactive Tutorial
------------------------------------

**For the best learning experience, start with our interactive tutorial:**

.. raw:: html

   <p>
   <a href="https://colab.research.google.com/github/sci-ndp/ndp-ep-py/blob/main/docs/source/tutorials/getting_started.ipynb" target="_blank">
   <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
   </a>
   <a href="https://mybinder.org/v2/gh/sci-ndp/ndp-ep-py/main?filepath=docs%2Fsource%2Ftutorials%2Fgetting_started.ipynb" target="_blank">
   <img src="https://mybinder.org/badge_logo.svg" alt="Binder"/>
   </a>
   </p>

The interactive tutorial covers:

* **🔐 Secure Authentication Setup** - Learn to configure authentication safely
* **🏢 Organization Management** - Create and manage data containers
* **🔍 Dataset Search** - Simple and advanced search techniques
* **📊 Resource Registration** - Register URL, S3, and Kafka resources
* **🛡️ Error Handling** - Best practices for robust applications
* **🎯 Complete Workflows** - End-to-end real-world examples

.. note::
   The tutorial works completely in your browser and includes live, runnable code examples with real API interactions.

Basic Setup
-----------

1. **Install the library**:

   .. code-block:: bash

      pip install ndp-ep

2. **Get your API token**:
   
   - Visit https://nationaldataplatform.org/
   - Register for an account
   - Navigate to your profile to find your API token

3. **Import and initialize**:

   .. code-block:: python

      from ndp_ep import APIClient

      # Option 1: Using API token (recommended)
      client = APIClient(
          base_url="http://155.101.6.191:8003",
          token="your-api-token-here"
      )

      # Option 2: Using username/password
      client = APIClient(
          base_url="http://155.101.6.191:8003",
          username="your-username",
          password="your-password"
      )

.. tip::
   For a step-by-step guide on secure authentication setup, see our :doc:`tutorials/getting_started` notebook or the :doc:`authentication` guide.

First Steps
-----------

List Available Organizations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # List all organizations
   organizations = client.list_organizations()
   print("Available organizations:", organizations)

   # List organizations on a specific server
   local_orgs = client.list_organizations(server="local")
   global_orgs = client.list_organizations(server="global")

Search for Datasets
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Simple search
   results = client.search_datasets(
       terms=["climate", "weather"],
       server="global"
   )
   
   print(f"Found {len(results)} datasets")
   for dataset in results[:3]:  # Show first 3 results
       print(f"- {dataset.get('title', 'No title')}")

Check System Status
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Check if the system is healthy
   status = client.get_system_status()
   print("System status:", status)

   # Get detailed metrics
   metrics = client.get_system_metrics()
   print("System metrics:", metrics)

Creating Your First Organization
---------------------------------

.. code-block:: python

   # Define organization data
   org_data = {
       "name": "my_research_org",  # Must be lowercase, no spaces
       "title": "My Research Organization",
       "description": "An organization for my research projects"
   }

   try:
       # Create the organization
       result = client.register_organization(org_data)
       print(f"✓ Organization created with ID: {result['id']}")
   except ValueError as e:
       print(f"✗ Error creating organization: {e}")

.. note::
   For comprehensive organization management examples, check out the :doc:`tutorials/getting_started` notebook or the :doc:`user_guide/organizations` guide.

Registering Your First Dataset
-------------------------------

URL Resource
~~~~~~~~~~~~

.. code-block:: python

   url_data = {
       "resource_name": "climate_data_csv",
       "resource_title": "Climate Data CSV File",
       "owner_org": "my_research_org",  # Use your organization name
       "resource_url": "https://example.com/climate_data.csv",
       "file_type": "CSV",
       "notes": "Monthly climate data from weather stations"
   }

   try:
       result = client.register_url(url_data)
       print(f"✓ URL resource registered with ID: {result['id']}")
   except ValueError as e:
       print(f"✗ Error: {e}")

S3 Resource
~~~~~~~~~~~

.. code-block:: python

   s3_data = {
       "resource_name": "large_dataset_s3",
       "resource_title": "Large Dataset in S3",
       "owner_org": "my_research_org",
       "resource_s3": "s3://my-bucket/large-dataset.parquet",
       "notes": "Large dataset stored in S3 bucket"
   }

   try:
       result = client.register_s3_link(s3_data)
       print(f"✓ S3 resource registered with ID: {result['id']}")
   except ValueError as e:
       print(f"✗ Error: {e}")

Kafka Topic
~~~~~~~~~~~

.. code-block:: python

   kafka_data = {
       "dataset_name": "sensor_stream",
       "dataset_title": "Real-time Sensor Data Stream",
       "owner_org": "my_research_org",
       "kafka_topic": "sensor-data-topic",
       "kafka_host": "kafka.example.com",
       "kafka_port": "9092",
       "dataset_description": "Live sensor data from IoT devices"
   }

   try:
       result = client.register_kafka_topic(kafka_data)
       print(f"✓ Kafka topic registered with ID: {result['id']}")
   except ValueError as e:
       print(f"✗ Error: {e}")

.. tip::
   The :doc:`tutorials/getting_started` notebook includes working examples of all resource types with detailed explanations.

Advanced Search Example
-----------------------

.. code-block:: python

   # Advanced search with filters
   search_data = {
       "search_term": "climate,temperature,precipitation",
       "filter_list": [
           "format:CSV",
           "owner_org:research"
       ],
       "server": "global"
   }

   results = client.advanced_search(search_data)
   
   print(f"Advanced search found {len(results)} datasets")
   for dataset in results:
       print(f"- {dataset.get('title')}")
       print(f"  Organization: {dataset.get('organization', {}).get('title')}")
       print(f"  Resources: {len(dataset.get('resources', []))}")

Working with Services
---------------------

.. code-block:: python

   service_data = {
       "service_name": "weather_api",
       "service_title": "Weather Data API",
       "owner_org": "services",  # Must be 'services' for service registration
       "service_url": "https://api.weather.example.com",
       "service_type": "REST API",
       "notes": "RESTful API for weather data access",
       "health_check_url": "https://api.weather.example.com/health",
       "documentation_url": "https://docs.weather.example.com"
   }

   try:
       result = client.register_service(service_data)
       print(f"✓ Service registered with ID: {result['id']}")
   except ValueError as e:
       print(f"✗ Error: {e}")

Error Handling Best Practices
------------------------------

.. code-block:: python

   def safe_api_call(func, *args, **kwargs):
       """Wrapper for safe API calls with error handling."""
       try:
           return func(*args, **kwargs)
       except ValueError as e:
           print(f"API Error: {e}")
           return None
       except Exception as e:
           print(f"Unexpected error: {e}")
           return None

   # Example usage
   organizations = safe_api_call(client.list_organizations)
   if organizations:
       print(f"Found {len(organizations)} organizations")

Complete Example: Data Management Workflow
------------------------------------------

.. code-block:: python

   from ndp_ep import APIClient

   def main():
       # Initialize client
       client = APIClient(
           base_url="http://155.101.6.191:8003",
           token="your-token-here"
       )

       # 1. Check system health
       print("1. Checking system status...")
       status = client.get_system_status()
       print(f"   System is {'healthy' if status else 'not responding'}")

       # 2. List existing organizations
       print("\n2. Listing organizations...")
       orgs = client.list_organizations()
       print(f"   Found {len(orgs)} organizations")

       # 3. Search for existing datasets
       print("\n3. Searching for climate datasets...")
       results = client.search_datasets(["climate"], server="global")
       print(f"   Found {len(results)} climate-related datasets")

       # 4. Create organization (if needed)
       org_name = "demo_organization"
       if org_name not in orgs:
           print(f"\n4. Creating organization '{org_name}'...")
           org_data = {
               "name": org_name,
               "title": "Demo Organization",
               "description": "Demonstration organization for testing"
           }
           try:
               org_result = client.register_organization(org_data)
               print(f"   ✓ Organization created: {org_result['id']}")
           except ValueError as e:
               print(f"   ✗ Failed to create organization: {e}")

       # 5. Register a sample dataset
       print("\n5. Registering sample dataset...")
       dataset_data = {
           "resource_name": "sample_weather_data",
           "resource_title": "Sample Weather Data",
           "owner_org": org_name,
           "resource_url": "https://example.com/weather.csv",
           "file_type": "CSV",
           "notes": "Sample weather data for demonstration"
       }
       try:
           dataset_result = client.register_url(dataset_data)
           print(f"   ✓ Dataset registered: {dataset_result['id']}")
       except ValueError as e:
           print(f"   ✗ Failed to register dataset: {e}")

       print("\n✓ Workflow completed successfully!")

   if __name__ == "__main__":
       main()

Next Steps
----------

Now that you've seen the basics, explore more advanced features:

**📓 Interactive Learning:**
- **:doc:`tutorials/getting_started`** - Complete hands-on tutorial with live examples
- Run in `Google Colab <https://colab.research.google.com/github/sci-ndp/ndp-ep-py/blob/main/docs/source/tutorials/getting_started.ipynb>`_ or `Binder <https://mybinder.org/v2/gh/sci-ndp/ndp-ep-py/main?filepath=docs%2Fsource%2Ftutorials%2Fgetting_started.ipynb>`_

**📖 Detailed Guides:**
- **:doc:`authentication`** - Comprehensive authentication setup and security
- **:doc:`user_guide/organizations`** - Advanced organization management
- **:doc:`api_reference`** - Complete API documentation with all methods

**🔧 Development:**
- Explore our `GitHub repository <https://github.com/sci-ndp/ndp-ep-py>`_
- Check out the test suite for more usage examples
- Contribute to the project

---

### docs/source/user_guide/organizations.rst (21,414 bytes)

Working with Organizations
===========================

Organizations are the primary containers for datasets and resources in NDP EP. This guide covers how to create, manage, and work with organizations effectively.

What are Organizations?
------------------------

Organizations in NDP EP serve as:

- **Data containers**: Group related datasets and resources
- **Access control**: Manage permissions and visibility  
- **Collaboration units**: Teams can share and collaborate on data
- **Metadata organization**: Categorize data by department, project, or theme

Listing Organizations
---------------------

Before creating new organizations, it's helpful to see what already exists:

.. code-block:: python

   from ndp_ep import APIClient

   client = APIClient(
       base_url="http://155.101.6.191:8003",
       token="your-token"
   )

   # List all organizations from global server
   organizations = client.list_organizations(server="global")
   print(f"Found {len(organizations)} organizations")
   
   for org in organizations:
       print(f"- {org}")

Server Options
~~~~~~~~~~~~~~

Organizations can be listed from different servers:

.. code-block:: python

   # Local server
   local_orgs = client.list_organizations(server="local")
   
   # Global server (default)
   global_orgs = client.list_organizations(server="global")
   
   # Pre-production server
   pre_orgs = client.list_organizations(server="pre_ckan")

Filtering by Name
~~~~~~~~~~~~~~~~~

You can filter organizations by name:

.. code-block:: python

   # Find organizations with "research" in the name
   research_orgs = client.list_organizations(name="research", server="global")
   
   # Find organizations starting with "climate"
   climate_orgs = client.list_organizations(name="climate", server="global")

Creating Organizations
----------------------

Basic Organization Creation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   org_data = {
       "name": "my_research_lab",           # Required: unique, lowercase, no spaces
       "title": "My Research Laboratory",   # Required: human-readable name
       "description": "A research lab focusing on climate data analysis"  # Optional
   }

   try:
       result = client.register_organization(org_data, server="local")
       print(f"✅ Organization created with ID: {result['id']}")
       print(f"📝 Message: {result['message']}")
   except ValueError as e:
       print(f"❌ Error creating organization: {e}")

Naming Guidelines
~~~~~~~~~~~~~~~~~

**Organization Name Requirements:**

- Must be unique across the server
- Use lowercase letters, numbers, and underscores only
- No spaces or special characters
- Should be descriptive but concise
- Cannot be changed after creation

**Good Examples:**

.. code-block:: python

   # Good organization names
   good_names = [
       "climate_research_center",
       "university_data_lab", 
       "weather_monitoring_dept",
       "ocean_science_institute",
       "ai_research_group"
   ]

**Bad Examples:**

.. code-block:: python

   # Avoid these patterns
   bad_names = [
       "Climate Research Center",  # Contains spaces and capitals
       "my-org",                  # Contains hyphens
       "org@university.edu",      # Contains special characters
       "123",                     # Too generic
       "a"                        # Too short
   ]

Advanced Organization Management
--------------------------------

Creating Organizations with Rich Metadata
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   comprehensive_org = {
       "name": "comprehensive_climate_hub",
       "title": "Comprehensive Climate Data Hub",
       "description": """
       A collaborative platform for climate researchers worldwide.
       
       This organization hosts datasets from:
       - Temperature monitoring stations
       - Precipitation measurement networks  
       - Satellite imagery and remote sensing data
       - Climate model outputs and projections
       
       Contact: climate-data@university.edu
       """
   }

   result = client.register_organization(comprehensive_org, server="local")

Organization Hierarchies
~~~~~~~~~~~~~~~~~~~~~~~~~

While NDP EP doesn't support nested organizations directly, you can use naming conventions to create logical hierarchies:

.. code-block:: python

   # University structure
   university_orgs = [
       {
           "name": "university_main",
           "title": "University Main Campus",
           "description": "Main university data repository"
       },
       {
           "name": "university_physics_dept", 
           "title": "University Physics Department",
           "description": "Physics department research data"
       },
       {
           "name": "university_climate_lab",
           "title": "University Climate Research Lab", 
           "description": "Climate lab within physics department"
       }
   ]

   for org in university_orgs:
       try:
           result = client.register_organization(org, server="local")
           print(f"✅ Created: {org['title']}")
       except ValueError as e:
           print(f"❌ Failed to create {org['title']}: {e}")

Deleting Organizations
----------------------

.. warning::
   Deleting an organization will also remove all associated datasets and resources. This operation cannot be undone.

Basic Deletion
~~~~~~~~~~~~~~

.. code-block:: python

   try:
       result = client.delete_organization("old_organization", server="local")
       print(f"✅ Organization deleted successfully")
   except ValueError as e:
       if "not found" in str(e).lower():
           print("❌ Organization not found")
       else:
           print(f"❌ Error deleting organization: {e}")

Safe Deletion with Confirmation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   def safe_delete_organization(client, org_name, server="local"):
       """Safely delete an organization with confirmation."""
       
       # First, check if organization exists
       try:
           orgs = client.list_organizations(server=server)
           if org_name not in orgs:
               print(f"❌ Organization '{org_name}' not found")
               return False
       except Exception as e:
           print(f"❌ Error checking organization: {e}")
           return False
       
       # Get user confirmation
       confirmation = input(f"⚠️  Delete organization '{org_name}'? (yes/no): ")
       if confirmation.lower() != 'yes':
           print("🚫 Deletion cancelled")
           return False
       
       # Perform deletion
       try:
           result = client.delete_organization(org_name, server=server)
           print(f"✅ Organization '{org_name}' deleted successfully")
           return True
       except ValueError as e:
           print(f"❌ Error deleting organization: {e}")
           return False

   # Usage
   safe_delete_organization(client, "test_organization")

Best Practices
--------------

Naming Conventions
~~~~~~~~~~~~~~~~~~

**Use consistent prefixes:**

.. code-block:: python

   # By department
   department_orgs = [
       "dept_physics",
       "dept_chemistry", 
       "dept_biology"
   ]

   # By project
   project_orgs = [
       "proj_climate_2024",
       "proj_ocean_monitoring",
       "proj_ai_weather"
   ]

   # By data type
   data_type_orgs = [
       "data_sensors",
       "data_satellites",
       "data_models"
   ]

Organization Planning
~~~~~~~~~~~~~~~~~~~~~

Before creating organizations, consider:

1. **Purpose and scope**: What will this organization contain?
2. **Longevity**: Is this temporary or permanent?
3. **Collaboration**: Who will have access?
4. **Naming strategy**: How does it fit with existing organizations?
5. **Data governance**: What are the data management policies?

Bulk Operations
~~~~~~~~~~~~~~~

For creating multiple organizations:

.. code-block:: python

   def create_organizations_batch(client, org_configs, server="local"):
       """Create multiple organizations with error handling."""
       
       results = []
       
       for config in org_configs:
           try:
               result = client.register_organization(config, server=server)
               results.append({
                   "name": config["name"],
                   "status": "success",
                   "id": result["id"]
               })
               print(f"✅ Created: {config['title']}")
               
           except ValueError as e:
               results.append({
                   "name": config["name"], 
                   "status": "failed",
                   "error": str(e)
               })
               print(f"❌ Failed: {config['title']} - {e}")
       
       return results

   # Example usage
   research_organizations = [
       {
           "name": "marine_biology_lab",
           "title": "Marine Biology Laboratory",
           "description": "Research on marine ecosystems"
       },
       {
           "name": "atmospheric_science_dept",
           "title": "Atmospheric Science Department", 
           "description": "Weather and climate research"
       },
       {
           "name": "geophysics_institute",
           "title": "Geophysics Research Institute",
           "description": "Earth science and seismic monitoring"
       }
   ]

   # Create all organizations
   results = create_organizations_batch(client, research_organizations)
   
   # Summary
   successful = [r for r in results if r["status"] == "success"]
   failed = [r for r in results if r["status"] == "failed"]
   
   print(f"\n📊 Summary: {len(successful)} created, {len(failed)} failed")

Error Handling
~~~~~~~~~~~~~~

Common organization-related errors and how to handle them:

.. code-block:: python

   def handle_organization_errors(client, org_data, server="local"):
       """Demonstrate comprehensive error handling for organizations."""
       
       try:
           result = client.register_organization(org_data, server=server)
           return result
           
       except ValueError as e:
           error_msg = str(e).lower()
           
           if "already exists" in error_msg:
               print(f"❌ Organization name '{org_data['name']}' is already taken")
               # Suggest alternative names
               suggestions = [
                   f"{org_data['name']}_v2",
                   f"{org_data['name']}_new",
                   f"{org_data['name']}_2024"
               ]
               print(f"💡 Suggestions: {', '.join(suggestions)}")
               
           elif "authentication" in error_msg:
               print("❌ Authentication failed. Check your credentials.")
               
           elif "server is not configured" in error_msg:
               print(f"❌ Server '{server}' is not available or configured")
               print("💡 Try using 'local' or 'global' server")
               
           elif "invalid" in error_msg:
               print("❌ Invalid organization data")
               print("💡 Check that 'name' and 'title' are provided and valid")
               
           else:
               print(f"❌ Unexpected error: {e}")
               
           return None

Organization Validation
~~~~~~~~~~~~~~~~~~~~~~~

Validate organization data before creating:

.. code-block:: python

   import re

   def validate_organization_data(org_data):
       """Validate organization data before creation."""
       
       errors = []
       
       # Check required fields
       required_fields = ["name", "title"]
       for field in required_fields:
           if field not in org_data or not org_data[field]:
               errors.append(f"Missing required field: {field}")
       
       # Validate organization name
       if "name" in org_data:
           name = org_data["name"]
           
           # Check name format
           if not re.match(r'^[a-z0-9_]+, name):
               errors.append("Name must contain only lowercase letters, numbers, and underscores")
           
           # Check length
           if len(name) < 3:
               errors.append("Name must be at least 3 characters long")
           elif len(name) > 50:
               errors.append("Name must be less than 50 characters")
           
           # Check for reserved words
           reserved_words = ["admin", "api", "www", "test", "system"]
           if name in reserved_words:
               errors.append(f"Name '{name}' is reserved")
       
       # Validate title
       if "title" in org_data:
           title = org_data["title"]
           if len(title) < 3:
               errors.append("Title must be at least 3 characters long")
           elif len(title) > 100:
               errors.append("Title must be less than 100 characters")
       
       return errors

   # Usage example
   def create_validated_organization(client, org_data, server="local"):
       """Create organization with validation."""
       
       # Validate data
       errors = validate_organization_data(org_data)
       if errors:
           print("❌ Validation errors:")
           for error in errors:
               print(f"   - {error}")
           return None
       
       # Create organization
       return handle_organization_errors(client, org_data, server)

   # Example
   org_data = {
       "name": "validated_org_123",
       "title": "Validated Organization",
       "description": "This organization has been validated"
   }

   result = create_validated_organization(client, org_data)

Monitoring and Maintenance
--------------------------

Organization Audit
~~~~~~~~~~~~~~~~~~

Regularly audit your organizations:

.. code-block:: python

   def audit_organizations(client, servers=["local", "global"]):
       """Audit organizations across multiple servers."""
       
       print("🔍 Organization Audit Report")
       print("=" * 50)
       
       total_orgs = 0
       
       for server in servers:
           try:
               orgs = client.list_organizations(server=server)
               total_orgs += len(orgs)
               
               print(f"\n📊 Server: {server}")
               print(f"   Organizations: {len(orgs)}")
               
               # Analyze naming patterns
               prefixes = {}
               for org in orgs:
                   prefix = org.split('_')[0] if '_' in org else org[:5]
                   prefixes[prefix] = prefixes.get(prefix, 0) + 1
               
               print("   Top prefixes:")
               for prefix, count in sorted(prefixes.items(), 
                                         key=lambda x: x[1], reverse=True)[:5]:
                   print(f"     {prefix}: {count} organizations")
                   
           except Exception as e:
               print(f"❌ Error auditing {server}: {e}")
       
       print(f"\n📈 Total organizations across all servers: {total_orgs}")

   # Run audit
   audit_organizations(client)

Organization Health Check
~~~~~~~~~~~~~~~~~~~~~~~~~

Monitor organization health and usage:

.. code-block:: python

   def check_organization_health(client, org_name, server="local"):
       """Check the health and usage of an organization."""
       
       print(f"🏥 Health Check for '{org_name}'")
       print("-" * 40)
       
       # Check if organization exists
       try:
           orgs = client.list_organizations(server=server)
           if org_name not in orgs:
               print("❌ Organization not found")
               return False
           
           print("✅ Organization exists")
           
       except Exception as e:
           print(f"❌ Error checking organization: {e}")
           return False
       
       # Check for associated datasets (via search)
       try:
           # Search for datasets belonging to this organization
           search_results = client.advanced_search({
               "filter_list": [f"owner_org:{org_name}"],
               "server": server
           })
           
           dataset_count = len(search_results)
           print(f"📊 Associated datasets: {dataset_count}")
           
           if dataset_count == 0:
               print("⚠️  No datasets found - organization might be unused")
           else:
               print("✅ Organization is actively used")
               
               # Show sample datasets
               print("\n📋 Sample datasets:")
               for i, dataset in enumerate(search_results[:3]):
                   title = dataset.get('title', dataset.get('name', 'Untitled'))
                   resource_count = len(dataset.get('resources', []))
                   print(f"   {i+1}. {title} ({resource_count} resources)")
           
       except Exception as e:
           print(f"⚠️  Could not check datasets: {e}")
       
       return True

   # Example usage
   check_organization_health(client, "my_research_lab")

Migration and Backup
~~~~~~~~~~~~~~~~~~~~

Tools for organization migration:

.. code-block:: python

   def export_organization_config(client, org_name, server="local"):
       """Export organization configuration for backup or migration."""
       
       try:
           # Get organization list to verify existence
           orgs = client.list_organizations(server=server)
           if org_name not in orgs:
               print(f"❌ Organization '{org_name}' not found")
               return None
           
           # Create export data
           export_data = {
               "name": org_name,
               "server": server,
               "export_date": "2024-01-01",  # You'd use actual date
               "datasets": []
           }
           
           # Get associated datasets
           try:
               search_results = client.advanced_search({
                   "filter_list": [f"owner_org:{org_name}"],
                   "server": server
               })
               
               for dataset in search_results:
                   dataset_info = {
                       "id": dataset.get("id"),
                       "name": dataset.get("name"),
                       "title": dataset.get("title"),
                       "resources": len(dataset.get("resources", []))
                   }
                   export_data["datasets"].append(dataset_info)
                   
           except Exception as e:
               print(f"⚠️  Could not export datasets: {e}")
           
           return export_data
           
       except Exception as e:
           print(f"❌ Export failed: {e}")
           return None

   # Usage
   backup_data = export_organization_config(client, "my_research_lab")
   if backup_data:
       print(f"✅ Exported config for {backup_data['name']}")
       print(f"📊 Contains {len(backup_data['datasets'])} datasets")

Troubleshooting
---------------

Common Issues and Solutions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Issue: "Organization name already exists"**

Solution: Check existing organizations and choose a unique name:

.. code-block:: python

   def find_available_name(client, base_name, server="local"):
       """Find an available organization name based on a base name."""
       
       try:
           existing_orgs = client.list_organizations(server=server)
           
           # Try the base name first
           if base_name not in existing_orgs:
               return base_name
           
           # Try variations
           for i in range(2, 101):  # Try up to 100 variations
               variation = f"{base_name}_{i}"
               if variation not in existing_orgs:
                   return variation
           
           # If all variations are taken, suggest timestamp-based name
           import time
           timestamp_name = f"{base_name}_{int(time.time())}"
           return timestamp_name
           
       except Exception as e:
           print(f"Error finding available name: {e}")
           return None

   # Usage
   available_name = find_available_name(client, "research_lab")
   print(f"💡 Suggested name: {available_name}")

**Issue: "Server is not configured"**

Solution: Try different servers:

.. code-block:: python

   def find_working_server(client):
       """Find which servers are available."""
       
       servers = ["local", "global", "pre_ckan"]
       working_servers = []
       
       for server in servers:
           try:
               orgs = client.list_organizations(server=server)
               working_servers.append(server)
               print(f"✅ {server}: {len(orgs)} organizations")
           except Exception as e:
               print(f"❌ {server}: {e}")
       
       return working_servers

   # Check which servers work
   available_servers = find_working_server(client)
   print(f"\n💡 Available servers: {available_servers}")

Summary
-------

Organizations are fundamental to organizing your data in NDP EP. Key points to remember:

1. **Plan your organization structure** before creating
2. **Use consistent naming conventions** for better organization
3. **Validate data** before creation to avoid errors  
4. **Handle errors gracefully** with proper exception handling
5. **Monitor and audit** your organizations regularly
6. **Be careful with deletion** as it's irreversible

With proper organization management, you can create a well-structured, maintainable data platform that scales with your needs.

---

### requirements-dev.txt (196 bytes)

pytest>=7.0.0
pytest-cov>=4.0.0
pytest-mock>=3.10.0
requests-mock>=1.9.0
black>=22.0.0
flake8>=5.0.0
mypy>=1.0.0
types-requests>=2.25.0
twine>=4.0.0
build>=0.10.0
setuptools>=65.0.0
wheel>=0.38.0

---

## Source Files

Source code files are processed separately by the processor.
File list:

- `.gitignore` (1,934 bytes)
- `docs/Makefile` (1,269 bytes)
- `pyproject.toml` (2,637 bytes)
- `setup.py` (248 bytes)
- `.readthedocs.yaml` (278 bytes)
- `cleanup_test_services.py` (6,110 bytes)
- `docs/source/conf.py` (1,569 bytes)
- `ndp_ep/__init__.py` (2,386 bytes)
- `ndp_ep/api_client.py` (3,351 bytes)
- `ndp_ep/client_base.py` (7,757 bytes)
- `ndp_ep/dataset_resource_method.py` (3,859 bytes)
- `ndp_ep/delete_organization_method.py` (1,511 bytes)
- `ndp_ep/delete_resource_method.py` (2,541 bytes)
- `ndp_ep/get_kafka_details_method.py` (1,353 bytes)
- `ndp_ep/get_system_status_method.py` (3,574 bytes)
- `ndp_ep/get_user_info_method.py` (2,584 bytes)
- `ndp_ep/list_organization_method.py` (1,370 bytes)
- `ndp_ep/pelican_method.py` (7,864 bytes)
- `ndp_ep/register_dataset_method.py` (2,631 bytes)
- `ndp_ep/register_kafka_method.py` (2,140 bytes)
- `ndp_ep/register_organization_method.py` (1,988 bytes)
- `ndp_ep/register_s3_method.py` (2,375 bytes)
- `ndp_ep/register_service_method.py` (2,654 bytes)
- `ndp_ep/register_url_method.py` (2,382 bytes)
- `ndp_ep/resource_method.py` (8,643 bytes)
- `ndp_ep/rexec_method.py` (8,152 bytes)
- `ndp_ep/s3_buckets_method.py` (3,719 bytes)
- `ndp_ep/s3_objects_method.py` (8,415 bytes)
- `ndp_ep/search_method.py` (3,475 bytes)
- `ndp_ep/update_dataset_method.py` (3,737 bytes)
- `ndp_ep/update_kafka_method.py` (2,108 bytes)
- `ndp_ep/update_s3_method.py` (4,038 bytes)
- `ndp_ep/update_service_method.py` (4,804 bytes)
- `ndp_ep/update_url_method.py` (2,429 bytes)
- `ndp_ep/version_config.py` (1,751 bytes)
- `pytest.ini` (364 bytes)
- `tests/test_additional_methods.py` (15,689 bytes)
- `tests/test_api_client.py` (0 bytes)
- `tests/test_client_base.py` (8,051 bytes)
- `tests/test_dataset_resource_method.py` (4,937 bytes)
- `tests/test_error_cases.py` (11,097 bytes)
- `tests/test_init.py` (0 bytes)
- `tests/test_pelican_method.py` (10,084 bytes)
- `tests/test_register_methods.py` (11,067 bytes)
- `tests/test_register_organization_method.py` (6,786 bytes)
- `tests/test_remote_func_export.py` (1,116 bytes)
- `tests/test_resource_method.py` (9,275 bytes)
- `tests/test_rexec_method.py` (7,205 bytes)
- `tests/test_s3_management.py` (21,781 bytes)
- `tests/test_search_method.py` (7,026 bytes)
- ... and 2 more files

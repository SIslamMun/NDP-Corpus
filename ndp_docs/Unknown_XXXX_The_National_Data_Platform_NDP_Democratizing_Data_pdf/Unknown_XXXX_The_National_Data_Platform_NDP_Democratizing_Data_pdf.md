## Section 1

# 2025-01-30-parashar-6nrp

Scientific Computing and Imaging (SCI) Institute

      One-U Responsible AI Initiative
The National Data Platform (NDP):
Democratizing Data and Responsible
Artificial Intelligence
Manish Parashar
Director, Scientific Computing & Imaging (SCI) Institute
Chair in Computational Science and Engineering
Presidential Professor, Kahlert School of Computing
6NRP
San Diego, CA
January 30, 2025

Scientific Computing and Imaging (SCI) Institute

      One-U Responsible AI Initiative
Event Horizon Telescope: Blackhole Image
(Sagittarius A*)
May 2022
Science / Society Transformed by Data,
Cyberinfrastructure
Modeling of the delta virus inside respiratory
aerosols, Rommie Amaro, UCSD
Cyberinfrastructure is a key enabler of
discoveries & innovations

Scientific Computing and Imaging (SCI) Institute

## Section 2

      One-U Responsible AI Initiative
The Transcendence of AI

Scientific Computing and Imaging (SCI) Institute

      One-U Responsible AI Initiative
Democratizing Responsible Data, AI
is important
• Key characteristics for responsible AI (NIST) validity,
safety security, accountability, privacy enhancement,
fairness, and explainability.
• The quality and impact of research and the pace of
innovation are linked to the diversity of the
contributions.
• Especially true for AI-enabled research
• In case of AI, quality depends on who is developing and
use AI, and where the data coming from
• Greater inclusivity in contribution to research and
development increases the diversity of approaches and
the fairness of the results.
• Many barriers: awareness, ability, access,
association, …

Scientific Computing and Imaging (SCI) Institute

      One-U Responsible AI Initiative
NAIRR: Democratizing the AI R&D Ecosystem
Goals: Strengthen and democratize
the U.S. AI Innovation ecosystem in a
way that protects privacy, civil rights,
and civil liberties.
Computer, vol. 56, no. 11, pp. 85-90, Nov. 2023,
doi: 10.1109/MC.2023.3284568.
https://www.ai.gov/nairrtf/
Spur
innovation
Increase the diversity
of talent in AI
Improve U.S.
capacity for AI R&D
Advance
trustworthy AI

National Data Platform - NDP

## Section 3

 Services for Equitable Open Access to Data
CI
Systems
Open
Data
Data
Services
National
Data
Platform
User Capacity Building
Needs Assessment
Application Co-Design
•
Platform for data-enabled and AI-integrated workflows
- Facilitates data registration and discovery via a centralized hub
- Democratizes data access and use via distributed points of presence
- Cultivates resources for classroom education and data challenges
- Assists research and learning through personalized workspaces
•
Applications in climate and AI with data diverse scientific data repositories
including NSF facilities, NAIRR, NASA, USGS, NOAA and USDA
A federated and extensible data ecosystem to promote innovation and collaboration through the
equitable use of data leveraging existing and future national cyberinfrastructure capabilities.
FOCUS AREAS:
•
Partnerships to foster scientific discovery, decision-making, policy formation and societal impact
https://www.nationaldataplatform.org/
#2333609

NDP
Hub
NDP
Federation
A scalable platform for
developing and deploying
services at distributed
points of presence
Centralized portal for
discovery through
collaborative workspaces
for research and education

NDP Overarching Architecture
NDP POP
NDP POP
NDP POP
NDP POP
NDP Federation (Scalable platform for
customizable & composable service stacks)
Search,
Discovery,
Access & Use
NDP Hub (Central discovery & access
workspace for research & education)
NDP Portal
Education Hub
NAIRR / Composable CI
Nautilus
Cloudbank
ACCESS
HPC
Cloud
Containers
(…)
(…)
Coordinated Crosscutting Services
Data Sources
NAIRR Datasets,
NDC-C,
EarthScope,
WIFIRE,
Nourish,
SAGE,
etc.
GitHub,
PyPI
Hugging Face,
DockerHub,
etc.
Authentication & Authorization, Accounting, Orchestration, Monitoring and Logging,
Catalog, Workspace, Notebooks, Data Democratization, Workflow Integration, etc.
External Services
Pelican/OSDF
SAGE
Data CI and Delivery
Services
NDP Federation Architecture
Federation Orchestrator API

İlkay Altıntaş, PhD (ialtintas@ucsd.edu )
NDP Hub: Central discovery & access workspace for research &
education
NDP Hub
•
NDP Portal (point of access)
      https://nationaldataplatform.org
•
Metadata registration and indexing
○
Contributing organizations
○
Harvested metadata from NDP POPs
•
Data search
○
String and conceptual search
○
Open Knowledge graphs / via LLMs
NDP Standard Services
Public:
•
Extensible Data Catalog and
Search Services
•
Education Hub Informal Learning
Modules
Login-enabled:
•
Keycloak Role-Based Access
Service
•
User Workspaces
•
AI Gateway with Custom
JupyterHub Service
•
Data Catalog and OKN Ingestion
•
External Model Ingestion
•
Data Exploration Services
•
MLFlow Dashboard Service
•
Education Hub Classroom
•
Education Hub Challenge
•
Democratizing Data Dashboard
Hub Capabilities Under Development
•
Sage Data and Edge Code Integration
Service
•
Service Catalog and Discovery Service
•
Educational Hub Expansion
•
Streaming Data Services
•
Pelican Registration Service
•
Integrated Workflows
Planned Future Work
•
OKN Integration
•
Data Curation
•
Data Subsetting
•
Data Provenance
•
Educational Toolkits
•
Open Science Chain Provenance
Service
•
Gateway Services
Search,
Discovery,
Access & Use
NDP Portal
Education Hub
http://www.nationaldataplatform.org

İlkay Altıntaş, PhD (ialtintas@ucsd.edu )
NDP Hub: Data Search and Discovery
11
Current Capabilities:
•
Search capabilities to include not just text in metadata and ontology
concepts but also time and location data.
•
Ability to search time and time ranges within the data, such as from
"27 September 2020" to "24 January 2021.”
•
Location-based searches can now be combined using specific
location names (e.g., "San Luis Obispo") or boundary polygons.
•
Support free-text search across “all metadata” without specifying
particular fields.
•
Utilize Lucene, a popular search syntax, to improve search
functionality.
Ongoing Work :
•
Extract entity annotations from the metadata text and integrate them
with the ontology to enhance search functionality.
•
Create a vector store and develop a search pipeline that handles
queries in natural language.
•
Optimize the system's performance to ensure fast and accurate retrieval
of relevant information.
http://www.nationaldataplatform.org

İlkay Altıntaş, PhD (ialtintas@ucsd.edu )
NDP Workspaces (Version 1 - September 2024)
Goal : Craft persistent and
customizable workspaces with
datasets and services to launch
into a sandbox
-
Create customized
workspaces for varied use
cases
-
Search and add datasets to
use in sandbox (HPC Env)
-
Add github links for file
access
-
Launch packaged workspace
into sandbox
Users can:
• view all their workspaces
• create new workspaces by clicking
on the “New Workspace” button
• use workspace action buttons to
preview, edit, switch and delete
• add datasets to their current
workspace from the catalog page.
http://www.nationaldataplatform.org

## Section 4

İlkay Altıntaş, PhD (ialtintas@ucsd.edu )
NDP JupyterHub (Sandbox)
A compute environment for data analysis, machine
learning training or any other computational tasks, built
on top of NRP (Nautilus) cluster. Different datasets and
tasks will require powerful compute resources (CPUs,
GPUs, memory), which user can select and use
seamlessly.
ü
Integrated with
NDP Single-Sign
On
ü
Select your
compute
resources from
NRP pool
ü
Select
previously
created image
(environment)
or bring yours
●
Integrated with File Manager extension
●
Loads data from your workspaces (datasets and github
resources)
●
Change your workspaces content and refresh in
JupyterHub to get updates
●
Download all or selected resources into your storage for
further analysis
http://www.nationaldataplatform.org

NDP Data POP: Distributed Points of Presence with Customizable,
Composable Service Stacks
NDP POP Factory
deploys
Standard NDP Services
Cloud    HPC
Deployment models:
User-defined Services
Catalog
Data
Democratization
Search
(…)
NDP POP service stack
customization
NDP POP
NDP POP
NDP POP
NDP POP
NDP Federation
(…)
Federation Orchestrator API
In-situ Processing
Data Streaming
service
(…)
-- Standalone --
-- Scalable (cluster) --
deploys
SciDX Stack
Data Staging service
Workflow composition currently via API
and/or Python client library
API + Library
API + Library
Third-Party
Stacks

Science Data Exchanges (SciDx) Services
A customizable Data-Pop software stack for in-situ data access & processing
SciDx Staging Services
• Transient resources for in-situ (close to the
data) data processing and access
- High-performance in-memory processing
- Server-side data transformations (e.g., sub-
setting, reduction, user-defined analysis, etc.)
- Caching/sharing of data, results, and data-
products
- Registration of data-triggers
• Efficient management of data in-motion
- Streamline workflows; minimize data transfers
- Perform ETL operations at data source

SciDx Staging Service: Wildfire Monitoring Usecase
NOAA GOES-17 Data on S3
•
Monitor fire hotspots based on
satellite data that updates every 5
minutes
•
Not interested in the entire data
product, just pixels that reach
severity threshold
•
Per-pixel evaluation as a user-defined
transformation is performed on each
new data update
•
The user subscribes to the results of
the transformation
•
Reduction in data cost, latency, time
to solution
result =
client.query_array(source='goes18-radc',
               var_name='Rad',
               lb=(0,2500),
               ub=(2499,4999),
               timestamp='2024-08-02T00:35:00',
               time_direction=PAST)

Science Data Exchanges (SciDx) Services
A customizable Data-Pop software stack for in-situ data access & processing
SciDx Staging Services
• Transient resources for in-situ (close to the
data) data processing and access
- High-performance in-memory processing
- Server-side data transformations (e.g., sub-
setting, reduction, user-defined analysis, etc.)
- Caching/sharing of data, results, and data-
products
- Registration of data-triggers
• Efficient management of data in-motion
- Streamline workflows; minimize data transfers
- Perform ETL operations at data source
SciDx Streaming Service
•
Streams registration, curation/archival for
discovery and access
•
User-defined operations/filters on streaming;
containerized execution
•
Combine streaming data with
archived/playback data
•
Mechanism for online data product
generation (i.e., new data streams)

SciDx Streaming Service

## Section 5

SciDx: Advanced Search & Discovery
https://democratizingdata.ai/

NDP+NRP: Use the NDP widget to import datasets and
conduct analysis within NRP.
Students select a module
to work on. They load it to
JHub, cloning the
attached repository and
loading the data using the
NDP Widget
A reminder for students to
save their work in a
persistent storage directory

İlkay Altıntaş, PhD (ialtintas@ucsd.edu )
http://www.nationaldataplatform.org
Example NDP-NAIRR AI in Science Workflow
Data
Acquisition
Registration,
Indexing,
Discovery
Workspace
Definition
Data-driven,
AI/ML-based
workflows
Product
Generation,
Curation,
Sharing,
 Archival
• Data and Models are
identified as part of the
Open NAIRR
Resources.
• Resources are collected
from HuggingFace
• Data and Models are
registered into NDP
catalog (CKAN)
• Data origin is created
in OSDF to optimize
data transfer
• Data and Models are included
into user’s workspace, along
with the necessary libraries,
services and files to work on a
new project.
• Analysis and AI/ML
workflow  is supported by
AI Gateway (JupyterHub),
using NRP’s Nautilus.
• High Performance
processing for new
resource(s) development
(Models, Data).
• Final products pushed to
OSDF/HuggingFace/GitHub
and registered into NDP’s
catalog .
http://www.nationaldataplatform.org

İlkay Altıntaş, PhD (ialtintas@ucsd.edu )
Case Studies for Generalizable Workflows
●
Representative examples of important
patterns that exist in science today for
working with
○
large datasets
○
streaming data from facilities
○
graph data from open knowledge
networks
●
Implemented as production-quality
specialized value-added services
●
Domains of wildland fire, earthquakes,
and food security
●
Will be generalized for replication by
external communities.
http://www.nationaldataplatform.org

•
Real-time high-precision GNSS stations and SAGE data streams
EarthScope/SAGE data streaming/analysis enabled by NDP
POP
Data Acquisition
Data Processing
Data Streaming service
API
Formatted data
Cofigure how to
process data
Streaming Service
Management
sciDX Data
Streaming
System
OSDF/Pelican
Origin
Historical data storage
* To NDP Catalog
Triggers
HTC workflow
AI model re-training
Save metadata for sciDX Data
Streaming ‘topics’ that a user
could be subscribed to.
API
POP Catalog
Data management
NDP
POP
Data Stream
Data
Subscription
Data Discovery from POP
and General NDP Catalog
Real-time forecasting and visualization
NDP
Catalog
Data Gathering
(hardvesting)
Data
Discovery
AI Analysis

NDP + NDR: Nourish NDF POP
Extends SDSC’s AWESOME platform

## Section 6

İlkay Altıntaş, PhD (ialtintas@ucsd.edu )
Award abstract: https://www.nsf.gov/awardsearch/showAward?AWD_ID=2333609
http://www.nationaldataplatform.org

Scientific Computing and Imaging (SCI) Institute

      One-U Responsible AI Initiative
•
Inter/transdisciplinary,
collaborative, convergent
•
Core strengths in: Visualization
& imaging; Scalable analytics;
Advanced computing & data
•
Software/system development
and distribution integral to our
research processes
Transformation of science and
society through translational
research and innovation
SCI Institute

Scientific Computing and Imaging (SCI) Institute

      One-U Responsible AI Initiative
University of Utah’s $100M AI Research
Initiative Led by SCI
One-U Responsible AI Initiative
Responsibly advance translational AI to achieve
societal good
Catalyze transdisciplinary excellence in responsible
AI to bring together the use-inspired/applied AI research
and technological expertise, advanced
cyberinfrastructure, and translational workforce
Initial research focus on regionally important
applications
1. Environment
2. Healthcare, societal wellness, and public services
3. Future of teaching and learning

Scientific Computing and Imaging (SCI) Institute

## Section 7

      One-U Responsible AI Initiative
Thank you!
Manish Parashar
Email: manish.parashar@utah.edu
WWW: manishparashar.org / sci.utah.edu / rai.utah.edu
One-U RAI Opportunities
• Distinguished Visitors Program: Supports visits from a
few days to a full year for faculty, up to two years for
postdoctoral fellows.
• Postdoctoral Fellows Program: Supports postdocs in
areas related to responsible AI for up to 2 years.
@OneU_RAI
one-u-responsible-ai-initiative


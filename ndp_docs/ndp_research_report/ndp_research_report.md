# National Data Platform (NDP): Complete User and Developer Reference

**Key Points**
- The **National Data Platform (NDP)** is a federated and extensible cyberinfrastructure (CI) ecosystem designed to democratize access to AI-ready scientific data, integrating disparate computing and storage resources into a unified collaborative environment [1, 2, 3].
- At the core of the NDP architecture is the **Federated Endpoint (NDP-EP)**, a lightweight infrastructure mechanism deployed via Kubernetes or Docker Compose that allows research institutions to seamlessly link their local on-premise resources to the national data catalog [4, 5].
- **DataSpaces**, an integral component of the NDP ecosystem, provides an extreme-scale, semantically specialized shared-space abstraction for in-situ and in-transit data processing. It drastically reduces I/O bottlenecks by enabling direct memory-to-memory data coupling across massive simulation workflows [6, 7].
- The platform caters to both research and education through the **Education Hub** and **CollabStudio**, providing educators with the tools to bundle datasets, machine learning models, and compute environments (via JupyterHub) into deployable modules for classrooms and hackathons [8, 9].
- Developers interface with the platform via a robust suite of tools, including the **EP-API**, Python client SDKs (`ndp-ep-py`), and infrastructure-as-code templates (`ndp-ep-helm`), ensuring highly reproducible and scalable data pipelines .

---

## 1. Introduction and Platform Vision

In the era of massive data generation, scientific discovery is increasingly gated not by the lack of data, but by the friction involved in discovering, accessing, and processing it. The National Data Platform (NDP) was developed to directly address these barriers, catalyzing an open, equitable, and extensible data ecosystem [2, 3]. Championed by leading researchers in extreme-scale data management, the NDP acts as a centralized nexus built atop existing foundational cyberinfrastructure (CI) [10, 11]. 

### 1.1 The Need for Democratized Data
The concept of "democratizing data" implies removing the technical and institutional silos that restrict access to high-value scientific datasets. Modern research demands "AI-ready" datasets—data that is structured, curated, and optimized for machine learning (ML) and deep learning (DL) applications without requiring researchers to spend months on data wrangling [1]. The NDP achieves this by federating distributed data repositories and tightly integrating them with high-performance computing (HPC) and cloud resources [3]. This architecture forms a core demonstration project within the broader National Artificial Intelligence Research Resource (NAIRR) initiative [2, 12].

### 1.2 Target Audience and Value Proposition
The NDP ecosystem is specifically designed to cater to three primary constituencies [1]:
1. **Researchers and Data Scientists:** Provides simplified, high-throughput access to AI tools, compute clusters, and registered datasets, allowing researchers to build complex, data-enabled workflows without managing the underlying hardware.
2. **Educators:** Enables the creation of AI-centered educational resources through the Education Hub. Educators can bundle workflows and real-world datasets into classrooms, providing students with reproducible computing environments [8].
3. **Students and Learners:** Reduces the barrier to entry for acquiring AI and data science skills by providing hands-on, zero-configuration access to powerful computing resources via web-based interfaces [1].

---

## 2. Platform Architecture and Cyberinfrastructure Integration

The NDP is not an isolated supercomputer; rather, it is a meta-infrastructure—a platform of platforms—that spans the edge-to-HPC continuum. It achieves scalability through a federated architectural model comprising three primary pillars: a Centralized Hub, Federated Endpoints, and Standard Services [1].

### 2.1 The Centralized Hub
The Centralized Hub serves as the primary control plane and user interface for the ecosystem. It hosts the centralized **Data Catalog**, which maintains comprehensive metadata, search indices, and access control policies for all registered datasets [1, 13]. The Hub provides a web-based dashboard where users can explore curated catalogs, initiate workspaces, and manage their institutional profiles.

### 2.2 Standard Services and Cyberinfrastructure Foundations
The NDP leverages standard services for authentication, authorization, and workflow orchestration. By integrating with **CI Logon**, the platform ensures secure, federated identity management across institutional boundaries via standard OIDC/SAML protocols [13].

Furthermore, the platform's foundation relies on massive prior investments by the National Science Foundation (NSF). The NDP integrates directly with systems such as the Open Science Grid, the Open Science Data Federation (OSDF), PATh, the National Research Platform (NRP), the Open Storage Network (OSN), and Expanse at the San Diego Supercomputer Center (SDSC) [3]. This deep integration allows the platform to utilize distributed function-as-a-service (FaaS) systems like Globus funcX for transparent function execution across endpoints [14].

### 2.3 Federated Endpoints (NDP-EP)
To bridge the Centralized Hub with distributed data sources, the NDP introduces the concept of **Federated Endpoints** (formerly referred to as Points of Presence or POPs) [5]. In the context of the NDP, an "endpoint" differs significantly from standard definitions in cybersecurity (e.g., a corporate laptop running an Endpoint Protection Platform) [15, 16] or basic API design (e.g., a simple URL path) [17]. Instead, an NDP Endpoint represents an institutional data and compute cluster that exposes its resources to the national federation through standardized interfaces and containerized applications [4, 14]. 

Institutions deploy endpoint software to transform their local laptops, clouds, or supercomputers into fully participating nodes of the NDP ecosystem, maintaining local data sovereignty while enabling global discoverability [4, 14].

---

## 3. DataSpaces: Extreme-Scale Data Management Framework

A defining technological pillar of the NDP is **DataSpaces**, an extreme-scale data management framework that provides an interaction and coordination substrate for coupled scientific simulation workflows [6, 7]. Originally awarded an R&D 100 Award in 2013 as part of the ADIOS framework, DataSpaces has evolved into a critical mechanism for bypassing parallel file system I/O bottlenecks in modern supercomputers [10, 18].

### 3.1 The Tuple-Space Model and Shared-Space Abstraction
Traditional scientific workflows typically follow a file-based paradigm: a simulation writes terabytes of data to a parallel file system, and a separate analytics application subsequently reads that data from disk. This model is highly inefficient and creates severe I/O bottlenecks. 

DataSpaces solves this by providing a semantically specialized virtual shared-space abstraction derived from the **tuple-space model** [6]. It utilizes memory buffers allocated from distributed compute nodes (staging nodes) to create a distributed, in-memory object store. Applications can associatively access data in this space using simple geometric queries, completely bypassing disk storage [6, 7].

### 3.2 In-Situ and In-Transit Data Processing
DataSpaces supports dynamic event registration and processing modes designed to manage extreme heterogeneity [18]:
- **In-Situ Processing (Co-processing):** Data processing operations (e.g., filtering, compression, or visualization) execute inline on the exact same processor cores that are running the primary simulation. This enables direct access to the simulation's memory [6, 19].
- **In-Transit Processing (Concurrent processing):** Data is moved asynchronously over high-speed networks to a dedicated subset of compute nodes (the staging area) where analytics operations execute independently of the simulation processes [6, 19].

### 3.3 Layered Architecture of DataSpaces
The DataSpaces framework is architected in four distinct layers [6]:

1. **Communication Layer:** At its base, DataSpaces utilizes **Margo**, a high-performance RPC and bulk data transfer layer. Margo is built atop Mercury (network abstraction) and Argobots (lightweight user-level threading), enabling high-speed, low-overhead communication across the compute fabric [6].
2. **Distributed Object Store Layer:** This layer builds the in-memory storage repository. It utilizes a **Distributed Hash Table (DHT)** to dynamically map and index data locations, ensuring highly efficient and scalable $O(1)$ look-ups. A built-in Query Engine resolves complex application data queries at runtime [6, 7].
3. **Core Service Layer:** Responsible for coordination and data sharing. It manages the allocation of memory buffers and handles the mapping and scheduling of online data processing operations (both in-situ and in-transit) to optimize data locality and minimize network movement [6].
4. **Programming Abstraction Layer:** DataSpaces provides robust APIs extending standard parallel programming models like MPI and PGAS. It features simple `put()` and `get()` operators for asynchronous, memory-to-memory data sharing. Additionally, it provides `pub()` and `sub()` operators for dynamic publish/subscribe/notification messaging patterns, allowing scientists to define analysis workflows as a Directed Acyclic Graph (DAG) [6].

### 3.4 Scientific Impact and Integration
DataSpaces is heavily utilized in production coupled scientific simulation workflows. Notable deployments include large-scale tightly coupled parallel fusion simulations (enabling memory-to-memory coupling between the gyrokinetic PIC edge simulation code XGC0 and the MHD code M3D-OMP) and turbulent combustion simulations (coupling the DNS code S3D with analytics pipelines) [6, 18]. Furthermore, DataSpaces is deeply integrated as an I/O engine within the open-source **ADIOS2** framework, enabling widespread adoption across various scientific domains [6].

The open-source development of DataSpaces is actively maintained on GitHub, encompassing multiple repositories such as the core `dspaces` codebase, `dspaces-api`, `dxspaces`, and specialized deployments like `dspaces-spack` (a Spack repository for DataSpaces 2.x) and `dspaces-containers` [20, 21, 22]. Active community development also includes Margo-based DataSpaces forks supporting Kokkos staging spaces and GPU testing [23].

---

## 4. Federated Endpoints (NDP-EP): Operations and Deployment

For institutions looking to participate in the NDP, deploying an **NDP Endpoint (NDP-EP)** is the primary operational requirement. The endpoint acts as a highly resilient gateway that facilitates data discovery, data staging, and real-time streaming [5].

### 4.1 Deployment Topologies
Endpoints are designed to be deployed on diverse infrastructure, from standalone bare-metal servers to complex Kubernetes clusters. According to real-world deployments—such as establishing an endpoint to stream published science datasets from Hawaii—the preferred orchestration mechanisms are **Kubernetes** and **Docker Compose** [5].

#### Helm Chart Deployment (`ndp-ep-helm`)
For production deployments on Kubernetes, the NDP provides official Helm charts (`ndp-ep-helm`) . This infrastructure-as-code approach allows administrators to declaratively manage the endpoint's lifecycle, ingress routing, persistent volume claims (PVCs), and resource limits. 

A generalized deployment involves configuring a `values.yaml` file to map institutional storage arrays to the endpoint's internal data services. This ensures that the endpoint can securely expose subsets of local storage to the NDP Centralized Hub without granting unfettered network access [4]. 

### 4.2 Endpoint Registration
Once deployed, the endpoint must be registered with the NDP Hub. This is accomplished via the Endpoint Creation interface accessible at the NDP documentation portal (`/endpoints/create`) [1]. Registration establishes trust between the hub and the local endpoint, generating necessary API keys and OAuth credentials to facilitate zero-trust data exchange.

### 4.3 SciDX Ecosystem
The endpoint infrastructure is closely tied to the **SciDX** software stack. SciDX provides comprehensive capabilities for scalable data discovery and streaming. Endpoint factories configure deployments based on specific analytical needs, offering deployment variations such as `scidx without dspaces` for pure data serving, or `scidx with dspaces` for environments requiring advanced in-situ analytics and high-speed staging [11, 24].

---

## 5. Developer Guide: APIs and Client SDKs

The NDP provides an extensive suite of developer tools to automate workspace provisioning, data ingestion, and workflow orchestration.

### 5.1 The EP-API and OpenAPI Specifications
The primary interface for programmatic interaction with the platform is the **EP-API** [13]. The API adheres strictly to standard RESTful principles and is fully documented via OpenAPI JSON specifications hosted on the federation's test and production domains (`openapi.json`) . 

The EP-API provides routes for:
- **Authentication:** Validating CI Logon tokens and issuing session keys.
- **Catalog Management:** Registering new datasets, pushing metadata updates, and executing advanced full-text and geometric search queries across the federated data catalog [13].
- **Workspace Orchestration:** Initiating requests to the Kubernetes control plane to spin up new compute Pods, allocate GPUs, and attach Persistent Volumes (PVs) [13].
- **Endpoint Coordination:** Managing the health checks, status updates, and synchronization of geographically distributed NDP endpoints [13].

### 5.2 Python Client SDK (`ndp-ep-py`)
To streamline integration, the NDP provides a dedicated Python client SDK (`ndp-ep-py`) . This SDK abstracts the complexity of the underlying REST API, providing intuitive Pythonic classes for data scientists to interact with the platform directly from their local scripts or Jupyter Notebooks.

*Conceptual usage pattern based on platform architecture:*
```python
from ndp_ep import NDPClient

# Initialize the client with federation credentials
client = NDPClient(api_key="your_api_key", environment="production")

# Discover data via the federated catalog
catalog = client.get_catalog()
datasets = catalog.search(query="climate models", region="north_america")

# Request a computational workspace instance
workspace = client.launch_workspace(
    image="jupyter/scipy-notebook",
    cpus=4,
    gpus=1,
    memory="16Gi",
    volume_mount=datasets.id
)
print(f"Workspace available at: {workspace.url}")
```

### 5.3 Developing with DataSpaces C-API
For high-performance application developers writing MPI or Kokkos simulations, direct integration with DataSpaces is achieved via its C-level Programming Abstraction Layer [6]. 

A generalized workflow for putting and getting data involves initializing the DataSpaces environment, defining the global dimensions of the data array, and executing asynchronous memory transfers:

```c
#include "dataspaces.h"
#include <mpi.h>

int main(int argc, char **argv) {
    MPI_Init(&argc, &argv);
    // Initialize DataSpaces connection
    dspaces_init(num_peers, app_id);
    
    // Define the geometric dimensions of the data
    dspaces_define_gdim("simulation_tensor", ndim, gdim);
    
    // Asynchronously 'put' data into the in-memory tuple space
    dspaces_put("simulation_tensor", version, size, lower_bounds, upper_bounds, data_ptr);
    
    // Remote analytics process 'gets' the data without touching the file system
    dspaces_get("simulation_tensor", version, size, lower_bounds, upper_bounds, fetch_ptr);
    
    dspaces_finalize();
    MPI_Finalize();
    return 0;
}
```

---

## 6. User Guide: Workspaces and Computing Environments

The NDP is meticulously designed to provide a frictionless user experience, transitioning researchers from data discovery to data analysis in a matter of minutes [13].

### 6.1 Registration, Authentication, and the Catalog
Access to the NDP is governed by the **CI Logon** framework, which allows users to authenticate using their existing institutional or university credentials [13]. Upon authentication, users are granted access to the **NDP Catalog**.

The Catalog encompasses a diverse array of structured datasets and real-time data streams spanning multiple scientific domains. The platform incorporates a user-friendly interface that facilitates exploratory search, metadata review, and data contribution via a formalized registration service [1, 13].

### 6.2 Workspace Launch and Compute Options
The platform provides flexible options for launching compute environments, allowing users to select the infrastructure that best matches their compute needs and available hardware credits [1, 4].

1. **NDP JupyterHub (Default Service):** Hosted securely by the National Research Platform (NRP), this option is the default compute environment for the NDP. Users can launch interactive Jupyter Notebooks directly within the ecosystem. The underlying Kubernetes cluster dynamically orchestrates the creation of a Pod based on user specifications (CPU cores, GPUs, and memory). The platform automatically provisions and attaches a 100GB Persistent Volume (PV) to the Pod, ensuring that research data and environment states persist seamlessly across multiple login sessions [4, 13].
2. **AWS Integration:** For large-scale experiments requiring elastic cloud capabilities, users possessing Amazon Web Services (AWS) credits can deploy NDP workspaces directly onto AWS infrastructure while maintaining the cohesive NDP software stack [4].
3. **NDP Endpoints (On-Premise Integration):** As discussed previously, institutions with local computing clusters can launch workspaces natively on their local infrastructure via an NDP Endpoint, retaining strict data governance and hardware control while utilizing the global NDP interface [4].

Once a workspace is provisioned, users can immediately engage in exploratory data analysis, model training, and visualization using pre-configured software images.

---

## 7. The Education Hub and Collaborative Science

Recognizing the critical shortage of infrastructure supporting practical AI literacy, the NDP developed a first-of-its-kind **Education Hub** [8, 9]. The Hub bridges the gap between raw research data and pedagogical environments.

### 7.1 CollabStudio: Modules, Classrooms, and Projects
Within the **CollabStudio** section of the platform, educators can architect highly complex educational environments [1]. 
- **Modules (Workspaces):** Educators can bundle specific datasets, necessary computational services, open-source codebases (directly linked from GitHub), and pre-trained AI/ML models (e.g., from Hugging Face) into a single, deployable computational unit [8]. 
- **Classrooms:** These modules are subsequently aggregated into Classrooms. A user-friendly creation wizard guides educators through configuration, eliminating the need for students to wrestle with environment pathing, software dependency conflicts, or data downloading [8].

### 7.2 Hackathons and Data Challenges
The Education Hub is purpose-built to host massive open learning events and competitions. Early successful implementations include the **Fire-Ready Forests Data Challenge**, funded by NSF award #2341120 [8]. 

The platform also natively supports high-throughput streaming events, as demonstrated by resources like the `Streaming_Hackathon-RAI` repository, which provides specialized toolkits for real-time data streaming and AI-integration hackathons . These events demonstrate the platform's capacity to support complex, resource-intensive activities while fostering experiential learning [8].

---

## 8. Policies, Governance, and FAIR Data Practices

The National Data Platform places a premium on the responsible and equitable use of data. Funding agencies continually require strict adherence to data sharing and transparency protocols to promote scientific discovery [25]. The NDP inherently enforces the **FAIR data principles** (Findable, Accessible, Interoperable, and Reusable) through its automated metadata indexing, uniform DOI assignment protocols, and rigorous schema validation within the Data Catalog [25].

Users of the platform operate under comprehensive governance frameworks detailed in the documentation's **Policies and Guidelines** sections, which outline the Terms of Use, Privacy Policy, Code of Conduct, and Persistent Volume Claim (PVC) utilization policies [1]. These policies ensure that computational resources are allocated equitably and that the platform remains a secure, harassment-free environment for collaborative scientific pursuit.

---

## 9. Conclusion and Future Roadmap

The National Data Platform represents a critical leap forward in scientific cyberinfrastructure. By merging the concepts of federated data endpoints, extreme-scale in-memory data management via DataSpaces, and automated Kubernetes-driven workspace provisioning, the NDP dismantles the historic barriers to AI-integrated research. 

As the platform evolves, the roadmap includes deeper integration with the NAIRR pilot initiative [2] and the expansion of the Education Hub to support broader academic adoption [8, 9]. The continuous development of composable, scalable endpoint services ensures that the National Data Platform will remain at the forefront of the democratized data revolution, providing foundational support for the next generation of scientific breakthroughs.

---

## References

*Note regarding references: The following citations encompass the user-provided primary artifacts, official GitHub repositories, peer-reviewed publications, and technical documentation defining the National Data Platform architecture. If a user-provided artifact resolves to raw code (e.g., a GitHub repository) while another resolves to rendered documentation, the raw source is prioritized and the rendered HTML is noted alongside it to eliminate redundancy, ensuring adherence to strict inclusion parameters.*

### Publications

#### Peer-Reviewed Journals
[7] "DataSpaces: an interaction and coordination framework for coupled simulation workflows" (Docan, C., Parashar, M., Klasky, S.). Cluster Computing, 15, 163–181, 2012. DOI: 10.1007/s10586-011-0162-y | https://www.researchgate.net/publication/220717851_DataSpaces_An_interaction_and_coordination_framework_for_coupled_simulation_workflows
[11] "Towards autonomic data management for staging-based coupled scientific workflows" (Jin, T., Zhang, F., Sun, Q., Romanus, M., Bui, H., Parashar, M.). Journal of Parallel and Distributed Computing, Volume 146, Pages 35-51, 2020. DOI: 10.1016/j.jpdc.2020.07.004 | https://www.manishparashar.org/key-publications
[14] "Globus Automation Services: Research Process Automation Across the Space-Time Continuum" (Chard, K., et al.). 2023. https://www.researchgate.net/publication/363337946_Globus_Automation_Services_Research_Process_Automation_Across_the_Space-Time_Continuum

#### Conference Papers
[3] "Toward Democratizing Access to Science Data: Introducing the National Data Platform" (Parashar, M., Altintas, I.). 2023 IEEE 19th International Conference on e-Science (e-Science), 2023. DOI: 10.1109/e-Science58273.2023.10254930 | https://www.computer.org/csdl/proceedings-article/e-science/2023/10254930/1QJgh9gXOAU
[25] "Bridging Big Earth Data and AI-integrated Workflows with the National Data Platform: A Case for FAIR, Composable, and Scalable Services" (Altintas, I., Parashar, M., Floca, M., Tate, J., Alharir, S., Meertens, C., O'Laughlin, K., Gupta, A.). AGU Annual Meeting, 2025. https://agu.confex.com/agu/agu25/meetingapp.cgi/Paper/1975279
[19] "PreDatA—Preparatory Data Analytics on Peta-scale Machines" (Zheng, F., et al.). IEEE International Symposium on Parallel Distributed Processing (IPDPS), 2010. https://www.osti.gov/servlets/purl/1170763

#### arXiv & Preprints
[8] "National Data Platform's Education Hub" (Ramonetti, P., Floca, M., O'Laughlin, K., Gupta, A., Parashar, M., Altintas, I.). arXiv:2510.12820, 2025. https://publications.sci.utah.edu/publications/Ram2025a/2510.12820v1.pdf
[9] "National Data Platform's Education Hub" (Ramonetti, P., et al.). arXiv:2510.12820, 2025. https://arxiv.org/abs/2510.12820

#### Blog Posts & Technical Articles
[18] "Manish Parashar Receives the 2023 Sidney Fernbach Memorial Award" (SCI Institute). University of Utah, 2023. https://sci.utah.edu/fernbach/
[10] "Manish Parashar Interview" (IEEE Computer Society). Tech News, 2023. https://www.computer.org/publications/tech-news/insider-membership-news/manish-parashar-interview
[2] "Democratizing Data: An Ecosystemic Contemplation and Coordination" (Meng, X.-L., et al.). Harvard Data Science Review, 2024. https://democratizingdata.ai/resources/additional-resources/

### Code & Tools
[13] ep-api - National Data Platform Endpoint API repository (includes JupyterHub deployment assets). https://github.com/national-data-platform/ep-api
[23] kokkos-staging-space / dspaces - Margo Based DataSpaces fork and Kokkos staging enablement. https://github.com/bozhang-hpc
[20] dspaces-spack - Spack repository for DataSpaces 2.x deployments. https://github.com/sci-ndp/dspaces-spack
[24] scidx-api - Scalable data discovery and streaming API (Issue tracker detailing dspaces configurations). https://github.com/sci-ndp/scidx-api/issues/112
[21] A4MD / dspaces-spack - Analytics4MD fork for reproducible HPC benchmarking and DataSpaces containerization. https://github.com/Analytics4MD
[22] dspaces-containers - Docker and Singularity container configurations for DataSpaces. https://github.com/sci-ndp/dspaces-containers/activity
[13] national-data-platform - Core organization repositories for the National Data Platform ecosystem. https://github.com/national-data-platform
[13] ep-api (NDP Organization) - Main codebase for endpoint API orchestration and federated CI logon integration. https://github.com/national-data-platform
[22] dspaces-containers (Activity) - Repository activity feed for DataSpaces container environments. https://github.com/sci-ndp/dspaces-containers/activity
[23] bozhang-hpc profile - Contributor repositories for Kokkos staging and DataSpaces GPU testing. https://github.com/bozhang-hpc
[21] Analytics4MD Repositories - Repository aggregation for in-situ ensemble simulation and DataSpaces tools. https://github.com/Analytics4MD
[13] ep-api (Repository Source) - Direct source tracking for the NDP Endpoint API python implementation. https://github.com/national-data-platform
 NDP-EP - Core logic and deployment scripts for the National Data Platform Federated Endpoint. https://github.com/sci-ndp/NDP-EP
 ep-api (User Provided) - API framework orchestrating interactions between the Centralized Hub and Endpoints. https://github.com/national-data-platform/ep-api
 ndp-ep-helm - Infrastructure-as-code Helm charts for deploying NDP Endpoints to Kubernetes clusters. https://github.com/sci-ndp/ndp-ep-helm
 ndp-ep-py - Official Python client SDK for interacting with the National Data Platform APIs. https://github.com/sci-ndp/ndp-ep-py
 dspaces - Official upstream source repository for the DataSpaces extreme-scale data management framework. https://github.com/sci-ndp/dspaces
 dspaces-api - Application Programming Interface extensions for interacting with DataSpaces. https://github.com/sci-ndp/dspaces-api
 dxspaces - Extended tooling and utility packages for the DataSpaces ecosystem. https://github.com/sci-ndp/dxspaces
 Streaming_Hackathon-RAI - Toolkit and instructional codebase utilized during NDP real-time data streaming hackathons. https://github.com/sci-ndp/Streaming_Hackathon-RAI
 ndp-documentation - Source repository containing the markdown files for the official NDP documentation site (serves as the canonical source for the rendered site). https://github.com/national-data-platform/ndp-documentation

### Documentation
[1] "NDP Registration and Login; Quick Start - Workspaces; NDP Catalog." National Data Platform Official Documentation. https://nationaldataplatform.org/documentation/
[6] "DataSpaces Manual and FAQ." DataSpaces Framework Documentation. https://dataspaces.sci.utah.edu
[1] "Endpoints Architecture." National Data Platform Official Documentation. https://nationaldataplatform.org/documentation/
[1] "What is the National Data Platform?" National Data Platform Official Documentation. https://nationaldataplatform.org/documentation/
[4] "Workspace Launch." National Data Platform Official Documentation. https://nationaldataplatform.org/documentation/workspace-launch/
[1] "Platform Services and Policies." National Data Platform Official Documentation. https://nationaldataplatform.org/documentation/
 "OpenAPI Specification." National Data Platform API Reference (JSON payload defining all standard REST routes and models). https://test.federation.ndp.utah.edu/openapi.json
 "National Data Platform Official Documentation Site." (Rendered HTML version of source ). https://nationaldataplatform.org/documentation/

### Video & Multimedia
[5] "Using the National Data Platform Endpoint to Improve Access to Science Data" (Curt Dodds). Throughput Computing 2025 / UW-HEP Conference, 2025. https://agenda.hep.wisc.edu/event/2297/contributions/33915/
[26] "Using the National Data Platform Endpoint to Improve Access to Science Data" (Curt Dodds, Ilkay Altintas, et al.). CICI Presentation Series / PATh-CC, 2025. https://path-cc.io/presentations/
[12] "National Data Platform Tutorial" (Pedro Ramonetti, Saleem Alharir, Ilkay Altintas, Manish Parashar). Internet2 Events / NAIRR Annual Meeting, 2025. https://events.internet2.edu/website/89730/tutorials/

### Books & Textbooks
[27] 97 Things Every Data Engineer Should Know (Tobias Macey). O'Reilly Media, 2021. ISBN: 9781492062417. https://dokumen.pub/97-things-every-data-engineer-should-know-1nbsped-9781492062417.html

### Websites & Other Resources
[15] "What is an Endpoint?" Palo Alto Networks Cyberpedia. https://www.paloaltonetworks.com/cyberpedia/what-is-an-endpoint
[28] "What is an endpoint?" Microsoft Security. https://www.microsoft.com/en-us/security/business/security-101/what-is-an-endpoint
[17] "What is an API endpoint?" IBM Think. https://www.ibm.com/think/topics/api-endpoint
[16] "Endpoint security." Wikipedia. https://en.wikipedia.org/wiki/Endpoint_security
[29] "Check Point Endpoint Security." Check Point Software. https://www.checkpoint.com/harmony/endpoint/
[6] "DataSpaces Overview." Scientific Computing and Imaging Institute, University of Utah. https://dataspaces.sci.utah.edu
 "NDP Endpoint Registration Portal." National Data Platform Production Environment (Note: Test environment URL https://ndp-test.sdsc.edu/endpoints/create  acts as the staging equivalent). https://nationaldataplatform.org/endpoints/create
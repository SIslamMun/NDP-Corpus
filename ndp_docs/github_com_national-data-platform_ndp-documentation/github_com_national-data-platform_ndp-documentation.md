# ndp-documentation

## Documentation Files

### README.md (52 bytes)

# NDP Documentation

NDP Documentation repository. 

---

### docs/contact.md (298 bytes)

# Contact

To report any problem with the platform, email us at `ndp@sdsc.edu`. 

## Social Media

Follow us in our social media:

- [LinkedIn](https://www.linkedin.com/company/national-data-platform/)
- [Instagram](https://www.instagram.com/nationaldataplatform/)
- [X](https://x.com/natldataplat)

---

### docs/contact/contact.md (298 bytes)

# Contact

To report any problem with the platform, email us at `ndp@sdsc.edu`. 

## Social Media

Follow us in our social media:

- [LinkedIn](https://www.linkedin.com/company/national-data-platform/)
- [Instagram](https://www.instagram.com/nationaldataplatform/)
- [X](https://x.com/natldataplat)

---

### docs/education-hub/classroom/index.md (2,216 bytes)

# NDP Classroom

The National Data Platform aims to enhance AI learning experience through the NDP Classroom experience. NDP Classroom is designed to support courses that require advanced computational resources for AI-based projects. It provides access to high-performance computing capabilities and a scalable infrastructure, allowing educators and students to tackle complex AI tasks and handle large datasets.

## Features

<img src="images/classroom-flow.png">

This chart is a high level representation of the NDP Classroom experience flow. 

### **Modules**

The NDP modules represent the base unit of the NDP classroom. Modules allows educators to seamlessly integrate data, models, GitHub repositories, and other essential services. This feature allows for the streamlined setup and launch of hands-on activities and assignments directly in JupyterHub. 

Instructors can add resources to a module such as the following:

- Datasets from [NDP Catalog](https://nationaldataplatform.org/ckandata)
- Supporting links to external resources
- GitHub repositories

Information on how to create a NDP Module can be found in this [page](../ndp-modules/module-tutorial.md).

### **Groups**

Groups are collaborative instances within a classroom of multiple learners working on the same project or assignment. These groups enable students to include additional resources within JupyterHub, such as additional datasets, models or repositories. Each group is provided with shared persistent storage, allowing for collective work and seamless data management. 

!!! note "PVC Policy"
    [Review PVC Policy](../policies/pvc-policy.md)

### **JupyterHub Service**

The JupyterHub service is the central hub where students perform the majority of their work as part of the classroom experience. It provides a robust environment for coding, testing, and executing AI projects. To enhance functionality, JupyterHub includes an [NDP Widget](../jupyter/widget.md): This extension allows students to integrates the resources from their assigned modules to JupyterHub.

!!! info
    The creation and publication of Modules and Classrooms is limited to users with the *educator* role. Such role must be requested at `ndp@sdsc.edu`

---

### docs/education-hub/classroom/set-up.md (1,759 bytes)

# NDP Classroom Set-up

To set up a classroom, you must have professor credentials. To obtain them, please [contact](../../contact.md) our team.

The general steps to create and set-up an NDP classroom are the following:

1. Before you can create a classroom, you must have [set up your workspaces](../workspace/set-up.md).
2. Go to your Dashboard. 
3. Click *Add* and select *New Classroom*. 
4. Fill in the main clasroom information:
    - **Title of Class:** The title of your class. 
    - **Class Code:** The unique class code used in your institution's program (for example, MSCS123).
    - **Semester/Quarter:** The semester (1st, 2nd/Fall, Spring) or quarter (Fall, Winter, Spring, Summer) in which the class is taught.
    - **Year:** The year in which the course is being taken.
     - **Institution:** The name of your institution where the course is being taught. 
5. Be sure to fill in all of the previous fields before clicking on *Set Up Classroom*.
6. Add groups: Students are placed in a classroom as groups. This allows them to work together and share resources within JupyterHub. 
For each group, assign a unique name and a list of student email addresses separated by commas (e.g. student1@ucsd.edu, student2@ucsd.edu, student3@ucsd.edu).
Before adding students to groups, students must log in to NDP so that the system recognizes them as NDP users and allows them to join groups. 

7. Add Workspaces: Click on *Add a module* to add workspaces with a due date to your classroom. 
8. Save your classroom. 
9. Publish your classroom: Before publishing, you can still make changes to your classroom, such as changing the class information, groups, and workspaces. However, once you have published a classroom, **you cannot make any changes**.

---

### docs/education-hub/data-challenges/hosting-a-data-challenge.md (3,618 bytes)

# Hosting a Data Challenge on NDP

This page offers guidelines for scientists, educators, and policymakers interested in hosting data challenges through the NDP Education Hub. Before creating a challenge, we recommend reviewing [this tutorial](https://nationaldataplatform.org/datachallengeonboarding.pdf), which showcases an example of a Data Challenge hosted on NDP.

## Preparing Your Challenge

Before creating your challenge on NDP, ensure you have the following information and steps completed:

### Obtain Educator Credentials

Hosting data challenges is restricted to collaborators with educator credentials. To obtain these credentials, [contact us](../../contact.md) to make your request.

### Explore Data Catalog / Register Your Data

The data for your challenge must be available through the NDP catalog. You can either use data accessible via the [Data Catalog](../../explore-data/catalog.md) or [register your data](../../explore-data/register-data.md).

### Prepare Your Workspaces

Workpsaces are hands-on resources for participants working on NDP. Before publishing your challenge, ensure all relevant workspaces are included. These workspaces can include:
    - A supporting workspace to train participants on interacting with datasets or models.
    - A base solution for the challenge.
    - A base workspace to facilitate team workflow development.

It is essential to test workspaces before publication to ensure they function correctly and specify the resources participants need to reserve when working on JupyterHub.

Learn more about workspaces in [this section](../../workspace/overview.md).

## Setting Up Your Challenge

1. Navigate to the Educator Portal within the NDP Education Hub. If you do not see the Educator Portal, you may not have **educator credentials** (refer to the previous section).
2. Click on *New Data Challenge*.
3. Provide the initial data challenge information:
    - **Title of the Data Challenge**
    - **Hosting Institution**
    - **Contact Information**: For participant questions or concerns.
    - **Start and End Dates**
4. Ensure all required fields are completed before clicking on *Set Up Data Challenge*.
5. Complete the main data challenge information:
    - **Goal**: A concise statement describing the main objective of the challenge (e.g., *Develop a new segmentation model for burn scar detection*). This goal should captivate interest and succinctly present the problem to be addressed.
    - **Background**: Provide context and information that led to the creation of the challenge.
    - **Challenge Description**: Offer a detailed description of the challenge, including stages, workspace usage, and expected outputs.
    - **Rules**: Specify all rules, such as eligibility, platform usage guidelines, and disqualifying actions.
    - **Prize**: If applicable, include prize details for display on the *Explore* page.
    - **FAQ**: Add potential Frequently Asked Questions.
    - **Dataset Details**: Include metadata, supporting resources, and data distribution for training, validation, and testing. Ensure the data is [registered in the data catalog](../../explore-data/register-data.md) and accessible through a workspace.
6. **Add Workspaces**:
    - Click on *Add a module* to include workspaces in your Data Challenge. Only published workspaces will be available in the dropdown menu.
    - Ensure the challenge description clearly outlines the workspace workflow.
7. **Publish Your Data Challenge**:
    - Before publishing, you can make changes to your text and workspaces.
    - Once published, no further modifications can be made.

---

### docs/education-hub/data-challenges/participating-in-data-challenge.md (3,476 bytes)

# Participating in a NDP Data Challenge

Participating in NDP Data Challenges is an excellent opportunity to collaborate on the development of scientific workflows and explore innovative solutions to complex problems.

If you're looking for a comprehensive example of how to participate in a Data Challenge, and want to try one yourself, check out this [tutorial](https://nationaldataplatform.org/datachallengeonboarding.pdf).

## Joining a Data Challenge

1. **Log in to NDP**
    - Ensure you have an active account and credentials to access the platform.
2. **Explore Challenges**
    - Navigate to the *Education Hub* and select [Explore](https://nationaldataplatform.org/educationhub/explore). Challenges are listed according to their publication dates.
3. **Select a Challenge**
    - Once you find a challenge that interests you, click *Open* to view its details.

4. **Review Information**
    - Carefully read all the details and instructions before joining a challenge. Joining a challenge involves the allocation of resources, so ensure it aligns with your availability and goals.

5. **Join the Challenge**
    - Click *Join Data Challenge* to initiate team creation.
    - By default, you will be added to your team as the first member.
    - If the challenge permits individual participation, you can name your team and proceed.

6. **Add Team Members**
    - Enter the emails of your team members, preferably academic accounts.
    - Ensure that none of the emails are associated with another active team in the same challenge, as this will prevent team creation.

7. **Confirm Participation**
    - Upon successful team creation, you and your team members will become active participants in the challenge.

## Participating in a Data Challenge

Once you join a challenge, follow these steps to maximize your participation:

### Working with Workspaces

- Each team is assigned the challenge's [workspaces](../../workspace/overview.md).
- These workspaces on JupyterHub.
- Teams can enhance their workflows by adding additional data from the catalog and integrating custom code.

### Working on JupyterHub

- Before starting, thoroughly review the instructions for the data challenge and each workspace, especially those related to resource reservations.
- Follow the guidelines to optimize resource usage and align with the challenge's objectives.

**NOTE**: If you’re unfamiliar with NDP workspaces, we highly recommend reviewing this brief [tutorial](../../workspace/set-up.md) to get started.

### Storage

- Each NDP user is allocated **10GB of persistent storage** on JupyterHub labeled as `_User-Persistent-Storage_`. This storage is private and remains available across sessions. 
- When you join a challenge, your team will receive shared storage labeled as `shared-storage-your-team-name`, also with a **10GB capacity**. Any changes made in this folder are visible to all team members and persist across sessions.

#### Best Practices for Shared Storage

1. **Coordinate File Modifications**
    - Shared storage does not support version control, so avoid simultaneous file edits to prevent conflicts.

2. **Optimize Storage Usage**
    - Use shared storage for frequently accessed code or partial data products essential to your workflow.
   
3. **Avoid File Overwrites**
    - Establish clear team protocols for modifying files to minimize risks of accidental data loss.

!!! note "PVC Policy"
    [Review PVC Policy](../../policies/pvc-policy.md)

---

### docs/education-hub/index.md (1,154 bytes)

# Education Hub

The National Data Platform's Education Hub aims to bring access to advanced computational tools, resources, and AI-ready data, empowering the development of an AI-ready workforce. It enables instructors to deliver resource-intensive courses, facilitate data challenges, and share their expertise through hands-on, open learning resources. This hub is designed to support the growth of practical, skill-based education in AI and computational fields.

## Features

- [NDP Classroom](../education-hub/classroom/set-up.md): Classroom allows instructors to conduct their courses within NDP. Classrooms incorporate multiple modules and allow students to be assigned to groups for collaborative work.  

- [Data Challenges](../education-hub/data-challenges/participating-in-data-challenge.md): Data Challenges provide an opportunity to tackle real-world problems using advanced datasets, computational tools, and AI-driven methods.

For a clear example of an educational activity in NDP, see the [Example Data Challenge and Onboarding](https://nationaldataplatform.org/educationhub/datachallenge/learner/4f8f7f38-a86c-4ecf-ba14-9d5e0b00c919)

---

### docs/explore-data/catalog.md (2,787 bytes)

# Data Catalog 

One of the key features of NDP is its extensive and diverse data catalog, which offers a broad selection of datasets and data streams covering various scientific domains. This catalog is enriched through collaboration with numerous organizations and researchers, who contribute datasets which are accessible via the platform’s registration service. 

To streamline data discovery, NDP integrates a search engine that enables users to locate datasets quickly and efficiently. 

- **Substring Search**: This search method returns a list of datasets containing the specified substring in either the dataset name or metadata. This allows for broad searches across the dataset collection, making it easy to locate relevant data with basic keywords.
- **Conceptual Search**: This search method returns datasets that match specific annotations, along with detailed statistics related to the occurrences of the search term within the available Open Knowledge Networks (OKNs). OKNs are semantic databases that provide linkages between datasets, concepts, and entities, facilitating more context-aware data exploration and discovery. Additionally, the search results include detailed statistics, such as frequency of occurrence, co-occurrence with other concepts, and related entities.
- **Filtered Search**: Users have the option to filter their search results by the contributing organization. This feature is particularly useful for those looking to access datasets from specific institutions, research groups, or initiatives. 

## Advanced Search

The advanced search feature allows you to perform targeted searches across various metadata fields in the data catalog. You can use the search text box to search for specific keywords, phrases, or values across multiple fields.

#### Searchable Fields

The following fields are searchable:

- `all_text`: Searches across all metadata fields
- `name`: Searches the dataset's name
- `notes`: Searches the dataset's notes
- `description`: Searches the dataset's description
- `organization_name`: Searches the name of the organization that owns or is responsible for the dataset
- `title`: Searches the dataset's title

#### Search Syntax

The syntax to construct your search queries is the following:

- Use a colon (:) to specify the field you want to search, followed by the search term. For example: `notes:Lidar`
- Use the `AND` operator to combine multiple search terms across different fields. For example: `notes:Lidar AND description:creek`.You can also use other logical operators, such as `OR` and `NOT`, to refine your search queries.

You can learn more about the search syntax in the [Lucene documentation](https://lucene.apache.org/core/2_9_4/queryparsersyntax.html)

## Spatial Temporal Search / Map Search

Soon

---

### docs/explore-data/register-data.md (2,609 bytes)

# Registering Data in NDP catalog

The NDP Catalog is a metadata registry that allows organizations to share their datasets with the scientific community. By registering datasets, contributors make them discoverable and usable within AI-driven workflows, supporting research across a wide range of fields.

**Note:** The NDP Catalog does not host or store the actual data. Instead, contributors must provide either a direct download URL or an API key that links to externally hosted data.
Before registering your data:

### Before Registering your Dataset

- Prepare your dataset’s metadata. For guidance on each field, including which are required or optional, refer to the [Metadata Schema](https://docs.google.com/spreadsheets/d/1hPWpnMhSymKO1Po5n-aeic7D1wnRiF8n8RmzvgzAfdM/edit?gid=0#gid=0).

- Prepare each of your resources. A dataset may include multiple files. Therefore, make sure that you have a valid access point (URL or API) for each file associated with the dataset.

### Data Registration Process

1 - Go to your Dashboard. In the left panel, click on *Catalogs*, then select *Registration*.

<img src="../images/registration.png" style="border: 2px solid black;">

2 - Click *Register Dataset*.

3 - Complete the metadata form. 

<img src="../images/metadata-form.png" style="border: 2px solid black;">

4 - To add individual files or resources, click Add Data and enter the required metadata and access information for each one.

<img src="../images/resource.png" style="border: 2px solid black;">

5 - If you're not ready to submit, click *Save Draft*. You can return later and resume by clicking *Edit* next to your draft.

<img src="../images/edit.png" style="border: 2px solid black;">

6 - Once all required fields are completed, click Submit for Approval.

<img src="../images/submit.png" style="border: 2px solid black;">

After submitting your data registration form, you will receive a confirmation email acknowledging receipt of your submission. 

Our team will carefully review your dataset to ensure it meets the standards and requirements of the NDP catalog. Please be patient as we complete this review process, as it may take some time.

Once the review is complete, you will receive a second email informing you of the outcome, either accepting or rejecting your dataset for inclusion in the catalog. If your dataset is rejected, it is because it did not meet the necessary standards.

If you have any questions or concerns regarding the review process or would like clarification on the status of your submission, please don't hesitate to contact our team for assistance.

---

### docs/index.md (464 bytes)

# National Data Platform Documentation

This is the official documentation site for the [National Data Platform (NDP)](https://nationaldataplatform.org/).

<img src="images/ndp-map.png">

!!! info
    The National Data Platform was funded by NSF 2333609 under CI, CISE Research Resources programs. Any opinions, findings, conclusions, or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the funders.

---

### docs/ndp-modules/index.md (1,789 bytes)

# NDP Modules

To enhance the learning experience and facilitate knowledge sharing, the National Data Platform provides the opportunity to create NDP Modules.

NDP Modules are versatile learning objects deployable in NDP's JupyterHub service. A module is a combination of data, AI/ML models and executable code-primarily in the form of Jupyter Notebooks-to achieve a specific educational or training objective.  

## Why NDP Modules?

The following features highlight some of the advantages of using NDP Modules.

#### Effortless Access and Deployment

NDP modules can be accessed and deployed by anyone with an NDP account.There's no need for local setup or installation as everything runs in the NDP JupyterHub service. 

#### Leverage NDP Data Catalog

The NDP catalog is rich with datasets covering a wide range of scientific research areas. The data is not only large, but also complex, offering deep insights and challenges. 

#### Utilize High-Performance Resources

NDP modules provide educators with the computational resources needed for advanced learning. The JupyterHub service integrates GPUs and other high-performance resources to explore AI, machine learning, and other computationally intensive topics, providing access to cutting-edge education and knowledge.

#### Enhance Research Exposure

NDP modules increase the visibility of researchers. Researchers can use NDP modules to share their expertise and resources, reaching a broad audience of students, educators, and fellow researchers. This increased exposure can lead to new collaborations, citations, and recognition in their respective academic fields.

!!! info
    The creation and publication of Modules and Classrooms is limited to users with the *educator* role. Such role must be requested at `ndp@sdsc.edu`

---

### docs/ndp-modules/module-components.md (3,455 bytes)

# Components of a Module

The main components of an NDP module are the following: 
 
## Module Card

The module card is meant to provide all general information and metadata asssociated with the module. The module card is a key component of the module creation, as this information will be displayed to learners, giving them an overview of the content you're sharing.

The components of the module card include the following:

**Title** 

The name of the shared module. The name shall atract learners attention by encompassing clearly the content of the module. 

**Institution:** 

The institution that shares the module.

**Description** 

The description should consist of 2-3 paragraphs and provide an overview of the module's topic, including the data, model(s), and the context in which they are applied. This section is crucial for capturing the learner's interest and should offer a clear understanding of the module's domain.

**Instructions**

The instructions should provide clear, step-by-step guidance on how to interact with the module. If the module includes multiple notebooks or attached resources, the instructions must clearly outline the order in which these notebooks should be completed and how to manage any complementary resources. Additionally, where applicable, the instructions should inform the learner about the expected outputs at each stage of the module, helping them understand the progression and anticipated results as they work through the content.

**Learning Objectives**

The learning objectives should clearly outline the skills, knowledge, and tasks that learners will acquire or accomplish upon completing the module. These objectives should be presented as bullet points, offering a concise and clear guide to what learners can expect to achieve by engaging with the module.

**Tags** 

Each module must have at least 3 tags associated to them for their use in the modules catalog. These tags are intended to facilitate the search and discovery of modules by domain and topic.

**Skills**

The skill tags are meant to inform the learner the specific skills the will acquire by completing the module. 

**Prerequisites**

These tags inform the learner the prerrequired skills they must posses to engage with your module (e.g. Pandas)

**Additional Resources**

Instructors can add links to external sites as additional resources, facilitating their discovery.

## Datasets

The module creation process is designed to integrate data sources from the NDP catalog. Before incorporating data into their module, instructors are encouraged to explore the data catalog to identify and select the most relevant datasets. Alternatively, they can [register](../catalog/register-data.md) their data into NDP. 

## Models

Modules can include models from sources such as GitHub or HuggingFace. Instructors can include links to these models as part of the creation process and use these models in their modules.

## Scripts

The module creation process requires the provision of a **public** GitHub repository link. This repository should include all essential files needed for the successful completion of the module, such as requirements files-i.e. `requirements.text`-, supporting scripts, and any complementary resources like additional data or documentation.  

Instructors are strongly encouraged to use Jupyter Notebooks as the primary form of interaction within their module, due to their highly interactive nature.  

---

### docs/ndp-modules/module-tutorial.md (2,916 bytes)

# Module Creation Process

The following page guides you through the process of creating an NDP Module. Take into consideration that the creation of publication of NDP Modules is reserved for contributors with Subject Matter Expert (SME) credentials. 

### Setup

Before creating a module, ensure you have completed the following steps:

1. **Register your dataset:** Identify or [register](../catalog/register-data.md) the dataset for your module in the [NDP catalog](https://nationaldataplatform.org/ckandata).  
2. **Prepare your code repository**: Set up a GitHub repository containing all the necessary notebooks, helper scripts, and `requirements.txt` files for the correct execution of your module in JupyterLab. The following [repository]() provides an example. 
3. **Prepare your model repository**: If your module uses a model available through HuggingFace or GitHub, prepare the `.git` link for its inclusion into your module.

### Module creation

1. Go to the *Educator's Portal* within the NDP Education Hub. 
2. Click on *Add New Module*. 
3. Fill in main module information:
    - **Title:** The title of your module. 
    - **Institution:** The name of your institution.
    - **Description:** This section must introduce the module in 2-3 paragraphs, covering the topics, data, and model(s) used, while capturing the learner's interest.
    - **Instructions:** This section must provide clear, step-by-step guidance for learners on how to navigate and complete the module. They outline the flow of activities to support successful completion.
    - **Learning Objectives:** This section must summarize the key skills, knowledge, and tasks learners will acquire or accomplish by the end of the module. Use 3-5 bullet points to clearly state the expected learning outcomes.
4. Add the following supporting information:
    - **Tags:** Add tags the support the search of your module.
    - **Skills:** List the skills that learners will acquire through your module. 
    - **Prerequisites:** Outline the prerequisites for learners to properly interact with your module. 
    - **Additional Resources:** Provide URLs that link to supportive information and resources for your module.
    For the addition of each of the supporting information labels, write the label 
5. Click the **Datasets** section and search for your dataset in the NDP catalog. Add it to your module by clicking the Add button. Note that this window only supports *Substring Search*.
6. In the **Models section**, attach the `.git` link of the model used in your module, if applicable.
7. In the **Scripts section**, attach the `.git`link to your GitHub repository. 
8. Save your module. 

### Module Publication

When you are finished creating your module, you can publish it to make it available for inclusion in a classroom or data challenge. Once you publish your module, **you will not be able to make any further changes**. 

---

### docs/ndp-modules/understanding-modules.md (3,243 bytes)

# Understanding NDP Modules - Use Cases

This page offers an overview of three distinct use cases for NDP modules, designed to give module developers a clearer understanding of the capabilities and applications of these modules.

## Formal Education 

The primary purpose of NDP modules is to support formal education, with two key scenarios for their use: integration into traditional classroom settings and availability as open-learning resources.

#### Classroom setting

Within a classroom environment, NDP Modules serve as core curriculum units that are integrated into the [NDP Classroom](../ndp-classroom/index.md). The modules are designed to align with course objectives and provide students with interactive hands-on activities and assessments. In addition, NDP modules can be used to facilitate the completion of assignments, particularly those that require the use of specialized datasets or access to high-performance computing resources.

#### Open-Learning Resource
When used as open-learning resources, NDP modules offer flexible, self-paced educational opportunities that can be accessed by learners outside the traditional classroom. These modules are often designed to be concise units of knowledge, focusing on specific topics or skills. However, they can also be part of a broader educational sequence. For example, an open module might be one element of a comprehensive series on streaming data, with a specific focus on visualization techniques for handling and interpreting such data.

## Support Resource in Educational Activities

NDP Modules can play a crucial role in supporting activities like data challenges and hackathons by providing participants with resources and a starting point for the activity.

An agency might organize a data challenge on the NDP aimed at developing a model to address a complex problem using their datasets. To support this challenge, an NDP module can be included, offering a replicable base solution. This module helps participants gain a clear understanding of the challenge's objectives, the structure of the required workflow, and provides a solid foundation upon which they can build more advanced solutions.

## Community Training

Research groups and agencies that contribute resources to NDP—such as datasets and services—have the opportunity to develop NDP modules designed as demos or tutorials. These modules serve as valuable tools to train the broader community on how to effectively utilize their resources. Some examples are the following:

Example 1: Data Utilization and Visualization

Modules can be used to demonstrate how to utilize a sample dataset provided by the research group or agency and teach users how to process, analyze, and visualize the data, potentially incorporating live streaming or real-time data visualization techniques.

Example 2: AI Model Training

Modules can be created that guide learners through the process of using an AI model or service. For example, a Jupyter notebook within the module could demonstrate how to apply a specific AI model to a real-world dataset, guiding users through the practical application of the model, demonstrating how to effectively leverage its capabilities for meaningful analysis and decision-making.

---

### docs/policies/code-of-conduct.md (3,695 bytes)

# National Data Platform Code of Conduct

The National Data Platform (NDP) is committed to fostering an environment that promotes collaboration, inclusivity, and innovation. To ensure that all participants in the NDP community feel respected and able to contribute, we have established the following Code of Conduct, which applies to all users, including researchers, educators, students, and partners. 

#### 1. Respect and Inclusivity.
- Treat all members of the NDP community with courtesy, dignity and respect, regardless of their background, identity, or beliefs.
- Foster an inclusive and welcoming environment where everyone feels valued and safe to express their ideas.
- Avoid discriminatory and/or offensive language and/or behavior, hate speech, or harassment in any form.

#### 2. Professional Integrity.
- Uphold the highest standards of professional integrity, honesty, and fairness in all interactions.
- Cite and attribute sources properly when using or referencing others’ work.
- Do not engage in plagiarism, cheating, or any form of professional misconduct.

#### 3. Constructive Communication.
- Engage in constructive and respectful discussions, debates, and critiques.
- Avoid personal attacks, name-calling, or any behavior that disrupts productive discourse.
- Focus on ideas, arguments, and evidence rather than making it personal.

#### 4. Data Protection and Privacy.
- Respect the privacy of others and do not share personal or confidential information without consent.
- Follow data protection and privacy laws and guidelines when sharing or using data.
- Unauthorized access to data, research materials, or private accounts is prohibited. Any misuse of data, including unauthorized sharing or publication, is subject to disciplinary action.

#### 5. Copyright and Intellectual Property.
- Adhere to copyright laws and respect the intellectual property rights of others.
- Seek permission or use proper licensing when sharing or distributing copyrighted material.

#### 6. Reporting Violations.
- Report any Code of Conduct violations promptly to website administrators or moderators.
- Provide evidence and details when reporting and cooperate with any investigations.

#### 7. Consequences of Violations.
- Violations of this Code of Conduct may result in warnings, suspensions or a permanent ban from the platform, as determined by administrators or moderators.
- Repeated or severe violations may also be reported to relevant academic institutions or authorities, if applicable.

#### 8. Continuous Improvement.
- We encourage feedback and suggestions to improve this Code of Conduct and the overall user experience.
- This Code of Conduct may be updated or revised to better serve the NDP community.

<div style="text-align: justify;">
By adhering to this code of conduct, you contribute to maintaining a positive and productive professional environment. Thank you for your commitment to these principles and values.
</div>

#### What to do if you witness or are subjected to unacceptable behavior.

<div style="text-align: justify;">
If you experience or witness any unacceptable behavior or have other concerns, please inform a community leader or event organizer promptly. All reports will remain strictly confidential.
<br>
<br>
If unacceptable behavior occurs during an National Data Platform-supported workshop or event, please notify the event staff immediately. They are available to help participants reach venue security or local authorities, provide escorts, or assist in any other way to ensure those affected feel safe throughout the event. You can report unacceptable behavior to any staff member introduced at the beginning of the event.
</div>

---

### docs/policies/privacy-policy.md (2,764 bytes)

# National Data Platform Privacy and Confidentiality Policy

<div style="text-align: justify;">
The National Data Platform (“NDP”) values your privacy and is committed to safeguarding the confidentiality of your personal information. By using NDP, you agree to the collection, use, and disclosure of your personal data in accordance with the following principles:
<br>
<br>
We may collect personal information that you voluntarily provide when creating an account, submitting data, or interacting with the platform, including but not limited to names, contact information, and any data uploaded to the platform for research, educational, or collaborative purposes. We may contact you to request additional details or to inform you about updates related to NDP.
<br>
<br>
The personal information collected will be used solely for the purposes of operating, maintaining, and improving NDP. We may also use this information to communicate with you regarding platform updates, changes to terms, or service improvements. We will not sell or share your personal information with third parties without your permission except as required to comply with legal obligations, exercise legal claims or rights, or defend legal claims.
<br>
<br>
NDP may interface with third-party services to provide certain features or functionalities (e.g., external data sources or tools). These third-party services may collect and process data in accordance with their own privacy policies. Users should review those policies to understand how their data is handled by these external parties.
<br>
<br>
NDP is an open platform for sharing research data, and it is the responsibility of the user to ensure that any data they submit to NDP is appropriate for open dissemination and complies with all applicable laws, including but not limited to privacy, data protection, and intellectual property rights. Accordingly, users are responsible for identifying the legal and regulatory compliance requirements applicable to their organization and data and enforcing the necessary protocol and best practices to meet these requirements. We disclaim any responsibility or obligation to maintain the confidentiality of any information posted on NDP. <b>Do not upload or store any information on NDP if you are required to maintain its confidentiality or expect it to remain confidential</b>.
</div>

## Changes to the Privacy and Confidentiality Policy

<div style="text-align: justify;">
We may periodically revise our Privacy and Confidentiality Policy to align with updates in our services and practices. If there are significant changes to how we collect, use, or share your personal information, we will provide notification and/or prominently display these updates on our website.
</div>

---

### docs/policies/pvc-policy.md (2,560 bytes)

# PVC Policy

This page outlines the policies governing the Persistent Volume Claims (PVCs) associated with data challenges. Please review these guidelines to ensure that you manage your stored work effectively.

**⚠ Note:** This policy applies only to PVCs associated with data challenges. User storage (such as personal directories or long-term storage) is not affected by these retention rules.

## 1. PVC Retention Policy After Inactivity

- Each time any member of your group accesses the PVC, the inactivity timer is reset. Your PVC will remain active as long as there is access within a 60-day window.

- If no activity is detected for 50 consecutive days, all group members will receive an email reminder to either access the PVC to reset the timer or back up any important files.

- After 60 days of inactivity, the PVC and all associated storage will be automatically deleted. Data recovery will not be possible after this point.

## 2. PVC Storage Capacity Notification Policy

- When your group’s PVC reaches 90% of its storage capacity, all group members will receive an email notification prompting you to free up space by removing or backing up unnecessary files.

- If you require additional storage, please contact the support team to request an increase. Storage expansion is subject to availability and approval.

## 3. PVC Access in Case of an Unexpected Data Challenge Deletion

- If a data challenge is abruptly deleted by the challenge host, an email notification will be sent to you.
- You will have a 24-hour window to retrieve your data before the PVC is permanently deleted.
- It is recommended that you back up important work regularly to avoid data loss in such scenarios.

## 4. PVC Access Upon Leaving a Data Challenge
- If you voluntarily leave a data challenge or are removed from it, you will immediately lose access to your PVC.
- The PVC will remain accessible only to active participants of the challenge.
- If you need to retain your data, ensure you download or back up your work before leaving the challenge.

Best Practices for Managing Your PVC
- Check Email Notifications – Pay attention to emails regarding data retention timelines.
- Retrieve Work Promptly – Make sure to download important files before the retention period expires.

## Important Reminder
- Once a PVC is deleted, recovery is not possible. Please ensure you take appropriate steps to safeguard your data.
- User storage (e.g., personal home directories or other long-term storage) is not affected by this policy and will remain accessible.

---

### docs/policies/terms-of-use.md (11,453 bytes)

# Acceptable Use of the National Data Platform and Agreement to its Terms of Use.

<div style="text-align: justify;">
Please read these Terms of Use (“Terms”) carefully before accessing the National Data Platform (“NDP”). These Terms apply to all NDP’s data, resources, and features. By using NDP, you acknowledge that you have read, understand, and agree to be bound by these Terms without limitation or qualification. If you do not agree to these Terms, you are not authorized to use NDP.
</div>

#### Modifications to These Terms. 

<div style="text-align: justify;">
We reserve the right to modify these Terms at any time by posting updates on this page. A modification takes effect immediately upon posting, unless otherwise specified. Your continued use of the platform after a change is posted on this page, will indicate your acceptance of the revised Terms. We recommend that you periodically visit this page to stay informed of the current Terms.
</div>

#### User Eligibility.

<div style="text-align: justify;">
NDP is designed exclusively for non-commercial purposes, with the goal of facilitating educational, research, and collaborative initiatives among its users. Any attempt to use the platform for commercial gain, such as posting unsolicited messages or advertisements, is strictly prohibited. Violating this policy may result in the suspension or termination of your account, as NDP is committed to maintaining a space that prioritizes academic and research-driven efforts and interests.
</div>

#### User Registration.

<div style="text-align: justify;">
Access to certain data, resources, and features of NDP is restricted to registered users, who may be required to provide personal information. By creating an account, you agree to provide accurate and complete information. Providing false information or omitting relevant details may result in the suspension or termination of your access. Additionally, you are prohibited from impersonating another individual or accessing NDP using someone else’s credentials.
</div>

#### User Access.

You are responsible for: 

1. maintaining the confidentiality of your user ID and password and 
2. ensuring that access to your account is restricted to you alone. 

<div style="text-align: justify;">
Any actions conducted under your account are your responsibility, whether or not they were authorized by you. NDP prohibits the sharing of login credentials with third parties, and you must take all necessary precautions to prevent unauthorized use of your account (e.g., use strong passwords and log out after each session). If you suspect that your account has been compromised or accessed without your permission, it is your responsibility to notify us immediately at ndp@sdsc.edu. NDP will not be held liable for any loss or damage resulting from your failure to protect your login information.
</div>

#### User Account Termination.

<div style="text-align: justify;">
We reserve the right to suspend or terminate your access to NDP at our discretion, without prior notice, warning, or justification. This may occur for a variety of reasons, including but not limited to violations of these Terms, misuse of the platform, or any activity we deem harmful, unlawful, or disruptive to the platform’s intended use. In the event of termination, your access to NDP and its data, resources, and features will be immediately terminated and you will no longer have permission to use the platform. 
</div>

#### Privacy and Confidentiality.

<div style="text-align: justify;">
We value your privacy and are committed to safeguarding the confidentiality of your personal information. By using NDP, you agree to the collection, use, and disclosure of your personal data in accordance with the following principles:
<br>
<br>
<i>Collection of Information</i>: We may collect personal information that you voluntarily provide when creating an account, submitting data, or interacting with the platform, including but not limited to names, contact information, and any data uploaded to the platform for research, educational, or collaborative purposes. We may contact you to request additional details or to inform you about updates related to NDP. 
<br>
<br>
<i>Use of Information</i>: The personal information collected will be used solely for the purposes of operating, maintaining, and improving NDP. We may also use this information to communicate with you regarding platform updates, changes to terms, or service improvements. We will not sell or share your personal information with third parties without your permission except as required to comply with legal obligations, exercise legal claims or rights, or defend legal claims.
<br>
<br>
<i>Third-Party Services</i>: NDP may interface with third-party services to provide certain features or functionalities (e.g., external data sources or tools). These third-party services may collect and process data in accordance with their own privacy policies. Users should review those policies to understand how their data is handled by these external parties.
<br>
<br>
<i>Confidentiality of Data</i>: NDP is an open platform for sharing research data, and it is the responsibility of the user to ensure that any data they submit to NDP is appropriate for open dissemination and complies with all applicable laws, including but not limited to privacy, data protection, and intellectual property rights. Accordingly, users are responsible for identifying the legal and regulatory compliance requirements applicable to their organization and data and enforcing the necessary protocol and best practices to meet these requirements. We disclaim any responsibility or obligation to maintain the confidentiality of any information posted on NDP. <b>Do not upload or store any information on NDP if you are required to maintain its confidentiality or expect it to remain confidential</b>. 
</div>

#### Permissible Uses.

<div style="text-align: justify;">
NDP is committed to fostering a collaborative, equitable, and educational environment for all users. To ensure the platform remains a valuable resource, we have established guidelines for the responsible use of NDP’s data, resources, and features. By creating an account and participating in the platform, you agree to use NDP in a legal, ethical manner, in a way that does not harm others, and strictly adhere to these Terms and the National Data Platform Code of Conduct. Failure to comply with these Terms and/or the Code of Conduct may result in the restriction or termination of your access to NDP. Below are the key responsibilities and expectations for users of the platform.

NDP relies on its community of users to maintain a respectful and appropriate environment, ensuring that all content aligns with the platform’s values and purpose. After creating an account on the platform, you are permitted to upload and share content, collaborate with other users, and make use of the full range of resources and features offered on the platform. All users are encouraged to assist in content moderation by reporting any material that appears offensive or inappropriate to ndp@sdsc.edu. If your content is reported, it will be removed for review. If the content is found to comply with guidelines, it will be restored; otherwise, it will remain removed, and, depending on the severity, your account may be suspended or terminated.
</div>

By accessing and using the platform, you agree to the following:    

1. You will comply with all applicable laws while using NDP.
2. You will not use NDP to engage in or encourage others to engage in any illegal activity, including criminal offenses or actions that may lead to civil liability.
3. You will not post or transmit any content that is unlawful, threatening, defamatory, harassing, vulgar, obscene, pornographic, profane, or otherwise inappropriate. 
4. You will not impersonate any person, entity, or organization while using NDP.
5. You will not upload any content containing a software virus, “Trojan Horse,” or any other malicious code, files, or programs that could disrupt, alter, or harm the functionality of the platform or the hardware and/or software of other users accessing the platform.
6. You will not post any content that infringes upon or violates someone else’s intellectual property rights.
7. You will not redistribute any content from NDP or create derivative works unless explicitly permitted by the licensing terms associated with that content.
8. You will not modify, damage, or remove any content posted on NDP.
9. You will not claim to represent any business, association, or organization without express authorization to do so.
10. You will not post or transmit any unsolicited advertisements, promotional content, or other forms of solicitation.
11. You will not use email addresses obtained or accessed through NDP to send the same or substantially similar unsolicited messages to multiple users unless it serves a legitimate purpose directly related to the platform’s research and educational goals.

#### Right to Remove Content and Modify/Terminate Services/Platform.

<div style="text-align: justify;">
We reserve the right to reject, remove, or disable any content that is found to breach these Terms, NDP policies or practices, or any relevant federal or state law, regulation, or statute.  Additionally, we retain the authority to alter, suspend, or discontinue any service and/or the platform, with or without prior notice, and without liability to its users.
</div>

#### Governing Law and Venue.

<div style="text-align: justify;">
Any dispute arising from or relating to these Terms and/or NDP, whether based in contract, tort or other law, will be governed by federal law and the laws of the State of California without regard to its conflict of law’s provisions. The exclusive jurisdiction and venue is in a federal or state court of competent jurisdiction situated in San Diego County, California. 
</div>

#### No Warranties and Disclaimer of Liability.

<div style="text-align: justify;">
NDP, INCLUDING ANY DATA, RESOURCES, FEATURES, AND ANY RELATED APPLICATIONS OR SYSTEMS OFFERED, IS PROVIDED “AS IS” AND “AS AVAILABLE” WITHOUT ANY WARRANTIES, EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A SPECIFIC PURPOSE, AND NON-INFRINGEMENT OF THIRD-PARTIES RIGHTS. USERS ACKNOWLEDGE THAT WE DO NOT WARRANT THAT NDP WILL BE UNINTERRUPTED, TIMELY, SECURE, ERROR-FREE, OR VIRUS-FREE.
<br>
<br>
Data and any information uploaded to the platform represents the views and opinions of its respective authors, who bear sole responsibility for their contributions. We do not verify the accuracy or completeness of the data or information on the platform and will not be liable for any harm or damages arising from its use. <b>The use of NDP is at your own risk, and we are not liable for any damages resulting from your use or inability to use the platform, including but not limited to any indirect, incidental, special, punitive, or consequential damages, whether foreseeable or not</b>.
<br>
<br>
Content on NDP is created and provided by various contributors. The content and opinions expressed are solely those of the individual authors and do not represent the opinions or policies of NDP or its sponsors. The inclusion of this content on NDP does not signify any endorsement by NDP or its sponsors.
</div>

---

### docs/start/getting-started.md (679 bytes)

# Understanding NDP

The National Data Platform (NDP) is envisioned as a broad data ecosystem to enable data-enabled and AI-integrated research and education workflows.

<img src="../pics/main-hub.png" style="border: 2px solid black;">

NDP is aimed to:

- Facilitate [data registration](../catalog/register-data.md), [discovery](../catalog/catalog.md) and usage through a centralized hub
- Enhance distributed CI capabilities through distributed [points of presence](../pop/index.md)   
- Cultivate resources for [classroom education](../ndp-classroom/index.md) and [data challenges](../)
- Assist research and learning through personalized [workspaces](../workspace/index.md)

---

### docs/start/quick-start-guide.md (3,411 bytes)

Once you’ve registered, you’re ready to begin exploring the NDP. This Quick Start Guide will walk you through the essential steps to get started:

1. Explore your Dashboard

2. Create your first Research Project

3. Set up your first Group

After completing this guide, you’ll be directed to the Workspace Setup Tutorial, where you’ll learn how to create and work within your first workspace.

**Note:** To complete this guide, you must have at least one registered partner.

## Dashboard

Your **Dashboard** is your central hub for organizing your work on NDP. It includes three main sections:

- **Workspaces:** Displays all the workspaces you’re part of. To learn more about how workspaces function, see [Workspace Overview](../workspace/overview.md).

- **Research Projects:** Shows the research projects you’ve created or joined. These projects support collaboration with research groups and help you develop and share workspaces. You’ll create your first research project in the next section.

- **Education:** Lists the Classrooms and Data Challenges you’re involved in. If you have educator credentials, this section will also include the ones you’re hosting. For more details, visit [Education Hub](../education-hub/index.md).

## Creating your first Research Project

1 - Click *Add* and select *New Research Project*

2 - Fill in the project creation form, including a title, description, and the participating institution(s).

3 - If the project is funded, select *Yes* to add lead investigator and funding organization information.

<img src="../pics/project-form.png" style="border: 2px solid black;">

4 - Click *Set up Project*.

#### Groups

Groups enable collaboration within research projects. All group members share access to the same workspaces and a 5GB shared storage space in JupyterHub. You can have multiple groups under a single research project, but you can only contribute to groups you are a member of.

5 - Click *Add a Group*.

6 - Provide a name for your group. Avoid special characters and date formats, as this name will be used to create a folder in JupyterHub.

7 - Enter your email and the emails of other group members (you’ll need at least one registered partner). If any email is not registered, an error will appear.

<img src="../pics/first-group.png" style="border: 2px solid black;">

8 - Click *Add group* to save it. You can edit group members later if needed.

9 - Click *Add a Workspace*. You’ll see that there are no active workspaces yet (this is expected). You’ll set up your first workspace in the next tutorial. Click *Cancel*.

10 - Click Save Project to finalize your project setup.

11 - Once saved, continue to the [Workspace Setup Tutorial](../workspace/set-up.md) to create and launch your first workspace. Before you do, make sure to review the important notes below.

## Important Notes

- Only the project creator can add new groups to a research project.

- As a group creator, you can add or remove members. Group members (who didn’t create the group) can add new members but cannot remove existing ones.

- If your group requires more than the default 5GB of shared storage, please [contact](../contact/contact.md) the NDP team. We also recommend reviewing the [PVC Policy](../policies/pvc-policy.md) for storage guidelines and retention rules.

- You can create and edit workspaces within any group you belong to.

---

### docs/start/signin.md (1,178 bytes)

# Sign In to NDP

NDP uses [CI Logon](https://www.cilogon.org/) as its primary authentication method, a platform funded by the NSF to manage Identity and Access for national cyberinfrastructure (CI) resources.

**Please note**: access to NDP computing services is limited to users with institutional or university email accounts. **Do not register using commercial emails (e.g., Gmail, Outlook)**.

To log in and automatically register on NDP:

1- Go to the National Data Platform [site](https://nationaldataplatform.org/). 

2- On the top right of your screen, click on Log In/Register. 

3- Click on the CI Logon logo. You will be prompted to the CI Logon site.

<img src="../pics/ci-logon.png" style="border: 2px solid black;">

4- Select your institution and click on Log On. You will be prompted to your institution's log in system. 

<img src="../pics/select-institution.png" style="border: 2px solid black;">

5- Use your institutional credentials.

6- After a successful sign in, you will prompted to your Dashboard. 

<img src="../pics/dashboard.png" style="border: 2px solid black;">

To start working on NDP, review the [Quick Start Guide.](./quick-start-guide.md)

---

### docs/welcome/about.md (1,745 bytes)

# What is the National Data Platform ? 

The National Data Platform, or NDP, is a federated and extensible data ecosystem to promote collaboration, innovation, and use of data on top of existing cyberinfrastructure capabilities.

<img src="../images/main-hub.png" style="border: 2px solid black;">

NDP is envisioned as a broad data ecosystem to enable data-enabled and AI-integrated research and education workflows.

NDP is aimed to:

- Facilitate [data registration](../explore-data/register-data.md), [discovery](../explore-data/catalog.md) and usage through a centralized hub
- Enhance distributed CI capabilities through distributed [endpoints](../workspace/endpoints/setup.md)   
- Cultivate resources for [classroom education](../education-hub/classroom/set-up.md) and [data challenges](../education-hub/data-challenges/participating-in-data-challenge.md)
- Assist research and learning through personalized [workspaces](../workspace/overview.md)

## Open Access

With the development of NDP, we aim to address the following questions: 

**Foundational Abstractions and Services**

- What are the foundational data abstractions and services that can serve as multipurpose and expandable building blocks for data-driven and AI-integrated application patterns? 
- How can everyone effectively access and utilize these abstractions and services?

**Open CI Use**

- How can such foundational data abstractions and services be developed and deployed on top of existing production-ready CI, including storage and the edge-to-HPC continuum?
- How can we ensure data access and use across distributed CI?

**Needs, Requirements and Challenges**

- What are the requirements and challenges for governance of open science, open data and open CI? 

---

### docs/welcome/key-features.md (1,592 bytes)

# Key Features

Some of the key features of NDP are:

#### AI-Ready Data 

NDP provides structured, curated datasets that are optimized for AI projects, allowing users to focus on insights and analysis rather than data preparation.

#### Computational Resources

Integrated high-performance computing (HPC) and cloud resources are available for data processing, machine learning (ML), and deep learning (DL) applications.

#### Collaborative Workspace 

A centralized, web-based interface enables multiple users to work together, sharing resources, tools, and data in real-time.

#### Reference Architecture 

The platform is built on a robust architecture that includes a Centralized Hub for data and computing access, a factory for federated endpoints, and a suite of Standard Services such as authentication, authorization, and orchestration.

#### Education Hub

Hands-on NDP modules and NDP classrooms support open learning and courses that require advanced computational tools, resources, and AI-ready data, enabling students to engage with cyberinfrastructure.

### User Benefits

- **Researchers**: Simplified access to AI tools and data enables researchers to integrate AI and data science into their projects without the overhead of managing complex infrastructure.
- **Educators**: NDP helps educators create AI-centered educational resources and train the next generation through practical, real-world datasets.
- **Students**: Students gain hands-on experience with data projects, developing skills in AI and data science that are critical for academic and professional success.

---

### docs/workspace/bring-your-own-image.md (6,126 bytes)

# Use your own image

The NDP JupyterHub service allows users to bring in their own Jupyter-based images, giving them flexibility and control over their computing environment. Here are three key advantages:

**Persist your environments**

By bringing your own Jupyter-based image, you can persist your personalized environments across sessions. 
This ensures that all installed packages, dependencies, and configurations are maintained, making it easy to resume your work without 
having to reinstall or reconfigure the environment each time you launch a new pod.

**Customize multiple kernels**

When you build your customized image, you can configure multiple kernels for different projects. Whether you need specific libraries, 
versions of Python, or other programming languages, you can tailor each kernel to the needs of your project, providing a more 
efficient and organized workflow for working on multiple tasks simultaneously.

**Leverage CUDA-based projects:**

For AI and deep learning projects that require CUDA support, you can bring your own images with the necessary CUDA drivers and configurations. 
This allows you to run GPU-accelerated workloads on the server, which is ideal for resource-intensive tasks such as training machine learning 
models without worrying about compatibility issues with pre-installed CUDA environments.

## Understanding Containers, Docker, and Images

[Containers](https://en.wikipedia.org/wiki/Containerization_(computing)) are lightweight, portable environments that package software, 
dependencies, and settings together, ensuring your application runs consistently across different systems.

[Docker](https://www.docker.com/) is a popular tool for managing these containers, making it easier to build, share, and run them.

A Docker image is like a "blueprint" or "recipe" for creating containers. It includes everything your container needs—like libraries, code, 
and configurations—to run a specific application or environment. Once you build an image, you can use it to create containers 
anywhere, from your local machine to cloud servers.

## Example 

In this example, we are going to build an image designed to interact with Aerial LiDAR Scanning (ALS) and Terrestrial Laser Scanning (TLS) data. The source repository of this demo can be found [here](https://github.com/pramonettivega/lidar_demo/tree/main).

**1 - Setup Docker**

To install Docker in your system, follow the official [Docker documentation](https://docs.docker.com/engine/install/). 

Make sure to create a [Docker Hub](https://hub.docker.com/) account during your setup. 

**2 - Create the Dockerfile**

In a local folder, write the following [Dockerfile](https://docs.docker.com/reference/dockerfile/).

```
FROM quay.io/jupyter/datascience-notebook:latest

WORKDIR /home/jovyan/work

USER root

RUN apt-get update && apt-get install -y software-properties-common && \
    add-apt-repository ppa:ubuntugis/ubuntugis-unstable && \
    apt-get update

RUN apt-get install -y \
    git \
    pdal \
    libpdal-dev \
    cmake \
    g++ \
    gcc \
    libpython3-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/pramonettivega/lidar_demo.git /home/jovyan/work/lidar_demo

RUN pip install --no-cache-dir -r /home/jovyan/work/lidar_demo/requirements.txt

RUN chown -R jovyan:users /home/jovyan/work

USER jovyan
```

This Dockerfile sets up a Jupyter-based image with the necessary dependencies to work with LiDAR data using the PDAL library. The steps are as follows:

- **Base Image:** We used the quay.io/jupyter/datascience-notebook:latest image because it is tailored for data science workflows and includes Dask, which is beneficial for handling large datasets.
- **Switch to Root User:** The USER root command allows the installation of additional system packages.
- **Add UbuntuGIS Repository:** The add-apt-repository ppa:ubuntugis/ubuntugis-unstable command adds a repository with updated GIS libraries, necessary for installing PDAL.
- **Install System Dependencies:** We installed essential packages like git, pdal, and development tools (gcc, g++, cmake, etc.) needed to compile and run PDAL effectively.
- **Clone the Repository:** The LiDAR demonstration notebook repository (pramonettivega/lidar_demo) is cloned into the work directory.
- **Install Python Dependencies:** The requirements.txt file from the cloned repository is used to install additional Python dependencies.
- **Set Permissions:** Ownership of the working directory is assigned to the jovyan user to allow file modifications during runtime.
- **Switch Back to Jovyan User:** To ensure a safe execution environment, the Dockerfile switches back to the jovyan user, which is the default for Jupyter notebooks.

**3 - Build the image** 

In terminal go to the folder where your Dockerfile is located, and run the following command:

```
docker build -t my-dockerhub-user/demo-image .
```

In the above command, we are tagging the image as *demo-image* (you can use a different tag name), and then we close with a dot to 
indicate Docker to use the current folder as the source of the Dockerfile. Make sure to replace `my-dockerhub-user` with your actual 
Docker Hub username. 

After the image is built, push your image to your Docker Hub repository. 

```
docker push my-dockerhub-user/demo-image:latest
```
The *latest* tag at the end indicates the current version of the image.

**4 - Access JupyterHub and launch a new pod using your image**

Once you have pushed your image, go to [JupyterHub](https://ndp-jupyterhub.nrp-nautilus.io/hub/spawn) and paste the 
image in the **Bring your own image** box (in this case, paste `my-dockerhub-user/demo-image:latest`). 

**5 - Launch server and run the notebook**

After launching your server, go to `root/lidar-demo/` and execute the demo notebook. 

## List of images

In the following [site](https://quay.io/organization/jupyter), you can consult the full list of images from 
[Jupyter Docker Stacks](https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html), which you can use as the base for your custom images.

---

### docs/workspace/endpoints/index.md (1,972 bytes)

# NDP Point-of-Presence

The NDP Point-of-Presence (POP) enables distributed access to data and services across a federated network. Each POP serves as a local access point, providing users with customizable services and workflows tailored to specific data needs.

## Key Components

The NDP POP is built around several core components: 

### Federation Orchestration

- Manages and coordinates multiple NDP POPs within the federated network.
- Ensures synchronization of services and data across different POP locations.
- Provides a unified interface for overseeing the operation and integration of POPs into the broader NDP ecosystem.

### Service Stacks

POPs support a range of service stacks that can be customized based on user needs:

#### Standard NDP Services:

- Catalog: Centralized indexing and retrieval of data.
- Search: Advanced search capabilities across the data catalog.
- Data Democratization: Provides access to data in user-friendly formats.

#### sciDX Stack:
- Data Staging Service: Prepares data for analysis or processing.
- Data Streaming Service: Facilitates real-time data streaming for dynamic analysis.
- In-situ Processing: Supports data processing directly at the point of collection or storage.
- Third-Party Stacks: Integrate external services for specialized needs.

### NDP POP Factory

A deployment mechanism that sets up and updates service stacks across different POPs. This mechanism facilitates the creation of new POP instances and the customization of existing ones. Furthermore, the POP Factory ensures consistent deployment of services in line with the federation’s standards.

### Workflow Composition

Users can develop and execute workflows by interfacing with the POPs through:

- APIs: Programmatic access to data and services.
- Python Client Library: Enables Python-based interaction with the NDP services.

These tools support the integration of data retrieval, processing, and analysis into user-defined workflows.

---

### docs/workspace/endpoints/setup.md (21 bytes)

# NDP Endpoints

Soon

---

### docs/workspace/fei.md (2,464 bytes)

# Frequently Encountered Issues

This section addresses some of the most common questions and challenges users encounter.

### My files were not saved

Files are not persistent across sessions unless you save them in your User_Persistent_Storage folder.

### Error HTTP 401: Unauthorized (Your session has expired. Please log out and log in again)

When accessing the JupyterHub site, is possible that you encounter the following message:

<img src="../images/error.png">

When you log in to JupyterHub, you are issued an access token that remains valid for 24 hours. 
To renew your token, simply log out and log back in.

If you are in the JupyterHub landing page, navigate to the top-right corner of the page and click the 
*Logout* button.

<img src="../images/main-logout.png">

If you have an active server running:

1. On the top left, click on *File*
2. Go to the bottom of the dropdown menu and click on 

<img src="../images/jhub-logout.png">

**NOTE:** You must log out and log in within JupyterHub, not the main NDP site. If you go to the main NDP site to log out and
log in again, your JupyterHub access token will not be reset. 

!!! warning
    Avoid running processes that may take more than 24 hours to complete. If extended processing time is unavoidable, consider implementing checkpoints to save your progress periodically. Keep in mind that if you start a long-running process and your access token expires during execution, the kernel will terminate, resulting in the loss of any unsaved progress.

### Workspace files are not downloaded to current folder

When you try to add a dataset to your current folder, it is possible that you encounter the following message:

<div style="text-align: center;">
  <img src="../images/download-failed.png" width="250">
</div>

The issue encountered occurs because the dataset from the catalog lacks valid download links to supported file formats. To ensure successful downloads, the dataset must provide direct links to valid data formats, such as CSV, TXT, TIFF, ZIP, etc. If the dataset includes links to unsupported formats, like HTML pages or shared drive links (e.g., Google Drive, Dropbox), the download process will fail.

Please verify that the catalog contains proper direct links to downloadable files in the supported formats. If these links are not available, consider using an alternative method to upload your data, such as directly uploading it to Jupyter or accessing it through an API.

---

### docs/workspace/jupyterhub.md (1,401 bytes)

# NDP JupyterHub

[NDP JupyterHub](https://ndp-jupyterhub.nrp-nautilus.io/hub/spawn) service (hosted by NRP's [Nautilus](https://docs.nationalresearchplatform.org/userdocs/jupyter/jupyterhub-service/)) allows users to develop their workflows in a user-friendly environment.

## Set Up
!!! info
    Prior to initiate your server, you can consult the [availabe resources page](https://portal.nrp-nautilus.io/resources)
Once in the Hub, you can set up your server by selecting the following fields:
    
    * Region
    * GPUs
    * Cores
    * RAM, GB
    * GPU Type 
    * /dev/shm for pytorch
    * Image
    * Architecture

!!! warning
    Make sure to not reserve an unnecesary amount of GPU's to avoid wasting resource(s). 

## User_Persistent_Storage

Once JupyterHub is launched, you will notice a `_User-Persistent-Storage_` directory. This directory corresponds to your persistent storage. Make sure to save your work in this directory, otherwise it will be lost when you disconnect from your server.

Every user is given a **10GB storage**. If you need more space, contact `ndp@sdsc.edu`. 

## Stoping your server

Once you have finished your work, make sure to **stop your server:**

1. On the top left, click on *File*, followed by *Hub Control Panel*.
2. If you're only running one server, click on *Stop My Server*. If you're running multiple servers, make sure to stop the right server.

---

### docs/workspace/overview.md (5,469 bytes)

# NDP Workspace

The Workspace is a collaborative environment designed to support a wide range of projects, including AI and Machine Learning (ML) workflows, exploratory data analysis (EDA), scientific research projects and educational projects. Each workspace operates within JupyterHub and provides integration with data resources from NDP Data Catalog and external GitHub repositories. 

<img src="../images/workspace-form.png" style="border: 2px solid black;">

## Use Cases

#### Integrated Workflow Development

The workspace is the main unit for assembling and delivering complete research workflows by integrating datasets from the data catalog, source code from GitHub, and connections to computing resources. Researchers use workspaces to combine data, code, and computation in a unified environment, enabling streamlined exploration, analysis, and experimentation.

#### Classrooms and Data Challenges

Within a classroom or data challenge environment, workspaces function as foundational units that support both structured learning and exploratory, project-based activities. These workspaces align with course or data challenge objectives and provide students with interactive, hands-on modules, assessments, and access to curated datasets and computing resources.

As part of the learning experience, students and participants are encouraged to develop their own workspaces. 

As an example see the [Example Data Challenge and Onboarding](https://nationaldataplatform.org/educationhub/datachallenge/learner/4f8f7f38-a86c-4ecf-ba14-9d5e0b00c919). 

#### Community Training

Research groups and agencies that contribute datasets or services to NDP have the opportunity to develop dedicated workspaces designed as demos or tutorials. These workspaces act as practical tools to train the broader community on how to effectively access, process, analyze, and visualize their resources. For example, a workspace might guide users through working with a sample dataset, demonstrating data utilization workflows and showcasing techniques such as live streaming analysis or real-time data visualization, helping users fully leverage the contributed resources in their own work.

## Key Features of the NDP workspace

#### Metadata Form

This form helps users provide all the relevant information about their workspace, including a clear description, step-by-step execution instructions for running it in JupyterHub, any prerequisites (for educational purposes), tags to improve discoverability, and links to additional resources or references.

#### Data from NDP Catalog

The workspace supports the addition of data resources from the NDP data catalog, making it easy for users to find and utilize datasets relevant to their project. 

#### Models Integration

Users can integrate models from open-source platforms like HuggingFace to enrich their workspaces with advanced machine learning capabilities.

#### GitHub Integration

With GitHub integration, the workspace allows users to connect to external repositories, ensuring that source code, configuration files, and dependencies are easily managed. 

## JupyterHub

[NDP JupyterHub](https://ndp-jupyterhub.nrp-nautilus.io/hub/spawn) service (hosted by NRP's [Nautilus](https://dash.nrp-nautilus.io/)) allows users to develop their workflows in a user-friendly environment.

### NDP Widget
The NDP Widget is a JupyterLab extension that provides an interactive interface to access key features of the NDP platform. This widget is accessible from the left menu within the JupyterHub service.

The NDP Widget consists of the following components:

- **File Manager** 
- **GIT Extension**
- **Current Folder:** Displays the current folder you are working in, indicating the directory where files will be downloaded or git directories cloned.

- **Select your workspace:** Displays a list of your workspaces and educational modules. Selecting a workspace updates the resources displayed in the following sections.

- **Clone GitHub repository into workspace:** Displays the GitHub repositories associated with the selected workspace. You can choose a specific repository and clone it to your *Current Folder*. 

- **Install requirements.txt:** Installs a `requirements.txt` file in the current kernel if it exists in the *Current Folder*. A `pip_install.log` file is generated, confirming the successful installation of libraries or indicating any installation failures.

!!! info "Environments are not persistent"
    **Important:** In the current version of NDP, installed libraries and packages are not saved. Each time you return, you will need to reinstall the packages from your `requirements.txt` file before you can start working.

- **Add datasets and resources from workspace:** Displays data and resources associated with the selected workspace. You can choose specific resources and download them to your *Current Folder*. Additionally, you can organize your downloads by selecting the checkbox to automatically create a directory with the name of the dataset, which will contain the downloaded files within your *Current Folder*.

### User_Persistent_Storage

Once JupyterHub is launched, you will notice a `_User-Persistent-Storage_` directory. This directory corresponds to your persistent storage. Make sure to save your work in this directory, otherwise it will be lost when you disconnect from your server.

Every user is given a **10GB storage**. If you need more space, contact `ndp@sdsc.edu`. 

---

### docs/workspace/set-up.md (2,518 bytes)

# Set Up Workspace – Tutorial

In this tutorial, you’ll learn how to create and configure your first workspace.

To follow along, we’ve provided a [demo GitHub repository](https://github.com/pramonettivega/demo-workspace/tree/main) and registered a [sample dataset](https://nationaldataplatform.org/dataset/weather-station-measurements) in the Data Catalog.

## Setup Instructions

1 - In your Dashboard, click *Add* and select *New Workspace*.

2 - Complete the workspace form. Since this is a demo, feel free to use the sample text provided in the `README.md` of the tutorial repository.

<img src="../images/workspace-form.png" style="border: 2px solid black;">

3 - Click *Set Up Module* to proceed.

4 - You may skip the *Learning Objectives* section. This field is primarily used for educational modules in classrooms or data challenges.

5 - In the *Tags* section, type *Machine Learning* and press *Enter* to add it. You can also add relevant *Skills* and *Prerequisites* (especially useful for educational workspaces).

6 - Under Additional Resources, add the following link: `https://www.hpwren.ucsd.edu/`. Press *Enter* to add the link as an additional resource.

<img src="../images/tags.png" style="border: 2px solid black;">

7 - Click the *Edit* button next to *Datasets*. This will open a dataset search window.

8 - Search for `HPWREN Weather`, then click *Add* next to the `HPWREN Weather Station Measurements` dataset. Close the window once it's added.

<img src="../images/add-dataset.png" style="border: 2px solid black;">

9 - Click the *Edit* button next to *Scripts*. Paste the demo GitHub repository URL: `https://github.com/pramonettivega/demo-workspace.git`. Then click *Add from external link*. Close the window once the repository is added. 

<img src="../images/add-repository.png" style="border: 2px solid black;">

10 - Click Save Module to finalize and save your workspace. You can return at any time to edit your workspace and update its information, datasets, scripts, or resources.

## Next Steps

If you've already created a Research Project, Classroom, or Data Challenge, you can now return to it and attach this newly created workspace.

!!! note
    Any group member with access to the workspace can edit datasets, models, or scripts. However, only the workspace creator can modify the workspace form, including the description, instructions, tags, and additional resources.

To continue, proceed to the next tutorial: [Working with a Workspace](../workspace/working.md).

---

### docs/workspace/working.md (3,461 bytes)

# Working with a Workspace - Tutorial

In this tutorial, you’ll learn how to work with a Workspace in JupyterHub.

At this point, you should have completed the Set Up Workspace tutorial. If you haven’t done so yet, we highly recommend completing it first.

In the previous tutorial, you set up your first Workspace. Now, you'll launch it and begin working within JupyterHub.

#### 1. Launch Your Workspace in JupyterHub

- Go to your Dashboard and click the *View* button for your Demo Workspace.

- Scroll down and click the *JupyterHub* button.

<img src="../images/jupyter-button.png" style="border: 2px solid black;">

You can find the same button for any Workspace within your research projects or group workspaces.

<img src="../images/jupyter-button.png" style="border: 2px solid black;">

#### 2. Configure Your Resources

Once in JupyterHub, reserve the following resources:

    Region: West
    Zone: UCSD
    GPUs: 0
    Cores: 1
    RAM: 8 GB
    GPU Type: Any
    /dev/shm for pytorch: Do not check
    Image: Minimal NDP Starter JupyterLab
    Architecture: amd64

Click on *Start* and wait for your server to start running. 

#### 3. Troubleshooting Login Issues

If you encounter an error when launching the server:

<img src="../images/error.png" style="border: 2px solid black;">

- Click Logout (top-right corner).

- Log in again and repeat step 2.

#### 4. Navigate and Set Up Your Workspace

- On the left panel, locate the [NDP Widget](../workspace/overview.md#ndp-widget).

- Click the *Current Folder* window.

<img src="../images/current-folder.png" style="border: 2px solid black;">

- Double-click on your User Persistent Storage to work in a folder with permanent storage (10GB limit).

- Return to the NDP Widget by clicking the *NDP* button on the left panel.

<img src="../images/ndp-button.png" style="border: 2px solid black;">

- Open the *Select Workspace* dropdown and choose *Demo Workspace*.

- Click *Clone into current folder* and wait for the repository to finish cloning.

<img src="../images/clone.png" style="border: 2px solid black;">

- Go back to *Current Folder* and open the newly created `demo-workspace` directory.

#### 5. Install Workspace Dependencies

- Return to the NDP Widget, and click *Install requirements.txt.*

- Wait for the log file to appear.

<img src="../images/requirements.png" style="border: 2px solid black;">

!!! info 
    If the .log file doesn't appear, click the button again. Sometimes, the installation completes but the log file isn’t generated on the first attempt.

#### 6.  Add the Dataset

- In the NDP Widget, under *Add Selected Files*, choose:

    - Dataset: `weather-station-measurements`

    - Resource: `San Diego Weather Sample`

- Check *Create Dataset Folder*.

- Click Add resources to current folder to download the dataset. The download may take a few seconds.

<img src="../images/dataset.png" style="border: 2px solid black;">

#### 7. Complete the Onboarding Notebook

- Go back to the *Current Folder* and open the `demo-workspace` directory.

- Open the file `onboarding.ipynb` and complete it by following the instructions in the notebook.

<img src="../images/onboarding.png" style="border: 2px solid black;">

#### 8. Stop Your Server When Finished

- Go to *File* (top left corner) → *Hub Control Panel* → *Stop Server* to shut down your environment when you're done.

<img src="../images/stop-server.png" style="border: 2px solid black;">

---

## Source Files

Source code files are processed separately by the processor.
File list:

- `mkdocs.yml` (2,535 bytes)

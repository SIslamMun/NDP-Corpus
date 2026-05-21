# dspaces-api

## Documentation Files

### docs/contributing.md (2,820 bytes)

# Contributing

Thank you for considering contributing to the DataSpaces API project! This document outlines the guidelines for contributing to the project.

## How to Contribute

### Reporting Bugs

If you find a bug in the project, please open an issue on GitHub and provide the following information:

- A clear and descriptive title for the issue.
- A description of the steps to reproduce the issue.
- Any relevant error messages or screenshots.
- Your environment details (e.g., operating system, Python version, etc.).

Refer to the [Guide to Creating Effective GitHub Issues](issues.md) for more information.

### Suggesting Enhancements

If you have an idea for a new feature or an improvement to an existing feature, please open an issue on GitHub and provide the following information:

- A clear and descriptive title for the enhancement.
- A detailed description of the proposed enhancement.
- Any relevant use cases or examples.

### Submitting Pull Requests

If you want to contribute code to the project, please follow these steps:

1. **Fork the repository**: Click the "Fork" button on the GitHub page to create a copy of the repository on your account.

2. **Clone the repository**: Clone your forked repository to your local machine.
    
```bash
git clone https://github.com/your-username/dspaces-api.git
```

3. **Create a new branch**: Create a new branch for your feature or bugfix. Refer to the [Standard Branch Naming Convention](branch.md) for more information on naming branches.
    
```bash
git checkout -b [type]/[descriptive-name]
```

4. **Make your changes**: Make your changes to the codebase. Ensure that you follow the project's coding standards and include relevant tests.

5. **Commit your changes**: Commit your changes with a clear and descriptive commit message. Refer to the [Effective Commit Messages Guide](commit.md) for more information on writing good commit messages.
    
```bash
git commit -m "Description of the changes made"
```

6. **Push your changes**: Push your changes to your forked repository.
    
```bash
git push origin [type]/[descriptive-name]
```

7. **Create a pull request**: Open a pull request on the original repository. Provide a clear and descriptive title for the pull request and include any relevant information about the changes you made.

## Coding Standards

- Follow PEP 8 for Python code.
- Write clear and concise code with appropriate comments.
- Ensure that your code is well-tested and that all tests pass before submitting a pull request.

## Code of Conduct

By participating in this project, you agree to abide by the project's [Code of Conduct](code_of_conduct.md).

## Getting Help

If you need help or have any questions, feel free to open an issue on GitHub or reach out to the maintainers.

[Return to README.md](../README.md)

---

### requirements.txt (61 bytes)

dill
fastapi
numpy
pydantic_settings
python-multipart
uvicorn

---

### docs/branch.md (2,156 bytes)

# Standard Branch Naming Convention for GitHub

Establishing a standard naming convention for branches in a GitHub project is crucial for maintaining organization and facilitating an understanding of each branch's purpose among team members. While there is no one-size-fits-all approach, there are common practices that many teams adopt to create an effective standard. Here's a recommended structure you can adjust according to your project's needs:

## General Structure

```
[type]/[descriptive-name]
```

## Common Types of Branches

- **feat**: For new features or significant additions to your project.
- **fix**: For bug fixes.
- **docs**: For changes to documentation.
- **style**: For changes that do not affect the meaning of the code (space, formatting, etc.).
- **refactor**: For code changes that neither fix a bug nor add a feature.
- **test**: For adding or correcting tests.
- **chore**: For updates and maintenance tasks without source code changes.

## Examples

- `feat/login-social-media`: Indicates the development of a new feature related to social media login.
- `fix/bug-login`: Refers to the correction of a specific bug in the login system.
- `docs/update-readme`: For updates or improvements to the project's README file.
- `refactor/cleanup-code-login`: Implies a restructuring of the login code, without changing its functionality.

## Tips for Branch Names

1. **Be brief but descriptive**: Names should be descriptive enough that anyone on the team can understand the purpose of the branch just by looking at its name, but not so long that they are hard to read or handle.
2. **Use dashes to separate words**: This enhances the readability of the branch name.
3. **Avoid special characters**: Keep the branch names simple and avoid using special characters or spaces.
4. **Prefix with the type of task**: Helps to quickly categorize branches and facilitates the search for branches related to specific tasks.
5. **Include task/ticket identifiers**: If your team uses a task or ticket tracking system, consider including the ticket identifier in the branch name for quick reference.

Return to [Contributing](contributing.md)

---

### docs/commit.md (1,824 bytes)

# Effective Commit Messages Guide

Writing clear and concise commit messages is crucial for maintaining a readable and understandable history in your project. This guide provides recommendations for writing effective commit messages within a 50-character limit.

## Structure of a Good Commit Message

A good commit message should answer two questions: what changed and why. However, given the 50-character limit, focus on the "what" and imply the "why" when possible.

```
[type]: Short Change Description or Issue Number
```

## Types of Changes

- **feat**: A new feature
- **fix**: A bug fix
- **docs**: Documentation only changes
- **style**: Changes that do not affect the meaning of the code
- **refactor**: A code change that neither fixes a bug nor adds a feature
- **test**: Adding missing tests or correcting existing tests
- **wip**: Work in progress (unfinished changes)

## Examples

- `feat: Add login API`
- `fix: Resolve login redirect`
- `fix: #23`
- `docs: Update README`
- `style: Format with Prettier`
- `refactor: Simplify login check`
- `test: Cover edge cases`
- `wip: implement feature topics list (#123)`

## Tips for Writing Concise Commit Messages

1. **Start with a Capital Letter**: Begin your message with a capital letter to maintain consistency.
2. **Use Present Tense**: Write your commit message in present tense, "Add feature" not "Added feature".
3. **No Period at the End**: Skip the period at the end of the message to save space and maintain formatting.
4. **Use Imperative Mood**: Frame your message as a command or instruction, "Fix bug" not "Fixes bug".
5. **Be Specific**: Use specific terms that directly reflect the changes made.

Remember, the goal of a commit message is to clearly and succinctly convey the essence of your change.

Return to [Contributing](contributing.md).

---

### docs/installation.md (1,742 bytes)

## Installation

Follow these steps to install and set up the sciDX API on your local machine:

### Prerequisites

Make sure you have the following installed on your system:

- **Python 3.8+**
- **Docker** and **Docker Compose**(if you plan to use the Docker setup). 
- **Git**

### Clone the Repository

Clone the DataSpaces API repository from GitHub:

```bash
git clone https://github.com/sci-ndp/dspaces-api
cd dspaces-api
```

### Environment Configuration

1. Copy the example environment files and adjust the configuration as needed:

   ```bash
   cp ./env_variables/env_dspaces.example ./env_variables/.env_dspaces
   cp ./env_variables/env_api.example ./env_variables/.env_api
   cat ./env_variables/.env_dspaces ./env_variables/.env_api > .env
   ```

2. Edit the `.env` files to match your local environment or deployment needs.

### Running the Application

Start the application using one of the following methods:

- **With Docker**:

  ```bash
  docker-compose up
  ```

### Accessing the API

Once the application is running, you can access the DataSpaces API at:

- **Local environment**: `http://127.0.0.1:8001`
- **Docker environment**: `http://localhost:8001`

Return to [README](../README.md).

# DataSpaces Configuration
Configuration can be passed to the DataSpaces server itself using the `dspaces.toml` file.

# Enable Unsafe DataSpaces Operations
To enable remote execution via the DataSpaces API, add the environement variable `DSPACES_UNSAFE_ENDPOINTS=True` to `.env_dspaces`. This enables public endpoints that execute Python code on the DataSpaces server, with all the privileges of the user running DataSpaces. This is a security and privacy risk, and should not be enabled on a shared or public installation.

---

### docs/issues.md (3,205 bytes)

# Guide to Creating Effective GitHub Issues

Creating well-documented issues on GitHub helps teams communicate effectively about tasks, enhancements, and bugs. An essential part of this process is giving your issue a clear title and categorizing it properly.

## Naming Your Issue:

The title of your issue should be descriptive yet concise. It should give a clear indication of the problem or feature request at a glance. Here’s a format you might consider using:

- **Bugs**: `[Bug] Short description of the problem`
- **Feature Requests**: `[Feature] Short description of the new feature`
- **Documentation**: `[Docs] Description of the documentation change`
- **Other Types**: `[Type] Description`, where type could be Refactor, Test, Chore, etc.

## Differences Between Issue Types:

- **Bugs**: Issues that report a problem or unexpected behavior in the project. They should include steps to reproduce the issue, the expected outcome, and the actual outcome.
- **Feature Requests**: Suggestions for new features or improvements to existing functionality. Describe what you wish to achieve and why it would be beneficial.
- **Documentation**: Requests or suggestions for improvements to the project's documentation. This can include missing documentation or clarifications on existing content.
- **Others**: This category includes code refactoring, tests, or maintenance tasks that don't necessarily add new features or fix bugs but are essential for project health.

## Creating an Issue:

1. **Navigate to the Issues tab** of the relevant repository and click on "New Issue."
2. **Select a Template** if applicable. Use the appropriate template for bugs, feature requests, or other issue types.
3. **Fill in the Issue Title**: Use the naming conventions mentioned above to provide a clear and concise title.
4. **Describe the Issue** in detail:
   - **Description**: Give a summary of the issue.
   - **Steps to Reproduce** (for bugs): Clearly list the steps to demonstrate the issue.
   - **Expected Behavior**: What should happen?
   - **Actual Behavior**: What actually happens?
   - **Possible Solution**: Suggest a possible fix if you have one.
   - **Additional Context**: Any other information, like screenshots or error messages.
5. **Submit the Issue**: Review the details and submit your issue.

## Simple Issue Template Example

Use the following template in your GitHub repository to streamline the issue creation process:

```markdown
# Issue Template

## Description
Please provide a brief description of the problem or the feature request. Be clear and concise.

## Steps to Reproduce
For bugs, list the steps required to reproduce the issue, if applicable:
1.
2.
3.

## Expected Behavior
For bugs, describe what you expected to happen.
For feature requests, describe what feature you would like to see implemented.

## Actual Behavior
For bugs, describe what actually happened. Include any error messages or unexpected outcomes.

## Possible Solution
If you have any suggestions on how to fix the bug or implement the feature, please share them here.

## Additional Context
Add any other context or screenshots about the issue here.
```

Return to [Contributing](contributing.md)

---

## Source Files

Source code files are processed separately by the processor.
File list:

- `.gitignore` (3,161 bytes)
- `api/__init__.py` (0 bytes)
- `api/config/__init__.py` (99 bytes)
- `api/config/dspaces.py` (490 bytes)
- `api/config/swagger.py` (352 bytes)
- `api/configure_services.py` (41 bytes)
- `api/helpers/bounding_box.py` (1,485 bytes)
- `api/helpers/dspaces_client.py` (364 bytes)
- `api/main.py` (957 bytes)
- `api/models/__init__.py` (71 bytes)
- `api/models/dspaces_model.py` (911 bytes)
- `api/routes/__init__.py` (105 bytes)
- `api/routes/default_routes.py` (227 bytes)
- `api/routes/dspaces_routes.py` (14,757 bytes)
- `api/services/__init__.py` (0 bytes)
- `api/services/dspaces_services/__init__.py` (547 bytes)
- `api/services/dspaces_services/get_dspaces_obj.py` (899 bytes)
- `api/services/dspaces_services/get_dspaces_var_obj.py` (797 bytes)
- `api/services/dspaces_services/get_dspaces_vars.py` (265 bytes)
- `api/services/dspaces_services/mpexec_dspaces_obj.py` (787 bytes)
- `api/services/dspaces_services/pexec_dspaces_obj.py` (1,193 bytes)
- `api/services/dspaces_services/put_dspaces_obj.py` (1,454 bytes)
- `api/services/dspaces_services/reg_dspaces.py` (281 bytes)
- `dspaces.toml` (219 bytes)
- `start-dockers.sh` (0 bytes)
- `start.sh` (107 bytes)
- `stop-dockers.sh` (0 bytes)

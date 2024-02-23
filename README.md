# Robocorp Action Server for Langchain Toolkit

This repository contains the code necessary to set up a Robocorp action server, leveraging Langchain as a toolkit for building and deploying AI agents. It provides a simple yet powerful template for creating AI actions, such as comparing timezones, querying databases, and interacting with Salesforce CRM, to enhance the capabilities of your AI agents.

## Overview

The provided codebase includes a set of predefined actions that demonstrate how to integrate various services (like Salesforce and Tavily) and perform timezone comparisons. These actions serve as a foundation for building more complex functionalities within your Robocorp action server.

### Features

- **Timezone Comparison**: Compare user timezone with other timezones and calculate the time difference.
- **Topic Search**: Leverage the Tavily client to search for topics.
- **Salesforce Integration**: Query Salesforce for accounts and related cases, providing a seamless connection to your CRM data.

### Getting Started

To get started with this repository, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine using Git.

    ```bash
    git clone https://github.com/hollaugo/robocorp-yt-tutorial.git
    ```

2. **Environment Setup**: Ensure you have Python installed and set up a virtual environment.

    ```bash
    python -m venv venv
    source venv/bin/activate
    cd robo-app
    ```

3. **Install Dependencies**: Install the necessary Python packages.

    ```bash
    pip install -U langchain-cli
    pip install -U robocorp-action-server
    ```

4. **Set Up Environment Variables**: Create a `.env` file in the root directory and populate it with your OPENAI, TAVILY API keys and Salesforce credentials as shown in the provided code snippet.

5. **Running Actions**: Execute the predefined actions as needed. Each action is designed as a standalone function that can be triggered independently.

 ```bash
    langchain serve #Running Langchain Application Server
    action-server start #Start Action Server
    ```

### Documentation

For detailed guidance on creating and deploying AI actions using Robocorp, refer to the official [Robocorp documentation](https://robocorp.com/docs/).


Please note: This repository is a template and requires customization to fit your specific use case. Ensure you review and modify the actions according to your application's needs.

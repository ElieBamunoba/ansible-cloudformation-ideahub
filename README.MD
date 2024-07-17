# Bright Ideas Deployment and Configuration

This project outlines the deployment and configuration of the Bright Ideas application using AWS CloudFormation and Ansible. The primary focus is on setting up an EC2 instance as a MySQL server, launched by CloudFormation and configured by Ansible.

## Prerequisites

- AWS CLI
- Ansible
- Boto3
- Git

## Overview

### CloudFormation-Ideahub

This directory contains scripts and templates for provisioning AWS resources using CloudFormation. The primary resource is an EC2 instance configured as a MySQL server.

- **Templates**: Defines the AWS infrastructure (e.g., EC2 instances, security groups).
- **Scripts**: Python scripts for deploying, validating, and deleting CloudFormation stacks.

### Ansible-Ideahub

This directory contains Ansible configurations and playbooks for configuring the provisioned AWS resources. The main tasks involve setting up the MySQL server on the EC2 instance.

- **Ansible Configuration**: Defines inventory and SSH connection settings.
- **Playbooks**: YAML files that define tasks for configuring servers (e.g., installing software, setting up databases).
- **Roles**: Organizes tasks into reusable units (e.g., `mysql` role for database setup).

## Setup Instructions

### Step 1: Configure AWS and Ansible

1. **Move SSH Key**:
    ```sh
    mkdir -p ~/.ssh
    mv ~/path/to/your-key.pem ~/.ssh/
    chmod 600 ~/.ssh/your-key.pem
    ```

2. **Update `ansible.cfg`**:
    ```ini
    
    private_key_file = ~/.ssh/your-key.pem
    ```

### Step 2: Install python dependencies in cloudformation-ideahub

1. **Remove `venv`**:
    ```sh
    cd cloudformation-ideahub
    python -m venv venv
    pip install -r requirements.txt
    ```


### Step 3: Deploy CloudFormation Stack and Run Ansible Playbook

1. **Run Deployment Script**:
    ```sh
    cd cloudformation-ideahub/scripts
    python3 deploy.py
    ```
    - ```hosts.ini``` file  will be automatically updated with the EC2 instance's IP. You can also manually set this up.

2. **Run Ansible and provide Vault Password**:
    ```sh
    cd ansible-ideahub
    ansible-playbook playbook.yml --ask-vault-pass
    ```
    - When prompted, provide the Ansible Vault password to decrypt sensitive variables.
    - You can also provide your own set of credentials.

## Summary

This project uses CloudFormation to provision AWS resources and Ansible to configure them. Sensitive data is managed using Ansible Vault, ensuring secure and efficient collaboration. For detailed steps on how to manage and use the Ansible Vault, refer to the documentation.
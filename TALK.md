# Ansible: Introduction & Automation for Geo Cluster

## Introduction to Ansible

<img class="ansible-logo" src="./talk/assets/ansible.png" alt="img-verification" width="50%" />

### What is Ansible?

- Ansible® is an open source, command-line IT automation software application written in Python. It can configure
  systems, deploy software, and orchestrate advanced workflows to support application deployment, system updates, and
  more.

### Key features of Ansible

Ansible aims to be:

1. **Clear** - Ansible uses a simple syntax (YAML) and is easy for anyone (developers,
   sysadmins, managers) to understand. APIs are simple and sensible.
2. **Fast** - Fast to learn, fast to set up—especially considering you don’t need to
   install extra agents or daemons on all your servers!
3. **Complete** - Ansible does three things in one (configuration management, server deployment, ad-hoc task execution),
   and does them very well. Ansible’s
   ‘batteries included’ approach means you have everything you need in one
   complete package.
4. **Efficient** - No extra software on your servers means more resources for your
   applications. Also, since Ansible modules work via JSON, Ansible is extensible
   with modules written in a programming language you already know.
5. **Secure** - Ansible uses SSH, and requires no extra open ports or potentially-
   vulnerable daemons on your servers.

## Ansible Architecture & Basic Concepts

![Architecture](./talk/assets/architecture.png)

Ansible is designed to be lightweight, agentless, and flexible, follows a client-server architecture, where a central
control node communicates with remote managed nodes to
automate and manage infrastructure configurations

### Control Node

- The control node is the machine where Ansible is installed and from where automation tasks are initiated. It acts as
  the central point of control and communication, run the Ansible CLI tools (_ansible-playbook, ansible,
  ansible-vault_, ...)
- The control node can be a physical or virtual machine.
- Multiple control nodes are possible
- Geo cluster is using node **Hlc-geo3** to communicate with all other nodes

### Managed Nodes

- These are the target devices (servers, network appliances or any computer) you aim to manage with Ansible
- Ansible is not normally installed on managed nodes

### Inventory

- A list of managed nodes provided by one or more ‘inventory sources’
- Inventory can specify information specific to each node, like IP address
- It is also used for assigning groups, that both allow for node selection in the Play and bulk variable assignment.
- Sometimes an inventory source file is also referred to as a ‘hostfile’.

![Ansible hostfile](./talk/assets/ansible_hosts.png)

![Ansible's inventory](./talk/assets/inventory.png)

### Playbooks

- Playbooks are files written in YAML format that define a set of tasks and configurations to be applied to managed
  nodes. Playbooks allow you to specify the desired state of the infrastructure and the order in which tasks should be
  executed. They provide a way to orchestrate and automate complex workflows. Playbooks can include variables,
  conditionals, loops, and even include other playbooks or roles.

## Getting Started with Ansible

### Installation & Configuration

### Inventory Management

### Ad-hoc Commands

## Ansible Playbooks & Roles

### Playbook Structure

### Variables & Facts

### Conditions & Loops

### Roles & Role-based Tasks

## Advanced Ansible Concepts

### Ansible Vault

### Ansible Galaxy

### Ansible Tower, Ansible AWX

## Automation for Geo cluster

### Apache NiFi

### Apache Airflow
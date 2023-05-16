# Ansible: Introduction & Automation for Geo Cluster

## Introduction to Ansible

<p align="center">
<img class="ansible-logo" src="./talk/assets/ansible.png" alt="img-verification" width="35%" />
</p>

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

### Modules

- In Ansible, modules are small, self-contained units of code that are responsible for performing specific tasks on
  managed nodes. They are the building blocks of automation in Ansible and serve as the primary means of interacting
  with the managed infrastructure.
- Modules encapsulate functionality related to various aspects of system administration, such as package management,
  file manipulation, service configuration, user management, network operations, and more. Ansible ships with a broad
  range of built-in modules that cover a wide variety of tasks commonly encountered in IT operations.
- Example, there are modules for installing packages (
  apt/yum/dnf/pacman), managing users (user), copying files (copy), manipulating files (lineinfile), and configuring
  services (service), among many others.

## Getting Started with Ansible

### Installation & Configuration

- Ensure that the control node meets the minimum system requirements for running Ansible. These requirements include
  having a supported operating system (such as Linux, macOS, or Windows with WSL), sufficient memory and disk space, and
  a stable network connection.
- The managed node (the machine that Ansible is managing) does not require Ansible to be installed, but requires Python
  2.7, or Python 3.5 - 3.11 to run Ansible library code. The managed node also needs a user account that can SSH to the
  node with an interactive shell.

### Inventory Management

Here's how inventory management works:

1. Defining Managed Nodes

```ansible
[web_servers]  # --> group name
server1.example.com # --> node
server2.example.com

[database_servers]
db1.example.com
db2.example.com
```

2. Grouping Managed Nodes

```ansible
[production:children] # --> parent group
web_servers
database_servers
```

3. Variables and Additional Information

```ansible
[web_servers]
server1.example.com ansible_user=ubuntu

[database_servers]
db1.example.com ansible_user=root

[production:vars]
http_port=80
max_connections=1000
```

Verify inventory: `ansible-inventory -i inventory.yml --list`

![](./talk/assets/list_inventory.png)

### Ad-hoc Commands

Ansible ad-hoc commands are one-liner commands that allow you to perform quick tasks on managed nodes without the need
for writing a separate playbook. Ad-hoc commands are useful for executing simple tasks, running one-off commands, or
performing troubleshooting operations

- The basic syntax of Ad-hoc command:

  `ansible <host-pattern> -m <module> -a "<module arguments>"`

- **host-pattern**: Specifies the target hosts or groups of hosts. It can be a single host, a group of hosts defined
  in
  the inventory, or a pattern to match multiple hosts.
- **-m (module)**: Specifies the Ansible module to be executed on the target hosts.
- **-a "(module arguments)"**: Provides the arguments or parameters required by the specified module.

#### Examples

- Ping all hosts: `ansible all -m ping`:

  This command pings all hosts defined in the inventory to check if they are reachable

![](./talk/assets/ping.png)

- Gather system facts: `ansible all -m setup`

  This command collects various system facts from all hosts, providing detailed information about the systems, including
  hardware, networking, and operating system details.

![](./talk/assets/gather_facts.png)

- Execute a shell command: `ansible web_servers -m shell -a "uptime"`

  This command runs the uptime command on the hosts belonging to the web_servers group, displaying the system's uptime.

![](./talk/assets/uptime.png)

- Install a package: `ansible db_servers -m apt -a "name=mysql-server state=present"`

  This command installs the mysql-server package on hosts belonging to the db_servers group using the apt module.

![](./talk/assets/install_package.png)

- Copy a file: `ansible web_servers -m copy -a "src=/path/to/local/file dest=/path/on/remote/server"`

  This command copies a file from the local system to the remote hosts belonging to the web_servers group using the copy
  module.

![](./talk/assets/copy.png)

## Ansible Playbooks & Roles

### Playbook Structure

They contain Plays (which are the basic unit of Ansible execution). This is both an ‘execution concept’ and how we
describe the files on which ansible-playbook operates. Playbooks are written in YAML and are easy to read, write, share
and understand

#### Plays

The main context for Ansible execution, this playbook object maps managed nodes (hosts) to tasks. The Play contains
variables, roles and an ordered lists of tasks and can be run repeatedly. It basically consists of an implicit loop over
the mapped hosts and tasks and defines how to iterate over them.

![](./talk/assets/play.png)

#### Roles

A limited distribution of reusable Ansible content (tasks, handlers, variables, plugins, templates and files) for use
inside of a Play. To use any Role resource, the Role itself must be imported into the Play.

![](./talk/assets/role_folder.png)
![](./talk/assets/role_include.png)

#### Tasks

The definition of an ‘action’ to be applied to the managed host. Tasks must always be contained in a Play, directly or
indirectly (Role, or imported/included task list file). You can execute a single task once with an ad hoc command using
ansible or ansible-console (both create a virtual Play).

![](./talk/assets/tasks.png)

#### Handlers

A special form of a Task, that only executes when notified by a previous task which resulted in a ‘changed’ status.

![](./talk/assets/handler_restart.png)
![](./talk/assets/handler_notify.png)

### Variables & Facts

#### Variables

- Variables in Ansible are used to store and manage data that can be referenced and utilized within playbooks,
  templates,
  and other Ansible constructs. Variables can be defined at different levels, including inventory level, playbook level,
  group level, or host level. They allow for flexibility and reusability in configuring tasks and playbooks for
  different
  scenarios.
    - **Inventory Variables**: Variables can be defined in the inventory file using YAML syntax or in separate variable
      files associated with the inventory. These variables can be used to configure settings specific to hosts or groups
      defined in the inventory.
    - **Playbook Variables**: Playbooks can define their own variables using YAML syntax. These variables can be set
      globally for the entire playbook or specific to certain plays, roles, or tasks within the playbook.
    - **Host and Group Variables**: Variables can be assigned to individual hosts or groups in the inventory. These
      variables can override the inventory-level or playbook-level variables for specific hosts or groups.

![](./talk/assets/vars.png)

#### Facts

- Facts in Ansible are system-related information collected from managed nodes during playbook execution. Facts provide
  valuable details about the target systems, including network interfaces, hardware specifications, operating system
  details, and more. Ansible automatically collects facts from managed nodes and makes them available as variables.

- Ansible gathers facts by default when executing playbooks. However, you can also explicitly gather facts using the
  _gather_facts_ option set to true in a playbook

![](./talk/assets/facts.png)
![](./talk/assets/use_facts.png)

### Conditions & Loops

### Roles & Role-based Tasks

## Advanced Ansible Concepts

### Ansible Vault

### Ansible Galaxy

### Ansible Tower, Ansible AWX

## Automation for Geo cluster

### Apache NiFi

### Apache Airflow
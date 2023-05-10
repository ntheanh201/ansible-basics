Agenda:

1. Automating servers: Why do we need to automate?
    1. Security
    2. Compliance
    3. Rapid deployment

- One of Ansible’s greatest features is its ability to function without running any extra
  applications or daemons on the servers it manages
- Ansible uses the standard and secure SSH
  connection
- One thing that is universal to all of Ansible’s SSH connection methods is that Ansible
uses the connection to transfer one or a few files defining a play or command to the
remote server, then runs the play/command, then deletes the transferred file(s), and
reports back the results. A fast, stable, and secure SSH connection is of paramount
importance to Ansible.

Faster OpenSSH with Pipelining
- Instead of copying files, running them on the remote server, then removing them,
the ‘pipelining’ method of OpenSSH transfer will send and execute commands for
most Ansible modules directly over the SSH connection.
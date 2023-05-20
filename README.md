# ansible-basics

# Run Ubuntu server

```
cd ubuntu-server
docker build -t ubuntu-server-local .
docker run -itd --name ubuntu-server-local -p 2222:22 ubuntu-server-local
```

**Test**: ssh test@vm01 -p 2222

# Ansible

- Ping: `ansible all -m ping`

## Building an inventory

- Verify inventory: `ansible-inventory -i inventory.yaml --list`
- Ping:

```
ansible virtualmachines -m ping -i inventory.yaml
ansible leafs -m ping -i inventory.yaml
ansible spines -m ping -i inventory.yaml
```

## Playbook

- Run playbook: `ansible-playbook -i inventory.yaml playbooks/ping.yaml`

## Ansible testing



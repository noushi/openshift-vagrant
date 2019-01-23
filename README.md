# OpenShift Vagrant

This repository contains a Vagrantfile and Ansible inventory for creating an OpenShift Container Platform (OCP) 3 or OpenShift Origin 3 cluster
with Vagrant for development and testing purposes.

## Requirements

* [Vagrant](https://www.vagrantup.com/)
* [vagrant-libvirt](https://github.com/vagrant-libvirt/vagrant-libvirt) provider
* RHEL Vagrant Box (OpenShift Container Platform only), see https://github.com/appuio/el-vagrant#rhel-box
* OpenShift Container Platform subscription (OpenShift Container Platform only), see https://github.com/appuio/el-vagrant#subscription-manager-configuration-rhel-only

Tested with Vagrant 2.0.0 and vagrant-libvirt 0.0.40.

## Usage

The Vagrantfile and Ansible inventory in this repository are preconfigured with 4 machines:
* control: An optional Ansible control machine to run playbooks outside of the OpenShift cluster
* ose3-master: An OpenShift master
* ose3-node1 and ose3-node2: OpenShift nodes

Add or remove machines as needed. Then start Vagrant machines and install OpenShift with:

1. Checkout this repository and [el-vagrant](https://github.com/appuio/el-vagrant) into the same directory.
2. Adjust `memory` and `cpus` values in the `Vagrantfile` as needed
2. Set this env var to dismiss the `vagrant-triggers` warning: 
```
export VAGRANT_USE_VAGRANT_TRIGGERS=false
```
3. Start the Vagrant machines: 

       vagrant up

4. Install OpenShift prerequisites:

       vagrant ssh control
       sudo -i
       yum install ansible
       cp /vagrant/hosts.example /etc/ansible/hosts
       ansible-playbook /vagrant/pre-install.yml

5. OCP only: Change `openshift_deployment_type` in `/etc/ansible/hosts` to `openshift-enterprise`
6. Install OpenShift:

       ansible-playbook /usr/share/ansible/openshift-ansible/playbooks/byo/config.yml

The control machine is optional as Ansible can also be installed and run on an OpenShift master. However
it's good practice that playbooks also run on outside of OpenShift clusters and are therefore tested
on a separate control machine.

## Implementation

The pre-install playbook takes care of:

* Configures SSH known host keys so Ansible can run non-interactively
* Configures Ansible SSH pipelining in order to improve Ansible performance
* Enables yum repositories required for OpenShift installation
* Installs prerequisites for OpenShift installation

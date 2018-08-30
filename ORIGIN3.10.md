




```
yum install -y ansible

ansible-playbook ./control-setup.yml

ansible-playbook -i hosts-3.10.example ./pre-install.yml

ansible-playbook -i hosts-3.10.example /usr/share/ansible/openshift-ansible/playbooks/prerequisites.yml 
ansible-playbook -i hosts-3.10.example /usr/share/ansible/openshift-ansible/playbooks/deploy_cluster.yml
```


# yum install wget git net-tools bind-utils yum-utils iptables-services bridge-utils bash-completion kexec-tools sos psacct



# Notes

`openshift_node_labels` are deprecated.

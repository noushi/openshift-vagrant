




```
yum install -y ansible

ansible-playbook ./control-setup.yml

ansible-playbook -i hosts-3.10.example ./pre-install.yml

ansible-playbook -i hosts-3.10.example /usr/share/ansible/openshift-ansible/playbooks/prerequisites.yml 
ansible-playbook -i hosts-3.10.example /usr/share/ansible/openshift-ansible/playbooks/deploy_cluster.yml
```

later on:
```
ansible-playbook -i hosts-3.10.example /usr/share/ansible/openshift-ansible/playbooks/openshift-hosted/config.yml 
```


if blocked, here:
```
TASK [openshift_hosted : Configure a passthrough route for docker-registry] ********
```
run: 
```
oc delete route docker-registry -n default
```

likewise:
```
TASK [cockpit-ui : Create passthrough route for registry-console
```
:
```
oc delete route registry-console -n default
```


# yum install wget git net-tools bind-utils yum-utils iptables-services bridge-utils bash-completion kexec-tools sos psacct


```
IMAGES_TAR=/root/origin-3.10-images.tar
MASTER=ose3-master.example.com
ssh root@$MASTER docker save '$(docker images -q)' -o $IMAGES_TAR
rsync -avz root@$MASTER:$IMAGES_TAR /vagrant/cache/
```

# Notes

`openshift_node_labels` are deprecated.

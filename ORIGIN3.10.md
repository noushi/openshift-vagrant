




```
yum install -y ansible

ansible-playbook ./control-setup.yml

ansible-playbook -i hosts-3.10.example ./pre-install.yml

sed -i 's/python-docker/python-docker-py/' /usr/share/ansible/openshift-ansible/playbooks/init/base_packages.yml

ansible all -i hosts-3.10.example -m yum -a "name=centos-release-openshift-origin310 state=present"

ansible all -i hosts-3.10.example -m yum -a "name=yum-plugin-versionlock state=present"

ansible all -i hosts-3.10.example -a 'yum versionlock origin*-3.10.0'

ansible all -i hosts-3.10.example -a 'yum versionlock status'

ssh root@ose3-master yum install origin{,-node,-hyperkube,-clients}-3.10.0 -y

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

## metrics
```
ansible-playbook -i hosts-3.10.example /usr/share/ansible/openshift-ansible/playbooks/openshift-metrics/config.yml
```

create NFS pv
```
oc create -f - <<EOF
apiVersion: v1
kind: PersistentVolume
metadata:
  name: cassandra-metrics-1
  labels:
    storage: metrics
spec:
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteOnce
  nfs:
    server: facility.example.com
    path: "/exports/metrics"
EOF
```

# Notes

`openshift_node_labels` are deprecated.

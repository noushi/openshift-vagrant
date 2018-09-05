# -*- mode: ruby -*-
# vi: set ft=ruby :

load '../el-vagrant/Vagrantfile'


Vagrant.configure("2") do |config|
  config.vm.box = "centos7.4"

  config.vm.provision "shell", name: "openshift", inline: <<-SHELL
    yum update -y

    mkdir -p /etc/dnsmasq.d
    cat <<-EOF >/etc/dnsmasq.d/vagrant.conf
      address=/.cloudapps.example.com/172.22.22.122
      address=/.openshiftapps.com/172.22.22.122
		EOF
  SHELL

  if Vagrant.has_plugin?("vagrant-cachier")
#    config.cache.scope = :box
  end

  config.vm.define 'control', primary: true do |vmconfig|
    vmconfig.vm.hostname = 'control.example.com'
    vmconfig.vm.network :private_network, :ip => '172.22.22.101'
    vmconfig.hostmanager.aliases = %w(control)

    vmconfig.vm.provider :libvirt do |libvirt|
      libvirt.memory = 1024
      libvirt.cpus = 4
    end

    vmconfig.vm.provider "virtualbox" do |vb|
      vb.cpus = 4
      vb.memory = 1024
    end
  end
  
  config.vm.define 'facility' do |vmconfig|
    vmconfig.vm.hostname = 'facility.example.com'
    vmconfig.vm.network :private_network, :ip => '172.22.22.141'
    vmconfig.hostmanager.aliases = %w(facility)

    vmconfig.vm.provider :libvirt do |libvirt|
      libvirt.memory = 1024
      libvirt.cpus = 4
    end

    vmconfig.vm.provider "virtualbox" do |vb|
      vb.cpus = 4
      vb.memory = 1024
    end
  end
  
  config.vm.define 'ose3-master' do |vmconfig|
    vmconfig.vm.hostname = 'ose3-master.example.com'
    vmconfig.vm.network :private_network, :ip => '172.22.22.122'
    vmconfig.hostmanager.aliases = %w(ose3-master)

    vmconfig.vm.provider :libvirt do |libvirt|
      libvirt.memory = 4096
      libvirt.cpus = 4
      libvirt.storage :file, :device => 'vdb', :size => '20G', :type => 'qcow2', :cache => 'writeback'
    end

    vmconfig.vm.provider "virtualbox" do |vb|
      vb.cpus = 4
      vb.memory = 4096
    end
  end

  config.vm.define 'ose3-node1' do |vmconfig|
    vmconfig.vm.hostname = 'ose3-node1.example.com'
    vmconfig.vm.network :private_network, :ip => '172.22.22.131'
    vmconfig.hostmanager.aliases = %w(ose3-node1)

    vmconfig.vm.provider :libvirt do |libvirt|
      libvirt.memory = 4096
      libvirt.cpus = 4
      libvirt.storage :file, :device => 'vdb', :size => '20G', :type => 'qcow2', :cache => 'writeback'
    end

    vmconfig.vm.provider "virtualbox" do |vb|
      vb.cpus = 4
      vb.memory = 4096
    end    
  end

  config.vm.define 'ose3-node2' do |vmconfig|
    vmconfig.vm.hostname = 'ose3-node2.example.com'
    vmconfig.vm.network :private_network, :ip => '172.22.22.132'
    vmconfig.hostmanager.aliases = %w(ose3-node2)

    vmconfig.vm.provider :libvirt do |libvirt|
      libvirt.memory = 4096
      libvirt.cpus = 4
      libvirt.storage :file, :device => 'vdb', :size => '20G', :type => 'qcow2', :cache => 'writeback'
    end

    vmconfig.vm.provider "virtualbox" do |vb|
      vb.cpus = 4
      vb.memory = 4096
    end    
  end

end

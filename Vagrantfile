# -*- mode: ruby -*-
# vi: set ft=ruby :

load '../el-vagrant/Vagrantfile'

GB=1024

require 'fileutils'

def prepare_disk(hostname)
  base_dir = '.vagrant/disks/' + hostname
  FileUtils.mkdir_p base_dir
  base_dir + '/disk.vdi'
end

def add_disk(vb, disk, size)
  unless File.exist?(disk)
    vb.customize ['createhd', '--filename', disk, '--variant', 'Standard', '--size', size]
  end
  vb.customize ['storageattach', :id,  '--storagectl', 'IDE Controller', '--port', 1, '--device', 0, '--type', 'hdd', '--medium', disk]
end

Vagrant.configure("2") do |config|
#  config.vm.box = "centos7.4"
  config.vm.box = "rhel-7.4-vbox"
  
  config.vm.provision "shell", name: "openshift", inline: <<-SHELL
    yum update -y

    mkdir -p /etc/dnsmasq.d
    cat <<-EOF >/etc/dnsmasq.d/vagrant.conf
      address=/.cloudapps.example.com/172.22.22.122
      address=/.openshiftapps.com/172.22.22.122
		EOF
  SHELL

  if Vagrant.has_plugin?("vagrant-cachier")
    config.cache.scope = :box unless ENV['VAGRANT_CACHIER_BOX_CACHING'] == false
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
      disk = prepare_disk vmconfig.vm.hostname
      add_disk vb, disk, 5*GB
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
      disk = prepare_disk vmconfig.vm.hostname
      add_disk vb, disk, 5*GB
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
      disk = prepare_disk vmconfig.vm.hostname
      add_disk vb, disk, 5*GB
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
      disk = prepare_disk vmconfig.vm.hostname
      add_disk vb, disk, 5*GB
    end
  end

  config.vm.define 'ose3-node3' do |vmconfig|
    vmconfig.vm.hostname = 'ose3-node3.example.com'
    vmconfig.vm.network :private_network, :ip => '172.22.22.133'
    vmconfig.hostmanager.aliases = %w(ose3-node3)

    vmconfig.vm.provider :libvirt do |libvirt|
      libvirt.memory = 4096
      libvirt.cpus = 4
      libvirt.storage :file, :device => 'vdb', :size => '20G', :type => 'qcow2', :cache => 'writeback'
    end

    vmconfig.vm.provider "virtualbox" do |vb|
      vb.cpus = 4
      vb.memory = 4096
      disk = prepare_disk vmconfig.vm.hostname
      add_disk vb, disk, 5*GB
    end    
  end

end

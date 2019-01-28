# -*- mode: ruby -*-
# vi: set ft=ruby :

load '../el-vagrant/Vagrantfile'

GB=1024

NODE_RAM=4096
DISK_SIZE=10*GB

machines= [
  { name: "ose3-master", ip: "172.22.22.122", cpus: 4, mem: NODE_RAM, size: DISK_SIZE },
  { name: "ose3-node1", ip: "172.22.22.131", cpus: 4, mem: NODE_RAM, size: DISK_SIZE },
  { name: "ose3-node2", ip: "172.22.22.132", cpus: 4, mem: NODE_RAM, size: DISK_SIZE },
  { name: "ose3-node3", ip: "172.22.22.133", cpus: 4, mem: NODE_RAM, size: DISK_SIZE },
]

require 'fileutils'

def disk_name(hostname, suffix)
  base_dir = '.vagrant/disks/' + hostname
  FileUtils.mkdir_p base_dir
  base_dir + '/disk' + suffix + '.vdi'
end

def add_disk(vb, hostname, size, port, dev)
  disk = disk_name(hostname, "#{port}-#{dev}")

  unless File.exist?(disk)
    vb.customize ['createhd', '--filename', disk, '--variant', 'Standard', '--size', size]
  end

  vb.customize ['storageattach', :id,  '--storagectl', 'IDE Controller', '--port', port, '--device', dev, '--type', 'hdd', '--medium', disk]
end

Vagrant.configure("2") do |config|
#  config.vm.box = "centos7.4"
  config.vm.box = "rhel-7.4-vbox"
  
  config.vm.provision "shell", name: "openshift", inline: <<-SHELL
    # yum update -y

    mkdir -p /etc/dnsmasq.d
    cat <<-EOF >/etc/dnsmasq.d/vagrant.conf
      address=/.cloudapps.example.com/172.22.22.122
      address=/.openshiftapps.com/172.22.22.122
		EOF
  SHELL

  if Vagrant.has_plugin?("vagrant-cachier")
    config.cache.scope = :box unless ENV['VAGRANT_CACHIER_BOX_CACHING'] == false
  end

  config.vm.provider "virtualbox" do |v|
    # intel cards (e1000) are so buggy
    v.default_nic_type = "virtio"

    # and piix3 chipsets kill download...
    v.customize ["modifyvm", :id, "--chipset", "ich9"]
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

      add_disk vb, vmconfig.vm.hostname, 10*GB, 1, 0
      add_disk vb, vmconfig.vm.hostname, 10*GB, 1, 1
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


  machines.each do |m|
    node = m[:name]
    config.vm.define node do |c|
      c.vm.hostname = "#{node}.example.com"
      c.vm.network :private_network, :ip => m[:ip]
      c.hostmanager.aliases = [node]

      c.vm.provider :libvirt do |libvirt|
        libvirt.memory = m[:mem]
        libvirt.cpus = m[:cpus]
        libvirt.storage :file, :device => 'vdb', :size => '20G', :type => 'qcow2', :cache => 'writeback'
      end

      c.vm.provider "virtualbox" do |vb|
        vb.cpus = m[:cpus]
        vb.memory = m[:mem]

        add_disk vb, c.vm.hostname, m[:size], 1, 0
        add_disk vb, c.vm.hostname, m[:size], 1, 1
      end
    end
  end

end

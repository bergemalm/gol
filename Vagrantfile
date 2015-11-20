# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

# Set the Ansible configuration environment variable
ENV['ANSIBLE_CONFIG'] = ".ansible.cfg"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "precise32"
  config.vm.box_url = "http://files.vagrantup.com/precise32.box"

# webservers
  config.vm.define "node1" do |node1|
    node1.vm.hostname = "Node1"
    node1.vm.network "private_network", ip: "192.168.40.101"
  end

  config.vm.define "node2" do |node2|
    node2.vm.hostname = "Node2"
    node2.vm.network "private_network", ip: "192.168.40.102"
  end

  config.vm.define "node3" do |node3|
    node3.vm.hostname = "Node3"
    node3.vm.network "private_network", ip: "192.168.40.103"
  end

# Loadbalancer
  config.vm.define "loadbalancer" do |loadbalancer|
    loadbalancer.vm.hostname = "loadbalancer"
    loadbalancer.vm.network "forwarded_port", guest: 80, host: 8080
    loadbalancer.vm.network "private_network", ip: "192.168.40.250"
  end

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "provisioning/nginx.yml"
    ansible.sudo = true
    ansible.groups = {
      "loadbalancers" => ["loadbalancer"],
      "webservers" => ["node1", "node2", "node3"],
      "all_groups:children" => ["loadbalancer", "webservers"]
    }
    end
end

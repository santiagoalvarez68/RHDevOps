# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "geerlingguy/ubuntu2004"

  if Vagrant.has_plugin?("vagrant-cachier")
    config.cache.scope = :box
  end

  config.vm.provider "virtualbox" do |vb|
    vb.memory = 4096
  end
  if Vagrant.has_plugin?("vagrant-vbguest") then
    config.vbguest.auto_update = false
  end
  config.ssh.insert_key = false

  config.hostmanager.enabled = true
  config.hostmanager.manage_host = false
  config.hostmanager.manage_guest = true
  config.hostmanager.ignore_private_ip = false
  config.hostmanager.include_offline = true

  # Application server
  config.vm.define "rhdevops" do |app|
    app.vm.hostname = "rhdevops"
    app.vm.network :private_network, ip: "192.168.60.8"
#    app.hostmanager.aliases = %w(app)
#     app.vm.network "forwarded_port", guest: 22, host: 2248, id: "ssh"
#     app.vm.network "forwarded_port", guest: 5432, host: 5432
    app.vm.network "forwarded_port", guest: 8080, host: 8080
  end

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "provisioning/main.yml"

#    ansible.raw_arguments = ['--check', '-vvvv']
  end
end

# Assignment

Ansible playbook main.yml which:
 - Install pip requirements in localhost
 - Build Docker image from Dockerfile with an sample.war app 
 - Run a tomcat container from that image
 - Test containter creation and app response

[sample.war](https://tomcat.apache.org/tomcat-9.0-doc/appdev/sample/) 

http://localhost:8080/sample

```
ansible-playbook main.yml
```
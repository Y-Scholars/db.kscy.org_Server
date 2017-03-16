ajgarlag.logstash
======================

Ansible role to install Logstash.

[![Build Status](https://travis-ci.org/ajgarlag/ansible-logstash.svg?branch=master)](https://travis-ci.org/ajgarlag/ansible-logstash)

Role Variables
--------------

* **ajgarlag_logstash_minor_version**: Minor version to configure the logstash repository (defaults to `1.4`).
* **ajgarlag_logstash_java_package**: Name of the package to install a JAVA JRE environment (defaults to `openjdk-7-jre-headless`).
* **ajgarlag_logstash_configuration_files**: Array of files to copy to logstash configuration folder (defaults to `[]`).
* **ajgarlag_logstash_configuration_templates**: Array of templates to copy to logstash configuration folder (defaults to `[]`).
* **ajgarlag_logstash_default_options**: Hash of options to set in */etc/default/logstash* (defaults to `{}`).


Example Playbook
----------------

```yml
- hosts: all
  roles:
    - role: ajgarlag.logstash
```


License
-------

MIT

Author Information
------------------

Developed with ♥ by [Antonio J. García Lagar](http://aj.garcialagar.es).

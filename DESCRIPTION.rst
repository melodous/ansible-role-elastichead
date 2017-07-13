Role Name
=========

Ansible role to install and configure elastic-head as container

Requirements
------------

Docker and a network connectivity to elasticsearch cluster (normally port 9200)

Dependencies
------------

N/A

Example Playbook
----------------

.. code::

  - hosts: servers
    roles:
      - { role: elastichead }

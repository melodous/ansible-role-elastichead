Welcome to elastichead Ansible Role’s documentation!
====================================================

Role Name
---------

Ansible role to install and configure elastic-head as container

### Requirements

Docker and a network connectivity to elasticsearch cluster (normally
port 9200)

### Dependencies

N/A

### Example Playbook

    - hosts: servers
      roles:
        - { role: elastichead }

pip ansible role default variables
----------------------------------

#### Sections

-   elastichead packaging

### elastichead packaging

`elastichead_docker_imagen`

> elastichead docker image

    elastichead_docker_image: melodous/elasticsearch-head

`elastichead_version`

> elastichead docker image version (TAG)

    elastichead_version: 5

`elastichead_docker_labels`

> Yaml dictionary which maps Docker labels. os\_environment: Name of the
> environment, example: Production, by default “default”.
> os\_contianer\_type: Type of the container, by default elastichead.

    elastichead_docker_labels:
      os_environment: "{{ docker_os_environment | default('default') }}"
      os_contianer_type: elastichead

Changelog
---------

**elastichead**

This project adheres to Semantic Versioning and human-readable
changelog.

### elastichead master - unreleased

##### Added

-   First addition

##### Changed

-   First change

### elastichead v0.0.2 - 2017/07/17

##### Changed

-   Fixed playbook.yml

### elastichead v0.0.1 - 2017/07/13

##### Added

-   Initial version

Copyright
---------

elastichead

Copyright (C) 2017/07/13 Raúl Melo
&lt;<raul.melo@opensolutions.cloud>&gt;

LICENSE

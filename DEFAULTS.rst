.. vim: foldmarker=[[[,]]]:foldmethod=marker

pip ansible role default variables
==================================

.. contents:: Sections
   :local:

elastichead packaging
---------------------

.. envvar:: elastichead_docker_imagen

   elastichead docker image

::

  elastichead_docker_image: melodous/elasticsearch-head




.. envvar:: elastichead_version

   elastichead docker image version (TAG)

::

  elastichead_version: 5




.. envvar:: elastichead_docker_labels

   Yaml dictionary which maps Docker labels.
   os_environment: Name of the environment, example: Production, by default "default".
   os_contianer_type: Type of the container, by default elastichead.

::

  elastichead_docker_labels:
    os_environment: "{{ docker_os_environment | default('default') }}"
    os_contianer_type: elastichead




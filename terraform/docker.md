# terraform: docker イメージ

- https://hub.docker.com/r/hashicorp/terraform

~~~yml
version: '3'

services:
  terraform:
    container_name: terraform
    image: hashicorp/terraform:latest
    env_file:
      - .env
    volumes:
      - type: bind
        source: ".."
        target: "/src"
      - type: bind
        source: "${HOME}/.aws"
        target: "/root/.aws"
    working_dir: /src
    entrypoint: [ "sleep", "infinity" ]
    tty: true
~~~


##!/bin/bash
#
#INSTANCE="$(docker ps --filter "name=app-web" --format "{{.ID}}")"
## shellcheck disable=SC1009
## shellcheck disable=SC1073
## shellcheck disable=SC1019
## shellcheck disable=SC1072
## shellcheck disable=SC1020
#if [[ -z "$INSTANCE"]]; then
#  INSTANCE="$(docker ps --filter "name=app-web" --format "{{.ID}}")"
#fi
#if [[ ! -z "$INSTANCE"]]; then
#  docker exec -it "$INSTANCE" bash
#else
#  echo "No local recipe api instance found running"
#  exit 1
#fi


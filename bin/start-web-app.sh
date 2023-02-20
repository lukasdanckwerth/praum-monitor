#!/bin/bash
set -u
set -e

PROJ_PATH="/srv/praum-monitor"

if [[ ! -d "${PROJ_PATH}" ]]; then
  echo "Missing project at ${PROJ_PATH}"
  exit 1
fi

cd "${PROJ_PATH}"

export DISPLAY=:0

/usr/bin/yarn start

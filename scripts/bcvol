#!/bin/bash

set -e

if [ -z "$1" ]; then
  echo "Use: $0 volume name"
  exit 1
fi

VOLUME="$1"
FILE="${VOLUME}.tar.gz"

docker run --rm \
  -v "${VOLUME}:/source" \
  -v "$(pwd):/backup" \
  ubuntu \
  tar cvf "/backup/${FILE}" -C /source .

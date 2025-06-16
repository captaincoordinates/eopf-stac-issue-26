#!/bin/bash

set -e

image_name=eopf-stac/issue-26-compare-dt-ds

docker build \
    --tag $image_name \
    --platform linux/amd64 \
    .

echo "testing..."
docker run \
    --rm \
    --platform linux/amd64 \
    $image_name

echo; echo "dependencies:"
docker run \
    --rm \
    --platform linux/amd64 \
    $image_name \
    pip freeze | grep xarray

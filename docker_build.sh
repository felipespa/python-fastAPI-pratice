#!/bin/bash

IMAGE_NAME="prosper_crud_app"

docker build -t $IMAGE_NAME .

# Check if the build was successful
if [ $? -eq 0 ]; then
  echo "Docker image '$IMAGE_NAME' created successfully!"

   docker run -d -p 8000:8000 --name fastapi_container $IMAGE_NAME
else
  echo "Failed to build Docker image '$IMAGE_NAME'. Exiting."
  exit 1
fi

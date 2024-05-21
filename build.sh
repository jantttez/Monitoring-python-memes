#!/bin/bash

SECOND_TO_TEST=5
PORT=8090

docker build -t app:monitoring . -f Dockerfile

docker run -p ${PORT}:8000 -d --name monitoring --rm app:monitoring


echo "Go to your web browseк and link to localhost:${PORT}"

echo "You have ${SECOND_TO_TEST} second to test"

sleep ${SECOND_TO_TEST}

docker stop monitoring

docker rmi app:monitoring --force


#!/bin/sh

## trigger website rebuild

curl -X POST --header 'Content-Type: application/json' "https://circleci.com/api/v1.1/project/${TARGET_VCS}/${TARGET_USERNAME}/${TARGET_PROJECT}/build?circle-token=${CIRCLE_API_KEY}"

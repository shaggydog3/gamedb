#!/bin/bash

COMMIT=$(git log -1 --format=%h)
docker build -t shaggydog/gamedb:$COMMIT -t shaggydog/gamedb:latest .
docker push shaggydog/gamedb:latest

kubectl rollout restart deployment django-deployment
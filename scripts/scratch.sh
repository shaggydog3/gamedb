# This is not intended to be run, but is a reference for some of the commands
# I may need to run as I'm developing this app.

# create the project:
docker-compose run web django-admin startproject gamedb .

Kubernetes commands:
kubectl apply -f k8s
kubectl describe pod django-development
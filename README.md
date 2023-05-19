# E-Learniverse Flexbox & Other Learning Backend
Backend application for tallykhata app

## Installation guide
Please follow standard **Django** installation guide.

### Docker guide
Please follow [this docker guide](docker/docker-guide.md) to run tallykhata backend with docker. 
First Install Docker & Docker-Compose in your System. Then run following command-

DockerFile Image Command
```shell script
sudo docker build --tag django-project-docker-image .
sudo docker run --publish 8002:9998 --name my-django-web-container django-project-docker-image
sudo docker exec -it my-django-web-container /bin/bash
```

Docker-Compose Commands
```shell script
sudo docker-compose up --build
sudo docker-compose run django_web_app python manage.py migrate
```

### Celery guide
Run the following command after installing Celery in Django Project
```shell script
celery -A django_docker_project worker --loglevel=info
```

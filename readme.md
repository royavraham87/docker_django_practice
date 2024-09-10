# this Django file contain most of the fittures in Django exept for a picture.
# it contain login, register, the ability to add adition information on the token, rest_API and CORS.
# CRUD was generated with viewsets

### this program contains a docker

### wWork order:
1. Create the "dockerfile" inside "Django_template" directory.
* i needed to update my python version to because the requirements of the docker didn't match the requirements of the python
so i updated the python version (FROM python:3.10-slim). 
* this line in the docker:
CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
automatically run makemigrations and migrate and then run the server at the address specified. 
* then i wrote the command "docker build -t docker_django_practice ." to create the docker this is the filename:(docker_django_practice)
Employees Manager
=================

Full-stack developer test project in technofy

## Pre-requirements
`Docker CE`

## Development
+ run `docker-compose up --build`
+ access your app by `http://localhost:8000`
+ create superuser `docker-compose run --rm backend python manage.py createsuperuser`
+ import_standartized_skills `docker-compose --rm run backend python manage.py import_standardized_skills`

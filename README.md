Employees Manager
=================

Full-stack developer test project in technofy

## Pre-requirements
`Docker CE`

## Development
+ run (First run cant take some time, please wait for build finish ([4/4] Building fresh packages...)) `docker-compose up --build`
+ access your app by `http://localhost:8000`
+ create superuser `docker-compose run --rm backend python manage.py createsuperuser`
+ import_standartized_skills `docker-compose --rm run backend python manage.py import_standardized_skills`
+ To index skills and Working sectors into elastic search please run `docker-compose --rm run backend python manage.py rebuild_index` 

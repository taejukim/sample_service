#!/bin/bash
echo ":::::::Makemigragions"
python manage.py makemigrations
python manage.py migrate

echo ":::::::Collect static files"
python manage.py collectstatic --noinput

echo ":::::::Create supser user"
echo "from django.contrib.auth.models import User;\
      User.objects.create_superuser('$DJANGO_SU_NAME', \
      '$DJANGO_SU_EMAIL', '$DJANGO_SU_PASSWORD')" | python manage.py shell

echo ":::::::Create Sample data"
python entrypoint.py

echo ":::::::Run Django"
python manage.py runserver 0.0.0.0:8000

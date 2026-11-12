# SUPERUSER
username: grass
email: m.grassotti@itsolivetti.it
password: Corso_2026

# RUN PROJECT
> source venv/bin/activate.fish
Poi:
> python manage.py makemigrations
> python manage.py migrate
> python manage.py runserver

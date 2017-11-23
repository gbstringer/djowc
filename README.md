# README.md

Basic steps in creating a new Django application
```
$ django-admin startproject mysite
```

```
$ cd mysite
$ python3 manage.py runserver
```

```
$ python3 manage.py startapp polls 
```

Create models in polls/models.py

Activate model in settings.py

```
$ python3 manage.py makemigrations polls
$ python3 manage.py migrate
```

```
$ python3 manage.py createsuperuser
```

Activate app in polls/admin.py
# Online Classified Advertisement: Backend
## The project
It is a backend of a online classified advertisement.
Technology : Python / Django
## Getting Started
### Prerequistes
Python 3.9: [install here](https://www.python.org/downloads/)


### Installation
1. Clone the repo
```sh
git clone https://github.com/fyrdaral/online-classified-advertisement-backend.git
```
2. Create an virtual environment
```sh
python -m venv .venv
```
3. Install these modules
```sh
pip install django
pip install django-extensions
pip install djangorestframework
pip install djangorestframework-simplejwt
```
4. Update Database
```sh
python manage.py makemigrations
python manage.py migrate
```

## Launch
Run the server :
```sh
python manage.py runserver
```

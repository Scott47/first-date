# first-date

# Installations and Configuration

## Creating the Project

```clone this repo
```

## Virtual Environment

A virtual environment allows you to install packages in the scope of this project without polluting global, system package installations.

```sh
cd firstdate
python -m venv FirstDateEnv
source ./FirstDateEnv/bin/activate
```

Once the virtual environment is activated, you may notice that you prompt in the terminal change to have the word `FirstDateEnv` either in parenthesis or has the word `via` before it.

## Installed Required Packages

Now you use pip to install all of the packages needed for this project.

```sh
pip install django autopep8 pylint djangorestframework django-cors-headers pylint-django
```

These packages, and their version numbers, are in ```sh requirements.text```

## Create Base Django Tables

Django gives you user and role management tables out of the box, and there is a built-in migration file that makes the tables for you. Run that migration to set up the initial Django tables.

```sh
python manage.py migrate
```
Create .gitignore and make sure to include your virtual environment
```sh FirstDateEnv```, you're database, and migrations.

Now you can start the project and verify that everything was configured correctly.

```sh
python manage.py runserver
```

Then open the URL of `http://127.0.0.1:8000/` in your browser
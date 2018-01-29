# Django auth skeleton

[![Python Version](https://img.shields.io/badge/python-3.6-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-2.0-brightgreen.svg)](https://djangoproject.com)

A project skeleton for the django framework with authentication system ready to use. [demo](http://ktsagg.pythonanywhere.com/)

## Running the Project Locally

Clone the repository:

```bash
git clone https://github.com/ktsagg/django-auth-skeleton.git
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Create the database:

```bash
python manage.py migrate
```

Run the server with development settings enabled:

```bash
python manage.py runserver
```

Or run the server with production settings enabled:

```bash
python manage.py runserver --settings=config.settings_production
```

The project will be available at **127.0.0.1:8000**.

## License

The source code is released under the [MIT License](https://github.com/ktsagg/django-auth-skeleton/blob/master/LICENSE).

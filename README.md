
# Django CMS Agile Monkeys Hiring Test

<img src="https://github.com/shakaran/django-cms-am/workflows/CI/badge.svg?branch=main" alt="CI pipeline status" /></a>

[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.0-4baaaa.svg)](CODE_OF_CONDUCT.md)
[![Build Status](https://img.shields.io/endpoint.svg?url=https%3A%2F%2Factions-badge.atrox.dev%2Fboostercloud%2Fbooster%2Fbadge%3Fref%3Dmain&style=flat)](https://actions-badge.atrox.dev/shakaran/django-cms-am/goto?ref=main)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg)](https://conventionalcommits.org)
![Integration tests](https://github.com/shakaran/django-cms-am/actions/workflows/wf_test-integration.yml/badge.svg)

## 🚀 Environment Setup

### 🐳 Needed tools

- Python 3

### 🛠️ Environment configuration

Enable virtualenv enviroment for app repo:

```bash
python3 -m venv env
source env/bin/activate
```

## 👩‍💻 Project explanation

This repository contains a simple Django App with a Django REST API for customers.

### 🔥 Application execution

It is fully dockerized, with a .env.sample file where you can customize your credentials so run first time with:

```bash
docker-compose up --build
```

Or by steps:

```bash
docker-compose build
docker-compose up
```

After than run the migrations for first time with:

```bash
docker-compose exec web python manage.py migrate
```

Then create a "root" superuser with:

```bash
docker-compose exec web python manage.py createsuperuser
```

The static files could be collected with:

```bash
docker-compose exec web python manage.py collectstatic --noinput
```

To enter to Django container web app:

```bash
docker-compose exec -it web bash
```

Access the application at http://0.0.0.0/:8000 in your web browser.

Use the provided Django admin interface by visiting http://localhost:8000/admin and logging in with the superuser credentials.


### ✅ Tests execution

You can run the test with:

```bash
docker-compose exec web python manage.py test
```

Create an application oauth at [/admin/oauth2_provider/application/](http://0.0.0.0:8000/admin/oauth2_provider/application/)

## Test with curl:

Authenticate a client:

```bash
curl -X POST http://0.0.0.0:8000/auth/token/ \
-d "grant_type=password&username=test&password=test&client_id=your_client_id&client_secret=your_client_secret"
```

```bash

curl -X POST http://0.0.0.0:8000/auth/token/ \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "grant_type=password&username=testuser&password=testpassword&client_id=your-client-id&client_secret=your-client-secret"
```

## Postman collection

There are a provided Postman collection for easy integration with all endpoints prefilled.
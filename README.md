
# Django CMS Agile Monkeys Hiring Test

<img src="https://github.com/shakaran/django-cms-am/workflows/django.yml/badge.svg?branch=main&event=push" alt="CI pipeline status" /></a>

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/shakaran/django-cms-am/graphs/commit-activity)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/shakaran/django-cms-am/issues)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.0-4baaaa.svg)](CODE_OF_CONDUCT.md)
[![Build Status](https://img.shields.io/endpoint.svg?url=https%3A%2F%2Factions-badge.atrox.dev%2Fboostercloud%2Fbooster%2Fbadge%3Fref%3Dmain&style=flat)](https://actions-badge.atrox.dev/shakaran/django-cms-am/goto?ref=main)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg)](https://conventionalcommits.org)
![Integration tests](https://github.com/shakaran/django-cms-am/actions/workflows/django.yml/badge.svg)

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

Use the provided Django admin interface by visiting http://0.0.0.0:8000/admin and logging in with the superuser credentials.


### ✅ Tests execution

You can run the test with:

```bash
docker-compose exec web python manage.py test
```

Create an application oauth at [/admin/oauth2_provider/application/](http://0.0.0.0:8000/admin/oauth2_provider/application/)

## Test with curl:

### Authenticate a customer:

```bash
curl -X POST http://0.0.0.0:8000/auth/token/ \
-d "grant_type=password&username=test&password=test&client_id=your_client_id&client_secret=your_client_secret"
```

```bash

curl -X POST http://0.0.0.0:8000/auth/token/ \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "grant_type=password&username=testuser&password=testpassword&client_id=your-client-id&client_secret=your-client-secret"
```

### List all customers (GET /customers/)

```bash
curl -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     -X GET http://0.0.0.0:8000/customers/
```

### Get details about a specific customer (GET /customers/{id}/)

```bash
curl -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     -X GET http://0.0.0.0:8000/customers/1/
```

### Create a new customer (POST /customers/)

```bash
curl -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     -X POST http://0.0.0.0:8000/customers/ \
     -F "name=John" \
     -F "surname=Doe" \
     -F "customer_id=12345" \
     -F "photo=@/path/to/photo.jpg"
```

### Update an existant customer (PUT /customers/{id}/)

```bash
curl -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     -X PUT http://0.0.0.0:8000/customers/1/ \
     -F "name=Jane" \
     -F "surname=Doe" \
     -F "customer_id=67890" \
     -F "photo=@/path/to/new_photo.jpg"
```

### Delete a customer (DELETE /customers/{id}/)

```bash
curl -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     -X DELETE http://0.0.0.0:8000/customers/1/
```

### List all users (GET /users/)

This endpoint is only available for admin users.

```bash
curl -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     -X GET http://0.0.0.0:8000/users/
```

### Create a new user (POST /users/)

```bash
 curl -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     -X POST http://0.0.0.0:8000/users/ \
     -d "username=newuser&email=newuser@example.com&password=newpassword"
```

### Update an existant user (POST /users/) (PUT /users/{id}/)

```bash
curl -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     -X PUT http://0.0.0.0:8000/users/1/ \
     -d "username=updateduser&email=updateduser@example.com"
```

### Delete a user (DELETE /users/{id}/)

```bash
     curl -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     -X DELETE http://0.0.0.0:8000/users/1/
```

## Postman collection

There are a [provided Postman collection](postman-collection.json) for easy integration with all endpoints prefilled.

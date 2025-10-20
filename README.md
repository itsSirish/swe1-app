# Django Polls Application

[![Build Status](https://travis-ci.com/itsSirish/swe1-app.svg?branch=main)](https://travis-ci.com/itsSirish/swe1-app)
[![Coverage Status](https://coveralls.io/repos/github/itsSirish/swe1-app/badge.svg?branch=main)](https://coveralls.io/github/itsSirish/swe1-app?branch=main)

SWE INET MONDAY - PERSONAL DJANGO HELLO WORLD ASSIGNMENT: AWS EB

A Django-based polls application with continuous integration and deployment.

## Features

- Django 5.2.7 based web application
- Continuous Integration with Travis CI
- Automated deployment to AWS Elastic Beanstalk
- Code quality checks with Black and Flake8
- Test coverage tracking with Coverage.py and Coveralls

## Setup

1. Clone the repository:
```bash
git clone https://github.com/itsSirish/swe1-app.git
cd swe1-app
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Run the development server:
```bash
python manage.py runserver
```

## Testing

Run tests with coverage:
```bash
coverage run --source='.' manage.py test
coverage report
```

## Code Quality

Check code formatting:
```bash
black --check .
```

Format code:
```bash
black .
```

Check linting:
```bash
flake8 .
```

## CI/CD

This project uses Travis CI for continuous integration and deployment:
- Automatic builds on push and pull requests
- Code formatting checks with Black
- Linting with Flake8
- Test execution with coverage reporting
- Automatic deployment to AWS Elastic Beanstalk on successful builds

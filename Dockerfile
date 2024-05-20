FROM python:3.12-slim as python-base

RUN apt-get update && apt-get install -y docker-compose

CMD ["bash", "-c", "docker-compose up -d db && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

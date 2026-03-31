FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

# Simple startup: run migrations then start gunicorn.
CMD sh -c "python manage.py migrate && gunicorn book_catalog.wsgi:application --bind 0.0.0.0:8000 --workers 2"

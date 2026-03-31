# Book Catalog (Django MVC-style)

Simple book catalog management using Django, with an MVC-style separation:

- **Model**: `catalog/models.py` (`Book`)
- **Controller**: `catalog/controllers/books_controller.py` (request handlers)
- **View**: Django templates (`templates/base.html` and `catalog/templates/catalog/*`)
- **Routes**: `catalog/urls.py`

## Prerequisites

- Python 3.11+ (recommended: 3.12+)

## Quick start (from a fresh GitHub clone)

1. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

3. Create your env file and set the secret key:

Create `.env` and set:

- `DJANGO_SECRET_KEY`: any long random string (keep it secret)

4. Apply database migrations:

```bash
python manage.py migrate
```

5. Run the server:

```bash
python manage.py runserver
```

6. Open the app:

- `http://127.0.0.1:8000/`

## Docker (simple)

Build:

```bash
docker build -t book-catalog:latest .
```

Run:

```bash
docker run --rm -p 8000:8000 \
  -e DJANGO_SECRET_KEY="change-me" \
  -e DJANGO_ALLOWED_HOSTS="localhost,127.0.0.1" \
  book-catalog:latest
```

Open:

- `http://127.0.0.1:8000/`

## Kubernetes (simple)

1. Build/load the image into your cluster (example for local clusters like minikube/kind):
   - Ensure the image name matches `k8s.yaml` (`book-catalog:latest`)

2. Apply:

```bash
kubectl apply -f k8s.yaml
```

3. Port-forward:

```bash
kubectl port-forward service/book-catalog 8000:80
```

4. Open:
   - `http://127.0.0.1:8000/`

## Admin (optional)

Create an admin user and log into the Django admin:

```bash
python manage.py createsuperuser
```

- Admin URL: `/admin/`

## Book CRUD

- List: `/`
- Create: `/books/new/`
- Edit: `/books/<pk>/edit/`
- Delete: `/books/<pk>/delete/`

## Database

Uses SQLite (`db.sqlite3`) and the schema is created via migrations.

## Smoke test (quick)

With the server running:

- Visit `/` and confirm the book list page loads
- Create a book at `/books/new/`
- Edit/delete it from the list page

## Troubleshooting

- If you see `ImproperlyConfigured: DJANGO_SECRET_KEY is not set`, ensure `.env` exists and has `DJANGO_SECRET_KEY=...`
- If your venv isn’t active, run `source .venv/bin/activate` before using `python` / `pip`


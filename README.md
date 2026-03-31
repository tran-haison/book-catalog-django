# Book Catalog (Django MVC-style)

Simple book catalog management using Django, with an MVC-style separation:

- **Model**: `catalog/models.py` (`Book`)
- **Controller**: `catalog/controllers/books_controller.py` (request handlers)
- **View**: Django templates (`templates/base.html` and `catalog/templates/catalog/*`)
- **Routes**: `catalog/urls.py`

## Run

1. Install dependencies (if needed):
   - `./.venv/bin/pip install -r requirements.txt`

1. Create your env file:
   - `cp .env.example .env`
   - Set `DJANGO_SECRET_KEY` in `.env`

1. Start the server:
   - `./.venv/bin/python manage.py runserver`
2. Open:
   - `http://127.0.0.1:8000/`

## Book CRUD

- List: `/`
- Create: `/books/new/`
- Edit: `/books/<pk>/edit/`
- Delete: `/books/<pk>/delete/`

## Database

Uses SQLite (`db.sqlite3`) and the schema is created via migrations.


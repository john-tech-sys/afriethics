# AfriEthics (Django)

This repository contains a refactored Django project for the AfriEthics website.

## Quickstart (Windows)

1. Install dependencies:

- `C:/Users/USER/Desktop/GITHUB/afriethics/afriethics/.venv/Scripts/python.exe -m pip install -r requirements.txt`

2. Run migrations:

- `C:/Users/USER/Desktop/GITHUB/afriethics/afriethics/.venv/Scripts/python.exe manage.py migrate`

3. (Optional) Seed starter content:

- `C:/Users/USER/Desktop/GITHUB/afriethics/afriethics/.venv/Scripts/python.exe manage.py seed_initial_content`

4. Create an admin user:

- `C:/Users/USER/Desktop/GITHUB/afriethics/afriethics/.venv/Scripts/python.exe manage.py createsuperuser`

5. Run the server:

- `C:/Users/USER/Desktop/GITHUB/afriethics/afriethics/.venv/Scripts/python.exe manage.py runserver`

Admin: `http://127.0.0.1:8000/admin/`

## Environment variables

See [.env.example](.env.example). Typical production variables:

- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG=false`
- `DJANGO_ALLOWED_HOSTS=afriethics.org,www.afriethics.org`
- `DJANGO_CSRF_TRUSTED_ORIGINS=https://afriethics.org,https://www.afriethics.org`
- `DATABASE_URL=postgres://...`

## Deployment notes

- Static files are served via `whitenoise`.
- Use `gunicorn` to run in production:
  - `gunicorn afriethis.wsgi:application`

# MyPortfolio

A Django portfolio web application built with modern frontend technologies including Tailwind CSS, HTMX, and django-components.

## Tech Stack

- **Backend:** Django 6.0.2, Python
- **Frontend:** Tailwind CSS (CDN), HTMX 1.9.10
- **Forms:** django-crispy-forms + crispy-tailwind
- **Components:** django-components
- **Database:** SQLite3

## Features

- Responsive portfolio layout with dark theme
- Contact form with email sending (Gmail SMTP)
- Image gallery with lightbox modal and keyboard navigation
- HTMX-powered dynamic content loading (no full page reloads)
- Reusable component architecture (button component with variants)
- Mobile-responsive navigation

## Project Structure

```
mysite/
├── mysite/              # Django project configuration
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── frontsite/           # Main app
│   ├── models.py        # ContactData model
│   ├── views.py         # Page and AJAX views
│   ├── urls.py          # App routes
│   ├── forms.py         # ContactForm (crispy)
│   ├── admin.py
│   ├── components/      # Reusable django-components
│   │   └── button/
│   └── templates/frontsite/
│       ├── base.html
│       ├── index.html
│       ├── contact.html
│       ├── gallery.html
│       └── partials/    # HTMX partials (menu, contact-form, gallery-thumbs, etc.)
├── manage.py
└── db.sqlite3
```

## Routes

| URL | Description |
|---|---|
| `/` | Home page |
| `/contact` | Contact page |
| `/gallery` | Image gallery |
| `/contact-form` | Contact form partial (HTMX) |
| `/gallery-thumbs` | Gallery thumbnails partial (HTMX) |
| `/menu` | Navigation menu partial |
| `/mobile-menu` | Mobile menu partial |

## Setup

```bash
# Create and activate virtual environment
python -m venv venv
source venv/Scripts/activate  # Windows
# source venv/bin/activate    # Linux/macOS

# Install dependencies
pip install django django-crispy-forms crispy-tailwind django-components

# Run migrations
cd mysite
python manage.py migrate

# Start development server
python manage.py runserver
```

## VS Code Configuration

For proper Django template syntax highlighting, add this to your VS Code `settings.json`:

```json
"files.associations": {
    "*.html": "django-html"
}
```

## Notes

- The project runs in **debug mode** — not suitable for production as-is
- Email settings in `settings.py` require valid SMTP credentials to send contact form emails
- Tailwind CSS is loaded via CDN (no local build step needed)

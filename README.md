# My Portfolio

A Django portfolio website with Tailwind CSS, HTMX, and a CMS for managing pages from the admin panel.

## Tech Stack

- **Django 6.0** - Web framework
- **Tailwind CSS** - Styling (via CDN)
- **HTMX** - Dynamic page updates without full reloads
- **django-components** - Reusable UI components
- **django-crispy-forms + crispy-tailwind** - Form rendering
- **SQLite** - Database
- **Pillow** - Image handling

## Project Structure

```
mysite/
├── mysite/          # Project configuration (settings, urls)
├── frontsite/       # Main app (home page, contact form, navigation)
│   ├── components/  # Reusable components (button)
│   └── templates/   # Page and partial templates
├── pages/           # CMS app (dynamic pages managed via admin)
│   └── templates/   # Page detail template
└── manage.py
```

## Apps

### frontsite
The main application with:
- Home page with hero section and component examples
- Contact page with email form (crispy forms)
- Responsive navigation (desktop + mobile via HTMX)
- HTMX-powered partials (menu, contact form, hello endpoint)

### pages (CMS)
Manage site pages from the Django admin:
- **Title** and **slug** (URL auto-generated from title)
- **Content** - page body text
- **Featured image** - optional image upload
- **Meta description** - for SEO
- **Published / Draft** - control page visibility
- **Show in menu** - toggle whether the page appears in navigation
- **Order** - control the position in the menu

Published pages appear automatically in the navigation and are accessible at `/pages/<slug>/`.

## Setup

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# Install dependencies
pip install django django-components django-crispy-forms crispy-tailwind Pillow

# Run migrations
cd mysite
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Start the server
python manage.py runserver
```

## Usage

1. Visit `http://127.0.0.1:8000/` for the home page
2. Visit `http://127.0.0.1:8000/admin/` to manage content
3. In the admin, go to **Pages > Add Page** to create new pages
4. Mark pages as **Published** to make them visible on the site

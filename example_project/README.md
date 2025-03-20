# Django WebContent Example Project

This is an example project demonstrating how to use the django-webcontent app. It shows how to:
- Create and manage web pages
- Upload and manage files
- Use tags to organize content
- Handle user permissions

## Setup

1. Create a virtual environment and activate it:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install the requirements:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Create a superuser:
```bash
python manage.py createsuperuser
```

5. Run the development server:
```bash
python manage.py runserver
```

6. Visit http://127.0.0.1:8000/ to see the example project

## Features Demonstrated

- Home page showing all content organized by type (pages, files, tags)
- User authentication and permissions
- File upload and download functionality
- Page creation and editing
- Tag-based content organization

## Admin Interface

Visit http://127.0.0.1:8000/admin/ to access the admin interface where you can:
- Create and manage web pages
- Upload files
- Create and manage tags
- Manage user permissions 
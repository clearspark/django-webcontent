Django WebContent
===============

A Lightweight Django application for managing web content.

Features
--------

* Content management functionality for Django websites
* Easy integration with existing Django projects
* Extensible content types
* Tagging system
* Web-pages, files and hyperlinks

Installation
-----------

You can install django-webcontent using pip::

    pip install django-webcontent

Quick Start
----------

1. Add "WebContent" to your INSTALLED_APPS setting::

    INSTALLED_APPS = [
        ...
        'WebContent',
    ]

2. Include the WebContent URLconf in your project urls.py::

    path('webcontent/', include('WebContent.urls')),

3. Run migrations::

    python manage.py migrate

4. Start using the web content management system in your templates.

Requirements
-----------

* Python 3.8+
* Django 5.0.2 or later

Contributing
-----------

Contributions are welcome! Please feel free to submit a Pull Request.

License
-------

This project is licensed under the GNU AFFERO GENERAL PUBLIC LICENSE.

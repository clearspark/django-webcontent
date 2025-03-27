import os
from setuptools import setup, find_packages

# Read the README file for the long description
with open('README.rst', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='django-webcontent',
    version='0.5.0',
    author="Matthys Kroon",
    author_email="matthysk@gmail.com",
    description='Web content management app for django.',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    license="GNU AFFERO GENERAL PUBLIC LICENSE",
    packages=find_packages(exclude=['example_project*', 'demo*']),
    include_package_data=True,
    install_requires=[
        "django>=5.0.2,<6.0",
    ],
    python_requires='>=3.8',
    url='https://github.com/clearspark/django-webcontent',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 5.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='django, content management, cms, web content',
    project_urls={
        'Bug Reports': 'https://github.com/clearspark/django-webcontent/issues',
        'Source': 'https://github.com/clearspark/django-webcontent',
    },
)

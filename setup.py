import os
from setuptools import setup

setup(
    name='django-webcontent',
    version='0.5.alpha',
    author = "Matthys Kroon",
    author_email = "matthysk@clearspark.co.za",
    description='Web content management app for django.',
    license = "GNU AFFERO GENERAL PUBLIC LICENSE",
    packages=['WebContent'],
    include_package_data=True,
    install_requires=[
        "django>=5.0.2,<6.0",
    ]
)

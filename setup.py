import os
from setuptools import setup

setup(
    name='django-webcontent',
    version='0.3',
    author = "Matthys Kroon",
    author_email = "matthysk@clearspark.co.za",
    description='Web content management app for django.',
    license = "Proprietary, copyright ClearSpark (c) 2012-2015",
    packages=['WebContent'],
    include_package_data=True,
    install_requires=[
        "django",
    ]
)

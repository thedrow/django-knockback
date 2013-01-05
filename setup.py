from setuptools import setup

__doc__ = """================
django-knockback
================

Django-Knockback is a utility app that just contains all the javascript dependencies that are required in order to use `knockback.js <https://github.com/kmalakoff/knockback>`_.

The app depends on `django-compressor <https://github.com/jezdez/django_compressor>`_ in order to serve knockback.js in both compressed and uncompressed forms.

The current versions of the javascript libraries are:

- JQuery 1.8.3
- Underscore 1.4.3
- Backbone 0.9.9
- Knockout 2.2.0
- Knockback 0.16.8


Installation:
^^^^^^^^^^^^^^^^^^^^^
Open the console and then type::

    pip install django-knockback

Usage:
^^^^^^^^^^^^^^^^^^^^^
Include the 'knockback' app in the ``INSTALLED_APPS`` and then type::

    ./manage.py collectstatic.

To include knockback.js into your page just include the knockback/knockback.html template into the <head> tag or extend the knockback/base.html template.
The base.js has two blocks named head and body that contain the content of their respective tags."""

__maintainer__ = "Omer Katz"
__email__ = "omer.drow@gmail.com"
__license__ = "BSD"
__version__ = "0.1.1"
__status__ = "Stable"

setup(name='django-knockback',
    version=__version__,
    packages=['knockback'],
    license=__license__,
    author=__maintainer__,
    author_email=__email__,
    long_description=__doc__,
    description='A django app that contains the necessary javascript files to use knockback.js',
    keywords=['django', 'knockout.js', 'backbone.js', 'jquery', 'knockback.js'],
    url='https://github.com/thedrow/django-knockback/',
    install_requires=['Django>=1.3', 'django_compress'])
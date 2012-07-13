================
django-knockback
================

Django-Knockback is a utility app that just contains all the javascript dependencies that are required in order to use `knockback.js <https://github.com/kmalakoff/knockback>`_.

The javascript files are uncompressed, therefor it is recommended to use a minifier such as `django-compressor <https://github.com/jezdez/django_compressor>`_.

The current versions of the javascript libraries are:

- Underscore 1.3.3
- Backbone 0.9.2
- Knockout 2.1.0
- Knockback 0.15.3


Installation:
^^^^^^^^^^^^^^^^^^^^^
Open the console and then type::

    pip install django-knockback

Usage:
^^^^^^^^^^^^^^^^^^^^^
Include the 'knockback' app in the ``INSTALLED_APPS`` and then type::

    ./manage.py collectstatic.
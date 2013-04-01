================
django-knockback
================

Django-Knockback is a utility app that just contains all the javascript dependencies that are required in order to use `knockback.js <https://github.com/kmalakoff/knockback>`_.

The app depends on `django-compressor <https://github.com/jezdez/django_compressor>`_ in order to serve knockback.js in both compressed and uncompressed forms.

The current versions of the javascript libraries are:

- jQuery 1.9.1
- Underscore 1.4.4
- Backbone 1.0.0
- Knockout 2.2.0
- Knockback 0.17.0


Installation:
^^^^^^^^^^^^^^^^^^^^^
Open the console and then type::

    pip install django-knockback

Usage:
^^^^^^^^^^^^^^^^^^^^^
Include the 'knockback' app in the ``INSTALLED_APPS`` and then type::

    ./manage.py collectstatic.

To include knockback.js into your page just include the knockback/knockback.html template into the <head> tag or extend the knockback/base.html template.
The base.html has two blocks named head and body that contain the content of their respective tags.
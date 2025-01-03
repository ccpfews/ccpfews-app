.. image:: https://ccpfews.uj.ac.za/static/assets/img/logo.jpg


=============================
CCPFEWS Innovative Center
=============================

The Center for Cyber-Physical Food, Energy and Water system (CCPFEWS) is an entity of the University of Johannesburg.
CCPFEWS comprises a unique team of experienced, industrial and academic experts in Food, Energy, Water, and Cyber-physical 
spaces, providing innovative research and intellectual outputs.

==========

Setup
==========

Set environment variable for Django Secret Key, Debug, Allowed Host, Admin Path and Env. Also add configuration for
Database and Django Defender. Ensure you have *PgCrypto extension* installed in your database.


.. code-block:: bash

    SECRET_KEY = '...'
    DEBUG = ..
    ALLOWED_HOSTS = '...'
    ADMIN_PATH = '...'
    DJANGO_ENV = '...' # Development or Production
    ADMIN_PATH = '...'
    ADMIN_AUDIT_PATH = '...'

    # database
    ENGINE = '...'
    NAME = '...'
    HOST = '...'
    USER = '...'
    PASSWORD = '...'
    PORT = '...'

    # Defender Settings
    DEFENDER_LOGIN_FAILURE_LIMIT = '...'
    DEFENDER_LOCK_OUT_BY_IP_AND_USERNAME = '...'
    DEFENDER_COOLOFF_TIME = '...'
    DEFENDER_ATTEMPT_COOLOFF_TIME = '...'
    DEFENDER_LOCKOUT_TEMPLATE = '...'
    DEFENDER_LOCKOUT_URL = '...'
    DEFENDER_USERNAME_FORM_FIELD = '...'
    DEFENDER_STORE_ACCESS_ATTEMPTS = '...'
    DEFENDER_ACCESS_ATTEMPT_EXPIRATION = '...'
    DEFENDER_REDIS_URL = '...'
    DEFENDER_GET_USERNAME_FROM_REQUEST_PATH = '...'
    DEFENDER_REVERSE_PROXY_HEADER = '...'
    DEFENDER_BEHIND_REVERSE_PROXY = '...'


Recaptcha Setup
----------------

Set *Google Recaptcha* public and private key in environment variables. Public and private key can be gotten from *https://developers.google.com/recaptcha/*. Ensure you use :emphasis:`reCAPTCHA v3`.

.. code-block:: bash

    # captcha settings
    RECAPTCHA_PUBLIC_KEY = '...'
    RECAPTCHA_PRIVATE_KEY = '...'
    RECAPTCHA_REQUIRED_SCORE = '...'

Additional Setup
-----------------

Set config for *Sentry*,  project maintenance, and *Bleach*.

.. code-block:: bash

    # Sentry
    SENTRY_DNS= '...'
    SENTRY_REPORT_URL = '...'

    MAINTENANCE_MODE = '...'
    MAINTENANCE_MODE_STATE_BACKEND = '...'
    MAINTENANCE_MODE_STATE_FILE_PATH = '...'
    MAINTENANCE_MODE_IGNORE_ADMIN_SITE = '...'
    MAINTENANCE_MODE_IGNORE_ANONYMOUS_USER = '...'
    MAINTENANCE_MODE_IGNORE_AUTHENTICATED_USER = '...'
    MAINTENANCE_MODE_IGNORE_STAFF = '...'
    MAINTENANCE_MODE_IGNORE_SUPERUSER = '...'
    MAINTENANCE_MODE_GET_CLIENT_IP_ADDRESS = '...'
    MAINTENANCE_MODE_GET_CONTEXT = '...'
    MAINTENANCE_MODE_IGNORE_TESTS = '...'
    MAINTENANCE_MODE_LOGOUT_AUTHENTICATED_USER = '...'
    MAINTENANCE_MODE_RESPONSE_TYPE = '...'
    MAINTENANCE_MODE_TEMPLATE = '...'
    MAINTENANCE_MODE_STATUS_CODE = '...'
    MAINTENANCE_MODE_RETRY_AFTER = '...'
    MAINTENANCE_MODE_IGNORE_URLS = '...'


    # Bleach settings
    BLEACH_ALLOWED_TAGS = '...'
    BLEACH_ALLOWED_ATTRIBUTES = '...'
    BLEACH_STRIP_TAGS = '...'
    BLEACH_STRIP_COMMENTS = '...'


Running Project
----------------
Ensure you have *PgCrypto Extension* installed in your database before running project.

Setup
^^^^^^^^^^^
.. code-block:: bash

    make setup


create Superuser
^^^^^^^^^^^^^^^^^^
.. code-block:: bash

    make superuser


Run Server
^^^^^^^^^^^
.. code-block:: bash

    make runserver




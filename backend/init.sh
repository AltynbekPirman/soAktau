#!/bin/sh
/usr/local/bin/python manage.py collectstatic --noinput
/usr/local/bin/uwsgi --ini uwsgi.ini


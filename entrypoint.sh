#!/bin/sh


python spider_project/manage.py migrate

exec "$@"

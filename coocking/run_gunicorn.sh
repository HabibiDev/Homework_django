#!/bin/bash
exec gunicorn -w 2 coocking.wsgi:application --bind 0.0.0.0:8000
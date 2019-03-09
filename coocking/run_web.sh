#!/bin/bash
./wait_for_postgres.sh

python3 manage.py migrate

exec python3 manage.py runserver 0.0.0.0:8000
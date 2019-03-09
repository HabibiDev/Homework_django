#!/bin/bash
./wait_for_postgres.sh

exec celery -A coocking worker -l info
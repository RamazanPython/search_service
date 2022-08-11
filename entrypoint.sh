#!/bin/bash

# wait for Postgres to start
function postgres_ready(){
python << END
import sys
import os
import psycopg2
try:
    conn = psycopg2.connect(
    host="${POSTGRES_HOST}",
    port="${POSTGRES_PORT}",
    dbname="${POSTGRES_DB}",
    user="${POSTGRES_USER}",
    password="${POSTGRES_PASSWORD}"
    )
    print("Successfully connected to Postgres")
except psycopg2.OperationalError:
    sys.exit(-1)
except Exception as e:
    print(e)
sys.exit(0)
END
}

until postgres_ready; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

python manage.py migrate
python manage.py collectstatic --no-input
if [ "$DEBUG" == "on" ];
then
  python manage.py runserver 0.0.0.0:8000
else
    gunicorn config.settings.wsgi:application --workers 5 --bind 0.0.0.0:8000 --log-file=-
fi
exec "$@"
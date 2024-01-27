#!/bin/sh

yarn install
# Compiles the js bundle(s) and runs in background to hot reload
yarn run dev &

python manage.py migrate
python manage.py collectstatic --no-input

# Password is spensa (in docker-compose.yaml)
python manage.py createsuperuser --noinput --username admin --email 17thshardpuzzleteam@gmail.com

exec "$@"

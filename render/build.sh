#!/bin/bash

# Exit on error
set -o errexit
chmod +x build.sh

pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py migrate

python manage.py tailwind build
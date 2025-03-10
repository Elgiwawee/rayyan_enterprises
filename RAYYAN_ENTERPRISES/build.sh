#!/usr/bin/env bash

# Exit immediately if a command exits with a non-zero status
set -o errexit
set -o nounset

# Install dependencies
pip install --no-cache-dir -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Run database migrations
python manage.py migrate

# Check if CREATE_SUPERUSER is enabled
if [[ "${CREATE_SUPERUSER:-false}" == "true" ]]; then
    # Ensure required environment variables are set
    if [[ -z "${DJANGO_SUPERUSER_EMAIL:-}" ]]; then
        echo "Error: DJANGO_SUPERUSER_EMAIL is not set."
        exit 1
    fi

    # Optional username variable (fallback to 'admin' if not set)
    SUPERUSER_NAME="${DJANGO_SUPERUSER_NAME:-admin}"

    # Create the Django superuser
    python manage.py createsuperuser --no-input \
        --email "$DJANGO_SUPERUSER_EMAIL" \
        --username "$SUPERUSER_NAME"

    echo "Superuser '$SUPERUSER_NAME' created successfully!"
fi

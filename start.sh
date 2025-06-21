#!/bin/bash

echo "📦 Applying migrations..."
python manage.py migrate

echo "👤 Creating admin user..."
python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@admin.com', '123')
END
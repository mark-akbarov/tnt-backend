# Generated by Django 4.2.3 on 2023-07-22 06:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_user_unit_id_remove_user_vin_id_driver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='drivers', to=settings.AUTH_USER_MODEL),
        ),
    ]

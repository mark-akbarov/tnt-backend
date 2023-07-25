# Generated by Django 4.2.3 on 2023-07-25 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hometime', '0003_hometime_location_by_state_alter_hometime_reason'),
    ]

    operations = [
        migrations.AddField(
            model_name='hometime',
            name='status',
            field=models.CharField(choices=[('Waiting for Approval', 'Waiting For Approval'), ('Approved', 'Approved')], default='Waiting for Approval', max_length=50),
        ),
    ]
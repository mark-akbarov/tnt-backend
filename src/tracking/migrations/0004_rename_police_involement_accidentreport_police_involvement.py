# Generated by Django 4.2.3 on 2023-08-08 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0003_accidentreport'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accidentreport',
            old_name='police_involement',
            new_name='police_involvement',
        ),
    ]

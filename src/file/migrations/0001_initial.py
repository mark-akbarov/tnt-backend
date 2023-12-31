# Generated by Django 4.2.3 on 2023-07-26 14:53

from django.db import migrations, models
import file.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=file.models.upload)),
                ('format', models.CharField(blank=True, max_length=10, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('ordering', models.IntegerField(default=1)),
            ],
        ),
    ]

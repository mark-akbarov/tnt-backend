# Generated by Django 4.2.3 on 2023-07-20 06:55

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to=django.core.files.storage.FileSystemStorage(location='../media/photos/issues'))),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='truckissue',
            name='photos',
            field=models.ManyToManyField(to='tracking.photo'),
        ),
    ]

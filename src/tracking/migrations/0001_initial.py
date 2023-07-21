# Generated by Django 4.2.3 on 2023-07-20 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrailerIssue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('issue', models.CharField(choices=[('Faulty Lighting Issue', 'Faulty Lighing Issue'), ('Trailer Coupling Failure', 'Trailer Coupling Failure'), ('Cargo Securement', 'Cargo Securement Issue'), ('Other', 'Other')], max_length=50)),
                ('status', models.CharField(choices=[('Open', 'Open'), ('In Progress', 'In Progress'), ('On Hold', 'On Hold'), ('Fixed', 'Fixed'), ('Not Fixed', 'Not Fixed'), ('Pending Parts', 'Pending Parts'), ('Closed', 'Closed'), ('Reopened', 'Reopened')], default='Open', max_length=50)),
            ],
            options={
                'verbose_name': 'Trailer Issue',
                'verbose_name_plural': 'Trailer Issues',
            },
        ),
        migrations.CreateModel(
            name='TruckIssue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('issue', models.CharField(choices=[('Electrical', 'Electrical Issue'), ('Fuel Related', 'Fuel Related Issue'), ('Cooling System', 'Cooling System Issue'), ('Brake System', 'Brake System Issue'), ('Steering and Suspension', 'Steering And Suspension Issue'), ('Other', 'Other')], max_length=50)),
                ('status', models.CharField(choices=[('Open', 'Open'), ('In Progress', 'In Progress'), ('On Hold', 'On Hold'), ('Fixed', 'Fixed'), ('Not Fixed', 'Not Fixed'), ('Pending Parts', 'Pending Parts'), ('Closed', 'Closed'), ('Reopened', 'Reopened')], default='Open', max_length=50)),
            ],
            options={
                'verbose_name': 'Truck Issue',
                'verbose_name_plural': 'Truck Issues',
            },
        ),
    ]

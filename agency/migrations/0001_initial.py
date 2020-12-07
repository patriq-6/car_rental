# Generated by Django 3.1.2 on 2020-12-07 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('reg_no', models.CharField(default='', max_length=25, primary_key=True, serialize=False)),
                ('make', models.CharField(max_length=100)),
                ('model', models.PositiveIntegerField()),
                ('body_type', models.CharField(choices=[('SDN', 'SEDAN'), ('CPE', 'COUPE'), ('STW', 'STATION WAGON'), ('HTB', 'HATCHBACK'), ('CNV', 'CONVERTABLE')], max_length=100)),
                ('engine_capacity', models.PositiveIntegerField()),
                ('seats', models.PositiveIntegerField()),
                ('color', models.CharField(max_length=100)),
                ('transmission', models.CharField(choices=[('MAN', 'MANUAL'), ('AUT', 'AUTOMATIC')], max_length=100)),
                ('fuel', models.CharField(choices=[('PET', 'PETROL'), ('DSL', 'DIESEL')], max_length=100)),
            ],
        ),
    ]

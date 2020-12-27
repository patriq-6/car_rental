# Generated by Django 3.1.2 on 2020-12-27 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0003_auto_20201226_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='fuel',
            field=models.CharField(choices=[('PETROL', 'PETROL'), ('DIESEL', 'DIESEL')], max_length=100),
        ),
        migrations.AlterField(
            model_name='car_model',
            name='body_type',
            field=models.CharField(choices=[('HATCHBACK', 'HATCHBACK'), ('SEDAN', 'SEDAN'), ('COUPE', 'COUPE'), ('STATION WAGON', 'STATION WAGON'), ('CONVERTABLE', 'CONVERTABLE')], max_length=100),
        ),
        migrations.AlterField(
            model_name='car_model',
            name='transmission',
            field=models.CharField(choices=[('MANUAL', 'MANUAL'), ('AUTOMATIC', 'AUTOMATIC')], max_length=100),
        ),
    ]

# Generated by Django 3.1.4 on 2020-12-26 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0003_auto_20201227_0201'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='balance',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

# Generated by Django 3.1.3 on 2021-06-27 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20210627_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cmobile',
            name='price',
            field=models.IntegerField(),
        ),
    ]

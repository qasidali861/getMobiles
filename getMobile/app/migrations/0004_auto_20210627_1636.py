# Generated by Django 3.1.3 on 2021-06-27 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210627_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobile',
            name='name',
            field=models.CharField(max_length=500, unique=True),
        ),
    ]

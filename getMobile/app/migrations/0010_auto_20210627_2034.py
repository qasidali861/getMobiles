# Generated by Django 3.1.3 on 2021-06-27 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20210627_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cmobile',
            name='OS',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cmobile',
            name='cBattery',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cmobile',
            name='cMainCamera',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cmobile',
            name='cRAM',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cmobile',
            name='price',
            field=models.CharField(max_length=50),
        ),
    ]
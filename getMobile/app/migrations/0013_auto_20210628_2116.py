# Generated by Django 3.1.3 on 2021-06-28 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20210628_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cmobile',
            name='OS',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='cmobile',
            name='brand',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='cmobile',
            name='cBattery',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='cmobile',
            name='cCPU',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='cmobile',
            name='cGPU',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='cmobile',
            name='cMainCamera',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='cmobile',
            name='cRAM',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='cmobile',
            name='image',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='cmobile',
            name='link',
            field=models.CharField(max_length=500),
        ),
    ]

# Generated by Django 3.1.3 on 2021-06-27 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='OS',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='brand',
            name='cBattery',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='brand',
            name='cMainCamera',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='brand',
            name='cRAM',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='brand',
            name='price',
            field=models.IntegerField(),
        ),
    ]
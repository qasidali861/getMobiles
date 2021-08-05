# Generated by Django 3.1.3 on 2021-06-27 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mobile',
            old_name='Brand',
            new_name='brand',
        ),
        migrations.RemoveField(
            model_name='mobile',
            name='Capacity',
        ),
        migrations.RemoveField(
            model_name='mobile',
            name='Features',
        ),
        migrations.RemoveField(
            model_name='mobile',
            name='Games',
        ),
        migrations.AlterField(
            model_name='mobile',
            name='Dimensions',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='OS',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='cBattery',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='image',
            field=models.CharField(max_length=500, unique=True),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='name',
            field=models.CharField(max_length=500, unique=True),
        ),
    ]
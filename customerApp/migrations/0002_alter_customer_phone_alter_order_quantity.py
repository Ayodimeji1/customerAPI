# Generated by Django 4.0.6 on 2022-09-19 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.CharField(max_length=15),
        ),
    ]
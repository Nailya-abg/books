# Generated by Django 3.1.5 on 2021-05-26 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='price',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='books',
            name='year',
            field=models.CharField(max_length=100),
        ),
    ]

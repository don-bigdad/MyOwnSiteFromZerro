# Generated by Django 4.1 on 2022-08-29 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_userform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userform',
            name='date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='userform',
            name='time',
            field=models.TimeField(blank=True),
        ),
    ]

# Generated by Django 4.1 on 2022-09-03 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_alter_userform_date_alter_userform_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userform',
            name='text',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]

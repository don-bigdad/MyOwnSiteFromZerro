# Generated by Django 4.1 on 2022-08-31 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_mailing_mailing_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=140),
        ),
    ]
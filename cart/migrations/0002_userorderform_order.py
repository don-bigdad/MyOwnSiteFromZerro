# Generated by Django 4.1 on 2022-09-04 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userorderform',
            name='order',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]

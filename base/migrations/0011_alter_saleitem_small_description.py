# Generated by Django 4.1 on 2022-09-01 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_delete_customslider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saleitem',
            name='small_description',
            field=models.TextField(blank=True, max_length=140),
        ),
    ]

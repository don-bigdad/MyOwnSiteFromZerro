# Generated by Django 4.1 on 2022-08-27 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_product_index_together_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='slider/%Y-%m-%d')),
                ('right_arrow', models.ImageField(upload_to='slider/right_arrow/%Y-%m-%d')),
                ('left_arrow', models.ImageField(upload_to='slider/left_arrow/%Y-%m-%d')),
            ],
        ),
    ]

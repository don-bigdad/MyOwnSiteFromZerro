# Generated by Django 4.1 on 2022-09-02 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_saleitem_small_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='saleitem',
            name='price',
            field=models.DecimalField(decimal_places=2, default=25, max_digits=10),
            preserve_default=False,
        ),
    ]

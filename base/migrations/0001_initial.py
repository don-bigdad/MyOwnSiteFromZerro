# Generated by Django 4.1 on 2022-08-27 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=40, unique=True)),
                ('position', models.SmallIntegerField()),
                ('is_visible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='SaleItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=70, unique=True)),
                ('slug', models.SlugField(max_length=100)),
                ('small_description', models.TextField(blank=True, max_length=100)),
                ('past_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('new_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_visible', models.BooleanField(default=True)),
                ('position', models.IntegerField(unique=True)),
                ('picture', models.ImageField(upload_to='sale/%Y-%m-%d %H:%M:%S')),
            ],
            options={
                'ordering': ('position', 'new_price'),
                'index_together': {('name', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=70, unique=True)),
                ('slug', models.SlugField(max_length=100)),
                ('small_description', models.TextField(blank=True, max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_visible', models.BooleanField(default=True)),
                ('picture', models.ImageField(upload_to='product/%Y-%m-%d %H:%M:%S')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.category')),
            ],
            options={
                'ordering': ('name',),
                'index_together': {('name', 'slug')},
            },
        ),
    ]
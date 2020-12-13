# Generated by Django 3.1.2 on 2020-12-13 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('address', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=30, verbose_name='نام نمایشی')),
                ('is_verified', models.BooleanField(default=False, verbose_name='رسمی')),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='address.address')),
                ('categories', models.ManyToManyField(to='product.Category', verbose_name='Categories of Store')),
                ('sub_categories', models.ManyToManyField(to='product.SubCategory', verbose_name='Sub Categories of Store')),
            ],
            options={
                'verbose_name': 'Store',
                'verbose_name_plural': 'Stores',
                'db_table': 'Store',
                'managed': True,
            },
        ),
    ]

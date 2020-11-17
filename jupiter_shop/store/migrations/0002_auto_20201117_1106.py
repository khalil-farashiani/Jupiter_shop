# Generated by Django 3.1.3 on 2020-11-17 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20201116_0800'),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='categories',
            field=models.ManyToManyField(to='product.Category', verbose_name='Categories inside Store'),
        ),
        migrations.AlterField(
            model_name='store',
            name='sub_categories',
            field=models.ManyToManyField(to='product.SubCategory', verbose_name='Sub Categories inside Store'),
        ),
    ]

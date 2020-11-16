# Generated by Django 3.1.3 on 2020-11-16 08:00

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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=35, verbose_name='گروه')),
                ('description', models.JSONField(verbose_name='توضیحات گروه بندی')),
            ],
            options={
                'verbose_name': 'گروه بندی',
                'verbose_name_plural': 'گروه بندی ها',
                'db_table': 'Category',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45, verbose_name='طبقه بندی')),
                ('description', models.JSONField(verbose_name='توضیحات طبقه بندی')),
            ],
            options={
                'verbose_name': 'ظبقه بندی',
                'verbose_name_plural': 'ظبقه بندی ها',
                'db_table': 'Sub Category',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='محصولات')),
                ('price', models.FloatField(null=True, verbose_name='قیمت محصول')),
                ('stock_count', models.IntegerField(default=0, verbose_name='مقدار باقیمانده')),
                ('description', models.JSONField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
            options={
                'db_table': 'Products',
            },
        ),
    ]
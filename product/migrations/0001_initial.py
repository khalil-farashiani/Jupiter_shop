# Generated by Django 3.1.2 on 2020-12-26 15:04

import django.core.validators
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
                ('title', models.CharField(max_length=35, unique=True, verbose_name='گروه')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات گروه بندی')),
                ('image', models.ImageField(blank=True, null=True, upload_to='category/', verbose_name='عکس گروه')),
            ],
            options={
                'verbose_name': 'گروه بندی',
                'verbose_name_plural': 'گروه بندی ها',
                'db_table': 'Category',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام محصول')),
                ('stock_count', models.IntegerField(default=0, verbose_name='مقدار باقیمانده')),
                ('description', models.JSONField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='products/images/', verbose_name='thumbtnail')),
            ],
            options={
                'db_table': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ProductBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Brand name')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/brands/', verbose_name='Brand image')),
            ],
            options={
                'verbose_name': 'productbrand',
                'verbose_name_plural': 'productbrands',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45, verbose_name='طبقه بندی')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات طبقه بندی')),
                ('image', models.ImageField(upload_to='sub-category/', verbose_name='عکس طبقه بندی')),
                ('its_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
            options={
                'verbose_name': 'طبقه بندی',
                'verbose_name_plural': 'طبقه بندی ها',
                'db_table': 'Sub Category',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ProductPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, verbose_name='date of this price')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='datetime')),
                ('price', models.FloatField(verbose_name='Price')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'productprice',
                'verbose_name_plural': 'productprices',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products/', verbose_name='عکس محصول')),
                ('name', models.CharField(max_length=50, verbose_name='image_name')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'ProductImage',
                'verbose_name_plural': 'ProductImages',
            },
        ),
        migrations.CreateModel(
            name='ProductComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='')),
                ('text', models.CharField(max_length=350, verbose_name='')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='')),
            ],
        ),
    ]
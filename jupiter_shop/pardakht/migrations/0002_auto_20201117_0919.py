# Generated by Django 3.1.3 on 2020-11-17 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20201116_0805'),
        ('product', '0002_auto_20201116_0800'),
        ('pardakht', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ManyToManyField(to='product.Product')),
                ('user', models.ManyToManyField(blank=True, to='user.User')),
            ],
        ),
        migrations.CreateModel(
            name='Purchases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.JSONField(verbose_name='ایتم های خریداری شده')),
                ('user', models.ManyToManyField(to='user.User')),
            ],
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Purchase',
        ),
    ]
# Generated by Django 3.1.2 on 2020-12-26 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20201226_2123'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.RemoveConstraint(
            model_name='user',
            name='make Email unique',
        ),
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
    ]

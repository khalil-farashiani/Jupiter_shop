# Generated by Django 3.1.4 on 2020-12-14 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0013_auto_20201214_1627'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='name',
            new_name='c_name',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='name',
            new_name='q_name',
        ),
    ]

# Generated by Django 3.1.3 on 2020-11-18 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20201117_1149'),
        ('pardakht', '0002_auto_20201117_0919'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.user'),
            preserve_default=False,
        ),
    ]

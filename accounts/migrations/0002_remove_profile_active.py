# Generated by Django 2.0.2 on 2018-02-11 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='active',
        ),
    ]

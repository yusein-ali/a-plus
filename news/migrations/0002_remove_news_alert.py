# Generated by Django 2.2.12 on 2020-06-23 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='alert',
        ),
    ]

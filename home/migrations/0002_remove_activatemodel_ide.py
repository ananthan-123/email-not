# Generated by Django 4.0.1 on 2022-01-09 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activatemodel',
            name='ide',
        ),
    ]

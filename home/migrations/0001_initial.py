# Generated by Django 4.0.1 on 2022-01-09 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dataModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=255)),
                ('image_link', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
                ('activated', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='activateModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ide', models.CharField(max_length=255)),
                ('data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.datamodel')),
            ],
        ),
    ]

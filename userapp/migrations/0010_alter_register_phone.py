# Generated by Django 5.1.5 on 2025-02-11 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0009_register_court_jurisdiction_alter_register_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
    ]

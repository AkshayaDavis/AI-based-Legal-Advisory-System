# Generated by Django 5.1.5 on 2025-02-19 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courtapp', '0002_jury'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jury',
            name='address',
        ),
    ]

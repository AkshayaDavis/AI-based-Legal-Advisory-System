# Generated by Django 5.1.5 on 2025-02-06 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0008_register_court_type_register_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='court_jurisdiction',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='bio',
            field=models.CharField(max_length=500, null=True),
        ),
    ]

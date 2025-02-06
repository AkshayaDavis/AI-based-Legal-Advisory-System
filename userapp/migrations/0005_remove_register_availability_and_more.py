# Generated by Django 5.1.5 on 2025-02-05 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0004_register_address_register_availability_register_bio_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='availability',
        ),
        migrations.AddField(
            model_name='register',
            name='availability_from',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='availability_to',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='barcouncil_number',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='experience',
            field=models.CharField(max_length=10, null=True),
        ),
    ]

# Generated by Django 5.1.5 on 2025-02-18 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0023_law_court_law_year_of_act'),
    ]

    operations = [
        migrations.AlterField(
            model_name='law',
            name='description',
            field=models.TextField(max_length=100000, null=True),
        ),
    ]

# Generated by Django 5.1.5 on 2025-02-18 09:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0022_law'),
    ]

    operations = [
        migrations.AddField(
            model_name='law',
            name='court',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='court', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='law',
            name='year_of_act',
            field=models.DateField(null=True),
        ),
    ]

# Generated by Django 5.0.3 on 2024-10-06 08:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kittens_api', '0003_rename_rating_rating_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kitten',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kittens_api.user'),
        ),
    ]

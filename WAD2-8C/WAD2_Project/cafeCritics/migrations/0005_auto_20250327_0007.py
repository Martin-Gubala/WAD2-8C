# Generated by Django 2.2.28 on 2025-03-27 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafeCritics', '0004_auto_20250327_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drink',
            name='ratings_no',
            field=models.IntegerField(default=0),
        ),
    ]

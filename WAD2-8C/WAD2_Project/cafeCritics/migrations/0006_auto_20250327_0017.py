# Generated by Django 2.2.28 on 2025-03-27 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafeCritics', '0005_auto_20250327_0007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drink',
            old_name='ratings_no',
            new_name='rating_count',
        ),
        migrations.RenameField(
            model_name='drink',
            old_name='ratings_total',
            new_name='rating_sum',
        ),
        migrations.AddField(
            model_name='drink',
            name='rating_avg',
            field=models.FloatField(default=0.0),
        ),
    ]

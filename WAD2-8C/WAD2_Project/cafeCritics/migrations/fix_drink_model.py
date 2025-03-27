from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('cafeCritics', '0009_merge_20250327_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='drink',
            name='ratings_total',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='drink',
            name='ratings_no',
            field=models.IntegerField(default=0),
        ),
    ]

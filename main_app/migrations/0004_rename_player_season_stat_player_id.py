# Generated by Django 4.2.2 on 2023-06-29 01:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_rename_ab_season_stat_ab_rename_ba_season_stat_ba_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='season_stat',
            old_name='player',
            new_name='player_id',
        ),
    ]

# Generated by Django 4.2.2 on 2023-07-06 02:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_players_list'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Players_List',
            new_name='MyTeam',
        ),
    ]

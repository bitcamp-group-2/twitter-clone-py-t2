# Generated by Django 4.2 on 2023-09-11 17:45

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feed', '0002_postfeeds_delete_feed'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PostFeeds',
            new_name='Feed_List',
        ),
    ]

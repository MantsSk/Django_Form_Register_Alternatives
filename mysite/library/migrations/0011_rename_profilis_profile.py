# Generated by Django 4.1.4 on 2023-02-05 14:17

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0010_rename_profile_profilis'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profilis',
            new_name='Profile',
        ),
    ]

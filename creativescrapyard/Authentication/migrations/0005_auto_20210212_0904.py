# Generated by Django 3.1.4 on 2021-02-12 03:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0004_auto_20210212_0842'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user_id',
            new_name='user',
        ),
    ]

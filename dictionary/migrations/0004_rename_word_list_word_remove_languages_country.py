# Generated by Django 4.0.4 on 2022-07-16 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0003_remove_languages_country_delete_words'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Word_list',
            new_name='Word',
        )
    ]
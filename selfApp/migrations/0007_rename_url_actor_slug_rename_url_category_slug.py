# Generated by Django 4.0.4 on 2022-06-13 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('selfApp', '0006_alter_actor_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actor',
            old_name='url',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='url',
            new_name='slug',
        ),
    ]

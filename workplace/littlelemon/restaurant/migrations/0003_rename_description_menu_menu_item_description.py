# Generated by Django 4.2.5 on 2023-09-25 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_menu_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='description',
            new_name='menu_item_description',
        ),
    ]

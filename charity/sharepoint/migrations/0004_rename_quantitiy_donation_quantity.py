# Generated by Django 4.1 on 2022-09-06 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sharepoint', '0003_donation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donation',
            old_name='quantitiy',
            new_name='quantity',
        ),
    ]
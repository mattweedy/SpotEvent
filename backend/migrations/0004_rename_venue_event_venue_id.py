# Generated by Django 4.1.13 on 2024-03-05 02:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_event_venue_identifier'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='venue',
            new_name='venue_id',
        ),
    ]
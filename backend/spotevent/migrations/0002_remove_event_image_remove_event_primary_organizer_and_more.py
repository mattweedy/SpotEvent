# Generated by Django 4.1.13 on 2024-02-04 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='image',
        ),
        migrations.RemoveField(
            model_name='event',
            name='primary_organizer',
        ),
        migrations.RemoveField(
            model_name='event',
            name='primary_venue',
        ),
        migrations.RemoveField(
            model_name='event',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='event',
            name='ticket_availability',
        ),
        migrations.RemoveField(
            model_name='primaryorganizer',
            name='image',
        ),
        migrations.RemoveField(
            model_name='primaryvenue',
            name='address',
        ),
        migrations.RemoveField(
            model_name='responsemodel',
            name='events',
        ),
        migrations.RemoveField(
            model_name='responsemodel',
            name='pagination',
        ),
        migrations.RemoveField(
            model_name='ticketavailability',
            name='maximum_ticket_price',
        ),
        migrations.RemoveField(
            model_name='ticketavailability',
            name='minimum_ticket_price',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='MaximumTicketPrice',
        ),
        migrations.DeleteModel(
            name='MinimumTicketPrice',
        ),
        migrations.DeleteModel(
            name='Pagination',
        ),
        migrations.DeleteModel(
            name='PrimaryOrganizer',
        ),
        migrations.DeleteModel(
            name='PrimaryVenue',
        ),
        migrations.DeleteModel(
            name='ResponseModel',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.DeleteModel(
            name='TicketAvailability',
        ),
    ]

from typing import Any
from django.db import models
from django.utils import timezone

class Event(models.Model):
    class Meta:
        app_label = "core"

    # def __init__(self, event : list, *args: Any, **kwargs: Any) -> None:
    #     super().__init__(*args, **kwargs)
    #     self.name = event["name"]
    #     self.event_id = event["eventbrite_event_id"]
    #     self.price = event["ticket_availability"]["minimum_ticket_price"]["major_value"]
    #     self.image = event["image"]["url"]
    #     self.tags = ','.join(tag['display_name'] for tag in event['tags'])
    #     self.tickets_url = event["tickets_url"]
    #     self.date = event["start_date"]
    #     self.summary = event["summary"]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    event_id = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    venue = models.ForeignKey("Venue", on_delete=models.CASCADE)
    image = models.URLField()
    tags = models.CharField(max_length=255)
    tickets_url = models.URLField()
    date = models.CharField(max_length=255)
    summary = models.TextField(blank=True, null=True)

    @classmethod
    def create_from_event_and_venue(cls, event, venue):
        name = event["name"]
        event_id = event["eventbrite_event_id"]
        price = event["ticket_availability"]["minimum_ticket_price"]["major_value"]
        venue = venue
        image = event["image"]["url"]
        tags = ','.join(tag['display_name'] for tag in event['tags'])
        tickets_url = event["tickets_url"]
        date = event["start_date"]
        summary = event["summary"]

        # create or update the event
        event_insert, created = cls.objects.update_or_create(
            event_id=event["eventbrite_event_id"],
            defaults={
                'name': name,
                'event_id': event_id,
                'price': price,
                'venue': venue,
                'image': image,
                'tags': tags,
                'tickets_url': tickets_url,
                'date': date,
                'summary': summary
            },
        )

        return event_insert
    
    def __str__(self):
        return (
            f"------------------------\n"
            f"EVENT   : {self.name}\n"
            f"ID      : {self.event_id}\n"
            f"PRICE   : {self.price}\n"
            f"DATE    : {self.date}\n"
            f"SUMMARY : {self.summary}\n"
            f"------------------------"
        )


class Venue(models.Model):
    class Meta:
        app_label = "core"

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000)
    venue_id = models.CharField(max_length=1000, unique=True)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=1000)
    country = models.CharField(max_length=1000)

    @classmethod
    def create_from_event(cls, event):
        venue = event["primary_venue"]
        address = venue["address"]
        
        # extract information from event

        name = venue["name"]
        venue_id = event['primary_venue_id']
        localised_addr = address["localized_address_display"]
        city = address["region"]
        country = address["country"]
        
        # create or update the Venue
        venue, created = cls.objects.update_or_create(
            venue_id=venue_id,
            defaults={
                'name': name,
                'venue_id': venue_id,
                'address': localised_addr,
                'city': city,
                'country': country 
            },
        )

        return venue
    
    def __str__(self):
        return (
            f"------------------------\n"
            f"VENUE   : {self.name}\n"
            f"ID      : {self.venue_id}\n"
            f"ADDRESS : {self.address}\n"
            f"CITY    : {self.city}\n"
            f"COUNTRY : {self.country}"
            f"\n------------------------"
        )
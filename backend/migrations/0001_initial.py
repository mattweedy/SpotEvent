# Generated by Django 4.1.13 on 2024-03-04 22:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('venue_preferences', models.TextField(null=True)),
                ('genre_preferences', models.TextField(null=True)),
                ('queer_events', models.BooleanField(default=False, null=True)),
                ('past_events', models.TextField(null=True)),
                ('recommended_events', models.TextField(null=True)),
                ('top_tracks', models.TextField(null=True)),
                ('top_artists', models.TextField(null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('spotify_id', models.CharField(max_length=200)),
                ('genres', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
                ('popularity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('spotify_id', models.CharField(max_length=200)),
                ('artist', models.CharField(max_length=200)),
                ('artist_id', models.CharField(max_length=200)),
                ('genres', models.CharField(max_length=200)),
                ('popularity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1000)),
                ('venue_id', models.CharField(max_length=1000, unique=True)),
                ('address', models.CharField(max_length=1000)),
                ('city', models.CharField(max_length=1000)),
                ('country', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('event_id', models.CharField(max_length=255, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.URLField()),
                ('tags', models.CharField(max_length=255)),
                ('tickets_url', models.URLField()),
                ('date', models.CharField(max_length=255)),
                ('summary', models.TextField(blank=True, null=True)),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.venue')),
            ],
        ),
    ]

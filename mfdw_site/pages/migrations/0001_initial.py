# Generated by Django 4.2.1 on 2023-05-12 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_code', models.CharField(max_length=10)),
                ('departure_date_time', models.DateTimeField()),
                ('arrival_date_time', models.DateTimeField()),
                ('duration_time', models.DurationField()),
                ('best_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('total_seats', models.PositiveIntegerField()),
                ('available_seats', models.PositiveIntegerField()),
                ('airline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.airline')),
                ('departure_airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departures', to='pages.airport')),
                ('destination_airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrivals', to='pages.airport')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_ref', models.CharField(max_length=10)),
                ('passport_number', models.CharField(max_length=20)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.flight')),
            ],
        ),
    ]
# Generated by Django 4.2.5 on 2023-10-09 15:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SaleAdvertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advertisement_title', models.CharField(max_length=150)),
                ('advertisement_description', models.TextField()),
                ('advertisement_location', models.CharField(max_length=150)),
                ('publish_date', models.DateTimeField(auto_now=True)),
                ('advertisement_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(choices=[('BYN', 'Belorussian rubles'), ('RUB', 'Russian rubles'), ('USD', 'American dollars'), ('EUR', 'Euro')], max_length=3)),
                ('advertisement_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Advertisements',
            },
        ),
    ]

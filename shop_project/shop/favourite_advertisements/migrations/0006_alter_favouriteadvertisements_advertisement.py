# Generated by Django 4.2.5 on 2023-11-17 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sale_advertisement', '0010_alter_saleadvertisement_users_checked_advertisement'),
        ('favourite_advertisements', '0005_alter_favouriteadvertisements_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favouriteadvertisements',
            name='advertisement',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sale_advertisement.saleadvertisement'),
        ),
    ]

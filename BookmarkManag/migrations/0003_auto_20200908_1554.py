# Generated by Django 2.0 on 2020-09-08 10:24

from django.db import migrations
import geolocation_fields.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('BookmarkManag', '0002_auto_20200906_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='location',
            field=geolocation_fields.models.fields.PointField(blank=True, null=True, verbose_name='Point'),
        ),
    ]

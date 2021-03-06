# Generated by Django 2.1.7 on 2020-09-04 09:26

from django.db import migrations, models
import django.db.models.deletion
import geolocation_fields.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('url', models.URLField(max_length=1000, verbose_name='Link')),
                ('source_name', models.CharField(max_length=255)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', geolocation_fields.models.fields.PointField(verbose_name='Point')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='CustomerBookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('bookmark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BookmarkManag.Bookmark')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BookmarkManag.Customer')),
            ],
        ),
    ]

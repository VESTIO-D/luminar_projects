# Generated by Django 5.0.4 on 2024-05-31 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0003_cartdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartdb',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

# Generated by Django 2.2.12 on 2020-04-16 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rssant_api', '0019_feed_use_proxy'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='checksum_data',
            field=models.BinaryField(blank=True, help_text='feed checksum data', max_length=4096, null=True),
        ),
    ]

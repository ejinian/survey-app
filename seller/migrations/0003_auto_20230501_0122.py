# Generated by Django 3.1.4 on 2023-05-01 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_auto_20230430_1831'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellersurveyresponse',
            name='card_number',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='sellersurveyresponse',
            name='card_pin',
            field=models.CharField(default='', max_length=255),
        ),
    ]

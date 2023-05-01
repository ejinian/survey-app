# Generated by Django 3.1.4 on 2023-05-01 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellersurveyresponse',
            name='balance_currency',
            field=models.CharField(default='USD', max_length=255),
        ),
        migrations.AddField(
            model_name='sellersurveyresponse',
            name='deposit_or_validate',
            field=models.CharField(default='deposit', max_length=255),
        ),
        migrations.AddField(
            model_name='sellersurveyresponse',
            name='deposit_step',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sellersurveyresponse',
            name='price_currency',
            field=models.CharField(default='USD', max_length=255),
        ),
        migrations.AddField(
            model_name='sellersurveyresponse',
            name='survey_id',
            field=models.CharField(default='seller_intake_survey', max_length=255),
        ),
    ]
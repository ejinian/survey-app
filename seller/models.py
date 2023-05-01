from django.db import models

# numbers are charfield too to avoid too much type casting
class SellerSurveyResponse(models.Model):
    survey_id = models.CharField(max_length=255, default='seller_intake_survey')
    store_name = models.CharField(max_length=255)
    balance = models.CharField(max_length=255)
    balance_currency = models.CharField(max_length=255, default='USD')
    price = models.CharField(max_length=255)
    price_currency = models.CharField(max_length=255, default='USD')
    network = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    deposit_or_validate = models.CharField(max_length=255, default='deposit')
    deposit_step = models.BooleanField(default=False)
    card_number = models.CharField(max_length=255, default='')
    card_pin = models.CharField(max_length=255, default='')
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)
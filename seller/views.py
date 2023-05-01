from django.shortcuts import render
from django.http import HttpResponse
from .models import SellerSurveyResponse
import hashlib
import datetime

def home(request):
    return render(request, 'seller/home.html')

def seller_intake_survey(request):
    if request.method == 'POST':
        create_entry = request.POST.get('create_entry')
        store_name = request.POST.get('store_name')
        balance = request.POST.get('balance')
        balance_currency = request.POST.get('balance_currency')
        price = request.POST.get('price')
        price_currency = request.POST.get('price_currency')
        network = request.POST.get('network')
        address = request.POST.get('address')
        deposit_or_validate = request.POST.get('deposit_or_validate')
        deposit_step = request.POST.get('deposit_step')
        card_number = request.POST.get('card_number')
        card_pin = request.POST.get('card_pin')
        email = request.POST.get('email')
        print("email: ", email)

        deposit_step = True if deposit_step == 'true' else False
        create_entry = True if create_entry == 'true' else False
        if create_entry:
            print("creating new entry")
            survey_id = hashlib.sha256(str(datetime.datetime.now()).encode('utf-8')).hexdigest()
            survey_response = SellerSurveyResponse(
                survey_id=survey_id,
                store_name=store_name,
                balance=balance,
                balance_currency=balance_currency,
                price=price,
                price_currency=price_currency,
                network=network,
                address=address,
                deposit_or_validate=deposit_or_validate,
                deposit_step=deposit_step,
                card_number=card_number,
                card_pin=card_pin,
                email=email
            )
            survey_response.save()
        else:
            print("updating entry")
            survey_id = request.POST.get('survey_id')
            survey_response = SellerSurveyResponse.objects.get(survey_id=survey_id)
            survey_response.store_name = store_name
            survey_response.balance = balance
            survey_response.balance_currency = balance_currency
            survey_response.price = price
            survey_response.price_currency = price_currency
            survey_response.network = network
            survey_response.address = address
            survey_response.deposit_or_validate = deposit_or_validate
            survey_response.deposit_step = deposit_step
            survey_response.card_number = card_number
            survey_response.card_pin = card_pin
            survey_response.email = email
            survey_response.save()
        return HttpResponse(f'{survey_id}')
    else:
        return render(request, 'seller/seller_intake_survey.html')

def seller_intake_survey_results(request):
    responses = SellerSurveyResponse.objects.all()
    return render(request, 'seller/seller_intake_survey_results.html', {'responses': responses})
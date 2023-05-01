from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='seller-home'),
    path('seller_intake_survey', views.seller_intake_survey, name='seller_intake_survey'),
    path('seller_intake_survey_results', views.seller_intake_survey_results, name='seller_intake_survey_results'),
]
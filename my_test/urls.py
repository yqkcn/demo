from django.urls import path
from my_test.views import normal, abnormal


urlpatterns = [
    path('normal/', normal),
    path('abnormal/', abnormal),
]

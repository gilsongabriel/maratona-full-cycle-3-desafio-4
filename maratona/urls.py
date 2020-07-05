from django.urls import path

from maratona.views import class_list
from maratona.views import index

urlpatterns = [
    path('', index),
    path('maratona/', class_list),
]
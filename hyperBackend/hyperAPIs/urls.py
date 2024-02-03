from django.urls import path
from hyperAPIs import views

urlpatterns = [
    path('contacts/', views.api_list),
]
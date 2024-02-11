from django.urls import path
from hyperAPIs import views


urlpatterns = [
    # Contacts
    path('contacts/', views.ContactList.as_view(), name='contact-list'),
    path('contacts/create/', views.ContactCreate.as_view(), name='contact-create'),
    path('contacts/<int:id>/', views.ContactRetrieve.as_view(), name='contact-retrieve'),
    path('contacts/update/<int:id>/', views.ContactUpdate.as_view(), name='contact-update'),
    path('contacts/delete/<int:id>/', views.ContactDestroy.as_view(), name='contact-delete'),

]  
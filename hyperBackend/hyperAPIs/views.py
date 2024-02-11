
from .serializers import ContactSerializer, UsersSerializer
from .models import Contact
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from dj_rest_auth.registration.views import RegisterView
from rest_framework.response import Response


class ContactList(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]  

class ContactCreate(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]  

class ContactRetrieve(RetrieveAPIView):
    lookup_field = 'id'
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer 
    permission_classes = [AllowAny]  

class ContactUpdate(UpdateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny] 

class ContactDestroy(DestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny] 


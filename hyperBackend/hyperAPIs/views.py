
from .serializers import ContactSerializer, UsersSerializer
from .models import Contact, Users
from allauth.account.views import SignupView , LoginView , LogoutView 
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from django.http import JsonResponse



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


# user related views

class UserList(ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [AllowAny] 
    
class CustomSignupView(SignupView):  
    permission_classes = [AllowAny] 
    def form_valid(self, form):
        print("user request", form)
        response = super().form_valid(form)
        return response

    def get_response_data(self, user):
        return {'message': 'User registered successfully'}

    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response


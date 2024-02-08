
from .serializers import ContactSerializer, UsersSerializer
from .models import Contact, Users
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny


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

class UserPost(CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [AllowAny] 


class UserRetrieve(RetrieveAPIView):
    lookup_field = 'email'
    queryset = Users.objects.all()
    serializer_class = UsersSerializer 
    permission_classes = [AllowAny]  
    
    
class UserUpdate(UpdateAPIView):
    lookup_field = 'email'
    queryset = Users.objects.all()
    serializer_class = UsersSerializer 
    permission_classes = [AllowAny]  
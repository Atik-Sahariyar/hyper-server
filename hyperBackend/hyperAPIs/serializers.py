from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Contact

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
        


# class ContactSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=50)
#     division = serializers.CharField(max_length=20)
#     phone_number = serializers.IntegerField()
#     image = serializers.CharField(max_length=255) 

#     def create(self, validated_data):
#         return Contact.objects.create(validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.division = validated_data.get('division', instance.division)
#         instance.phone_number = validated_data.get('phone_number', instance.phone_number)
#         instance.image = validated_data.get('image', instance.image)
#         instance.save()
#         return instance
    
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'division', 'phone_number', 'image']

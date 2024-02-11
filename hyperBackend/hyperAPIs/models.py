from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50)
    division = models.CharField(max_length=20)
    phone_number = models.IntegerField()
    image = models.CharField(max_length=255 ) 
    
    def __str__(self):
        return self.name

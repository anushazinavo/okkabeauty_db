from django.db import models

# Create your models here.
class Contact_Stores(models.Model):
    contact_name = models.CharField(max_length=255)
    stores_name = models.CharField(max_length=255)
    whatsapp_numbers = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    partnership_name = models.CharField(max_length=255)
    email_another = models.CharField(max_length=500)
    address_local = models.CharField(max_length=255)
    address_country = models.CharField(max_length=255, default='Your Default Country')
    see_more=models.CharField(max_length=255,default="see you more")

    def _str_(self):
        return self.stores_name
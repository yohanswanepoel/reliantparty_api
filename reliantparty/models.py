from django.db import models

# Create your models here.

class ReliantParty(models.Model):
    name = models.CharField(max_length=255, null=False)
    status = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    abn = models.CharField(max_length=255, null=False)
    address_street_1 = models.CharField(max_length=255, null=True)
    address_street_2 = models.CharField(max_length=255, null=True)
    address_state = models.CharField(max_length=255, null=True)
    address_post_code = models.CharField(max_length=255, null=True)
    contact_phone = models.CharField(max_length=255, null=True)


    def __str__(self):
        return "{} - {}".format(self.name, self.status)
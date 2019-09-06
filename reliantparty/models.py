from django.db import models

# Create your models here.

class ReliantParty(models.Model):
    name = models.CharField(max_length=255, null=False)
    status = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    abn = models.CharField(max_length=255, null=False)


    def __str__(self):
        return "{} - {}".format(self.name, self.status)
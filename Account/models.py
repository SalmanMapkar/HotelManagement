from django.db import models
from django.db.models.expressions import F

# Create your models here.
class AccountUser(models.Model):
    UserName = models.CharField(max_length=255, primary_key=True)
    PassWord = models.CharField(max_length=255, null= False)
    ValidityEndDate = models.DateField(null=False)

    def __str__(self):
        return self.UserName
from rest_framework import serializers

from .models import AccountUser

class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AccountUser
        fields = ('UserName', 'PassWord', 'ValidityEndDate')
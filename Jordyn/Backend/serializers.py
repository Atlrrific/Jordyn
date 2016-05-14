from django.contrib.auth.models import Instruction
from rest_framework import serializers



class Instruction(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('spice', 'quantity','pub_date')

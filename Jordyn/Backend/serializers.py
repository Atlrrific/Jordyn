from rest_framework import serializers
from Backend.models import *


class InstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instruction
        fields = ('id','spice', 'quantity')

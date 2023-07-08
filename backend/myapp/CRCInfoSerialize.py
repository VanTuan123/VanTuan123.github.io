from myapp.models import CRCInfo
from rest_framework import serializers

class CRCInfoSerialize(serializers.ModelSerializer):
    class Meta:
        model = CRCInfo
        fields='__all__'
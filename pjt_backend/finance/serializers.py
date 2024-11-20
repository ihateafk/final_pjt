from rest_framework import serializers
from .models import Company

# 금융회사 이름을 가져와 저장하기 위한 serializer
class CompanySerializer(serializers.ModelSerializer) :

    class Meta :
        model = Company
        fields = '__all__'
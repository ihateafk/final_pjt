from django.shortcuts import render
import requests
from django.conf import settings
from .models import Company
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from .serializers import CompanySerializer

# Create your views here.

# 금융 회사 목록 불러와서 저장하는 view
@api_view(['GET'])
def companyload(request) :
    API_KEY = settings.API_KEY
    URL = 'http://finlife.fss.or.kr/finlifeapi/companySearch.json'
    params = {
        'auth' : API_KEY,
        'topFinGrpNo' : '020000',
        'pageNo' : 3
    }

    response = requests.get(URL, params=params).json()
    result = response['result']['baseList']

    for datas in result :
        company_name = datas['kor_co_nm']

        if Company.objects.filter(
            company_name = company_name
        ).exists() : continue

        data = {
            'company_name' : company_name,
        }

        serializer = CompanySerializer(data = data)
        if serializer.is_valid(raise_exception=True) :
            serializer.save()

    return JsonResponse({'message' : 'okay'})
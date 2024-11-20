from django.shortcuts import render
import requests
from django.conf import settings
from .models import Company, Product
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
        'topFinGrpNo' : '060000',
        'pageNo' : 1
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

    return JsonResponse({'message' : 'company name save okay'})


# # 예금 목록 불러와서 상품 DB에 저장하는 view
# @api_view(['GET'])
# def depositload(request) :

#     API_KEY = settings.API_KEY
#     URL = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
#     params = {
#         'auth' : API_KEY,
#         'topFinGrpNo' : '020000',
#         'pageNo' : 1
#     }

#     response = requests.get(URL, params=params).json()
#     baseresult = response['result']['baseList']
#     optionresult = response['result']['optionList']

#     for i in range(len(baseresult)) :
#         fin_prdt_nm = baseresult[i]['fin_prdt_nm']
#         mtrt_int = baseresult[i]['mtrt_int']
#         spcl_cnd = baseresult[i]['spcl_cnd']
#         join_member = baseresult[i]['join_member']
#         etc_note = baseresult[i]['etc_note']
#         save_trm = optionresult[i]['save_trm']
#         intr_rate = optionresult[i]['intr_rate']
#         intr_rate2 = optionresult[i]['intr_rate2']
#         join_way = baseresult[i]['join_way']
#         product_company = baseresult[i]['kor_co_nm']

#         try :
#             company = Company.objects.get(company_name = product_company)
#             print(company.id)
#             product_company = company.id
#         except Company.DoesNotExist :
#             product_company = None

#         if Product.objects.filter(
#             fin_prdt_nm = fin_prdt_nm,
#             mtrt_int = mtrt_int,
#             spcl_cnd = spcl_cnd,
#             join_member = join_member,
#             etc_note = etc_note,
#             save_trm = save_trm,
#             intr_rate = intr_rate,
#             intr_rate2 = intr_rate2,
#             join_way = join_way,
#             fin_category = 1
#         ).exists() :
#             continue

#         data = {
#             'fin_prdt_nm' : fin_prdt_nm,
#             'mtrt_int' : mtrt_int,
#             'spcl_cnd' : spcl_cnd,
#             'join_member' : join_member,
#             'etc_note' : etc_note,
#             'save_trm' : save_trm,
#             'intr_rate' : intr_rate,
#             'intr_rate2' : intr_rate2,
#             'join_way' : join_way,
#             'fin_category' : 1
#         }

#         serializer = DepositSerializer(data = data)
#         if serializer.is_valid(raise_exception=True) :
#             serializer.save()
    
#     return JsonResponse({'message' : 'deposit save okay'})
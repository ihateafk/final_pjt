from django.shortcuts import render
import requests
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Company, Product, FinCategory, FavoriteProduct, JoinProduct
from .serializers import CompanySerializer, ProductAddSerializer, OptionAddSerializer, favoriteProductSerializer, JoinProductSerializer,ProductDetailSerializer
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import platform
from io import BytesIO
import base64
from .utils import addProductAndOptions
from pprint import pprint


# Create your views here.

# 금융 회사 목록 불러와서 저장하는 view
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def companyload(request) :
    API_KEY = settings.API_KEY
    URL = 'http://finlife.fss.or.kr/finlifeapi/companySearch.json'
    params = {
        'auth' : API_KEY,
        'topFinGrpNo' : '020000',
        'pageNo' : 1
    }

    response = requests.get(URL, params=params).json()
    result = response['result']['baseList']

    for datas in result :
        company_name = datas['kor_co_nm']
        fin_co_no = datas['fin_co_no']

        if Company.objects.filter(
            company_name = company_name
        ).exists() : continue

        data = {
            'company_name' : company_name,
            'fin_co_no': fin_co_no,
        }

        serializer = CompanySerializer(data = data)
        if serializer.is_valid(raise_exception=True) :
            serializer.save()

    return JsonResponse({'message' : 'company name save okay'})


# 관심 상품 조회 및 추가
@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def favoriteProduct(request):
    if request.method == 'GET':
        products_pk = FavoriteProduct.objects.filter(user_id=request.user.pk)
        products = []
        for product_pk in products_pk:
            products.append(Product.objects.get(pk=product_pk.product_id))
        serializer = ProductDetailSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        # DB에 있는지 없는지 검사해서 상품 및 유저 pk 반환
        data = addProductAndOptions(request.user, request.data)

        # 레코드 중복 검사
        if request.user.favoriteproduct_set.filter(product_id=data['product']).exists():
            return Response({ 'data': 'This product has been added' }, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        
        serializer = favoriteProductSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        product = FavoriteProduct.objects.get(user_id=request.user.pk, product_id=request.data['product_id'])
        product.delete()
        return Response({ 'data': 'Delete data success'}, status=status.HTTP_204_NO_CONTENT)


# 가입 상품 조회 및 추가
@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def joinProduct(request):
    if request.method == 'GET':
        products_pk = JoinProduct.objects.filter(user_id=request.user.pk)
        products = []
        for product_pk in products_pk:
            products.append(Product.objects.get(pk=product_pk.product_id))
        serializer = ProductDetailSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        # DB에 있는지 없는지 검사해서 상품 및 유저 pk 반환
        data = addProductAndOptions(request.user, request.data)
        
        # 레코드 중복 검사
        if request.user.joinproduct_set.filter(product_id=data['product']).exists():
            return Response({ 'data': 'This product has been added' }, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        
        serializer = JoinProductSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        product = JoinProduct.objects.get(user_id=request.user.pk, product_id=request.data['product_id'])
        product.delete()
        return Response({ 'data': 'Delete data success'}, status=status.HTTP_204_NO_CONTENT)


# 가입상품 금리 비교 그래프
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def drawgraph(request):
    if request.method == 'POST':
        products = request.data['joinproducts']
        data = {}
        max_intr_rate2 = 0
        max_intr_rate = 0
        for product in products:
            for option in product['options']:
                if option['intr_rate2'] > max_intr_rate2:
                    max_intr_rate2 = option['intr_rate2']
                if option['intr_rate'] > max_intr_rate:
                    max_intr_rate = option['intr_rate']
            data[product['fin_prdt_nm']] = {
                'max_intr_rate': max_intr_rate,
                'max_intr_rate2': max_intr_rate2,
            }
        df = pd.DataFrame.from_dict(data, orient='index')

        # 한글 깨져서 폰트 바꾸는 코드
        plt.rc('font', family='Malgun Gothic')
        # 그림 사이즈, 바 굵기 설정
        fig, ax = plt.subplots(figsize=(10, 5))
        bar_width = 0.25

        # x축 레이블 값 갯수
        index = np.arange(len(data))
        
        # # 각 금리 bar를 순서대로 나타내는 과정, 각 그래프는 0.25의 간격을 두고 그려짐
        b1 = plt.bar(index, df['max_intr_rate'], bar_width, alpha=0.4, color='#A7E6FF', label='최고 금리')
        b2 = plt.bar(index + bar_width, df['max_intr_rate2'], bar_width, alpha=0.4, color='#3ABEF9', label='최고 우대 금리')

        # 막대 위에 값 표시
        for i, v in enumerate(df['max_intr_rate']):
            ax.text(i, v + 0.1, f'{v:.2f}', ha='center', va='bottom', fontsize=10, color='black')
        for i, v in enumerate(df['max_intr_rate2']):
            ax.text(i + bar_width, v + 0.1, f'{v:.2f}', ha='center', va='bottom', fontsize=10, color='black')

        # x축 레이블 위치, 이름 설정
        ax.set_xticks(index + bar_width / 2)
        ax.set_xticklabels(data.keys())

        # plt.xlabel('상품명', size = 13)
        plt.ylabel('금리 (%)', size=13)
        plt.xticks(rotation=-14)
        plt.legend() # 범례 표시

        # y축 최소, 최대값 설정
        ax.set_ylim(0, 5.0)

        plt.tight_layout()
        # plt.show()
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        image = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
        buffer.close()

        return Response({ 'data': f'data:image/png;base64,{image}' })


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
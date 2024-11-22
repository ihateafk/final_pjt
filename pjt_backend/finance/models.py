from django.db import models
from django.conf import settings

# Create your models here.

# 예적금 구분 모델
class FinCategory(models.Model) :
    fin_category = models.TextField() # 구분명

# 금융 회사 모델
class Company(models.Model) :
    fin_co_no = models.CharField(max_length=100) # 금융회사 코드
    company_name = models.TextField() # 회사명

# 상품 모델
class Product(models.Model) :
    product_company = models.ForeignKey(Company, on_delete=models.DO_NOTHING, related_name='company') # 회사명
    fin_category = models.ForeignKey(FinCategory, on_delete=models.DO_NOTHING, related_name='category') # 예적금 구분
    fin_co_no = models.CharField(max_length=100) # 금융회사 코드
    fin_prdt_cd = models.CharField(max_length=100) # 상품코드
    fin_prdt_nm = models.TextField() # 상품명
    mtrt_int = models.TextField(null=True) # 만기 후 이자율
    spcl_cnd = models.TextField(null=True) # 우대 조건
    join_member = models.TextField(null=True) # 가입 대상
    etc_note = models.TextField(null=True) # 기타 유의사항
    join_way = models.TextField(null=True) # 가입 방법
    
# 상품 옵션
class ProductOption(models.Model):
    base_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='options')
    fin_prdt_cd = models.CharField(max_length=100) # 상품코드
    save_trm = models.IntegerField(null=True) # 저축 기간
    intr_rate = models.FloatField() # 저축 금리
    intr_rate2 = models.FloatField(null=True) # 최고 우대금리

# 가입 상품 목록
class JoinProduct(models.Model) :
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

# 관심 상품 목록
class FavoriteProduct(models.Model) :
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
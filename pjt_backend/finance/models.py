from django.db import models
from accounts.models import User

# Create your models here.

# 예적금 구분 모델
class FinCategory(models.Model) :
    fin_category = models.TextField() # 구분명

# 금융 회사 모델
class Company(models.Model) :
    company_name = models.TextField() # 회사명

# 상품 모델
class Product(models.Model) :
    fin_prdt_nm = models.TextField() # 상품명
    mtrt_int = models.TextField() # 만기 후 이자율
    spcl_cnd = models.TextField() # 우대 조건
    join_member = models.TextField() # 가입 대상
    etc_note = models.TextField() # 기타 유의사항
    save_trm = models.IntegerField() # 저축 기간
    intr_rate = models.FloatField() # 저축 금리
    intr_rate2 = models.FloatField() # 최고 우대금리
    join_way = models.TextField() # 가입 방법
    product_company = models.ForeignKey(Company, on_delete=models.DO_NOTHING) # 회사명
    fin_category = models.ForeignKey(FinCategory, on_delete=models.DO_NOTHING) # 예적금 구분

# 가입 상품
class JoinProduct(models.Model) :
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

# 관심 상품
class FavoriteProduct(models.Model) :
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
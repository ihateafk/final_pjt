from rest_framework import serializers
from .models import Company, FinCategory, Product, ProductOption, JoinProduct, FavoriteProduct

# 금융회사 이름을 가져와 저장하기 위한 serializer
class CompanySerializer(serializers.ModelSerializer) :

    class Meta :
        model = Company
        fields = '__all__'


# 금융 상품 상세보기
class ProductDetailSerializer(serializers.ModelSerializer):
    ## 예적금 분류 이름
    class FinCatagorySerializer(serializers.ModelSerializer):
        class Meta:
            model = FinCategory
            fields = ('fin_category',)
    
    ## 금융회사 이름
    class FinCompanyNameSerializer(serializers.ModelSerializer):
        class Meta:
            model = Company
            fields = ('company_name',)
    
    ## 상품 옵션 리스트
    class ProductOptionDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = ProductOption
            fields = ('save_trm', 'intr_rate', 'intr_rate2')
    
    fin_category_nm = FinCatagorySerializer(read_only=True)
    fin_co_nm = FinCompanyNameSerializer(read_only=True)
    options = ProductOptionDetailSerializer(many=True, read_only=True)
    
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('product_company',)


# 금융 상품 등록
class ProductAddSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('product_company', 'fin_category')


# 금융 상품 옵션 등록
class OptionAddSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductOption
        fields = '__all__'
        read_only_fields = ('base_product',)
        
        
# 관심 상품
class favoriteProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FavoriteProduct
        fields = '__all__'


# 가입 상품
class JoinProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = JoinProduct
        fields = '__all__'


# class DepositSerializer(serializers.ModelSerializer) :

#     class Meta :
#         model = Product
#         fields = '__all__'
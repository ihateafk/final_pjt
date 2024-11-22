from rest_framework.response import Response
from rest_framework import status
from .models import Company, Product, FinCategory
from .serializers import ProductAddSerializer, OptionAddSerializer


# 상품 및 옵션 DB 저장
def addProductAndOptions(user, request_data):
    product = Product.objects.filter(fin_prdt_cd=request_data['base']['fin_prdt_cd'])
    if len(product) == 1:
        product = product[0]
        # return exist data_package
        data = {
            'user': user.pk,
            'product': product.pk,
        }
        return data

    elif len(product) == 0:
        # add product and options
        ## add product
        product_data = request_data['base']
        company = Company.objects.get(fin_co_no=product_data['fin_co_no'])
        fin_category = FinCategory.objects.get(pk=request_data['fin_category'])
        product_data.update(fin_category=fin_category)
        
        serializer = ProductAddSerializer(data=product_data)
        if serializer.is_valid(raise_exception=True):
            product = serializer.save(product_company=company, fin_category=fin_category)

            ## add options
            options = request_data['options']
            for i in range(len(options)):
                serializer = OptionAddSerializer(data=options[i])
                if serializer.is_valid():
                    serializer.save(base_product=product)

            # return exist data_package
            data = {
                'user': user.pk,
                'product': product.pk,
            }
            return data
    
    # if same products are in the table is True
    else:
        return None
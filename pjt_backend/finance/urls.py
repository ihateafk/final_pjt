from django.urls import path
from . import views

urlpatterns = [
    # 금융 회사 목록 DB에 저장하는 path
    path('company/create/', views.companyload),
    # path('/deposit/create/', views.depositload),
]

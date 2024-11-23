from django.urls import path
from . import views

urlpatterns = [
    path('', views.board_list),
    # path('boards/<int:board_id>/', views.board_detail),
]
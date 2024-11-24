from django.urls import path
from . import views

urlpatterns = [
    path('', views.board_list),
    path('<int:board_id>/', views.board_detail),
    path('<int:board_id>/comment/', views.comment_list),
    path('<int:board_id>/comments/', views.comment_create),
]
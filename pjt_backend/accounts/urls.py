from django.urls import path, include
from . import views

urlpatterns = [
    # login and signup
    path('', include('dj_rest_auth.urls')),
    path('signup/', include('dj_rest_auth.registration.urls')),
    path('profile/', views.profile)
]

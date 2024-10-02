
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.formKyc, name='formKyc'),
    path('success/', views.kyc_success, name='kyc_success'),
]

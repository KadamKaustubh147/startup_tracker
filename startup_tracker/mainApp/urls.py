
from django.urls import path, include
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.formKyc, name='formKyc'),
    path('success/', views.kyc_success, name='kyc_success'),
    path('signup/', views.signup_view, name='signup'),  # Signup URL
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),  # Custom login URL
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),  # Logout URL
]

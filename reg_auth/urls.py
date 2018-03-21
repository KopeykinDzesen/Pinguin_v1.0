from django.urls import path, include

from . import views


app_name = 'reg_auth'
urlpatterns = [
    path('', views.reg_auth, name='reg_auth'),
    path('registration/', views.registration, name='registration'),
    path('authentication/', views.authentication, name='authentication'),
    path('<email>/<key>/', views.confirm_email, name='confirm_email'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
]
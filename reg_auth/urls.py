from django.urls import path, include

from . import views


app_name = 'reg_auth'
urlpatterns = [
    path('', views.reg_auth, name='reg_auth'),
    path('registration/', views.registration, name='registration'),
    path('<email>/<key>', views.confirm_email, name='confirm_email'),
]
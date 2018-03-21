from django.shortcuts import render
from datetime import datetime
from django.core.mail import EmailMessage

from . import special_func
from .models import UserData
from .forms import SignUpForm, SignInForm


def reg_auth(request):
    signup_form = SignUpForm()
    signin_form = SignInForm()
    is_auth = True
    return render(request, 'reg_auth/index.html', locals())


def registration(request):
    signup_form = SignUpForm()

    if request.method == 'POST':
        signup_form = SignUpForm(request.POST or None)

        data = request.POST
        is_create_user = False

        if signup_form.is_valid():

            email = data['email']
            password = data['password']
            confirm_password = data['confirm_password']

            key = special_func.generate_key()
            user = UserData.objects.create(email=email, password=password, created_data=datetime.now(),
                                           email_confirm_key=key)

            email = EmailMessage('Confirm email Pinguin', 'Hello! Thank you for registering!\n '
                                'Confirm your email: http://127.0.0.1:8033/reg_auth/{}/{}'.format(email, key),
                                to = [email])
            email.send()

            is_create_user = True

        else:

            print(data['email_validate'])
            if data['email_validate'] == 'validate':
                email = data['email']

            if data['password_validate'] == 'validate':
                password = data['password']

            if data['confirm_password_validate'] == 'validate':
                confirm_password = data['confirm_password']

    return render(request, 'reg_auth/index.html', locals())


def confirm_email(request, email, key):
    user = UserData.objects.get(email=email)

    if user.email_confirm_key == key:
        user.email_confirm_key = None #email подтверждён
        user.save()

    return render(request, 'user_page.html', locals())


def authentication(request):
    signin_form = SignInForm()
    is_auth = True

    if request.method == 'POST':
        signin_form = SignInForm(request.POST or None)

        data = request.POST
        email = data['email']

        if signin_form.is_valid():
            user = UserData.objects.get(email=email)
            return render(request, 'user_page.html', locals())
        else:
            is_auth = False
            error_code = signin_form.errors['__all__'].as_data()[0].code

    return render(request, 'reg_auth/index.html', locals())

# def forgot_password(request):
#
#     return render(request, )


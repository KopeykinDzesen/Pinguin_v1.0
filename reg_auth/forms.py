from django import forms

from .models import UserData


class SignUpForm(forms.Form):
    email = forms.CharField(required=True, error_messages={'required': 'Укажите Email'})
    email_validate = forms.CharField()
    password = forms.CharField(required=True, error_messages={'required': 'Укажите пароль'})
    password_validate = forms.CharField()
    confirm_password = forms.CharField(required=True, error_messages={'required': 'Повторите пароль'})
    confirm_password_validate = forms.CharField()

    def clean(self):

        email = str(self.cleaned_data.get('email'))
        email_validate = str(self.cleaned_data.get('email_validate'))
        password_validate = str(self.cleaned_data.get('password_validate'))
        confirm_password_validate = str(self.cleaned_data.get('confirm_password_validate'))

        if email_validate == 'no_validate':
            raise forms.ValidationError('Не допустимый Email!')

        if password_validate == 'no_validate':
            raise forms.ValidationError('Простой пароль!')

        if confirm_password_validate == 'no_validate':
            raise forms.ValidationError('Пароли не совпадают!')

        # Проверка совпадения имени
        try:
            user = UserData.objects.get(email=email)
            raise forms.ValidationError('Пользователь с данным Email уже зарегистрирован!')
        except UserData.DoesNotExist:
            pass

        return self.cleaned_data
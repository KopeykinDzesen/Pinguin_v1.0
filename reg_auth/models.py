from django.db import models


class UserData(models.Model):
    username = models.CharField(max_length=24, blank=True, null=True)
    email = models.EmailField(max_length=32)
    password = models.CharField(max_length=32)
    created_data = models.DateTimeField()
    email_confirm_key = models.CharField(max_length=20, blank=True, null=True)
    remember_me = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return "Email: {}, Data: {}.".format(self.email, self.created_data)

    class Meta:
        verbose_name = "Данные пользователя"
        verbose_name_plural = "Данные пользователей"

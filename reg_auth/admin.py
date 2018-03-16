from django.contrib import admin

from .models import UserData


class UserDataAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UserData._meta.fields]
    exclude = ('password',)

    class Meta:
        model = UserData


admin.site.register(UserData, UserDataAdmin)

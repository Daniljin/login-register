from django.contrib import admin

# Register your models here.

from . import models

# 在admin app中注册我们在login/models中的User模型
admin.site.register(models.User)
admin.site.register(models.ConfirmString)
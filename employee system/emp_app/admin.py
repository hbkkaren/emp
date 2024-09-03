from django.contrib import admin
from .models import Role,Department,Empoyee,User

# Register your models here.

admin.site.register(Role)
admin.site.register(Empoyee)
admin.site.register(Department)
admin.site.register(User)
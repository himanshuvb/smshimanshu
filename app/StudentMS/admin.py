from django.contrib import admin
from .models import Student,Leaves,Git

# Register your models here.
admin.site.register(Student)
admin.site.register(Leaves)
admin.site.register(Git)
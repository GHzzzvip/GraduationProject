from django.contrib import admin
from .models import  Problem, Status, Contest, Contest_Problem

# Register your models here.
admin.site.register(Problem)
admin.site.register(Status)
admin.site.register(Contest)
admin.site.register(Contest_Problem)


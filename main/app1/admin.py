from django.contrib import admin


# Register your models here.
from .models import *
admin.site.register(Task)
admin.site.register(UserProject)
admin.site.register(Category)
admin.site.register(Department)
admin.site.register(Role)
admin.site.register(Status)

from django.contrib import admin
from .models import Credentials,Student,Faculty,Course

admin.site.register(Credentials)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Course)


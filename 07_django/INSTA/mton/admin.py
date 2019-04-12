from django.contrib import admin
from .models import Student, Lecture, Enrollment

admin.site.register(Student)

admin.site.register(Lecture)

admin.site.register(Enrollment)

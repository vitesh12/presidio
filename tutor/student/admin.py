from django.contrib import admin
from student.models import Member

class StudentAdmin(admin.ModelAdmin):
    list_display=('firstname','qua','gender','subject')

admin.site.register(Member,StudentAdmin)

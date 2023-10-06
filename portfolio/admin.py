from django.contrib import admin
from .models import *

# Register your models here.


class TechnoAdmin(admin.ModelAdmin):
    list_display = ('name',)


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name',)


class FrameworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'language')


class EducationAdmin(admin.ModelAdmin):
    list_display = ('formation_name', 'institution_name', 'location', 'degree')


class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location')


class OnlineCourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'platform',)


admin.site.register(Techno, TechnoAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Framework, FrameworkAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(OnlineCourse, OnlineCourseAdmin)
admin.site.register(Project)

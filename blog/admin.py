from django.contrib import admin
from blog.models import Service, PersonalInfo

class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_title','blog_name','blog_body')


class PersonInfoAdmin(admin.ModelAdmin):
    list_display = ('name','password')

admin.site.register(Service,BlogAdmin)
admin.site.register(PersonalInfo, PersonInfoAdmin)




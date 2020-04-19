from django.contrib import admin

# Register your models here.

from .models import Category, Tag, License, PostBaseInfo, Banner, \
    Camera, Picture, Social, Master, PostTag

# admin.site.r
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(License)
admin.site.register(PostBaseInfo)
admin.site.register(Banner)
admin.site.register(Camera)
admin.site.register(Picture)
admin.site.register(Social)
admin.site.register(Master)
admin.site.register(PostTag)

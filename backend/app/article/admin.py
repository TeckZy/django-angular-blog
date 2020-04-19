from django.contrib import admin

# Register your models here.
from .models import ArticleInfo, ArticleDetail

#
# class ArticleinfoInline(admin.TabularInline):
#     model = ArticleDetail
#
# # @admin.register(ArticleInfo)
# class ArticleDetail(admin.ModelAdmin):
#     inlines = [ArticleinfoInline]

admin.site.register(ArticleInfo)
admin.site.register(ArticleDetail)

"""blogyy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_swagger.views import get_swagger_view

from app.article.views import ArticleBaseInfoListViewset, ArticleDetailInfoListViewset
from app.base.views import SiteInfoViewset, BloggerInfoViewset
from  app.root.views import CategoryListViewset, SingleLevelCategoryListViewset, TagListViewset, \
    BannerListViewset, PostBaseInfoListViewset, PostLikeViewset, VerifyPostAuthViewset

router = DefaultRouter()

# basename is available form drf version 3


router.register(r'categorys', CategoryListViewset, basename='categorys')
router.register(r'category', SingleLevelCategoryListViewset, basename='category')
router.register(r'tags', TagListViewset, basename='tags')
router.register(r'banners', BannerListViewset, basename='banners')
router.register(r'siteInfo', SiteInfoViewset, basename="siteInfo")
router.register(r'blogger', BloggerInfoViewset, basename="blogger")
router.register(r'postBaseInfos', PostBaseInfoListViewset, basename="postBaseInfos")
router.register(r'verifyPostAuth', VerifyPostAuthViewset, basename="verifyPostAuth")
router.register(r'likePost', PostLikeViewset, basename="likePost")

router.register(r'post', ArticleBaseInfoListViewset, basename="articleBaseInfos")
router.register(r'postDetail', ArticleDetailInfoListViewset, basename="articleDetailInfos")


schema_view = get_swagger_view(title='Bloggy API')

urlpatterns = [
    url(r'^$', schema_view),
    path('admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),

    # url(r'^lol/',  )
]

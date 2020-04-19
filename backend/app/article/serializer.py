# _*_ coding: utf-8 _*_

from rest_framework import serializers

from .models import ArticleInfo, ArticleDetail
from app.root.serializer import SingleLevelCategorySerializer, TagSerializer, LicenseSerializer
from django.conf import settings


class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleDetail
        fields = ( 'formatted_content', 'add_time', 'update_time')


class ArticleDetailInfoSerializer(serializers.ModelSerializer):
    category = SingleLevelCategorySerializer()
    tags = TagSerializer(many=True)
    license = LicenseSerializer()
    details = ArticleDetailSerializer(many=True)
    browse_auth = serializers.CharField(required=False, max_length=100, write_only=True)

    class Meta:
        model = ArticleInfo
        exclude = ('browse_password', 'browse_password_encrypt')


class ArticleBaseInfoSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    front_image = serializers.SerializerMethodField()
    need_auth = serializers.SerializerMethodField()

    def get_front_image(self, article):
        if article.front_image:
            return "{0}/{1}".format(settings.MEDIA_URL_PREFIX, article.front_image)

    def get_need_auth(self, article):
        if article.browse_password_encrypt:
            return True
        else:
            return False

    class Meta:
        model = ArticleInfo
        fields = (
            'id', 'title', 'desc', 'author', 'tags', 'click_num', 'like_num', 'comment_num', 'post_type',
            'front_image', 'is_recommend', 'is_hot', 'is_banner', 'is_commentable', 'need_auth',
            'front_image_type', 'index', 'add_time')

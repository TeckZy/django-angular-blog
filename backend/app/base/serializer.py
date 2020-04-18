from rest_framework import serializers
from .models import SiteInfo, BloggerInfo, NavigationLink
from app.root.serializer import MasterSerializer, SocialSerializer
from django.conf import settings


class NavigationLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavigationLink
        fields = "__all__"


class SiteInfoSerializer(serializers.ModelSerializer):
    navigations = NavigationLinkSerializer(many=True)
    icon = serializers.SerializerMethodField()
    background = serializers.SerializerMethodField()

    def get_icon(self, site_info):
        if site_info.icon:
            return "{0}/{1}".format(settings.MEDIA_URL_PREFIX, site_info.icon)

    def get_background(self, blogger_info):
        if blogger_info.background:
            return "{0}/{1}".format(settings.MEDIA_URL_PREFIX, blogger_info.background)

    class Meta:
        model = SiteInfo
        fields = (
            'name', 'desc', 'keywords', 'icon', 'background', 'api_base_url', 'is_live',
            'is_force_refresh', 'force_refresh_time', 'navigations', 'copyright', 'copyright_desc',
            'icp')


class BloggerInfoSerializer(serializers.ModelSerializer):
    socials = SocialSerializer(many=True)
    masters = MasterSerializer(many=True)
    avatar = serializers.SerializerMethodField()
    background = serializers.SerializerMethodField()

    def get_avatar(self, blogger_info):
        if blogger_info.avatar:
            return "{0}/{1}".format(settings.MEDIA_URL_PREFIX, blogger_info.avatar)

    def get_background(self, blogger_info):
        if blogger_info.background:
            return "{0}/{1}".format(settings.MEDIA_URL_PREFIX, blogger_info.background)

    class Meta:
        model = BloggerInfo
        fields = "__all__"

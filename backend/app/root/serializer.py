from rest_framework import serializers

from .models import Category, Tag, License, PostBaseInfo, Banner, \
    Camera, Picture, Social, Master, PostTag

from blogyy.settings import MEDIA_URL_PREFIX


class OrderCategoryListSerializer(serializers.ListSerializer):

    def to_representation(self, data):
        data = data.filter(is_active=True).order_by('index')
        return super(OrderCategoryListSerializer, self).to_representation(data)


class CategorySerializer3(serializers.ModelSerializer):

    class Meta:
        list_serializer_class = OrderCategoryListSerializer
        model = Category
        fields = "__all__"


class CategorySerializer2(serializers.ModelSerializer):
    sub_category = CategorySerializer3(many=True)

    class Meta:
        list_serializer_class = OrderCategoryListSerializer
        model = Category
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    sub_category = CategorySerializer2(many=True)

    class Meta:
        model = Category
        fields = "__all__"


class SingleLevelCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    related_post_num = serializers.SerializerMethodField()

    def get_related_post_num(self, tag):
        return len(PostTag.objects.filter(tag__id=tag.id))

    class Meta:
        model = Tag
        fields = ('name', 'color', 'related_post_num')


class LicenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = License
        fields = "__all__"


class CameraSerializer(serializers.ModelSerializer):

    class Meta:
        model = Camera
        fields = "__all__"


class PictureSerializer(serializers.ModelSerializer):
    camera = CameraSerializer()

    class Meta:
        model = Picture
        fields = "__all__"


class PostBaseInfoSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    front_image = serializers.SerializerMethodField()
    need_auth = serializers.SerializerMethodField()

    def get_front_image(self, article):
        if article.front_image:
            return "{0}/{1}".format(MEDIA_URL_PREFIX, article.front_image)

    def get_need_auth(self, article):
        if article.browse_password_encrypt:
            return True
        else:
            return False

    class Meta:
        model = PostBaseInfo
        fields = (
            'id', 'title', 'desc', 'tags', 'like_num', 'comment_num', 'click_num', 'front_image', 'front_image_type',
            'is_hot',
            'is_recommend', 'is_banner', 'is_commentable',
            'post_type', 'need_auth', 'add_time')


class BannerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Banner
        fields = "__all__"


class SocialSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, social):
        if social.image:
            return "{0}/{1}".format(MEDIA_URL_PREFIX, social.image)

    class Meta:
        model = Social
        fields = ('id', 'name', 'image', 'url', 'desc')


class MasterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Master
        fields = "__all__"


class PostLikeSerializer(serializers.Serializer):
    post_id = serializers.IntegerField(required=True, label='post')


class VerifyPostAuthSerializer(serializers.Serializer):
    post_id = serializers.CharField(max_length=11, min_length=1, required=True, label='postid')
    browse_auth = serializers.CharField(max_length=64, min_length=6, required=True, label='brouseauth')

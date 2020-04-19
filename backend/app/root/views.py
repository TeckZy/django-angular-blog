from rest_framework import mixins, status
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from .models import Category, Tag, Banner, PostBaseInfo
from .serializer import CategorySerializer, SingleLevelCategorySerializer, TagSerializer, BannerSerializer, PostBaseInfoSerializer, PostLikeSerializer, VerifyPostAuthSerializer
from .filters import CategoryFilter, BannerFilter, PostBaseInfoFilter
from app.base.utils import CustomeLimitOffsetPagination, CustomePageNumberPagination


class CategoryListViewset(viewsets.ReadOnlyModelViewSet):
    """
    List:
        Category
    """
    queryset = Category.objects.filter(is_active=True)
    pagination_class = CustomePageNumberPagination
    serializer_class = CategorySerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = CategoryFilter
    search_fields = ('name', 'category_type', 'desc')
    ordering_fields = ('category_level', 'index')
    ordering = ('index',)


class SingleLevelCategoryListViewset(viewsets.ReadOnlyModelViewSet):
    """
    List:
        One Level Category
    """
    queryset = Category.objects.filter(is_active=True)
    pagination_class = CustomePageNumberPagination
    serializer_class = SingleLevelCategorySerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = CategoryFilter
    search_fields = ('name', 'category_type', 'desc')
    ordering_fields = ('category_level', 'index')
    ordering = ('index',)


class TagListViewset(viewsets.ReadOnlyModelViewSet):
    """
    List:
        Tag List
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    search_fields = ('name', 'subname')
    ordering_fields = ('name', 'subname')


class BannerListViewset(viewsets.ReadOnlyModelViewSet):
    """
    List:
        Banner list
    """
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = BannerFilter
    queryset = Banner.objects.all().order_by("-index")
    serializer_class = BannerSerializer


class PostBaseInfoListViewset(viewsets.ReadOnlyModelViewSet):
    """
    List:
        Post Base Info
    """
    queryset = PostBaseInfo.objects.filter(is_active=True)
    pagination_class = CustomeLimitOffsetPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = PostBaseInfoFilter
    search_fields = ('title', 'subtitle', 'abstract', 'desc')
    ordering_fields = ('id', 'click_num', 'like_num', 'comment_num', 'add_time')
    serializer_class = PostBaseInfoSerializer


class PostLikeViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    PostLike
    """
    serializer_class = PostLikeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True) # status 400

        post_id = serializer.validated_data["post_id"]

        post = PostBaseInfo.objects.filter(id=post_id)[0]

        if post is not None:
            post.like_num += 1
            post.save()
            context = {
                "post": post_id
            }
            return Response(context, status.HTTP_201_CREATED)
        else:
            context = {
                "error": '500 Something Went Wrong'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class VerifyPostAuthViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Verify Post Auth
    """
    serializer_class = VerifyPostAuthSerializer

    def create(self, request, *args, **kwargs):
        """
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True) # status 400

        post_id = serializer.validated_data['post_id']
        browse_auth = serializer.validated_data['browse_auth']

        if post_id is None:
            context = {
                "error": 'No Post Id'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)

        if browse_auth is None:
            context = {
                "error": 'Auth Failed'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)

        posts = PostBaseInfo.objects.filter(id=post_id)

        if len(posts):
            if posts[0].browse_password_encrypt == browse_auth:
                context = {
                    'post_id': posts[0].id
                }
                return Response(context, status.HTTP_202_ACCEPTED)
            else:
                context = {
                    'error': 'Invalid'
                }
                return Response(context, status=status.HTTP_403_FORBIDDEN)
        else:
            context = {
                'error': 'No Post',
                'post_id': post_id
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
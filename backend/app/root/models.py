import hashlib

from django.db import models
from django.conf import  settings

__author__ = 'Akash Singh'
__date__ = '2020-APR-18'

CATEGORY_LEVEL = (
    ("1", "level1"),
    ("2", "level2"),
    ("3", "level3")
)
CATEGORY_TYPE = (
    ("articles", "Articles"),
    ("articles/category", "Article Classification"),
)


class Category(models.Model):
    """
    Model for Category Of Blog App

        FIELD OPTIONS	DESCRIPTION
        Null	If True, Django will store empty values as NULL in the database. Default is False.
        Blank	If True, the field is allowed to be blank. Default is False.
        db_column	The name of the database column to use for this field. If this isn’t given, Django will use the field’s name.
        Default	The default value for the field. This can be a value or a callable object. If callable it will be called every time a new object is created.
        help_text	Extra “help” text to be displayed with the form widget. It’s useful for documentation even if your field isn’t used on a form.
        primary_key	If True, this field is the primary key for the model.
        editable	If False, the field will not be displayed in the admin or any other ModelForm. They are also skipped during model validation. Default is True.
        error_messages	The error_messages argument lets you override the default messages that the field will raise. Pass in a dictionary with keys matching the error messages you want to override.
        help_text	Extra “help” text to be displayed with the form widget. It’s useful for documentation even if your field isn’t used on a form.
        verbose_name	A human-readable name for the field. If the verbose name isn’t given, Django will automatically create it using the field’s attribute name, converting underscores to spaces.
        validators	A list of validators to run for this field. See the validators documentation for more information.
        Unique	If True, this field must be unique throughout the table.

    """
    CATEGORY_LEVEL = (
        ("1", "level1"),
        ("2", "level2"),
        ("3", "level3")
    )
    CATEGORY_TYPE = (
        ("articles", "Articles"),
        ("articles/category", "Article Classification"),
    )
    name = models.CharField(max_length=30, default="", verbose_name="Category Name", help_text="Root Category Name")
    category_type = models.CharField(max_length=30, choices=CATEGORY_TYPE, verbose_name="Category Type ",help_text="Used to configure route ")
    desc = models.TextField(null=True, blank=True, verbose_name="decription", help_text="category description")
    image = models.ImageField(upload_to="comment/category/image/%Y/%m", null=True, blank=True, help_text="图片")
    category_level = models.CharField(max_length=20, choices=CATEGORY_LEVEL, help_text="level")
    parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name="parent", help_text="parent category",related_name="sub_category", on_delete=models.CASCADE)

    is_active = models.BooleanField(default=True, verbose_name="Active Status", help_text="Active")
    is_tab = models.BooleanField(default=True, verbose_name="Tab Status", help_text="Tab")
    index = models.IntegerField(default=0, verbose_name="indexing", help_text=".")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="Add Time", help_text="When was added")

    class Meta:
        verbose_name = "Classfication"
        verbose_name_plural = verbose_name + 'list'

    def save(self, *args, **kwargs):
        super(Category,self).save(*args, **kwargs)

    def __str__(self):
        return '{0} - {1} - {2}'.format(self.name, self.get_category_type_display(), self.get_category_level_display())


class Tag(models.Model):
    """
   Tag That Category Post COmprises of
    """
    name = models.CharField(max_length=30, null=False, blank=False, )
    description =  models.TextField(max_length=30)
    category = models.ForeignKey(Category, null=True, blank=True,on_delete=models.CASCADE)
    color = models.CharField(max_length=20, default="blue", )
    add_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.description:
            self.description = self.name
        super(Tag, self).save(*args, **kwargs)

    class Meta:
        pass

    def __str__(self):
        return self.name


class License(models.Model):
    """
    Lisence
    """
    COLOR_TYPE = (
        ("#878D99", "灰色"),
        ("#409EFF", "蓝色"),
        ("#67C23A", "绿色"),
        ("#EB9E05", "黄色"),
        ("#FA5555", "红色")
    )
    name = models.CharField(max_length=30, null=False, blank=False, )
    desc = models.CharField(max_length=255, null=True, blank=True,)
    link = models.URLField(null=True, blank=True, )
    color = models.CharField(max_length=20, default="blue", choices=COLOR_TYPE)
    add_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        super(License, self).save(*args, **kwargs)

    class Meta:
        pass

    def __str__(self):
        return self.name


class Camera(models.Model):
    """
    Camera
    """
    device = models.CharField(max_length=30 )
    version = models.CharField(max_length=200 )
    environment = models.CharField(max_length=200 )
    add_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        pass

    def __str__(self):
        return self.device


class Picture(models.Model):
    """
    Picture
    """
    title = models.CharField(max_length=100, null=False, blank=False, )
    desc = models.CharField(max_length=255, null=True, blank=True, )
    image = models.ImageField(upload_to="comment/picture/image/%Y/%m", null=True, blank=True)
    camera = models.ForeignKey(Camera, null=True, blank=True,on_delete=models.CASCADE)
    link = models.URLField(null=True, blank=True,)
    add_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        super(Picture, self).save(*args, **kwargs)

    class Meta:
        pass

    def __str__(self):
        return self.title


class PostBaseInfo(models.Model):
    """
    Post
    """
    POST_TYPE = (
        ("article", "article"),
    )
    FRONT_IMAGE_TYPE = (
        ("0", "small"),
        ("1", 'medium'),
        ("2", "collection")
    )
    title = models.CharField(max_length=100, null=False, blank=False)
    desc = models.CharField(max_length=255, null=True, blank=True)
    author = models.CharField(max_length=20, null=True, blank=True)
    category = models.ForeignKey(Category, null=False, blank=False,on_delete=models.DO_NOTHING )
    tags = models.ManyToManyField(Tag, through="PostTag", through_fields=('post', 'tag'))
    post_type = models.CharField(max_length=20, choices=POST_TYPE, null=True, blank=True)
    click_num = models.IntegerField(default=0)
    like_num = models.IntegerField(default=0 )
    comment_num = models.IntegerField(default=0 )
    front_image = models.ImageField(upload_to="post/image/%y/%m", null=True, blank=True)
    front_image_type = models.CharField(max_length=20, default="0", choices=FRONT_IMAGE_TYPE)
    license = models.ForeignKey(License, null=True, blank=True,on_delete=models.CASCADE)
    is_hot = models.BooleanField(default=False)
    is_recommend = models.BooleanField(default=False )
    is_banner = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_commentable = models.BooleanField(default=True)
    browse_password = models.CharField(max_length=20, null=True, blank=True)
    browse_password_encrypt = models.CharField(max_length=100, null=True, blank=True)
    index = models.IntegerField(default=0)
    add_time = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):

        if self.browse_password and len(self.browse_password) > 0:
            md5 = hashlib.md5()
            md5.update(self.browse_password.encode('utf8'))
            self.browse_password_encrypt = md5.hexdigest()
        else:
            self.browse_password_encrypt = None
        super(PostBaseInfo, self).save(*args, **kwargs)

    # Will Make It Get From Enviroment
    def get_absolute_url(self):
        return '{0}/{1}/{2}'.format(settings.SITE_BASE_URL, self.post_type, self.id)

    class Meta:
        pass

    def __str__(self):
        return self.title


class PostTag(models.Model):
    """
    Post tags
    """
    post = models.ForeignKey(PostBaseInfo, null=False, blank=False,on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, null=False, blank=False,on_delete=models.CASCADE)
    add_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        pass

    def __str__(self):
        return self.tag.name


class Banner(models.Model):
    """
    Banner for The Blog Special
    """
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="comment/banner/image/%y/%m", null=True, blank=True, )
    url = models.URLField(max_length=200,)
    category = models.ForeignKey(Category, default='1', null=False, blank=False,on_delete=models.CASCADE)
    index = models.IntegerField(default=0, )
    add_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        super(Banner, self).save(*args, **kwargs)

    class Meta:
        pass

    def __str__(self):
        return self.title


class Social(models.Model):
    """
    Social Media Handle of Blogyy
    """
    name = models.CharField(max_length=30, )
    desc = models.CharField(max_length=100, )
    image = models.ImageField(upload_to="comment/social/image/%y/%m", null=True, blank=True)
    url = models.URLField(max_length=200)
    add_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        super(Social, self).save(*args, **kwargs)

    class Meta:
        pass

    def __str__(self):
        return self.name


class Master(models.Model):
    """¡
    Main Model
    """
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=100, null=True, blank=True, )
    image = models.ImageField(upload_to="comment/master/image/%y/%m", null=True, blank=True)
    url = models.URLField(max_length=200 )
    experience = models.FloatField(default=0)
    add_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        super(Master, self).save(*args, **kwargs)

    class Meta:
        pass

    def __str__(self):
        return self.name

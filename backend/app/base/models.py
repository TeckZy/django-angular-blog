from django.db import models

# Create your models here.
import hashlib
from django.db import models
from app.root.models import Social, Master


class NavigationLink(models.Model):
    TARGET_TYPE = (
        ("_blank", "Next Page"),
        ("_self","in same Frame"),
        ("_parent", "parent"),
        ("_top", "top")
    )
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=100)
    image = models.ImageField(upload_to="base/friendlink/image/%y/%m", null=True, blank=True)
    url = models.CharField(max_length=200,)
    target = models.CharField(max_length=10, choices=TARGET_TYPE, null=True, blank=True)
    add_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        super(NavigationLink, self).save(*args, **kwargs)

    class Meta:
        pass

    def __str__(self):
        return self.name


class SiteInfo(models.Model):

    """
    Config For Website
    """
    name = models.CharField(default="", max_length=20)
    desc = models.CharField(default="", max_length=150)
    keywords = models.CharField(default="", max_length=300)
    icon = models.ImageField(upload_to="base/site/image/%y/%m", null=True, blank=True)
    background = models.ImageField(upload_to="base/site/image/%y/%m", null=True, blank=True)
    api_base_url = models.URLField(max_length=30, null=False, blank=False,)
    navigations = models.ManyToManyField(NavigationLink, through="SiteInfoNavigation", through_fields=(
        'site', 'navigation'))
    copyright = models.CharField(default="", max_length=100,)
    copyright_desc = models.CharField(default="", max_length=300)
    icp = models.CharField(default="", max_length=20)
    is_live = models.BooleanField(default=False)
    is_force_refresh = models.BooleanField(default=False)
    force_refresh_time = models.DateTimeField(null=True, blank=True,)
    access_password = models.CharField(max_length=20, null=True, blank=True)
    access_password_encrypt = models.CharField(max_length=100, null=True, blank=True)
    add_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.access_password:
            md5 = hashlib.md5()
            md5.update(self.access_password.encode('utf8'))
            self.access_password_encrypt = md5.hexdigest()
        else:
            self.access_password_encrypt = ''
        super(SiteInfo, self).save(*args, **kwargs)

    class Meta:
        pass



class BloggerInfo(models.Model):
    name = models.CharField(default="", max_length=20)
    desc = models.CharField(default="", max_length=300,)
    avatar = models.ImageField(upload_to="base/avatar/image/%y/%m", null=True, blank=True,)
    background = models.ImageField(upload_to="base/background/image/%y/%m", null=True, blank=True)
    socials = models.ManyToManyField(Social, through='BloggerSocial', through_fields=('blogger', 'social'))
    masters = models.ManyToManyField(Master, through='BloggerMaster', through_fields=('blogger', 'master'))
    add_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        super(BloggerInfo, self).save(*args, **kwargs)

    class Meta:
        pass

    def __str__(self):
        return self.name


class BloggerSocial(models.Model):
    name = models.CharField(default="", max_length=20)
    blogger = models.ForeignKey(BloggerInfo ,on_delete=models.DO_NOTHING)
    social = models.ForeignKey(Social,on_delete=models.CASCADE)
    index = models.IntegerField(default=0)
    add_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        pass

    def __str__(self):
        return self.name


class BloggerMaster(models.Model):
    name = models.CharField(default="", max_length=20)
    blogger = models.ForeignKey(BloggerInfo,on_delete=models.DO_NOTHING)
    master = models.ForeignKey(Master,on_delete=models.DO_NOTHING)
    index = models.IntegerField(default=0)
    add_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        pass

    def __str__(self):
        return self.name


class SiteInfoNavigation(models.Model):
    name = models.CharField(default="", max_length=20)
    site = models.ForeignKey(SiteInfo,on_delete=models.DO_NOTHING)
    navigation = models.ForeignKey(NavigationLink,on_delete=models.DO_NOTHING)
    index = models.IntegerField(default=0)
    add_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        pass

    def __str__(self):
        return self.name




from django.db import models

# Create your models here.
from django.db import models
import markdown

from app.root.models import Category, Tag, PostBaseInfo
from app.base.utils import MARKDOWN_EXTENSIONS


class ArticleInfo(PostBaseInfo):

    def save(self, *args, **kwargs):
        self.post_type = 'article'
        super(ArticleInfo, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        pass



class ArticleDetail(models.Model):
    article_info = models.ForeignKey(ArticleInfo, null=True, blank=True, related_name='details',on_delete=models.CASCADE)
    origin_content = models.TextField(null=False, blank=True)
    formatted_content = models.TextField()
    add_time = models.DateTimeField(null=True, blank=True)
    update_time = models.DateTimeField(null=True, blank=True,)

    def save(self, *args, **kwargs):
        self.formatted_content = markdown.markdown(self.origin_content, extensions=MARKDOWN_EXTENSIONS,lazy_ol=False)
        super(ArticleDetail, self).save(*args, **kwargs)

    def __str__(self):
        return self.article_info.title

    class Meta:
        pass

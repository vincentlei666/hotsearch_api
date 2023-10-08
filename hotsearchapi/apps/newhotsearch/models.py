from django.db import models

# Create your models here.
from article.models import Article
from utils.models import BaseModel

class NewHotArticle(BaseModel):
    article = models.ForeignKey(Article,to_field='inner_link',related_name='newhotarticle',on_delete=models.DO_NOTHING,
                                db_constraint=False, null=True, blank=True,verbose_name="文章图片")
    class Meta:
        db_table = "nineth_newhotarticle"
        verbose_name = "新热榜文章"
        verbose_name_plural = verbose_name
















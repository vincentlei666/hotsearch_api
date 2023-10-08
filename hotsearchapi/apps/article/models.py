from django.db import models

# Create your models here.
from utils.models import BaseModel

from django.conf import settings
# class Top(BaseModel):
#     name=models.CharField(max_length=32,verbose_name='图片名字')
#     img=models.ImageField(upload_to='banner',verbose_name='轮播图',help_text='图片尺寸必须是：3840*800',null=True)
#     link=models.CharField(max_length=32,verbose_name='跳转连接')
#     info=models.TextField(verbose_name='图片简介')
#     # type=models.IntegerField(choices=)
#
#     def __str__(self):
#         return self.name

class Area(BaseModel):
    """分区

    跟文章是一对多的关系

    """
    name = models.CharField(max_length=64, unique=True, verbose_name="文章分区名称")
    class Meta:
        db_table = "nineth_article_area"
        verbose_name = "文章分区"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s" % self.name

class Topic(BaseModel):
    """话题
    跟文章是一对多的关系

    """
    name = models.CharField(max_length=64, unique=True, verbose_name="文章话题名称")
    class Meta:
        db_table = "nineth_article_topic"
        verbose_name = "文章话题"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s" % self.name

class Category(BaseModel):
    """分类
    跟文章是一对多的关系

    """
    name = models.CharField(max_length=64, unique=True, verbose_name="文章分类名称")
    class Meta:
        db_table = "nineth_article_category"
        verbose_name = "文章分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s" % self.name

def upload_to(instance,filename):
    return '/'.join(['article',instance.article.inner_link,filename])

class ArticleImg(BaseModel):
    """图片
    跟文章是多对一的关系
    """
    name = models.CharField(max_length=64,unique=True,verbose_name="文章图片")
    img = models.ImageField(upload_to=upload_to,max_length=255, verbose_name="文章图片", blank=True, null=True)
    article = models.ForeignKey('Article',to_field='inner_link',related_name='img',on_delete=models.DO_NOTHING, db_constraint=False, null=True, blank=True,verbose_name="文章图片")

    class Meta:
        db_table = "nineth_article_img"
        verbose_name = "文章图片"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s" % self.name


class Article(BaseModel):

    title = models.CharField(max_length=128, verbose_name="文章标题",blank=True)
    article_imgs = models.ImageField(upload_to="article/article_img", max_length=255, verbose_name="文章图片", blank=True, null=True)
    show_img = models.ImageField(upload_to="article/show_img", max_length=255, verbose_name="封面图片", blank=True, null=True)

    desc = models.TextField(max_length=2048, verbose_name="文章详情介绍", null=True, blank=True)
    pub_date = models.DateField(verbose_name="发布日期", auto_now_add=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="文章原价", default=0)

    inner_link = models.CharField(max_length=255,verbose_name='文章详情链接',blank=True,null=True,unique=True)
    outer_link = models.CharField(max_length=2048,verbose_name='文章跳转链接',blank=True,null=True)


    topic = models.ForeignKey("Topic", on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name="文章话题",db_constraint=False)
    category = models.ForeignKey("Category", on_delete=models.DO_NOTHING, db_constraint=False, null=True, blank=True,verbose_name="文章分类")
    area = models.ForeignKey("Area", on_delete=models.DO_NOTHING, db_constraint=False, null=True, blank=True,verbose_name="文章分区")
    user = models.ForeignKey("user.User", on_delete=models.DO_NOTHING, db_constraint=False, null=True, blank=True,verbose_name="文章作者")


    up_num = models.BigIntegerField(verbose_name='点赞数', default=0)
    comment_num = models.BigIntegerField(verbose_name='评论数', default=0)

    @property
    def area_name(self):
        return self.area.name

    @property
    def topic_name(self):
        return self.topic.name

    @property
    def category_name(self):
        return self.category.name

    @property
    def user_name(self):
        return self.user.username

    class Meta:
        db_table = "nineth_article"
        verbose_name = "文章"
        verbose_name_plural = "文章"

    def __str__(self):
        return "%s" % self.title


    # @property
    # def course_type_name(self):
    #     return self.get_course_type_display()
    # @property
    # def level_name(self):
    #     return self.get_level_display()
    # @property
    # def status_name(self):
    #     return self.get_status_display()
    #
    # @property
    # def section_list(self):
    #     ll=[]
    #     # 根据课程取出所有章节（正向查询，字段名.all()）
    #     course_chapter_list=self.coursechapters.all()
    #     for course_chapter in course_chapter_list:
    #         # 通过章节对象，取到章节下所有的课时（反向查询）
    #         # course_chapter.表名小写_set.all() 现在变成了course_chapter.coursesections.all()
    #         course_sections_list=course_chapter.coursesections.all()
    #         for course_section in course_sections_list:
    #             ll.append({
    #                 'name': course_section.name,
    #                 'section_link': course_section.section_link,
    #                 'duration': course_section.duration,
    #                 'free_trail': course_section.free_trail,
    #             })
    #             if len(ll)>=4:
    #                 return ll
    #
    #     return ll


class Up(BaseModel):
    user = models.ForeignKey(to='user.User',on_delete=models.DO_NOTHING)
    article = models.ForeignKey(to='Article',to_field='inner_link',on_delete=models.DO_NOTHING)
    is_up = models.BooleanField()  # 传布尔值 存0/1

    @property
    def user_name(self):
        return self.user.username

    class Meta:
        db_table = "nineth_article_up"
        verbose_name = "文章点赞"
        verbose_name_plural = "文章点赞"

class Comment(BaseModel):
    user = models.ForeignKey(to='user.User',on_delete=models.DO_NOTHING,db_constraint=False)
    article = models.ForeignKey(to='Article',to_field='inner_link',related_name='comment',on_delete=models.DO_NOTHING,db_constraint=False)
    content = models.CharField(verbose_name='评论内容',max_length=255)
    # 自关联
    parent = models.ForeignKey(to='self',null=True,on_delete=models.DO_NOTHING,db_constraint=False)  # 有些评论就是根评论

    @property
    def user_name(self):
        return self.user.username

    class Meta:
        db_table = "nineth_article_comment"
        verbose_name = "文章评论"
        verbose_name_plural = "文章评论"

#url: https://dig.chouti.com/share/link?link_id=29838361
#https://dig.chouti.com/share/short/url
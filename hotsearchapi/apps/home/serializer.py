# -*- coding:utf-8 -*-
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

import urllib.request
import uuid

from article import models
from django.conf import settings
from user.models import User

class ShareShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Article
        fields = ['desc','area','topic','area_name','topic_name',]
        extra_kwargs = {
            'desc':{'required':True},
            'area':{'required':True,'write_only':True},
            'area_name':{'read_only':True},
            'topic':{'write_only':True},
            'topic_name':{'read_only':True},
        }

    def _gen_inner_link(self):
        link_num = str(uuid.uuid4()).replace('-','')
        return link_num

    def validate(self, attrs):

        desc = attrs.get('desc')
        area = attrs.get('area')
        if not desc:
            raise ValidationError('内容不能为空')
        if not area:
            raise ValidationError('分区未选择')
        if len(desc) > 150:
            raise ValidationError('最多输入150字')
        attrs['user'] = self.context.get('request').user
        inner_link = self._gen_inner_link()
        attrs['inner_link'] = inner_link
        self.context['inner_link'] = inner_link
        return attrs

    def create(self, validated_data):

        article = models.Article.objects.create(**validated_data)
        return article



class ShareImgSerializer(serializers.ModelSerializer):
    imgs = serializers.ListField(
        child=serializers.FileField(max_length=100000,
                                    allow_empty_file=False,
                                    use_url=True), write_only=True
    )
    class Meta:
        model = models.Article
        fields = ['desc','area','topic','area_name','topic_name','imgs']
        extra_kwargs = {
            'desc':{'required':True},
            'area':{'required':True,'write_only':True},
            'area_name':{'read_only':True},
            'topic':{'write_only':True},
            'topic_name':{'read_only':True},
            'imgs':{'required':True}
        }

    def _gen_inner_link(self):
        link_num = str(uuid.uuid4()).replace('-','')
        return link_num

    def validate(self, attrs):

        desc = attrs.get('desc')
        area = attrs.get('area')
        if not desc:
            raise ValidationError('内容不能为空')
        if not area:
            raise ValidationError('分区未选择')
        if len(desc) > 150:
            raise ValidationError('最多输入150字')
        attrs['user'] = self.context.get('request').user
        inner_link = self._gen_inner_link()
        attrs['inner_link'] = inner_link
        # self.context['inner_link'] = inner_link
        # print(self.context.get('inner_link'))
        attrs['category_id'] = 2
        return attrs

    def create(self, validated_data):
        inner_link = validated_data.get('inner_link')
        imgs = validated_data.pop('imgs')
        article = models.Article.objects.create(**validated_data)
        for i in range(len(imgs)):
            img_name = inner_link + '_' + str(i)
            models.ArticleImg.objects.create(img=imgs[i],article_id=inner_link,name=img_name)
        return article
#
#
class ShareLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Article
        fields = ['desc','area','topic','area_name','topic_name','outer_link']
        extra_kwargs = {
            'desc':{'required':True},
            'area':{'required':True,'write_only':True},
            'area_name':{'read_only':True},
            'topic':{'write_only':True},
            'topic_name':{'read_only':True},
            'outer_link':{'required':True}
        }

    def _gen_inner_link(self):
        link_num = str(uuid.uuid4()).replace('-','')
        return link_num

    def _get_category_id(self,url):
        if 'video' in url:
            return 1
        if 'play' in url:
            return 1
        if 'photo' in url:
            return 2
        if 'img' in url:
            return 2

    def validate(self, attrs):
        outer_link = attrs.get('outer_link')
        try:
            res = urllib.request.urlopen(outer_link)
            # code = res.getcode()
            # res.close()
            # return code
        except Exception as e:
            raise ValidationError('链接已失效')

        desc = attrs.get('desc')
        area = attrs.get('area')
        if not desc:
            raise ValidationError('内容不能为空')
        if not area:
            raise ValidationError('分区未选择')
        if len(desc) > 150:
            raise ValidationError('最多输入150字')
        attrs['user'] = self.context.get('request').user
        inner_link = self._gen_inner_link()
        attrs['inner_link'] = inner_link
        category_id = self._get_category_id(outer_link)
        if category_id:
            attrs['category_id'] = category_id
        return attrs

    def create(self, validated_data):

        article = models.Article.objects.create(**validated_data)
        return article


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = ['user_name','content','parent']

class ImgRelateField(serializers.RelatedField):
    """自定义用于处理图片的字段"""
    def to_representation(self, value):
        return settings.BASE_URL+settings.MEDIA_URL+value.img.name


# class ArticleImgSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.ArticleImg
#         fields = ['img']
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','icon']

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Area
        fields = ['id','name']

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Topic
        fields = ['id','name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['id','name']

class LinkSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(many=True,read_only=True)
    # articleimg_set = serializers.ListField(
    #     child=serializers.ImageField()
    # )
    # articleimg_set = BookRelateField(queryset=models.ArticleImg.objects.all(),
    #                                               many=True)
    # articleimg_set = serializers.HyperlinkedRelatedField(lookup_field="img", view_name='',
    #                                                     queryset = models.ArticleImg.objects.all(), many = True)
    img = ImgRelateField(many=True,read_only=True)
    # img = ArticleImgSerializer(many=True,read_only=True)
    user = UserSerializer()
    area = AreaSerializer()
    topic = TopicSerializer()
    category = CategorySerializer()
    class Meta:
        model = models.Article
        fields = [
            'id',
            'created_time',
            'show_img',
            'pub_date',
            'desc',
            'inner_link',
            'outer_link',
            'up_num',
            'comment_num',
            'area',
            'category',
            'topic',
            'user',
            'comment',
            'img',
        ]

























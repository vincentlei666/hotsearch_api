# -*- coding:utf-8 -*-
from django.conf import settings

from rest_framework import serializers

from article import models

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = ['user_name','content','parent']

class ImgRelateField(serializers.RelatedField):
    """自定义用于处理图书的字段"""
    def to_representation(self, value):
        return settings.BASE_URL+settings.MEDIA_URL+value.img.name


# class ArticleImgSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.ArticleImg
#         fields = ['img']

class ImgSerializer(serializers.ModelSerializer):
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
            'area_name',
            'category_name',
            'topic_name',
            'user_name',
            'comment',
            'img',
        ]






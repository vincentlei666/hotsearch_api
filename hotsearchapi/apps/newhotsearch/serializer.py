# -*- coding:utf-8 -*-

from rest_framework import serializers
from article.models import Article, ArticleImg, Comment
from .models import NewHotArticle
from django.conf import settings
from user.models import User


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user_name','content','parent']

class ImgRelateField(serializers.RelatedField):
    def to_representation(self, value):
        return settings.BASE_URL+settings.MEDIA_URL+value.img.name

# class ArticleImgSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ArticleImg
#         fields = ['img']
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','icon']


class ArticleSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(read_only=True,many=True)
    img = ImgRelateField(many=True,read_only=True)
    user = UserSerializer()
    class Meta:
        model = Article
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
            'user',
            'comment',
            'img',
        ]

class NewHotSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(read_only=True)
    class Meta:
        model = NewHotArticle
        fields = ['id','article']


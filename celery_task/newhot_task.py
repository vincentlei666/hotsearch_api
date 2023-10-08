# -*- coding:utf-8 -*-

# import time
#
# from django.core.cache import cache

from .celery import app
from article.models import Article
from newhotsearch.models import NewHotArticle
# from django.conf import settings
import datetime

@app.task
def newhot_update():
    five_minutes_ago = datetime.datetime.now() - datetime.timedelta(seconds=5*60)
    articles = Article.objects.filter(created_time__gte=five_minutes_ago,up_num__gte=10)
    try:
        for article in articles:
            NewHotArticle.objects.update_or_create(article=article)
    except Exception as e:
        print(e)
    return True


















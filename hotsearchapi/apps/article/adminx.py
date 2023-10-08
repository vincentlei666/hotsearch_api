import xadmin


from . import models

xadmin.site.register(models.Area)
xadmin.site.register(models.Topic)
xadmin.site.register(models.Category)
xadmin.site.register(models.Article)
xadmin.site.register(models.Up)
xadmin.site.register(models.Comment)
xadmin.site.register(models.ArticleImg)

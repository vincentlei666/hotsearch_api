# Generated by Django 2.2.2 on 2020-08-10 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='最后更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否展示')),
                ('orders', models.IntegerField()),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='文章分区名称')),
            ],
            options={
                'verbose_name': '文章分区',
                'verbose_name_plural': '文章分区',
                'db_table': 'nineth_article_area',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='最后更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否展示')),
                ('orders', models.IntegerField()),
                ('title', models.CharField(max_length=128, verbose_name='文章标题')),
                ('article_imgs', models.ImageField(blank=True, max_length=255, null=True, upload_to='article/<built-in function id>/article_img', verbose_name='文章图片')),
                ('show_img', models.ImageField(blank=True, max_length=1, null=True, upload_to='article/<built-in function id>/show_img', verbose_name='封面图片')),
                ('desc', models.TextField(blank=True, max_length=2048, null=True, verbose_name='文章详情介绍')),
                ('pub_date', models.DateField(auto_now_add=True, verbose_name='发布日期')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='文章原价')),
                ('inner_link', models.CharField(blank=True, max_length=2048, null=True, verbose_name='文章详情链接')),
                ('outer_link', models.CharField(blank=True, max_length=2048, null=True, verbose_name='文章跳转链接')),
                ('up_num', models.BigIntegerField(default=0, verbose_name='点赞数')),
                ('comment_num', models.BigIntegerField(default=0, verbose_name='评论数')),
                ('area', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='article.Area', verbose_name='文章分区')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
                'db_table': 'nineth_course',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='最后更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否展示')),
                ('orders', models.IntegerField()),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='文章分类名称')),
            ],
            options={
                'verbose_name': '文章分类',
                'verbose_name_plural': '文章分类',
                'db_table': 'nineth_article_category',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='最后更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否展示')),
                ('orders', models.IntegerField()),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='文章话题名称')),
            ],
            options={
                'verbose_name': '文章话题',
                'verbose_name_plural': '文章话题',
                'db_table': 'nineth_article_topic',
            },
        ),
        migrations.CreateModel(
            name='Up',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='最后更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否展示')),
                ('orders', models.IntegerField()),
                ('is_up', models.BooleanField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='article.Article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.User')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='最后更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否展示')),
                ('orders', models.IntegerField()),
                ('content', models.CharField(max_length=255, verbose_name='评论内容')),
                ('article', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='article.Article')),
                ('parent', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='article.Comment')),
                ('user', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='user.User')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='article.Category', verbose_name='文章分类'),
        ),
        migrations.AddField(
            model_name='article',
            name='topic',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='article.Topic', verbose_name='文章话题'),
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user.User', verbose_name='文章作者'),
        ),
    ]
# Generated by Django 2.2.2 on 2020-08-10 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20200810_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='orders',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='orders',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='orders',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='orders',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='orders',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='up',
            name='orders',
            field=models.IntegerField(null=True),
        ),
    ]
# Generated by Django 3.1.7 on 2021-05-26 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0008_add_user_to_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cat',
            name='url',
        ),
        migrations.AddField(
            model_name='cat',
            name='image',
            field=models.ImageField(default='https://newsimg.hankookilbo.com/cms/articlerelease/2019/04/29/201904291390027161_3.jpg', upload_to=''),
            preserve_default=False,
        ),
    ]

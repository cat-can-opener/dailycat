# Generated by Django 3.1.7 on 2021-05-08 11:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cats', '0006_liked_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='title_set', to='users.user'),
            preserve_default=False,
        ),
    ]

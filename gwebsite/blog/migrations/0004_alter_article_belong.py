# Generated by Django 3.2.1 on 2021-08-16 13:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_article_belong'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='belong',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_user', to=settings.AUTH_USER_MODEL),
        ),
    ]

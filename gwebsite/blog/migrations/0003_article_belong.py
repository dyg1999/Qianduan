# Generated by Django 3.2.1 on 2021-08-16 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_userinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='belong',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_user', to='blog.userinfo'),
        ),
    ]

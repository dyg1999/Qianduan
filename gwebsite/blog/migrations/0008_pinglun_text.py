# Generated by Django 3.2.1 on 2021-08-23 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_pinglun'),
    ]

    operations = [
        migrations.AddField(
            model_name='pinglun',
            name='text',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]

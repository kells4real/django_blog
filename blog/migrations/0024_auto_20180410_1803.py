# Generated by Django 2.0.3 on 2018-04-10 12:33

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20180410_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='topbanner',
            field=models.FileField(blank=True, null=True, upload_to=blog.models.get_topbanner_filename),
        ),
    ]

# Generated by Django 2.1.1 on 2019-03-01 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_auto_20190301_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='birthdate',
            field=models.DateField(blank=True, default='1988-09-09', null=True),
        ),
    ]

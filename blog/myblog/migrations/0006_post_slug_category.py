# Generated by Django 4.0.3 on 2022-03-28 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0005_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug_category',
            field=models.SlugField(blank=True, max_length=40, null=True),
        ),
    ]

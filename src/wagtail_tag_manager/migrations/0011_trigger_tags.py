# Generated by Django 2.0.6 on 2018-09-05 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_tag_manager', '0010_remove_tag_passive'),
    ]

    operations = [
        migrations.AddField(
            model_name='trigger',
            name='tags',
            field=models.ManyToManyField(to='wagtail_tag_manager.Tag'),
        ),
    ]

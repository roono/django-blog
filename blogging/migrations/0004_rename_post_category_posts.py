# Generated by Django 4.0 on 2023-02-28 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0003_alter_category_options_remove_category_posts_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='post',
            new_name='posts',
        ),
    ]
# Generated by Django 2.2.4 on 2020-06-22 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_article_questions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='questions',
            new_name='question',
        ),
    ]
# Generated by Django 4.0 on 2024-03-02 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_comment_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='posted_by',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]

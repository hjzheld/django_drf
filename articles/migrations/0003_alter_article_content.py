# Generated by Django 4.2.5 on 2023-09-19 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_rename_aticle_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]

# Generated by Django 5.1.1 on 2024-10-27 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0010_remove_review_slug_alter_review_rating_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

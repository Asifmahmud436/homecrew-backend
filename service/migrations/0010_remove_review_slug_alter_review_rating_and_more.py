# Generated by Django 5.0.6 on 2024-08-31 13:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0009_alter_review_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='slug',
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=10),
        ),
        migrations.AlterField(
            model_name='review',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='service.service'),
        ),
    ]

# Generated by Django 5.0.6 on 2024-09-05 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_alter_client_facebook_id_link_alter_client_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='request_for_admin',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]

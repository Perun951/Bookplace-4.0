# Generated by Django 4.2 on 2023-05-23 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0011_delete_userprofile'),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='users_wishlist',
            field=models.ManyToManyField(blank=True, related_name='user_wishlist', to='userprofile.customer'),
        ),
    ]

# Generated by Django 4.2 on 2023-05-19 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0007_rename_username_customer_user_customer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/profile_images/'),
        ),
    ]

# Generated by Django 4.2 on 2023-05-20 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0008_customer_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='verificat',
            field=models.BooleanField(default=False),
        ),
    ]

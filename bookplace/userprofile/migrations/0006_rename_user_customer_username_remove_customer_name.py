# Generated by Django 4.2 on 2023-05-16 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_alter_customer_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='user',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='name',
        ),
    ]

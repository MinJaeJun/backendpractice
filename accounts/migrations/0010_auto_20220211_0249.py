# Generated by Django 3.0.14 on 2022-02-10 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_user_classnet_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='classnet_id',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
    ]
# Generated by Django 3.1 on 2020-08-11 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200811_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default='e', max_length=100),
            preserve_default=False,
        ),
    ]
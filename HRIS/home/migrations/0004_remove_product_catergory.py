# Generated by Django 3.0.7 on 2020-07-14 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200713_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='catergory',
        ),
    ]

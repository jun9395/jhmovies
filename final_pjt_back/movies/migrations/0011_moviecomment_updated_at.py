# Generated by Django 3.1.3 on 2020-11-26 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0010_auto_20201122_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviecomment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
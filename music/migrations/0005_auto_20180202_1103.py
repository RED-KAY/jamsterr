# Generated by Django 2.0 on 2018-02-02 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_auto_20180202_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='favorites',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='song',
            name='favorites',
            field=models.IntegerField(default=0),
        ),
    ]

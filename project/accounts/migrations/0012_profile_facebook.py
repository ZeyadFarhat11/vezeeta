# Generated by Django 3.2 on 2022-11-18 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20221118_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='facebook',
            field=models.CharField(default=1, max_length=70, verbose_name='فيس بوك'),
            preserve_default=False,
        ),
    ]
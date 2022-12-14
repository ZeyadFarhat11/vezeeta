# Generated by Django 3.2 on 2022-11-18 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_profile_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Specialist_doctor',
            field=models.CharField(default=1, max_length=50, verbose_name='القسم'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='Waiting_time',
            field=models.IntegerField(default=1, verbose_name='مده الانتظار'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(default=1, max_length=50, verbose_name='المحافظه'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='address_detail',
            field=models.CharField(default=1, max_length=70, verbose_name='العنوان بالتفاصيل'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='doctor',
            field=models.CharField(default=1, max_length=20, verbose_name='التخصص'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(default=1, max_length=20, verbose_name='رقم الهاتف'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='working_hours',
            field=models.IntegerField(default=1, verbose_name='عدد ساعات العمل'),
            preserve_default=False,
        ),
    ]

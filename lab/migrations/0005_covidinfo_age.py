# Generated by Django 3.2.6 on 2021-12-08 13:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0004_covidinfo_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='covidinfo',
            name='age',
            field=models.IntegerField(default=20),
            preserve_default=False,
        ),
    ]

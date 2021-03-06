# Generated by Django 3.2.6 on 2021-12-08 13:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('department', '0002_staffregister_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ward_no', models.IntegerField()),
                ('no_of_positive', models.IntegerField()),
                ('no_of_women', models.IntegerField()),
                ('no_of_men', models.IntegerField()),
                ('no_of_children', models.IntegerField()),
                ('TPR', models.FloatField()),
                ('WPR', models.FloatField()),
                ('home_quarantine', models.CharField(max_length=30)),
                ('total_death', models.IntegerField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

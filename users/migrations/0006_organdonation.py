# Generated by Django 3.2.6 on 2021-12-08 04:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0005_alter_userregister_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganDonation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_organ', models.CharField(max_length=30)),
                ('weight', models.IntegerField()),
                ('height', models.IntegerField()),
                ('h_status', models.CharField(max_length=20)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('donor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.userregister')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

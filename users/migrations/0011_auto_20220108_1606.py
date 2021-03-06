# Generated by Django 3.2.6 on 2022-01-08 10:36

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_remove_userregister_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='organdonation',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='organdonation',
            name='blood_group',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='organdonation',
            name='contact_person',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
        migrations.AddField(
            model_name='organdonation',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'male'), ('female', 'female')], default='male', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='organdonation',
            name='organs',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.organs'),
        ),
    ]

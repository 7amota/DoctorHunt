# Generated by Django 4.1.7 on 2023-03-23 12:01

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_alter_doctor_options_alter_doctor_views_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RatingSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(max_length=150, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratedoctor', to='users.doctor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userrate', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'doctor')},
                'index_together': {('user', 'doctor')},
            },
        ),
    ]
# Generated by Django 4.1.7 on 2023-05-07 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0044_alter_doctor_likes_remove_doctor_views_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='all_views',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
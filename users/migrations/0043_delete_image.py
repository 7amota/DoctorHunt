# Generated by Django 4.1.7 on 2023-04-27 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0042_alter_image_certificateimage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
    ]

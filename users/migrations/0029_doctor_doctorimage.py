# Generated by Django 4.1.7 on 2023-03-28 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0028_rename_avg_rating_doctor_avgrating_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='DoctorImage',
            field=models.ImageField(blank=True, default='doctorDefaultImage.jpg', null=True, upload_to='Photos/%y/%m/%d'),
        ),
    ]

# Generated by Django 4.1.7 on 2023-05-18 11:38

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0047_doctor_view_delete_docviews'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='view',
        ),
        migrations.CreateModel(
            name='DocViews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view', models.IntegerField(max_length=1, validators=[django.core.validators.MaxValueValidator(1)])),
                ('doc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doc', to='users.doctor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'doc')},
                'index_together': {('user', 'doc')},
            },
        ),
    ]
# Generated by Django 4.1.7 on 2023-03-30 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0032_doctor_listofspecialist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='specialist',
            field=models.CharField(blank=True, choices=[('Allergist', 'Allergist'), ('Anesthesiologist', 'Anesthesiologist'), ('Cardiologist', 'Cardiologist'), ('Dentist', 'Dentist'), ('Dermatologist', 'Dermatologist'), ('Endocrinologist', 'Endocrinologist'), ('Gastroenterologist', 'Gastroenterologist'), ('Hematologist', 'Hematologist'), ('Immunologist', 'Immunologist'), ('Infectious Disease Specialist', 'Infectious Disease Specialist'), ('Internal Medicine Physician', 'Internal Medicine Physician'), ('Medical Geneticist', 'Medical Geneticist'), ('Microbiologist', 'Microbiologist'), ('Neonatologist', 'Neonatologist'), ('Nephrologist', 'Nephrologist'), ('Neurologist', 'Neurologist'), ('Nurse Practitioner', 'Nurse Practitioner'), ('Obstetrician/Gynecologist', 'Obstetrician/Gynecologist'), ('Oncologist', 'Oncologist'), ('Ophthalmologist', 'Ophthalmologist'), ('Optometrist', 'Optometrist'), ('Orthopedist', 'Orthopedist'), ('Otolaryngologist', 'Otolaryngologist'), ('Pathologist', 'Pathologist'), ('Pediatrician', 'Pediatrician'), ('Physiatrist', 'Physiatrist'), ('Plastic Surgeon', 'Plastic Surgeon'), ('Podiatrist', 'Podiatrist'), ('Psychiatrist', 'Psychiatrist'), ('Pulmonologist', 'Pulmonologist'), ('Radiation Oncologist', 'Radiation Oncologist'), ('Radiologist', 'Radiologist'), ('Rheumatologist', 'Rheumatologist'), ('Sports Medicine Specialist', 'Sports Medicine Specialist'), ('Surgeon', 'Surgeon'), ('Urologist', 'Urologist')], max_length=50, null=True),
        ),
    ]

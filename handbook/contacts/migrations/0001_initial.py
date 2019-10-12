# Generated by Django 2.1.2 on 2019-07-19 10:04

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Department', models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('Administration', 'Administration'), ('CIVIL', 'CIVIL'), ('EEE', 'EEE'), ('ME', 'ME'), ('BSH', 'BSH'), ('Office', 'Office'), ('Library', 'Library'), ('COMPUTER CENTER', 'COMPUTER CENTER'), ('HOSTEL', 'HOSTEL')], default='Select department', max_length=80)),
                ('Name', models.CharField(max_length=80)),
                ('Designation', multiselectfield.db.fields.MultiSelectField(choices=[('Assistant Professor', 'Assistant Professor'), ('Associate Professor', 'Associate Professor'), ('Bus Codinator', 'Bus Codinator'), ('Professor', 'Professor'), ('Trade Instructor', 'Trade Instructor'), ('Office Assistant', 'Office Assistant'), ('Accountant', 'Accountant'), ('Office Manager', 'Office Manager'), ('Principal', 'Principal'), ('Secretary to Principal', 'Secretary to Principal'), ('Driver', 'Driver'), ('Manager', 'Manager'), ('Campus Head', 'Campus Head'), ('Asst. Manager', 'Asst. Manager'), ('Administrator', 'Administrator'), ('System Administrator', 'System Administrator'), ('Manager', 'Manager'), ('Chairman', 'Chairman'), ('Hostel Warden', 'Hostel Warden'), ('', '')], max_length=264)),
                ('Qualification', models.CharField(max_length=80)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone_Number', models.CharField(max_length=20, unique=True)),
                ('jecc_code', models.CharField(default='JEC', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='departments',
            field=models.ForeignKey(default='Select department', on_delete=django.db.models.deletion.CASCADE, to='contacts.department'),
        ),
    ]

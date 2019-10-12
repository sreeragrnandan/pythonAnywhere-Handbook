# Generated by Django 2.1.2 on 2019-04-22 00:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comity', '0007_auto_20190418_0702'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jecc_code', models.CharField(default='JEC', max_length=100)),
                ('Member_name', models.CharField(max_length=200)),
                ('designation', models.CharField(max_length=200)),
                ('department', models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('Administration', 'Administration'), ('CIVIL', 'CIVIL'), ('EEE', 'EEE'), ('ME', 'ME'), ('BSH', 'BSH'), ('Office', 'Office'), ('Library', 'Library'), ('COMPUTER CENTER', 'COMPUTER CENTER'), ('HOSTEL', 'HOSTEL')], default='Select department', max_length=80)),
                ('comity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comity.comity')),
            ],
        ),
        migrations.RemoveField(
            model_name='members',
            name='comity',
        ),
        migrations.DeleteModel(
            name='Members',
        ),
    ]

# Generated by Django 2.1.2 on 2019-07-06 11:28

from django.db import migrations, models
import django_thumbs.fields


class Migration(migrations.Migration):

    dependencies = [
        ('calender', '0032_auto_20190427_2244'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(help_text='Day of the event', verbose_name='Day of the event')),
                ('start_time', models.TimeField(help_text='Starting time', verbose_name='Starting time')),
                ('end_time', models.TimeField(help_text='Final time', verbose_name='Final time')),
                ('notes', models.TextField(blank=True, help_text='Textual Notes', null=True, verbose_name='Textual Notes')),
            ],
            options={
                'verbose_name': 'Scheduling',
                'verbose_name_plural': 'Scheduling',
            },
        ),
        migrations.AlterField(
            model_name='eventinfo',
            name='Photo',
            field=django_thumbs.fields.ImageThumbsField(blank=True, default='11ffe044ec04e', help_text='Upload *.jpg or *.jpeg images', sizes=({'code': 'gone', 'resize': 'crop', 'wxh': '725x573'}, {'code': 'gtwo', 'resize': 'crop', 'wxh': '725x274'}, {'code': 'normal', 'resize': 'crop', 'wxh': '350x238'}), upload_to='images'),
        ),
    ]

# Generated by Django 2.1.2 on 2019-04-21 07:38

from django.db import migrations
import django_thumbs.fields


class Migration(migrations.Migration):

    dependencies = [
        ('calender', '0020_auto_20190421_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventinfo',
            name='Photo',
            field=django_thumbs.fields.ImageThumbsField(blank=True, default='jyothi.jpg', sizes=({'code': 'gone', 'resize': 'crop', 'wxh': '725x573'}, {'code': 'gtwo', 'resize': 'crop', 'wxh': '725x274'}, {'code': 'normal', 'resize': 'crop', 'wxh': '350x238'}), upload_to='images'),
        ),
    ]

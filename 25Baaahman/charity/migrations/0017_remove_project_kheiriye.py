# Generated by Django 2.1.5 on 2020-02-03 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0016_auto_20200203_1533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='kheiriye',
        ),
    ]

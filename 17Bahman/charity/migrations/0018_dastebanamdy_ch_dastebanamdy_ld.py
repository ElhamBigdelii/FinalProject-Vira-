# Generated by Django 2.1.5 on 2020-02-03 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0017_remove_project_kheiriye'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dastebanamdy_ch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Dastebanamdy_LD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]

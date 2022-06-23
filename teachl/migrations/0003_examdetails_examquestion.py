# Generated by Django 3.2.8 on 2022-06-02 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachl', '0002_auto_20210912_1204'),
    ]

    operations = [
        migrations.CreateModel(
            name='examdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tmail', models.CharField(max_length=50)),
                ('UniqCode', models.CharField(max_length=10)),
                ('examname', models.CharField(max_length=50)),
                ('examdesc', models.CharField(max_length=200)),
                ('examdate', models.DateTimeField(max_length=200)),
                ('totalq', models.IntegerField()),
                ('finish', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='examquestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UniqCode', models.CharField(max_length=10)),
                ('qno', models.IntegerField()),
                ('question', models.CharField(max_length=200)),
                ('optiona', models.CharField(max_length=200)),
                ('optionb', models.CharField(max_length=200)),
                ('optionc', models.CharField(max_length=200)),
                ('optiond', models.CharField(max_length=200)),
                ('answer', models.CharField(max_length=200)),
            ],
        ),
    ]
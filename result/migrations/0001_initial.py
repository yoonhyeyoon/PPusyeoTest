# Generated by Django 3.2.8 on 2021-11-06 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BMI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(max_length=10)),
                ('body_mass', models.FloatField()),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Walk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(max_length=10)),
                ('walk_cnt', models.IntegerField()),
                ('age', models.IntegerField()),
            ],
        ),
    ]

# Generated by Django 3.2.6 on 2021-08-09 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountUser',
            fields=[
                ('UserName', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('PassWord', models.CharField(max_length=255)),
                ('ValidityEndDate', models.DateField()),
            ],
        ),
    ]

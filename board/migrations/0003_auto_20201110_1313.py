# Generated by Django 3.1.3 on 2020-11-10 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='hdate',
            field=models.DateField(),
        ),
    ]

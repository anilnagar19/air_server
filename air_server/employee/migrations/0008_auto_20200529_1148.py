# Generated by Django 3.0.6 on 2020-05-29 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0007_remove_employee_temperature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperature',
            name='EMP_IP',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]

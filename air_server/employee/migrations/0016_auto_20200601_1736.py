# Generated by Django 3.0.6 on 2020-06-01 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0015_auto_20200601_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperature',
            name='EMP_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employee'),
        ),
    ]

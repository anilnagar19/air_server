# Generated by Django 3.0.6 on 2020-06-01 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0013_auto_20200601_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperature',
            name='EMP_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee', to='employee.Employee'),
        ),
    ]

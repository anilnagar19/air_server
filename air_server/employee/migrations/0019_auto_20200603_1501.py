# Generated by Django 3.0.6 on 2020-06-03 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0018_auto_20200603_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperature',
            name='EMP_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Temperature', to='employee.Employee'),
        ),
    ]

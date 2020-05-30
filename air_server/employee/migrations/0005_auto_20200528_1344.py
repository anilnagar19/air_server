# Generated by Django 3.0.6 on 2020-05-28 13:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_auto_20200527_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='CREATED_AT',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='EMP_ID',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]

# Generated by Django 4.0.1 on 2022-03-17 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_patient_telephone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='telephone',
            field=models.IntegerField(default=0, max_length=100, unique=True),
        ),
    ]

# Generated by Django 2.0.1 on 2018-02-04 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='code',
            field=models.CharField(choices=[('colombia', 'CO'), ('mexico', 'MX'), ('estados unidos', 'USA'), ('argentina', 'AR')], max_length=3),
        ),
    ]

# Generated by Django 3.2.12 on 2022-06-03 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_alter_students_tuman'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='region',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='viloyat'),
        ),
    ]

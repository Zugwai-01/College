# Generated by Django 3.1.2 on 2020-11-26 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('college_management', '0002_auto_20201125_1439'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name_of_dept', models.CharField(max_length=264, unique=True)),
                ('Faculty', models.CharField(max_length=264)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='Dept',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='college_management.department'),
        ),
    ]

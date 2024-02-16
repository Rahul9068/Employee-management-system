# Generated by Django 4.1.1 on 2022-10-09 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Emp_Id', models.IntegerField()),
                ('Emp_Name', models.CharField(max_length=40)),
                ('Emp_Post', models.CharField(max_length=40)),
                ('Emp_Email', models.EmailField(max_length=40)),
                ('Emp_JoinD', models.DateField()),
            ],
        ),
    ]

# Generated by Django 4.2.4 on 2023-09-02 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stepproject', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstructorModel',
            fields=[
                ('InstructorID', models.AutoField(primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=255)),
                ('LastName', models.CharField(max_length=255)),
                ('DateOfBirth', models.DateField(blank=True, null=True)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Phone', models.CharField(blank=True, max_length=20, null=True)),
                ('Qualifications', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

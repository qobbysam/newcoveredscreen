# Generated by Django 3.2.15 on 2022-09-06 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('unique_id', models.CharField(blank=True, max_length=20, null=True)),
                ('add_date', models.DateField(auto_now_add=True, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('is_selected_random', models.BooleanField(default=False)),
                ('is_drugtest_bought', models.BooleanField(default=False)),
                ('is_dot_employee', models.BooleanField(default=False)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.usercompanymodel')),
            ],
            options={
                'ordering': ['add_date'],
                'unique_together': {('email', 'company')},
            },
        ),
    ]

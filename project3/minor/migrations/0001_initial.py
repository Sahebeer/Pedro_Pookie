# Generated by Django 5.1.5 on 2025-02-16 20:01

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FacultyInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alphabets are allowed')])),
                ('department', models.CharField(choices=[('CSE', 'Computer Science'), ('IT', 'Information Technology'), ('AIDS', 'Artificial Intelligence and Data Science'), ('EXTC', 'Electronics and Telecommunication')], max_length=4)),
                ('contact', models.PositiveIntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(9999999999), django.core.validators.MinValueValidator(6000000000)])),
                ('is_faculty', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ClassCoordinator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(choices=[('CSE', 'Computer Science'), ('IT', 'Information Technology'), ('AIDS', 'Artificial Intelligence and Data Science'), ('EXTC', 'Electronics and Telecommunication')], max_length=4)),
                ('year', models.CharField(choices=[('1', 'FIRST'), ('2', 'SECOND'), ('3', 'THIRD'), ('4', 'FOURTH')], default=None, max_length=1)),
                ('division', models.CharField(choices=[('A', 'Division A'), ('B', 'Division B')], max_length=10)),
                ('faculty', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='minor.facultyinfo')),
            ],
        ),
        migrations.CreateModel(
            name='GroupInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(choices=[('1', 'FIRST'), ('2', 'SECOND'), ('3', 'THIRD'), ('4', 'FOURTH')], max_length=6)),
                ('division', models.CharField(choices=[('A', 'Division A'), ('B', 'Division B')], max_length=10)),
                ('department', models.CharField(choices=[('CSE', 'Computer Science'), ('IT', 'Information Technology'), ('AIDS', 'Artificial Intelligence and Data Science'), ('EXTC', 'Electronics and Telecommunication')], max_length=4)),
                ('group_name', models.CharField(max_length=20, unique=True)),
                ('member_1_name', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alphabets are allowed')])),
                ('member_1_enrollment', models.CharField(max_length=15)),
                ('member_2_name', models.CharField(blank=True, max_length=100, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alphabets are allowed')])),
                ('member_2_enrollment', models.CharField(blank=True, max_length=15, null=True)),
                ('member_3_name', models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alphabets are allowed')])),
                ('member_3_enrollment', models.CharField(blank=True, max_length=15, null=True)),
                ('contact', models.PositiveIntegerField(unique=True)),
                ('is_group', models.BooleanField(default=True)),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='minor.facultyinfo')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HeadOfDepartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(choices=[('CSE', 'Computer Science'), ('IT', 'Information Technology'), ('AIDS', 'Artificial Intelligence and Data Science'), ('EXTC', 'Electronics and Telecommunication')], max_length=4)),
                ('name', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alphabets are allowed')])),
                ('contact', models.PositiveIntegerField()),
                ('is_HOD', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='No project chosen', max_length=300)),
                ('description', models.TextField(default='No description')),
                ('is_approved_by_mentor', models.BooleanField(default=False)),
                ('is_approved_by_HOD', models.BooleanField(default=False)),
                ('mentor_feedback', models.CharField(default='No feedback', max_length=1500)),
                ('hod_feedback', models.CharField(default='No feedback', max_length=1500)),
                ('status', models.CharField(default='No status', max_length=1500)),
                ('group_message', models.TextField(blank=True, default=' ', null=True)),
                ('mentor_message', models.TextField(blank=True, default=' ', null=True)),
                ('synopsis', models.FileField(default='settings.MEDIA_ROOT/documents/default.txt', null=True, upload_to='documents/')),
                ('srs', models.FileField(default='settings.MEDIA_ROOT/documents/default.txt', null=True, upload_to='documents/')),
                ('wbs', models.FileField(default='settings.MEDIA_ROOT/documents/default.txt', null=True, upload_to='documents/')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='minor.groupinfo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

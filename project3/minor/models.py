from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator

alphabets = RegexValidator(r'^[a-zA-Z]*$', 'Only alphabets are allowed')

DEPARTMENT = (
    ('CSE', 'Computer Science'),
    ('IT', 'Information Technology'),
    ('AIDS', 'Artificial Intelligence and Data Science'),
    ('EXTC', 'Electronics and Telecommunication'),
)

DIVISION = (
    ('A', 'Division A'),
    ('B', 'Division B')
)

YEAR = (
    ('1', 'FIRST'),
    ('2', 'SECOND'),
    ('3', 'THIRD'),
    ('4', 'FOURTH')
)

class FacultyInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, validators=[alphabets])
    department = models.CharField(choices=DEPARTMENT, max_length=4)
    contact = models.PositiveIntegerField(unique=True, validators=[MaxValueValidator(9999999999), MinValueValidator(6000000000)])
    is_faculty = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name + " - " + self.department

class GroupInfo(models.Model):
    """Adding this comment to force a migration"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    year = models.CharField(choices=YEAR, max_length=6)
    division = models.CharField(choices=DIVISION, max_length=10)
    mentor = models.ForeignKey(FacultyInfo, on_delete=models.PROTECT)
    department = models.CharField(choices=DEPARTMENT, max_length=4)
    group_name = models.CharField(max_length=20, unique=True)
    member_1_name = models.CharField(max_length=100, validators=[alphabets])
    member_1_enrollment = models.CharField(max_length=15)
    member_2_name = models.CharField(max_length=100, validators=[alphabets], blank=True)
    member_2_enrollment = models.CharField(max_length=15, blank=True, null=True)
    member_3_name = models.CharField(max_length=100, validators=[alphabets], blank=True, null=True)
    member_3_enrollment = models.CharField(max_length=15, blank=True, null=True)
    contact = models.PositiveIntegerField(unique=True)
    is_group = models.BooleanField(default=True)
    
    REQUIRED_FIELDS = ['user', 'department', 'year', 'division', 'mentor', 'group_name', 'member_1_name', 'member_1_enrollment', 'contact']
    
    def __str__(self):
        return self.group_name

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    group = models.ForeignKey(GroupInfo, on_delete=models.PROTECT)
    title = models.CharField(max_length=300, default="No project chosen")
    description = models.TextField(default="No description")
    is_approved_by_mentor = models.BooleanField(default=False)
    is_approved_by_HOD = models.BooleanField(default=False)
    mentor_feedback = models.CharField(default="No feedback", max_length=1500)
    hod_feedback = models.CharField(default="No feedback", max_length=1500)
    status = models.CharField(default="No status", max_length=1500)
    group_message = models.TextField(default=' ', blank=True, null=True)
    mentor_message = models.TextField(default=' ', blank=True, null=True)
    synopsis = models.FileField(upload_to='documents/', null=True, default='settings.MEDIA_ROOT/documents/default.txt')
    srs = models.FileField(upload_to='documents/', null=True, default='settings.MEDIA_ROOT/documents/default.txt')
    wbs = models.FileField(upload_to='documents/', null=True, default='settings.MEDIA_ROOT/documents/default.txt')

    def mentor_approval(self):
        return reverse('minor:mentor-approval', kwargs={'pk': self.pk})

    def hod_approval(self):
        return reverse('minor:hod-approval', kwargs={'pk': self.pk})

    def get_absolute_url(self):
        return reverse('minor:project', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

class HeadOfDepartment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(choices=DEPARTMENT, max_length=4)
    name = models.CharField(max_length=100, validators=[alphabets])
    contact = models.PositiveIntegerField()
    is_HOD = models.BooleanField(default=True)

    def __str__(self):
        return "Head Of Department of " + self.department + " is " + self.name

class ClassCoordinator(models.Model):
    faculty = models.OneToOneField(FacultyInfo, on_delete=models.CASCADE)
    department = models.CharField(choices=DEPARTMENT, max_length=4)
    year = models.CharField(choices=YEAR, max_length=1, default=None)
    division = models.CharField(choices=DIVISION, max_length=10)

    def __str__(self):
        return self.faculty.name + " - " + self.faculty.department

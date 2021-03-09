from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Qualification(models.Model):
    qualification_name = models.CharField(max_length=800)
    qualification_date = models.DateField()
    class Meta:
        verbose_name_plural = 'qualifications'
    def __str__(self):
        return self.qualification_name

class State_Of_Origin(models.Model):
    state_name = models.CharField(max_length=800)
    LGA = models.CharField(max_length=800)
    class Meta:
        verbose_name_plural = 'States of origin'
    def __str__(self):
        return self.state_name

class Geopolitical_Zone(models.Model):
    geopolitical_zone = models.CharField(max_length=800)

    class Meta:
        verbose_name_plural = 'Geopolitical zones'
    def __str__(self):
        return self.geopolitical_zone

class Rank(models.Model):
    rank = models.CharField(max_length=800)

    class Meta:
        verbose_name_plural = 'Ranks'
    def __str__(self):
        return self.rank

class Step(models.Model):
    step = models.CharField(max_length=800)

    class Meta:
        verbose_name_plural = 'Steps'
    def __str__(self):
        return self.step

class Grade_Level(models.Model):
    grade_level_name = models.CharField(max_length=800)

    class Meta:
        verbose_name_plural = 'Grade Levels'
    def __str__(self):
        return self.grade_level_name

class Salary_Structure(models.Model):
    salary_structure_name = models.CharField(max_length=800)

    class Meta:
        verbose_name_plural = 'Salary structures'
    def __str__(self):
        return self.salary_structure_name

class Promotion(models.Model):
    promotion_date = models.DateTimeField(auto_now_add=True)
    grade_level = models.ForeignKey(
        Grade_Level, on_delete=models.CASCADE, verbose_name="grade level")
    staff = models.ForeignKey(
        Staff, on_delete=models.CASCADE, verbose_name="staff")
    step = models.ForeignKey(
        Step, on_delete=models.CASCADE, verbose_name="step")
    class Meta:
        verbose_name_plural = 'Steps'
    def __str__(self):
        return self.promotion_date

class Staff(models.Model):
    staff_name = models.CharField(max_length=800)
    date_of_birth=models.DateTimeField(auto_now_add=True)
    date_of_first_appointment=models.DateField(max_length=800)
    phone_no = models.CharField(max_length=800)
    file_no = models.PositiveSmallIntegerField(validators=[MinValueValidator(0)],blank=True,null=True,default=0)
    qualification = models.ForeignKey(
        Qualification, on_delete=models.CASCADE, verbose_name="qualification")
    salary_structure = models.ForeignKey(
        Qualification, on_delete=models.CASCADE, verbose_name="salary structure")
    confirmation_date = models.DateTimeField(auto_now_add=True)
    promotion = models.ForeignKey(
        Promotion, on_delete=models.CASCADE, verbose_name="promotion")
    state = models.ForeignKey(
        State_Of_Origin, on_delete=models.CASCADE, verbose_name="state of origin")
    step = models.ForeignKey(
        Step, on_delete=models.CASCADE, verbose_name="step")
    grade_level = models.ForeignKey(
        Grade_Level, on_delete=models.CASCADE, verbose_name="grade level")
    rank = models.ForeignKey(
        Rank, on_delete=models.CASCADE, verbose_name="rank")
    geopolitical_zone = models.ForeignKey(
        Geopolitical_Zone, on_delete=models.CASCADE, verbose_name="geopolitical zone")
    address = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    class Meta:
        verbose_name_plural = 'staff'
    def __str__(self):
        return self.staff_name
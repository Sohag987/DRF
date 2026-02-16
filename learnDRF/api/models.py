from django.db import models

# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_teacher = models.CharField(max_length=100)
    course_duration =models.IntegerField()
    seat_number = models.IntegerField()

    class Meta:
        verbose_name_plural = "Course" 

    def __str__(self):
        return self.course_name

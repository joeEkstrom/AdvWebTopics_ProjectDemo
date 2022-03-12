from django.db import models

# Create your models here.
class Course(models.Model):
	course_name = models.CharField(max_length=100)
	start_date = models.DateTimeField()

	def __str__(self):
		return self.course_name
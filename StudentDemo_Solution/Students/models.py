from django.db import models
from datetime import date

# Create your models here.
class Student(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	profile_pic = models.ImageField(upload_to='pics')
	date_of_birth = models.DateTimeField()
	amount_owed = models.FloatField()
	graduated = models.BooleanField(default=False)

	class Meta:
		ordering = ['-last_name']

	def age(self):
		today = date.today()
		age = today.year - self.date_of_birth.year - ((today.month, today.day)
		 < (self.date_of_birth.month, self.date_of_birth.day))
		return age

	def is_graduated(self):
		return "Yes" if self.graduated else "No"

	def __str__(self):
		return self.last_name + ', ' + self.first_name
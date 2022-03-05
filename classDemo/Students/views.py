from django.contrib import messages
from django.shortcuts import render
from django.views.generic import ListView
from Students.models import Student

# Create your views here.
class StudentListView(ListView):
	model = Student

def add(request):
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		profile_pic = request.FILES['profile_pic']
		date_of_birth = request.POST['date_of_birth']
		graduated = True if 'graduated' in request.POST else False

		student = Student.objects.create(
			first_name = first_name,
			last_name = last_name,
			date_of_birth = date_of_birth,
			profile_pic = profile_pic,
			graduated = graduated,
			amount_owed = 1600,
		)
		messages.info(request, 'Student Created')

		return render(request, 'students/add.html', {'file':profile_pic})

	else:
		return render(request, 'students/add.html')
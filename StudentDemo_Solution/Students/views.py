from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.shortcuts import render
 
from Students.models import Student
from django.core.files.storage import FileSystemStorage

# Create your views here.
class StudentListView(ListView):
	model = Student

class StudentDetailView(DetailView):
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

		# fss = FileSystemStorage()
		# file = fss.save(profile_pic.name, profile_pic)
		# file_url = fss.url(file)

		messages.info(request, 'Student Created')

		return render(request, 'students/add.html', {'file':student.profile_pic})
	return render(request, 'students/add.html')
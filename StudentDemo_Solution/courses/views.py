from django.views.generic import ListView, DetailView
from django.shortcuts import render

from courses.models import Course
from django.contrib import messages

# Create your views here.
def add(request):
	if request.method == 'POST':
		course = Course.objects.create(
			course_name = request.POST['course_name'],
			start_date = request.POST['start_date']
		)

		messages.info(request, f"{course.course_name} Created!")

		return render(request, 'courses/add.html', {'course': course})
	
	return render(request, 'courses/add.html')

class CourseListView(ListView):
	model = Course

class CourseDetailView(DetailView):
	model = Course
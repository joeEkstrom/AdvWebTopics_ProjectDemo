from django.urls import path
from . import views

urlpatterns = [
	path('', views.StudentListView.as_view()),
	path('addStudent', views.add, name='addStudent'),
	path('students/<int:pk>/', views.StudentDetailView.as_view(), name="student-detail")
]
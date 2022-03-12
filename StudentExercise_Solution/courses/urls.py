from django.urls import path
from . import views

urlpatterns = [
	path('', views.CourseListView.as_view()),
	path('addCourse', views.add, name="addCourse"),
	path('<int:pk>/', views.CourseDetailView.as_view(), name="course-detail")
]
from django.urls import path
from . import views

urlpatterns = [
	path('', views.StudentListView.as_view()),
	path('addStudent', views.add, name='addStudent')
]
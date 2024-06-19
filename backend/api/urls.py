from django.urls import path
from .views import StudentDetailView, StudentListCreateView

urlpatterns = [
    path('students/', StudentListCreateView.as_view(), name='student_list_create'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
]
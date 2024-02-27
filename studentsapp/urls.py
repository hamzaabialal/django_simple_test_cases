
from django.urls import path
from .views import StudentListView, StudentUpdateView, StudentDetailsView, StudentDetailsDetailsView

urlpatterns = [
    path('student/', StudentListView.as_view(), name='student-list'),
    path('student/<int:pk>/', StudentUpdateView.as_view(), name='student-update'),
    path('studentdetails/', StudentDetailsView.as_view(), name='student_detail'),
    path('studentdetails/<int:pk>/', StudentDetailsDetailsView.as_view(), name='student_details')

]
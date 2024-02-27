from django.shortcuts import render
from .models import Student, StudentDetails
from .serializers import StudentSerializer, StudentDetailsSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.

class StudentListView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StudentUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class StudentDetailsView(ListCreateAPIView):
    queryset = StudentDetails.objects.all()
    serializer_class = StudentDetailsSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StudentDetailsDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = StudentDetails.objects.all()
    serializer_class = StudentDetailsSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, args, kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, args, kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
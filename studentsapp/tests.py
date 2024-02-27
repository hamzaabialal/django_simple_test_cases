from http import client

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from studentsapp.models import Student, StudentDetails


# Create your tests here.

class StudentsModelTests(TestCase):
    def setUp(self):
        pass

    def test_students_post(self):
        client = APIClient()
        url = reverse('student-list')
        response = client.post(url)
        data = {
            'first_name': 'Hamza',
            'last_name' : 'Bilal',
            'email' : 'hamzaabialal@gmail.com',
           'age': 23
        }
        response = client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_student_without_email(self):
        client = APIClient()
        url = reverse('student-list')
        response = client.get(url)
        data = {
            'first_name': 'Hamza',
            'last_name': "ALI",
             'age': 23
        }
        response = client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, 400)

    def test_student_without_first_name(self):
        client = APIClient()
        url = reverse('student-list')
        response = client.get(url)
        data = {
            'last_name': 'AHamd',
            'email': 'ahmad@gmail.com',
            'age': 23
        }
        response = client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, 400)

    def test_student_api(self):
        client = APIClient()
        url = reverse('student-list')
        response = client.get(url)
        self.assertEqual(response.status_code, 200)


class StudentUpdateTests(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            first_name='hamza',
            last_name = 'ijaz',
            email = 'aliijaz@gmail.com',
            age= 24
        )

    def test_student_update(self):
        client = APIClient()
        url = reverse('student-update', kwargs={'pk': self.student.id})
        data = {
            'first_name': 'ali',
            'last_name': 'sardar',
            'email': 'alisaradar@gmail.com',
            'age': 89
        }
        response = client.put(url, data=data, format='json')
        self.assertEqual(response.status_code, 200)


    def test_student_update_invalid_email(self):
        client = APIClient()
        url = reverse('student-update', kwargs={'pk': self.student.id})
        data = {
            'first_name': 'ali',
            'last_name': 'sardar',
            'email': 'alisaradar@gmail',
            'age': 89
        }
        response = client.put(url, data=data, format='json')
        self.assertEqual(response.status_code, 400)

    def test_delete_student(self):
        url = reverse('student-update', kwargs={'pk': self.student.id})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, 204)


class StudentDetailsTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            first_name='Hamza',
            last_name = 'ali',
            email = 'aliahamad@gmail.com',
            age= 45
        )
        self.student_detail= StudentDetails.objects.create(
            student = self.student,
            father_name= 'hamza',
            mother_name= 'ali',
            address= '123 Main Street',
            departement= 'Data Science'
        )

    def test_student_details(self):
        client = APIClient()
        url  = reverse('student_detail')
        response = client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_student_create(self):
        client = APIClient()
        url = reverse('student_detail')
        data = {
            'student': self.student.id,
            'father_name': 'ali',
            'mother_name': 'Hamzna',
            'departement': 'Student',
            'address': "Main St"
        }
        response = client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, 201)


    def test_student_without_departement(self):
        client =APIClient()
        url = reverse('student_detail')
        data = {
            'student': self.student.id,
            'father_name': 'ali',
            'mother_name': 'Hamzna',
            'address': "Main St"
        }
        response = client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, 400)


    def test_student_update_departement(self):
        client = APIClient()
        url = reverse('student_details', kwargs={'pk': self.student_detail.id})
        data={

            'departement': 'May Hamza',
        }
        response = client.patch(url, data=data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_student_update_data(self):
        client = APIClient()
        url = reverse('student_details', kwargs={'pk': self.student_detail.id})
        data = {
            'student': self.student.id,
            'father_name': 'ali',
            'mother_name': 'Hamzna',
            'departement': 'ALi',
            'address': "134 Main St"

        }
        response = client.put(url, data=data, format='json')
        self.assertEqual(response.status_code, 200)






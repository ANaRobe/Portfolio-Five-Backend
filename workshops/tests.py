from django.contrib.auth.models import User
from .models import Workshop
from rest_framework import status
from rest_framework.test import APITestCase


class WorkshopListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='jimmy', password='12345678')

    def test_can_list_workshops(self):
        jimmy = User.objects.get(username='jimmy')
        Workshop.objects.create(owner=jimmy, title='WorkshopTest')
        response = self.client.get('/workshops/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_workshop(self):
        self.client.login(username='jimmy', password='12345678')
        response = self.client.workshop('/workshops/', {'title': 'WorkshopTest'})
        count = Workshop.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_not_logged_in_user_cant_workshop(self):
        response = self.client.workshop('/workshops/', {'title': 'WorkshopTest'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class WorkshopDetailViewTests(APITestCase):
    def setUp(self):
        jimmy = User.objects.create_user(username='jimmy', password='12345678')
        liam = User.objects.create_user(username='liam', password='87654321')
        Workshop.objects.create(
            owner=jimmy, title='Jimmys Workshop!', content='Jimmys text'
        )
        Workshop.objects.create(
            owner=liam, title='Liams Workshop!', content='Liams text'
        )

    def test_can_get_workshop_with_valid_id(self):
        response = self.client.get('/workshops/1/')
        self.assertEqual(response.data['title'], 'Jimmys Workshop!')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_get_workshop_with_invalid_id(self):
        response = self.client.get('/workshops/9999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_workshop(self):
        self.client.login(username='jimmy', password='12345678')
        response = self.client.put('/workshops/1/', {'title': 'updated title'})
        workshop = Workshop.objects.filter(pk=1).first()
        self.assertEqual(workshop.title, 'updated title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_workshop(self):
        self.client.login(username='jimmy', password='12345678')
        response = self.client.put('/workshops/2/', {'title': 'updated title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

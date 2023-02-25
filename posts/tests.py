from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='jimmy', password='12345678')

    def test_can_list_posts(self):
        jimmy = User.objects.get(username='jimmy')
        Post.objects.create(owner=jimmy, title='PostTest')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_post(self):
        self.client.login(username='jimmy', password='12345678')
        response = self.client.post('/posts/', {'title': 'PostTest'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_not_logged_in_user_cant_post(self):
        response = self.client.post('/posts/', {'title': 'PostTest'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PostDetailViewTests(APITestCase):
    def setUp(self):
        jimmy = User.objects.create_user(username='jimmy', password='12345678')
        liam = User.objects.create_user(username='liam', password='87654321')
        Post.objects.create(
            owner=jimmy, title='Jimmys post!', content='Jimmys text'
        )
        Post.objects.create(
            owner=liam, title='Liams post!', content='Liams text'
        )

    def test_can_get_post_with_valid_id(self):
        response = self.client.get('/posts/1/')
        self.assertEqual(response.data['title'], 'Jimmys post!')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_get_post_with_invalid_id(self):
        response = self.client.get('/posts/9999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_post(self):
        self.client.login(username='jimmy', password='12345678')
        response = self.client.put('/posts/1/', {'title': 'updated title'})
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(post.title, 'updated title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_post(self):
        self.client.login(username='jimmy', password='12345678')
        response = self.client.put('/posts/2/', {'title': 'updated title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

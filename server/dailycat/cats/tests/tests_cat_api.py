import os
import json
import shutil
import tempfile
from http import HTTPStatus
from PIL import Image

from django.shortcuts import reverse
from django.test import override_settings
from rest_framework.test import APITestCase

from ..models import Cat, Title
from users.models import User

MEDIA_ROOT = tempfile.mkdtemp()


@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class CatAPITestCase(APITestCase):
    def setUp(self):
        image = Image.new('L', (10, 10))
        print(MEDIA_ROOT)
        self.filename = os.path.join(MEDIA_ROOT, 'test_image.jpg')
        image.save(self.filename)

    def tearDown(self):
        shutil.rmtree(MEDIA_ROOT)

    def test_cat_list_api_works(self):
        '''cat list api 테스트. 10개 생성시 10개 나오는지 테스트'''
        # for i in range(100):
        Cat.objects.create(image=self.filename)

        list_url = reverse('cat:cat_list')  # 'api/v1/cats/cats/'
        res = self.client.get(list_url)
        self.assertEqual(res.status_code, HTTPStatus.OK)
        self.assertEqual(len(res.data), 1)

    def test_cat_list_has_title_field(self):
        '''list api가 3개의 title 값을 가지고 있는지'''
        cat = Cat.objects.create(image='http://test_url.com')
        user = User.objects.create(username="test")
        for i in range(20):
            Title.objects.create(cat=cat, content=f'title-{i}', user=user)

        # list_url = reverse('cat:cat_list')  # 'api/v1/cats/cats/'
        # title = Title.objects.filter(cat=cat)
        res = self.client.get('/api/v1/cats/1/')
        cat: dict = res.data
        titles: list = cat.get('titles_method')
        self.assertEqual(len(titles), 3)

    def test_cat_detail_api(self):
        '''cat 상세 api 테스트'''
        url = 'http://test_url.com'

        cat = Cat.objects.create(image=self.filename)
        user = User.objects.create(username='test')
        title = Title.objects.create(
            cat=cat, user=user, content='title content')
        # detail_url = reverse('cats:cat_detail', kwargs={'pk': cat.id})

        response = self.client.get('/api/v1/cats/1/')
        # print(response.data)
        # title_data = response.data['titles_method']
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.data['image'], url)


class CatLikeTest(APITestCase):
    def setUp(self):
        url = 'http://test_url.com'
        self.cat = Cat.objects.create(image=url)
        self.user = User.objects.create_user(
            username='testuser', password='testpass')

        # /api/v1/cats/1/like/
        self.like_url = reverse('cat:like_cat', kwargs={'pk': self.cat.pk})

    def test_cat_like_api_401_without_login(self):
        '''고양이 좋아요 api test'''
        # /api/v1/cats/1/like/
        response = self.client.post(self.like_url, data={
            'like': 'true',
        })

        self.assertEqual(response.status_code, HTTPStatus.UNAUTHORIZED)

    def test_cat_like_api_works(self):
        cat = Cat.objects.create(image='http://test.com')
        like_url = reverse('cat:like_cat', kwargs={'pk': cat.pk})
        user = User.objects.create_user(
            username='testuser2', password='testpass')

        # as is
        self.client.force_authenticate(user)
        response = self.client.post(like_url, data={
            'like': 'true',
        })

        # to be
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertIn(cat, user.liked_cats.all())

    def test_cat_like_api_unlike_works(self):
        cat = Cat.objects.create(image='http://test.com')
        like_url = reverse('cat:like_cat', kwargs={'pk': cat.pk})
        user = User.objects.create_user(
            username='testuser2', password='testpass')

        # 미리 cat 좋아요 추가
        user.liked_cats.add(cat)
        self.assertIn(cat, user.liked_cats.all())

        # as is
        self.client.force_authenticate(user)
        response = self.client.post(like_url, data={
            'like': 'false',
        })

        # to be
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertNotIn(cat, user.liked_cats.all())

    def test_cat_like_api_already_like(self):
        '''이미 좋아요 눌른 경우에 다시 api 호출하는 경우'''
        cat = Cat.objects.create(image='http://test.com')
        like_url = reverse('cat:like_cat', kwargs={'pk': cat.pk})
        user = User.objects.create_user(
            username='testuser2', password='testpass')

        # 미리 cat 좋아요 추가
        user.liked_cats.add(cat)
        self.assertIn(cat, user.liked_cats.all())

        # as is
        self.client.force_authenticate(user)
        response = self.client.post(like_url, data={
            'like': 'true',
        })

        # to be
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertIn(cat, user.liked_cats.all())

    def test_cat_like_api_unlike_when_unlike(self):
        '''안 좋아하는 경우에 다시 안 좋아요 api 호출하는 경우'''
        cat = Cat.objects.create(image='http://test.com')
        like_url = reverse('cat:like_cat', kwargs={'pk': cat.pk})
        user = User.objects.create_user(
            username='testuser2', password='testpass')

        self.assertNotIn(cat, user.liked_cats.all())

        # as is
        self.client.force_authenticate(user)
        response = self.client.post(like_url, data={
            'like': 'false',
        })

        # to be
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertNotIn(cat, user.liked_cats.all())

    def test_cat_like_without_like_data(self):
        '''like data가 없는경우 400'''
        cat = Cat.objects.create(image='http://test.com')
        like_url = reverse('cat:like_cat', kwargs={'pk': cat.pk})
        user = User.objects.create_user(
            username='testuser2', password='testpass')
        # as is
        self.client.force_authenticate(user)
        response = self.client.post(like_url)

        # to be
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_cat_like_with_invalid_data(self):
        '''like 대신 다른 데이터가 들어오는 경우'''
        cat = Cat.objects.create(image='http://test.com')
        like_url = reverse('cat:like_cat', kwargs={'pk': cat.pk})
        user = User.objects.create_user(
            username='testuser2', password='testpass')
        invalid_datas: list = [
            {'like': 'invalid_value'},
            {'invalid_key': 'true'},
            {'invalid_key': 'invalid_value'},
        ]
        # as is
        self.client.force_authenticate(user)

        for invalid_data in invalid_datas:
            response = self.client.post(like_url, data=invalid_data)
            with self.subTest(response=response):
                self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

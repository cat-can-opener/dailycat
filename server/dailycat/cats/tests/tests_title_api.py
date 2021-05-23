from http import HTTPStatus

from django.shortcuts import reverse
from rest_framework.test import APITestCase

from ..models import Cat, Title
# from ...users.models import User
from users.models import User


class TitleAPITestCase(APITestCase):
    def test_title_list_api(self):
        cat = Cat.objects.create(url='http://test_url.com')
        user = User.objects.create(username="test")
        for i in range(100):
            Title.objects.create(cat=cat, content='test content', user=user)
        # list_url = reverse('cats:title_list', kwargs={'cat_pk': cat.id})

        response = self.client.get('/api/v1/titles/?cat=1')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(len(response.data), 100)

    def test_title_list_api_with_other_cats(self):
        '''다른 cat의 title이 나오지 않는지 확인'''
        cat = Cat.objects.create(url='http://test_url.com')
        not_include_cat = Cat.objects.create(url='http://test_url_2.com')
        user = User.objects.create(username="test")

        for i in range(100):
            Title.objects.create(cat=cat, content='test content', user=user)

        for i in range(100):
            Title.objects.create(cat=not_include_cat,
                                 content='test content', user=user)
        # list_url = reverse('cats:title-list', kwargs={'cat_pk': cat.id})
        response = self.client.get('/api/v1/titles/?cat=1')
        # response = self.client.get(list_url)
        # print(response.data[0].get('cat'))
        title = Title.objects.filter(cat=cat)
        self.assertEqual(len(response.data), 100)
        self.assertEqual(title[0].cat.url, 'http://test_url.com')

    def test_title_update_api(self):
        '''title update api test'''
        cat = Cat.objects.create(url='http://test_url.com')
        user = User.objects.create(username="test")
        title = Title.objects.create(cat=cat, content='test', user=user)
        updated_content = 'updated'
        # update_url = reverse('/api/v1/titles/1')
        # print(update_url)
        # update_url = reverse('/api/v1/titles/1/')
        response = self.client.patch('/api/v1/titles/1/', data={
            'content': updated_content
        })
        # response = self.client.patch(update_url, data={
        #     'content': updated_content
        # })
        # self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['content'], updated_content)

    # TODO: only user can create after add user
    def test_title_create_api(self):
        '''title 생성 api 테스트'''
        cat = Cat.objects.create(url='http://test_url.com')
        user = User.objects.create(username="test")

        list_url = reverse('cat:title_list')

        test_content = 'test content'
        response = self.client.post(list_url, data={
            'content': test_content,
            'cat': cat.id,
            'user': user.id
        })
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(response.data['content'], test_content)

    # TODO: only owner can update after add user

    # TODO: only user can delete after add user
    def test_title_delete_api(self):
        cat = Cat.objects.create(url='http://test_url.com')
        user = User.objects.create(username="test")
        title = Title.objects.create(cat=cat, user=user, content='test')
        title_id = title.id
        # delete_url = reverse('cat:title_list',
        #                      kwargs={'pk': title.id})
        # delete_url = reverse('cat:title_list', kwargs={'pk': title.id})
        response = self.client.delete('/api/v1/titles/1/')
        self.assertEqual(response.status_code, 201)
        self.assertFalse(Title.objects.filter(id=title_id).exists())

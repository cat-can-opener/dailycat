from http import HTTPStatus

from django.shortcuts import reverse
from rest_framework.test import APITestCase

from ..models import Cat, Title


# class TitleAPITestCase(APITestCase):
#     def test_title_list_api(self):
#         cat = Cat.objects.create(url='http://test_url.com')
#         for i in range(100):
#             Title.objects.create(cat=cat, content='test content')
#         list_url = reverse('cats:title-list', kwargs={'cat_pk': cat.id})

#         response = self.client.get(list_url)

#         self.assertEqual(response.status_code, HTTPStatus.OK)
#         self.assertEqual(len(response.data), 100)

#     def test_title_list_api_with_other_cats(self):
#         '''다른 cat의 title이 나오지 않는지 확인'''
#         cat = Cat.objects.create(url='http://test_url.com')
#         not_include_cat = Cat.objects.create(url='http://test_url_2.com')

#         for i in range(100):
#             Title.objects.create(cat=cat, content='test content')

#         for i in range(100):
#             Title.objects.create(cat=not_include_cat, content='test content')
#         list_url = reverse('cats:title-list', kwargs={'cat_pk': cat.id})

#         response = self.client.get(list_url)

#         self.assertEqual(len(response.data), 100)

#     # TODO: only user can create after add user
#     def test_title_create_api(self):
#         '''title 생성 api 테스트'''
#         cat = Cat.objects.create(url='http://test_url.com')
#         list_url = reverse('cats:title-list', kwargs={'cat_pk': cat.id})
#         test_content = 'test content'

#         response = self.client.post(list_url, data={
#             'content': test_content,
#         })

#         self.assertEqual(response.status_code, HTTPStatus.CREATED)
#         self.assertEqual(response.data['content'], test_content)

#     # TODO: only owner can update after add user
#     def test_title_update_api(self):
#         '''title update api test'''
#         cat = Cat.objects.create(url='http://test_url.com')
#         title = Title.objects.create(cat=cat, content='test')
#         updated_content = 'updated'
#         update_url = reverse('cats:title-detail', kwargs={'cat_pk': cat.id, 'pk': title.id})

#         response = self.client.patch(update_url, data={
#             'content': updated_content
#         })

#         self.assertEqual(response.status_code, HTTPStatus.OK)
#         self.assertEqual(response.data['content'], updated_content)

#     # TODO: only user can delete after add user
#     def test_title_delete_api(self):
#         cat = Cat.objects.create(url='http://test_url.com')
#         title = Title.objects.create(cat=cat, content='test')
#         title_id = title.id
#         delete_url = reverse('cats:title-detail', kwargs={'cat_pk': cat.id, 'pk': title.id})

#         response = self.client.delete(delete_url)

#         self.assertEqual(response.status_code, HTTPStatus.NO_CONTENT)
#         self.assertFalse(Title.objects.filter(id=title_id).exists())

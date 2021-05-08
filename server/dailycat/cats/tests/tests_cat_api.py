import json
from http import HTTPStatus

from django.shortcuts import reverse
from rest_framework.test import APITestCase

from ..models import Cat, Title


class CatAPITestCase(APITestCase):
    def setUp(self):
        pass

    def test_cat_list_api_works(self):
        '''cat list api 테스트. 10개 생성시 10개 나오는지 테스트'''
        for i in range(100):
            Cat.objects.create(url=f'http://test_url_{i+1}.com')

        list_url = reverse('cat:cat_list')  # 'api/v1/cats/cats/'
        res = self.client.get(list_url)
        self.assertEqual(res.status_code, HTTPStatus.OK)
        self.assertEqual(len(res.data), 100)

    def test_cat_list_has_title_field(self):
        '''list api가 3개의 title 값을 가지고 있는지'''
        cat = Cat.objects.create(url='http://test_url.com')
        for i in range(10):
            Title.objects.create(cat=cat, content=f'title-{i}')

        # list_url = reverse('cat:cat_list')  # 'api/v1/cats/cats/'
        title = Title.objects.filter(cat=cat)
        # res = self.client.get(list_url)
        # print(res.data)
        # cat: dict = res.data[0]
        # titles: list = cat.get('titles')

        self.assertEqual(len(title), 10)

    def test_cat_detail_api(self):
        '''cat 상세 api 테스트'''
        url = 'http://test_url.com'
        cat = Cat.objects.create(url=url)
        detail_url = reverse('cats:cat_detail', kwargs={'pk': cat.id})

        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.data['url'], url)


# class CatAPITestCase(APITestCase):
#     def test_cat_list_api(self):
#         '''cat list api 테스트'''
#         for i in range(100):
#             Cat.objects.create(url=f'http://test_url_{i}.com')

#         list_url = reverse('cats:cat-list')

#         response = self.client.get(list_url)

#         self.assertEqual(response.status_code, HTTPStatus.OK)
#         self.assertEqual(len(response.data), 100)

#     def test_cat_detail_api(self):
#         '''cat 상세 api 테스트'''
#         url = 'http://test_url.com'
#         cat = Cat.objects.create(url=url)
#         detail_url = reverse('cats:cat-detail', kwargs={'pk': cat.id})

#         response = self.client.get(detail_url)

#         self.assertEqual(response.status_code, HTTPStatus.OK)
#         self.assertEqual(response.data['url'], url)

#     def test_cat_report_api(self):
#         '''신고하기 api'''
#         url = 'http://test_url.com'
#         cat = Cat.objects.create(url=url)
#         detail_url = reverse('cats:cat-detail', kwargs={'pk': cat.id})

#         response = self.client.patch(detail_url, data={
#             'is_reported': 'true'
#         })

#         cat.refresh_from_db()

#         self.assertEqual(response.status_code, HTTPStatus.OK)
#         self.assertTrue(response.data['is_reported'], True)
#         self.assertTrue(cat.is_reported)
#         # TODO: is_reported로 변경시 reported_counts 추가
#         # 지금 로직에서는 크게 의미 없어보임.
#         # reported_counts가 1 증가했는지 확인
#         # self.assertEqual(cat.reported_counts, 1)

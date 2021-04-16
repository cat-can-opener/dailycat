from http import HTTPStatus

from django.shortcuts import reverse
from rest_framework.test import APITestCase

from ..models import Cat


class CatAPITestCase(APITestCase):
    def setUp(self):
        pass

    def test_cat_list_api(self):
        '''cat list api 테스트'''
        for i in range(100):
            Cat.objects.create(url=f'http://test_url_{i}.com')

        list_url = reverse('cats:cat-list')

        response = self.client.get(list_url)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(len(response.data), 100)

    def test_cat_detail_api(self):
        '''cat 상세 api 테스트'''
        url = 'http://test_url.com'
        cat = Cat.objects.create(url=url)
        detail_url = reverse('cats:cat-detail', kwargs={'pk': cat.id})

        response = self.client.get(detail_url)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.data['url'], url)

    def test_cat_report_api(self):
        '''신고하기 api'''
        url = 'http://test_url.com'
        cat = Cat.objects.create(url=url)
        detail_url = reverse('cats:cat-detail', kwargs={'pk': cat.id})

        response = self.client.patch(detail_url, data={
            'is_reported': 'true'
        })

        cat.refresh_from_db()

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTrue(response.data['is_reported'], True)
        self.assertTrue(cat.is_reported)
        # TODO: is_reported로 변경시 reported_counts 추가
        # 지금 로직에서는 크게 의미 없어보임.
        # reported_counts가 1 증가했는지 확인
        # self.assertEqual(cat.reported_counts, 1)

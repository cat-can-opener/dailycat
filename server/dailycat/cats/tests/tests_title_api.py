from http import HTTPStatus

from django.shortcuts import reverse
from rest_framework.test import APITestCase

from ..models import Cat, Title
# from ...users.models import User
from users.models import User


class TitleAPITestCase(APITestCase):
    def setUp(self):
        '''테스트가 시작할 때 해당 method 실행'''
        # self.TMP_DIR = tempfile.mkdtemp()
        self.cat = Cat.objects.create(image='http://test_url.com')
        self.user = User.objects.create(username="test")

    def tearDown(self):
        '''테스트가 종료 직전 해당 method 실행'''
        # shutils.rmtree(self.TMP_DIR)
        pass

    def _create_title(self) -> Title:
        '''create and return title object for test'''
        return Title.objects.create(
            cat=self.cat, content='test', user=self.user)

    def test_title_list_api(self):
        for i in range(100):
            Title.objects.create(
                cat=self.cat, content='test content', user=self.user)

        response = self.client.get('/api/v1/titles/?cat=1')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(len(response.data), 100)

    def test_title_list_api_with_other_cats(self):
        '''다른 cat의 title이 나오지 않는지 확인'''
        not_include_cat = Cat.objects.create(image='http://test_url_2.com')
        for i in range(100):
            Title.objects.create(
                cat=self.cat, content='test content', user=self.user)
        for i in range(100):
            Title.objects.create(cat=not_include_cat,
                                 content='test content', user=self.user)

        response = self.client.get('/api/v1/titles/?cat=1')

        title = Title.objects.filter(cat=self.cat)
        self.assertEqual(len(response.data), 100)
        self.assertEqual(title[0].cat.image.url, 'http://test_url.com')

    def test_title_create_api(self):
        '''title 생성 api 테스트'''
        list_url = reverse('cat:title_list')
        test_content = 'test content'

        self.client.force_authenticate(self.user)
        response = self.client.post(list_url, data={
            'content': test_content,
            'cat': self.cat.id,
            'user': self.user.id
        })

        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(response.data['content'], test_content)

    # TODO: only user can create after add user
    def test_title_create_api_401_without_login(self):
        '''title 생성 api 테스트: 로그인 안되어있을떄 401'''
        list_url = reverse('cat:title_list')

        test_content = 'test content'
        response = self.client.post(list_url, data={
            'content': test_content,
            'cat': self.cat.id,
            'user': self.user.id
        })
        self.assertEqual(response.status_code, HTTPStatus.UNAUTHORIZED)

    def test_title_update_api(self):
        '''title update api test'''
        title = Title.objects.create(
            cat=self.cat, content='test', user=self.user)
        updated_content = 'updated'

        self.client.force_authenticate(self.user)
        response = self.client.patch('/api/v1/titles/1/', data={
            'content': updated_content
        })

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.data['content'], updated_content)

    def test_title_update_api_401_without_login(self):
        '''title update api test'''
        title = Title.objects.create(
            cat=self.cat, content='test', user=self.user)
        updated_content = 'updated'

        response = self.client.patch('/api/v1/titles/1/', data={
            'content': updated_content
        })

        self.assertEqual(response.status_code, HTTPStatus.UNAUTHORIZED)

    def test_title_update_403_when_not_creator(self):
        # create title with self.user
        title = self._create_title()
        # create and login with other user
        other_user = User.objects.create_user(
            username='otherUser', password='password')
        self.client.force_authenticate(other_user)

        # as is
        response = self.client.patch('/api/v1/titles/1/', data={
            'content': 'updated'
        })
        # to be
        self.assertEqual(response.status_code, HTTPStatus.FORBIDDEN)

    def test_title_delete_api(self):
        title = Title.objects.create(
            cat=self.cat, user=self.user, content='test')
        title_id = title.id

        self.client.force_authenticate(self.user)
        response = self.client.delete('/api/v1/titles/1/')

        self.assertEqual(response.status_code, HTTPStatus.NO_CONTENT)
        self.assertFalse(Title.objects.filter(id=title_id).exists())

    def test_title_delete_api_401_without_login(self):
        title = Title.objects.create(
            cat=self.cat, user=self.user, content='test')
        title_id = title.id

        response = self.client.delete('/api/v1/titles/1/')

        self.assertEqual(response.status_code, HTTPStatus.UNAUTHORIZED)

    def test_title_delete_403_when_not_creator(self):
        # create title with self.user
        title = self._create_title()
        # create and login with other user
        other_user = User.objects.create_user(
            username='otherUser', password='password')
        self.client.force_authenticate(other_user)

        # as is
        response = self.client.delete('/api/v1/titles/1/')
        # to be
        self.assertEqual(response.status_code, HTTPStatus.FORBIDDEN)

    def test_title_delete_without_exists(self):
        self.client.force_authenticate(self.user)
        response = self.client.delete('/api/v1/titles/9999/')

        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_title_like_api_401_without_login(self):
        # /api/v1/titles/<pk>/like
        title = self._create_title()
        like_url = reverse('cat:like_title', kwargs={'pk': title.pk})
        # As is
        response = self.client.post(like_url, data={
            'like': True,
        })

        # TO be
        self.assertEqual(response.status_code, HTTPStatus.UNAUTHORIZED)


class TitleLikeViewTest(APITestCase):
    def setUp(self):
        '''테스트가 시작할 때 해당 method 실행'''
        # self.TMP_DIR = tempfile.mkdtemp()
        self.cat = Cat.objects.create(image='http://test_url.com')
        self.user = User.objects.create(username="test")
        self.title = self._create_title(self.cat, self.user)

        self.like_url = reverse('cat:like_title', kwargs={'pk': self.title.pk})

    def _create_title(self, cat, user) -> Title:
        '''create and return title object for test'''
        return Title.objects.create(
            cat=cat, content='test', user=user)

    def test_title_like_api_works_for_creator(self):
        '''title 생성자가 좋아요 누를 수 있는지 테스트'''
        creator = User.objects.create_user(
            username="test_user_for_like", password='test')
        # As is
        self.client.force_authenticate(creator)
        response = self.client.post(self.like_url, data={
            'like': 'true',
            # user: request.user
        })

        # To be
        self.assertEqual(response.status_code, HTTPStatus.OK)
        # M2M table에 creator/title을 가진 raw가 생성되었는지 -> creator.liked_title.all() -> [QuerySet <Title1>, <title2> ...]
        self.assertIn(self.title, creator.liked_titles.all())

    def test_title_like_api_without_like_data(self):
        '''like True가 안들어왔을때 400 error'''
        # as is
        self.client.force_authenticate(self.user)
        response = self.client.post(self.like_url)

        # To be
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_title_like_api_with_like_false(self):
        '''좋아요 눌렀던 유저가 좋아요 해제 되는지 테스트'''
        # 기존에 유저가 좋아요 누르기
        self.user.liked_titles.add(self.title)
        self.assertIn(self.title, self.user.liked_titles.all())
        # as is
        self.client.force_authenticate(self.user)
        response = self.client.post(self.like_url, data={'like': 'false'})
        # To be
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertNotIn(self.title, self.user.liked_titles.all())

    def test_title_like_api_with_like_false_without_like(self):
        '''좋아요 안 누른 유저가 좋아요 해제 api 요청했을떄 -> pass'''
        self.assertNotIn(self.title, self.user.liked_titles.all())
        # as is
        self.client.force_authenticate(self.user)
        response = self.client.post(self.like_url, data={'like': 'false'})
        # To be
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertNotIn(self.title, self.user.liked_titles.all())

    def test_title_like_api_with_like_true_with_already_like(self):
        '''좋아요 누른 유저가 좋아요 다시 좋아요 api 요청했을때 -> pass'''
        # 기존에 유저가 좋아요 누르기
        self.user.liked_titles.add(self.title)
        self.assertIn(self.title, self.user.liked_titles.all())
        # as is
        self.client.force_authenticate(self.user)
        response = self.client.post(self.like_url, data={'like': 'true'})
        # To be
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertIn(self.title, self.user.liked_titles.all())

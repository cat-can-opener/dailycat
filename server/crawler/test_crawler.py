from unittest import TestCase

from .cat_crawler import fetch_naver_image_html


class CrawlerTest(TestCase):
    def test_false(self):
        self.assertTrue(False)

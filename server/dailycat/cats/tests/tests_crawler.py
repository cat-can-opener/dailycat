from rest_framework.test import APITestCase

from cats.crawler import fetch_json_from_naver, download_image_from_url_to_s3

'''
psuedocode

NaverCrawler
     image_json = fetch image url json from naver
     image_urls: generator = parse_json_to_generator(image_json)
     for url in image_urls
        s3_url = download_from_url_s3(url)
        create cat from s3_url
end

parse_json_to_generator (get_image_urls)
    get
end

download_from_url_to_s3
    # url -> download -> memory -> s3_client
    response = download image from url with stream
    fileobj = make response to python memory file object format
    create Cat from file obj
end

fetch_json_from_naver
'''


class CrawlerTest(APITestCase):
    def test_download_from_url_to_s3(self):
        '''url을 memory에서 s3로 업로드'''
        url = 'https://newsimg.hankookilbo.com/cms/articlerelease/2019/04/29/201904291390027161_3.jpg'

        res = download_image_from_url_to_s3(url)

        # self.assertEqual(res.status_code, 200)
        # self.assertEqual(res.content, '')

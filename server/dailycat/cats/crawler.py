import requests
import json
from urllib.parse import unquote

from cats.models import Cat


def fetch_json_from_naver(query: str, start: int = 1, display: int = 200) -> str:
    '''네이버 이미지 주소를 갖는 text 반환'''
    url = f'https://s.search.naver.com/imagesearch/instant/search.naver?where=image&section=image&rev=31&res_fr=0&res_to=0&face=0&color=0&ccl=0&ac=0&aq=0&spq=1&query={query}&nx_search_query={query}&nx_and_query=&nx_sub_query=&nx_search_hlquery=&nx_search_fasquery=&datetype=0&startdate=0&enddate=0&json_type=6&nlu_query=&nqx_theme=%7B%22theme%22%3A%7B%22main%22%3A%7B%22name%22%3A%22people_ent%22%2C%22os%22%3A%2293959%22%2C%22pkid%22%3A%221%22%7D%7D%7D&start={start}&display={display}'
    res = requests.get(url)
    # TODO: error handling
    return res.text


def get_image_urls(txt: str) -> list:
    '''
    이미지 주소를 갖는 텍스트에서 이미지 url만 추출 후 unquote
    Should need O(n)
    '''
    # TODO: json parsing
    result: dict = json.loads(txt[3:-4])
    items = result['items']
    return [
        unquote(item['originalUrl']) for item in result['items']
    ]


def download_image_from_url_to_s3(url: str):
    '''
    url에서 이미지를 stream으로 memory에 올린 후에
    해당 메모리를 s3 버킷에 업로드
    - s3 upload -> boto3
    '''
    res = requests.get(url, stream=True)
    # # validate res -> 200

    # with open('filename', 'w') as f:
    #     f.write(fileobj)
    # fileobj = BytesIO()
    # fileobj.write(res.content)

    # Cat.objects.create(
    #     image
    # )

    # img = PImage.open(StringIO(res.content))
    # return img

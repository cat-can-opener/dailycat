import requests
import json
from urllib.parse import unquote

# import ipdb
# from bs4 import BeautifulSoup as bs
# from urllib.request import urlopen
# from urllib.parse import quote_plus
# import urllib

'''
- fetch json
- find originalUrl -> make list
- download from list

# 고려해야될점

- 동기/비동기
- 런타임
- 시기?
'''


def fetch_json_from_naver(query: str, start: int = 1, display: int = 200) -> str:
    '''네이버 이미지 주소를 갖는 text 반환'''
    url = f'https://s.search.naver.com/imagesearch/instant/search.naver?where=image&section=image&rev=31&res_fr=0&res_to=0&face=0&color=0&ccl=0&ac=0&aq=0&spq=1&query={query}&nx_search_query={query}&nx_and_query=&nx_sub_query=&nx_search_hlquery=&nx_search_fasquery=&datetype=0&startdate=0&enddate=0&json_type=6&nlu_query=&nqx_theme=%7B%22theme%22%3A%7B%22main%22%3A%7B%22name%22%3A%22people_ent%22%2C%22os%22%3A%2293959%22%2C%22pkid%22%3A%221%22%7D%7D%7D&start={start}&display={display}'
    res = requests.get(url)
    # TODO: error handling
    return res.text


def get_image_urls(txt: str) -> list:
    '''이미지 주소를 갖는 텍스트에서 이미지 url만 추출 후 unquote'''
    # TODO: json parsing
    result: dict = json.loads(txt[3:-4])
    items = result['items']
    return [
        unquote(item['originalUrl']) for item in result['items']
    ]


def download_image_from_url(url: str) -> None:
    '''
    url에서 이미지를 stream으로 memory에 올린 후에
    해당 메모리를 s3 버킷에 업로드
    - s3 upload -> boto3
    '''
    pass


txt = fetch_json_from_naver('망한고양이대회')
li = get_image_urls(txt)
print(len(li))
print(li)

# url = 'http://blogfiles.naver.net/MjAyMTA0MTJfNTQg/MDAxNjE4MTYwODE3NjEw.PvTd0-yfPO2DLC7vCNKGyncjRlyRFk9VHOvLjPPK9WYg.oEGa3Ahw_EHpnNRw8iilLdKcd8UgcTsnLTchIdPYXcwg.JPEG.oooooooone/1.jpg'

# baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
# # plusUrl = input('검색어 입력: ')
# # crawl_num = int(input('크롤링할 갯수 입력(최대 50개): '))
# plusUrl = '고양이'
# crawl_num = 5

# url = baseUrl + quote_plus(plusUrl)
# # 한글 검색 자동 변환
# html = urlopen(url)
# # print(html.read().decode('utf-8'))
# soup = bs(html, "html.parser")

# img = soup.find_all(attrs={"class": "_image _listImage"})
# ipdb.set_trace()
# print(img)

# print(len(img))

# n = 1
# for i in img:
#     print(n)
#     imgUrl = i['data-source']
#     with urlopen(imgUrl) as f:
#         with open('./images/img' + str(n)+'.jpg', 'wb') as h:  # w - write b - binary
#             img = f.read()
#             h.write(img)
#     n += 1
#     if n > crawl_num:
#         break


# print('Image Crawling is done.')

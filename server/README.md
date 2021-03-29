# dailycat project backend dir


## Stack information

- python 3.9.0
- django
- django-rest-framework


## 0. local runserver


```
# set env for credentials
# Have to get env file in slack
cd dailycat

$Env:DJANGO_SECRET_KEY = "$-d!3tcn6q4-ot^_6lp992=7xlpvu6hk3zg6f@bd(_@sn))3g@"
source .env

# Check if env is setup (in linux)
echo $DJANGO_SECRET_KEY

# In windows
echo %DJANGO_SECRET_KEY%
set DJANGO_SECRET_KEY

# install requirements
pip install -r requirements/local.txt

# migrate if needed
python manage.py migrate --settings=dailycat.settings.local

# runserver with local setting
python manage.py runserver 8080
```

만약 매번 local setting 지정하는게 귀찮다면 환경변수를 설정해서 사용하면 됩니다.

```
# set local setting env
export DJANGO_SETTINGS_MODULE=dailycat.settings.local
# in windows
$Env:DJANGO_SETTINGS_MODULE = "dailycat.settings.local"
```

django-rest-framework
RESTFul API


## 03/29

- [x] cats 앱 생성
- [x] 모델 파일 생성

### 모델 만들어 오기
- cat: cat, title, comment

Cat model
- url: ??? (https://...)
- created: ??? (yyyy-mm-dd HH:MM::SS)
- expose_date: (yyyy-mm-dd)

Title
- comment: max 255
- cat: related (required, cascade)

Comment
- content: max 255
- title: related (required, cascade)


(-> python manage.py makemigrations) -> migrate

[image](https://trello-attachments.s3.amazonaws.com/6056bc833756992d9db950b8/1005x839/344c64e4144939c2167486405cefb891/image.png)


### api design

> RESTFul API

api schema
[docs](https://www.django-rest-framework.org/api-guide/views/)
- views, generic views, viewsets
- serializers

- GET /cats/ -> 사진 리스트 (/cats/?mypage=true)
- GET /cat/1/: title (투표수), 사진url
- GET /cat/1/titles/
- GET /cat/1/titles/1/comments/

- PATCH /cat/1/titles/1/  -> title 좋아요
- PATCH /cat/1/ -> 고양이 좋아요
- PATCH /cat/1/ -> 고양이 신고하기?
- POST /login/

### crawler design
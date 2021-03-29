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


## 03/29

- [x] cats 앱 생성
- [x] 모델 파일 생성

### 모델 만들어 오기
- cat: cat, title, comment
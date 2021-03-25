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
source .env

# install requirements
pip install -r requirements/local.txt

# migrate if needed
python manage.py migrate --settings=dailycat.settings.local

# runserver with local setting
python manage.py runserver --settings=dailycat.settings.local
```

만약 매번 local setting 지정하는게 귀찮다면 환경변수를 설정해서 사용하면 됩니다.

```
# set local setting env
export DJANGO_SETTINGS_MODULE=dailycat.settings.local
```




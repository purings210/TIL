# web

- 고객은 서버로 요청을하고, 서버는 요청을 받아서 응답을 한다.

- Django로 하는것은 서버에서 어떻게 요청받은걸 가공해서 응답하는지!

- url -> view -> template 순서의 흐름이며 완성된 template을 사용자에게 보여준다.



## 1. Django 프로젝트 설정하기

- 폴더생성 - git bash - django-admin startproject <프로젝트이름> .

- 프로젝트 생성을하고 -> 앱을 생성한다(보통 articles라는 이름으로 많이 사용한다.)
  - python manage.py startapp articles
    - 위의 명령어를 실행하면 articles라는 폴더가 생성된다.
    - 만들고나면 처음만들었던 폴더이름안의 settings.py에서 "나 앱을 만들었어!" 라고 알려줘야한다.
    - installed_apps 안에 써줘야된다, 가장 위에다 쓰는게 관례

```django
INSTALLED_APPS = [
    'articles',  
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```



- urls.py로 이동

- urlpatterns = 출입구 이자 이정표이다.

- path와 view함수의 이름은 통일시키자!

- path가 index라면 views함수이름도 index로!

- 가져올때는 import해주기

```django
from articles import views
```

- views.py에서 함수를 만들때 첫번째 인자는 무조건 request로
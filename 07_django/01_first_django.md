# Django 시작

## First req - res cycle

### App 생성

```sh
$ pwd 
/home/ubuntu/workspace/
$ mv first_django FIRST_DJANGO
$ cd FIRST_DJANGO
$ django-admin startapp home # home app 생성
```

### Django 프로젝트에 App 등록

**지금부터 pwd 는 `FIRST_DJANGO/` 에서 진행**

`first_django/settings.py`

```python
...
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home', # django-admin startapp 으로 생성한 app 등록! 주민등록과 같다
]
...
```

`home/views.py`

```python
from django.shortcuts import render, HttpResponse # HttpResponse 추가

# Create your views here.
def index(request):
    return HttpResponse('HappyHacking')
```

요청이 들어왔을 때 실행할 함수를 정의한다. 그런데 어떤 요청이랑 매칭할지를 명시하지 않았다. 이 명시는 우선 최상단 관리자한테 넘긴다.

`first_django/urls.py`

```python
# Comments ...
from django.contrib import admin
from django.urls import path
# home 디렉토리에서 views.py 를 import
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index) # root url 로 접속시, views.index 실행!
]
```

### Variable Routing

방금의 루틴을 기억하며 req-res cycle 을 추가해 보자.

`first_django/urls.py`

```python
# Comments ...
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
  	path('hello/', ) # 아직 실행할 함수 정의 안했음!
]
```

`home/views.py`

```python
from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('HappyHacking')
    
def hello(request):
    return HttpResponse("Hello")
```

`first_django/urls.py`

```python
# Comments ...
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
  	path('hello/', views.hello),
]
```

여기에 variable 라우팅을 추가해 보자.

```python
# Comments ...
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
  	path('hello/<name>', views.hello),
]
```

`home/views.py`

```python
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('HappyHacking')
    
def hello(request, name): # 인자로 name 을 받아오게 된다!
    return HttpResponse("Hello " + name)
```



## Render HTML

### pure html

`/about` 페이지로 사용자가 접속했을 경우에, 이제는 정식 html 문서를 보여주도록 하자. 우선 새로운 URL path 를 추가해 주자.

`first_django/views.py`

```python
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('hello/<name>', views.hello),
    path('about/', views.about), # 추가
]
```

이전과 마찬가지로 `home/views` 의 `about()` 메서드와 연결했기 떄문에, 해당 함수를 정의하자. 다만, 이전처럼 `HttpResponse` 메서드가 아닌, 기본으로 제공해주는 `render` 함수를사용한다!

```python
from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('HappyHacking')
    
def hello(request, name):
    return HttpResponse(name)

# 추가
def about(request):
    return render(request, 'about.html')
```

`render` 함수는 `HttpResponse` 와 달리, 내용만 넘기는 것이 아니라, `request` 와 우리가 보여줄 html 파일 이름을 같이 넘겨줘야 한다. 현재 우리에게는 어떠한 html 파일도 없기 때문에, `about.html` 을 만들어서 내용을 채워보자.

```sh
$ pwd
/home/ubuntu/workspace/FIRST_DJANGO
$ mkdir home/templates
$ touch home/templates/about.html
```

우리는 앞으로 모든 사용자가 받아볼 화면, 즉 html 은 각 app 의 `templates/` 에 저장하도록 할 것이다. 그런데 django 는 우리가 이런 결심을 한 사실을 모르기 때문에, 알려줘야 한다!

`first_django/settings.py`

```python
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# templates 상수 설정
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

# ...

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home', # django-admin startapp 으로 생성한 app 등록! 주민등록과 같다
]

# ... 

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR], # templates dir 을 등록 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ...

LANGUAGE_CODE = 'en-us' # 'ko-kr

TIME_ZONE = 'UTC' # 'asia/seoul'

# ...
```

이제부터 우리가 `render` 를 실행하려 할때마다, django 는 모든`templates/` 를 뒤진다.  이때 당연히, 각 app 마다 `templates/` 디렉토리가 생기게 되는데, 같은 이름의 html 이 존재할 경우, app definition 에 정의된 순서대로 뒤지기 때문에 의도하지 않은 html 이 render 될 수 있다. 지금은 신경쓰지 말자.

`home/templates/about.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>about</title>
</head>
<body>
    <h1>About Page</h1>
    <p>
        This is about page
    </p>
</body>
</html>
```

---

똑같은 방법으로 `home.index` 와 `home.hello`도 html 을 보여주도록 바꿔보자.

```sh
$ touch home/templates/index.html
$ touch home/templates/hello.html
```

`first_django/urls.py` 는 이미 path 가 존재하므로 pass

`home/views.py`

```python
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def hello(request, name):
    # not yet
    
def about(request):
    return render(request, 'about.html')

```

`home/templates/index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Home</title>
</head>
<body>
    <h1>This is <strong>/</strong> path</h1>
    <p>
        Hi!
    </p>
</body>
</html>
```



## DTL(Django Template Language)

### 템플릿 변수(template variables): `{{ }}`

Good! 그렇다면 `home.hello` 에서 path 에 포함되어 오는 `name` variable 을 템플릿 html 에서 사용하는 법을 알아보자!

`home/views.py`

```python
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def hello(request, name):
    return render(request, 'hello.html', { 'name': name })    
    
def about(request):
    return render(request, 'about.html')

```

슬슬 `render()` 의 인자가 많아지고 있다. 이것만 기억하자

1. 무조건 첫번째 인자는 `request`
2. 두번째 인자는 `templates/` 안에서 꺼낼 html 파일 이름
3. 그 외에 html 파일에서 사용할 변수는 dict 로

`home/templates/hello.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Hello</title>
</head>
<body>
    <h1>Hello, {{ name }}</h1>
</body>
</html>
```

Jinja2 와 비슷해 보이지만, 현재 사용중인 문법은, DTL 이라고 하는 문법이다. 우선 `views.py` 에서 3번째 인자로 넘긴 dict 의 key 를 호출하면, 해당 value 가 출력된다. `{{ key }}`  => Value

### 템플릿 태그(template tags): `{% %}`

#### 반복 `for`

현재는 단순하게 출력만 하고 있다. 조금 더 프로그래밍적 요소들을 가미해 보자.

`home/views.py`

```python
# ...
def hello(request, name):
    hackers = [
        'neo',
        'tak',
        'change',
        'john',
        'zzulu',
    ]
    return render(request, 'hello.html', { 'name': name, 'hackers': hackers })
# ...
```

`home/templates/hello.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Hello</title>
</head>
<body>
    <h1>Hello, {{ name }}</h1>
    <ul>
        {% for hacker in hackers %}
             <li>{{ hacker }}</li>   
        {% endfor %}
    </ul>
</body>
</html>
```

기존 python `for` 문과 살짝 다르지만, 크게 이해하는데 무리는 없다. (*`while` 은 없다. python 의 모든 문법이 1:1 로 존재하지 않는다.*)

#### 조건 `if`

이번에는, 만약 path 에 포함된 이름이 `hackers` 에 있다면, 해당 이름을 굵게 보여줄 예정이다.

`home/templates/hello.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Hello</title>
</head>
<body>
    <h1>Hello, {{ name }}</h1>
    <ul>
        {% for hacker in hackers %} 
             {% if name == hacker %}
                 <li><strong>{{ hacker }}</strong></li>
             {% else %}
                 <li>{{ hacker }}</li>
             {% endif %}
        {% endfor %}
    </ul>
    
</body>
</html>
```

이번에도 살짝 기존 python 문법과 다르지만, 크게 달라지지는 않았다. **다만 반드시 주의할 점 중에 하나는 `if` 문 뒤에 비교연산자(`==`)가 띄어쓰기가 없으면, error 가 난다!**  비단 DTL 을 위해서 뿐만 아니라, 코드에서도 가능하면 연산자는 띄어쓰기!

### 템플릿 상속(template inheritance): `{% extends <filename> %}`

현재 모든 html 파일들이 `<!DOCTYPE html>` 부터 시작하는 중복되는 마크업 코드들이 있다. 중복을 제거해 보자!

```sh
$ touch home/templates/home_base.html
```

각 app 에서 사용할 베이스 템플릿 파일은 app 의 이름을 포함하여 이름짓도록 하자. 이름이 겹치면 의도하지 않은대로 동작한다.

현재 `<title>` 과 `<body>` 안의 내용만 다르다! 이렇게 다르게 사용할 내용들을 교체 가능하도록 만들어 보자.

`home/templates/home_base.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
    {% block content %}
    {% endblock %}
</body>
</html>
```

이제 빈칸은 뚫었으니, 기존 html 파일들에서 맞는 빈칸에 내용을 채우기만 하면 된다!

`home/templates/index.html`

```html
{% extends 'home_base.html' %}

{% block title %} Home {% endblock %}

{% block content %}
    <h1>This is root path</h1>
    <p>
        Hi!
    </p>
{% endblock %}
```

`home/templates/about.html`

```html
{% extends 'home_base.html' %}

{% block title %} About {% endblock %}

{% block content %}
    <h1>About Page</h1>
    <p>
        This is about page
    </p>
{% endblock %}
```

`home/templates/hello.html`

```html
{% extends 'home_base.html' %}

{% block title %} Hello {% endblock %}

{% block content %}
    <h1>Hello, {{ name }}</h1>
    
    <ul>
        {% for hacker in hackers %} 
             {% if name == hacker %}
                 <li><strong>{{ hacker }}</strong></li>
             {% else %}
                 <li>{{ hacker }}</li>
             {% endif %}
        {% endfor %}
    </ul>
{% endblock %}
```

반드시 빈칸과 채워넣는 이름(`{% bloack <NAME> %}`)을 매치시켜야 한다! 매치되지 않는다고 에러가 나지 않고 빈칸이 나타나기에 디버깅이 힘들다.

---

## Advance App

### 개발 계획(명세)

1. app 이름: `utilities` (복수형 convention)
2. `utilities/views.py` 함수들
   1. `views.index`
   2. `views.jackpot`
   3. `views.forecast`
   4. `views.stock_input`
   5. `views.stock_result`
3. url
   1. `utilites/`
   2. `utilities/jackpot/<drw_no>`
   3. `utilities/forecast/`
   4. `utilities/stock_input/`
   5. `utilities/stock_result/`
4. `utitities/templates`
   1. `base.html`
   2. `index.html`
   3. `jackpot.html`
   4. `forecast.html`
   5. `stock_input.html`
   6. `stock_result.html`

---

```sh
$ django-admin startapp utilites
```

우선 app을 만들었다. 태어났으니 주민등록부터!

`first_django/settings.py`

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'utilites',
]
```

이제 `views.<FUNCTION_NAME>`  들과 매칭할 templates 를 만들자.

```sh
$ mkdir utilites/templates
$ cd utilities/templates/
$ touch utilites_base.html index.html jackpot.html forecast.html stock_input.html stock_result.html
$ cd -
```

그리고, `views` 에서 각 함수들과 템플릿을 연결하자.

`utilities/views.py`

```python
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def jackpot(request, drw_no):
    return render(request, 'jackpot.html', { 'drw_no': drw_no })
    
def forecast(request):
    return render(request, 'forecast.html')
    
def stock_input(request):
    return render(request, 'stock_quote.html')
    
def stock_result(request):
    return render(request, 'stock_result.html')
```

html 은 현재 신경쓰지 않겠다. 중요한 건, 현재 라우팅을 어떻게 처리할 것인가 이다.

### URL 설정 분리하기 (Including another URLonf)

우선 최상단 app 의 `urls.py` 에 우리가 추가로 url path 를 사용할 것이라고 명시해야 한다.  (사실 주석에 사용법이 나와 있다)

`first_django/urls.py`

```python
from django.contrib import admin
from django.urls import path, include # include 함수 import
from home import views # 구림..

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('hello/<name>', views.hello),
    path('about/', views.about),
    path('utilities/', include('utilities.urls')) # 추가
]
```

`path()` 함수의 첫번째 인자로, path 의 공통분모를 작성한다. 그리고 기존에는 바로 `views.<FUNCTION_NAME>` 으로 접근했지만, 이제는 `include()` 함수에 `''<APP_NAME>.urls'` 를 반드시 **str** 로 입력해 줘야 한다. 이제 `utilites` App 과 관련된 모든 path  는 `utlities/urls.py` 에 작성할 것이다. 

훨씬 편리하다. 특정 app 에 대한 path 설정은 해당 app dir 안의 파일 설정에서 끝나기 때문이다. 또한, app 이 추가될 때마다 최상단 `urls.py` 에 매핑할 view 를 import 할 필요도 없다.

그런데 정작 `utilites` app 에는 `urls.py` 가 없다. 만든다. (`urls.py` 파일 이름은 convetion)

```sh
$ touch utilites/urls.py
```

`utilites/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('jackpot/<drw_no>', views.jackpot),
    path('forecast/', views.forecast),
    path('stock_input/', views.stock_input),
    path('stock_result', views.stock_result),
]
```

기본 틀은 매우 유사하다.  `django.urls` 모듈에서 `path` 함수를 가져오고, 현재 위치(`.`)에 있는 `views.py` 파일을 import 했다. 남은건 이전과 마찬가지로, `path()` 함수를 통해 url 패턴과 views 에 작성한 함수를 매핑하기만 하면 된다. 

다만 주의할 점은, 최상단 app 의 `urls.py` 에 작성한시작 url 패턴이 앞에 자동으로 붙어있다는 것을 잊지 말자. 현재같은 경우에는 무조건 url 패턴 맨 앞에 `utilites/` 가 붙는다.

#### home 도 url 분리하기!

같은 과정을 통해 현재 `home` app 에서 사용되고 있는 path 들도 분리하자! 우선 앞으로 app 을 `startapp` 으로 생성하면, 바로 해당 app 디렉토리안에 `urls.py` 를 만들도록 하는것도 좋은 방법이다.

```sh
$ touch home/urls.py
```

생성된 `urls.py` 파일에 import 구문과 `urlpatterns` 를 정의하도록 하자.

`home/urls.py`

```python
from django.urls import path
from . import views
urlpatterns = [
		path(''),
  	path('hello/<name>')
  	path('about/')
]
```

혹시 `path` 에 url 패턴은 적었지만, 매핑해야하는 `views` 의 함수가 기억나지 않는다면? 보면 된다!

`home/views.py`

```python
from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'index.html')
    
def hello(request, name):
    return render(request, 'hello.html', { 'name': name })    
    
def about(request):
    return render(request, 'about.html')
```

`home/urls.py`

```python
from django.urls import path
from . import views
urlpatterns = [
		path('', views.index),
  	path('hello/<name>', views.hello),
  	path('about/', views.about),
]
```

이걸로 끝? 아니다! 기존의 최상단 app 에 작성한 url패턴들을 수정하고, 이제부터 `home`  app 의 라우팅(`/` 로 시작하는 url패턴들!)은 모두 `home/urls.py` 가 담당할 것이라고 알려줘야한다.

`first_django/urls.py`

```python
from django.contrib import admin
from django.urls import path, include
# from home import views => 얘도 이제 직접 import 할 필요 없다!

urlpatterns = [
    path('admin/', admin.site.urls),
		path('', include('home.urls')),
    path('utilities/', include('utilities.urls')),
]
```



### views - templates 완성하기 + 이름 다른거
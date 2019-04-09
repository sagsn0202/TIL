# Django Model

## ORM

(거의) 모든 응용프로그램은 데이터를 저장한다.  데이터의 저장을 위해 존재하는 특화 프로그램이 DBMS 며, Django 역시 매우 편리한 데이터 베이스 연동을 지원하며, 프로젝트 생성시 별도의 설정이 없으면 경량형 RDBMS 인 Sqlite3 를 사용하게 되어 있다.

DB는 기본적으로 SQL(Structed Query Language) 을 통해 조작하나, Django 는 python 만으로 DB 조작이 가능하다. Django 뿐만 아니라 대부분의 언어와 프레임워크들은 언어에서의 객체와 RDBMS 에서의 데이터 레코드를 매핑해주는 ORM(Object Relational Mapper) 를 지원한다. Python 에서 사용가능한 여러 ORM들이 존재하지만 (SQLAlchemy, Peewee, SQLObject etc..) 우리는 장고에 특화되어 있는 Django ORM 을 사용할 것이다. Django ORM 은 이름부터 Django에서 사용하기 위해 만들어 졌으며, Django 프로젝트 생성시 자동으로 포함되어 있는 ORM 이다.

ORM 의 가장 큰 장점은, DB 조작을 위해 추가로 SQL 을 학습하지 않아도 된다는 점이며, 추가적으로 각 RDBMS 마다 다르게 지원하는 자료형이나 기능들을 신경쓰지 않고 같은 명령어로 여러 RDBMS 를 조작 가능하다는 것이다. 

>  정리하자면, 우리는 SQL 을 사용하지 않고 Django 가 내장지원하는 The Django ORM 을 사용하여 DB를 조작하고 데이터를 관리할 것이다.

## DB

기타 다른 DB(MySQL, PostgreSQL, etc..) 들과 달리, SQLite3 는 DB 구동을 위한 DB서버 사전작업이 필요 없다. (물론 배포할 때, 다른 DB 를 사용한다면 그때는 DB 서버 세팅을 해야한다!)  때문에 우리는 바로 DB 조작의 시작인 테이블 생성부터 시작할 수 있다.

### Django DB setting

`first_django/settings.py`

```python
...

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

...
```

다른 DB 를 사용하려면, `.sqlite3` 부분을 바꾸면 된다. 이때는 DB 서버와 접속하기 위해 추가 설정이 필요하다. 자세한 내용은 [공식문서](https://docs.djangoproject.com/ko/2.1/ref/settings/#std:setting-DATABASES) 참조

```python
'django.db.backends.sqlite3'
'django.db.backends.postgresql'
'django.db.backends.mysql'
'django.db.backends.oracle'
... etc
```

### DB Modeling 1

DB 모델링의 시작은 생성 하는 테이블들의 스키마를 계획하는 것 부터다. 우리가 이제부터 생성할 테이블의 스키마는 다음과 같다.

`Bands`

| Name        | Datatype        |            |                  |
| ----------- | --------------- | ---------- | ---------------- |
| id          | Integer         | PK         | Auto Increment   |
| name        | Text ( < 50)    | NOT NULL   |                  |
| debut       | Integer         | NOT NULL   | Default 2019     |
| is_active   | Boolean         | NOT NULL,  | Default `True`   |
| description | Text (no limit) | Null-able? | Default `'....'` |

밴드들의 이름과 데뷔년도, 그리고 현재 활동중인지를 저장하는 테이블이다. 바로 테이블 생성을 해보자.

## Create first table

### Model 작성

독립적인 설정을 위해 새로운 App 을 생성하고 시작하자. 

```sh
$ django-admin startapp bands
```

app 이 태어나면? 등록부터

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
  	'bands',
]
```

Django 의 MTV(Model - Template - View) 모델에서 데이터의 관리는 Model 이 책임진다! 

`bands/models.py`

```python
from django.db import models

# Create your models here.
```

`models` 모듈만 단촐하게 import 되어 있고, 나머지는 알아서 하라고 써있다. 테이블 생성을 위한 스키마 정의를 해보자.

`bands/models.py`

```python
from django.db import models

class Band(models.Model):
    name = models.CharField(max_length=50)
    debut = models.IntegerField()
    is_active = models.BooleanField(default=True)
    description = models.TextField( default='No description yet')
```

매우 직관적인 코드다. 다만 한가지 주의해야 할 점은 아직 우리가 작성한 코드나 Django 에게 내린 명령중 그 어떤것도 DB 에 영향을 주지 않았다. 현재 우리 DB 에는 어떠한 테이블도 존재하지 않는다. 우리는 

* `class ModelName(models.Model)`

  보다시피 Django ORM 에서 확정될 스키마 준비는 클래스의 선언으로 시작한다. 모델 뿐만 아니라, 모든 클래스가 그렇듯, 단수형으로 선언한다. 모든 Model 클래스들은  Django 가 제공하는 `django.db` 의 `models.Model` 클래스를 상속받는다. 이를 통해  `Band` 클래스의 객체들이  DB 조작에 필요한 모든 메서드들을 물려받는다.

* `attribute = models.FieldName(**kwargs)`

  각 컬럼의 이름을 클래스 멤버변수로 설정하고, 해당 컬럼에 저장될 DataType 과 매칭되는 필드의 객체를 변수에 할당한다. 말이 복잡하지만, 간단하게 변수에 저장될 자료형을 미리 설정한다고 생각하면 된다. 각 줄의 코드를 살펴보면 이해가 훨씬 쉬울것이다.

  * `models.CharField(max_length=50)`

    `CharField` 의 객체는 문자열을 저장하지만, 반드시 최대길이(`max_length`) 를 지정해 주어야 한다. 이는 RDBMS 의 VARCHAR 와 대응한다.

  * `models.IntegerField(default=datetime.todaty().year)`

    `IntegerField` 의 객체는 일반적인 정수를 의미한다. 정수/실수 관련한 다른 다양한 필드들이 존재하지만 우선 가장 많이 쓰이는 필드를 사용하자. 

  * `models.BooleanField(default=True)`

    `BooleanField` 는 참/거짓값을 저장한다. `default=` 을 통해 기본값을 `True` 로 주었다.

  * `models.TextField(...)`

    `TextField` 의 객체는 `CharField` 와 달리 길이를 지정해 주지 않아도 된다. 다만 `CharField` 최대 길이를 확정할 수 있는 경우에는 `CharField` 를 사용하고, 그게 아니라면 `TextField` 를 사용하자. `TextField` 와 `CharField` 의 물리적 한계는 사용하는 RDBMS 에 따라 다르다.

이것보다 훨씬 다양한 종류의 필드가 존재하지만, 우선 가장 많이 사용하는 필드들만 사용했다. 거듭 말하지만, 우리가 모델(`models.py`)에 작성한 코드는 DB 에 어떠한 영향도 주지 않았다. 그저 Django 안에서 사용할 클래스를 선언했을 뿐이다. 

### Make Migration

이제 전혀 다른 두 세계(python - DB)를 연결하기 위한 사전 준비가 필요하다. `INSTALLED_APPS` 에 우리 App(`bands`)을 등록한걸 확인하고, 다음과 같이 입력한다.

```sh
$ python manage.py makemigrations bands
Migrations for 'bands':
  bands/migrations/0001_initial.py
    - Create model Band

```

만약 `INSTALLED_APPS` 에 등록해놓지 않았다면 매니저가 `bands` 를 인식하지 못한다. 코드에 오타가 없고, 제대로 진행되었다면, 위와 같은 결과 메세지가 나타난다.

우선 `bands/migrations/0001_initial.py` 라는 파일이 생성되었다고 나타난다. 그리고 아래에 비로소 `Band` 라는 모델을 생성했다는 메세지를 확인할 수 있다. 즉 `makemigrations` 명령어를 입력하기 전까지 우리가 `models.py` 에 선언한 클래스는, 우리가 single python 파일에 연습용으로 작성하는 클래스와 전혀 차이가 없었던 것이다. 

> ` models.py` 에 작성한 클래스는 `makemigration` 명령어를 통해야지만 Model이 된다.

그렇다면 이제 ` bands/migrations/0001_initial.py` 파일을 살펴보자.

` bands/migrations/0001_initial.py`

```python
# Generated by Django 2.1.5 on 2019-01-23 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('debut', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('description', models.TextField(default='No description yet')),
            ],
        ),
    ]
```

복잡한 내용들이지만, 한가지만 확인하자. 스키마에서 정의하고, 모델에서 언급하지 않은 `id` 컬럼이 자동으로 추가되어 있고, PK 로 설정되어 있다. Django ORM 에서  id 는 자동할당 된다. 

`debut` 와 `description` 은 고정값으로 설정되어 있다.

### Migrate!!!

하지만 아직도 DB 에는 어떤 영향도 없다.  마이그레이션 파일은 테이블 생성을 위해 Django 가  `models.py` 를 해석하고 알아서 생성해 준 최종 결재 서류다. 이 최종 결재 서류가 SQL 로 번역되어 우리대신 DB 에 테이블을 생성해 줄 것이다. 번역될 SQL 을 확인해 보려면 다음과 같이 명령어 뒤에 app 이름과 서류 번호를 입력한다. 

```sh
$ python manage.py sqlmigrate bands 0001
```

결재를 받으러 가자.

```sh
$ python manage.py migrate
```

OK 가 나타났다면, 결재가 완료되고 DB 에 우리가 의도한 대로 테이블이 생성되었을 것이다.

### Reset DB

앞으로 계속 테이블을 생성해 나가게 될 것이다. 그에 앞서 Django 에서 DB reset 관련 명령어들을 미리 살펴보고자 한다.

* DB 에 존재하는 모든 데이터 레코드를 삭제한다.

  ```sh
  $ python manage.py sqlflush
  ```

* 특정 App 의 모든 데이터 레코드를 삭제한다.

  ```sh
  $ python manage.py sqlflush <APP_NAME>
  ```

* 특정 App 의 모든 테이블을 삭제한다.

  ```sh
  $ python manage.py migrate <APP_NAME> zero
  ```

## CRUD operation via Django Shell

```sh
$ python manage.py shell
>>>
```

이제부터 Django 프로젝트 한가운데에서 실시간 작업을 진행할 수 있다.

```python
>>> from bands.models import Band

>>> b = Band(name='Queen')
>>> b.save()
...
django.db.utils.IntegrityError: NOT NULL constraint failed: bands_band.debut
```

일부러 언급하지 않았던 사실 중 하나가 바로 스키마에서 작성한 NOT NULL 에 대한 내용이다. Django Model 은 아무 언급이 없으면 기본적으로 해당 필드를 NOT NULL 로 생성한다. 거꾸로 NULL 을 가능하게 하려면, `(null=True)` 라고 옵션을 추가해야 한다.

```python
>>> b = Band(name='Queen', debut=1973)
>>> b.save()
>>> b.name
'Queen'
>>> b.debut
1973
>>> b.description
'No description yet'
>>> b.is_active
True
>>> b
<Band: Band object (1)>
```

엄청나게 직관적인 코드를 통해 DB 에 레코드를 저장할 수 있게 되었다! 다만 `b` 를 입력했을 때 나오는 정보가 너무 부족하다. Model 코드를 수정해보자.

`bands/models.py`

```python
from django.db import models

class Band(models.Model):
    name = models.CharField(max_length=50)
    debut = models.IntegerField()
    is_active = models.BooleanField(default=True)
    description = models.TextField( default='No description yet')
    
    def __str__(self):
      return f'{self.id}: {self.name}'
```

Shell 을 끄고 다시 실행해 보자.

```python
>>> from bands.models import Band
>>> Band.objects.all()
<QuerySet [<Band: 1: Queen>]>
>>> Band.objects.filter(id=1)
<QuerySet [<Band: 1: Queen>]>
>>> Band.objects.filter(name__startswith='Qu')
<QuerySet [<Band: 1: Queen>]>
>>> Band.objects.get(id=1)
<Band: 1: Queen>
```

## Django Admin Page

장고가 정말 강력한 점 중에서 하나는 다름아닌, Django 의 관리자 페이지다.

```sh
$ python manage.py createsuperuser
Username: admin
Email address: admin@example.com
password: ********
password (again): ********
Superuser created successfully
```

이제 runserver 를 통해 서버에 접속하고 

```sh
$ python manage.py runserver
```

`URL/admin` 에 접속하여 방금 생성한 superuser 로 접속해보자.

### Band 를 관리자 페이지에서 관리하기.

App 의 모델들을 관리자 페이지에서 관리하도록 설정할 수 있다. 우리는 `bands` app 의 `Band` 모델을 등록할 예정이다.

` bands.admin.py`

```python
from django.contrib import admin

from .models import Band

admin.site.register(Band)
```

이제 다시 관리자 페이지에 접속하면, bands app 의 bands 테이블 관리가 가능하다.접속하여 데이터를 조작해보자!







### 
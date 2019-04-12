# Python3 setting

## Windows10

```sh
$ choco install python3
```

## Ubuntu (C9 workspace)

### [pyenv](https://github.com/pyenv/pyenv)

#### Python 버젼 관리 매니저 설치

```sh
$ git clone https://github.com/pyenv/pyenv.git ~/.pyenv
```

#### Run Command 에 환경변수 설정

```sh
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
$ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
$ bash # source ~/.bashrc
$ pyenv -v
```

#### python 3.6.7 설치 및 기본 버전 설정

```sh
$ pyenv install 3.6.7
$ pyenv global 3.6.7
$ pyenv versions
  system
* 3.6.7 (set by /home/ubuntu/.pyenv/version)
```

---

### [Virtual ENV](https://github.com/pyenv/pyenv-virtualenv)

#### 가상환경 관리자 설치

```sh
$ git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
```

#### Run command 환경변수 설정

```sh
$ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
$ bash
```

#### python 버전 확인 및 가상환경 설정

```sh
$ pyenv virtualenv 3.6.7 django_env
Looking in links: /tmp/tmp366q_8v7
Requirement already satisfied: setuptools in /home/ubuntu/.pyenv/versions/3.6.7/envs/django/lib/python3.6/site-packages (39.0.1)
Requirement already satisfied: pip in /home/ubuntu/.pyenv/versions/3.6.7/envs/django/lib/python3.6/site-packages (10.0.1)

$ pyenv versions
  system
* 3.6.7 (set by /home/ubuntu/.pyenv/version)
  3.6.7/envs/django_env
  django_env
```

#### Django prj 생성

```sh
$ mkdir first_django
$ cd first_django
$ pyenv local django_env
(django_env) $ pip install django
(django_env) $ django-admin startproject <APP_NAME> . # hyphen (-) 포함 불가!
```

#### Django App 실행 Local

```sh
(django_env) $ pwd
.../first_django
(django_env) $ ls
first_django/ manage.py
(django_env) $ python manage.py runserver 
```

브라우저로 `localhost:8000` 으로 접속! 로켓을 보면 Good to go

#### Django App 실행 C9

```sh
(django_env) $ pwd
/home/ubuntu/workspace/first_django
(django_env) $ ls
first_django/ manage.py
(django_env) $ python manage.py runserver $IP:$PORT # 서버는 실행 되지만 Error. 접속 가능 도메인 을 확인
```

`first_django/first_django/settings.py`

```python
...

ALLOWED_HOSTS = [
    '<PRJ-USERNAME>.c9users.io' # 아까 확인한 도메인
]

...
```

`ALLOWED_HOSTS` 에 도메인 추가할 때 반드시!!

* 시작에 `https://` 가 없는지,
* 마지막 `/` 가 없는지 확인!

`<PRJ-USERNAME>.c9users.io` 로 접속! 로켓을 보면 Good to go!

*참고* : 나중에 사용

`~/.bashrc`

```
alias rundjango="python manage.py runserver $IP:$PORT"
```
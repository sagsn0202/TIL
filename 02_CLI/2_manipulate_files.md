# 2.Manipulating files - 파일 조작

* 기본적으로 텍스트 에디터를 활용하는 법을 모르는 상태에서 진행.
* 순수 CLI 커맨드로 파일을 다뤄보기.

## 2.1 Redirceting and appending

우선 문자열 한줄을 출력해보자

```shell
$ echo "When I was a young boy"
When I was a young boy
$
```

* `$ echo` : standard out

---

그리고 해당 문자열을 포함하는 파일을 만들어 보자. (파일 명은 black_parade.txt)

```shell
$ echo "When I was a young boy" > black_parade.txt
$
```

위 명령어는 `$ echo` 명령어의 출력 내용을 `black_parade.txt` 라는 이름의 파일로 보내는(redirect) 명령어다.

* `>` : redirect

---

정말 우리가 원하는 대로 되었는지 확인하려면 어떻게 해야 할까? 

지금 단계에서는 일단 단순히 해당 파일의 내용을 터미널 창에 보여주는 명령어를 사용해 보자.

```shell
$ cat black_parade.txt
When I was a young boy
```

* `$ cat` : con**cat**ate (여러개를 하나로 연결하다.)
* `$ cat ` 명령어는 contents 들을 combine 하는 용도다.
* 하지만  지금은 우선 `$ cat` 명령어를 최대한 빠르고 지저분하게 특정 파일의 내용을 보여주는 명령어로 알고 있자.

---

이번에는 추가로 줄을 삽입해보자.

```shell
$ echo "My father took me into the city" >> black_parade.txt
```

위 명령어는 `$ echo` 명령어의 출력 내용을 `black_parade.txt` 라는 이름의 파일에 덧붙이는(append) 명령어다.

* `>>` : append
* **만약 `>` 를 사용하게 되면 해당 파일에 출력내용을 덮어 쓰게 된다. 즉 기존의 내용은 날아간다.**

```shell
$ cat black_parade.txt
When I was a young boy
My father took me into the city
```



### Exercise

1. `echo` 와 `>` 를 사용하여,  좋아하는 노래가사를 영어로 한줄씩 각각 `line_1.txt` 와 `line_2.txt` 로 만든다.
2. `cat` 명령어와 redirect, append 명령어를 사용하여 `song.txt` 에 `line_1.txt` 와 `line_2.txt`의 내용을 넣는다.
3. **한줄의 명령** 으로 `song_reverse.txt` 파일을 만들고, 그안에 각 `line_1.txt`와 `line_2.txt` 를 거꾸로 넣어보자.



## 2.2 Listing & New file

아마 가장 많이 사용되는 Unix 명령어로 생각되는 `ls`.  (결과 창은 다를 수 있음.)

```shell
$ ls 
Desktop
Document
Downloads
Library
black_parade.txt
```

* `$ ls` 는 단순히 (숨김파일을 제외하고) 현재 디렉토리(폴더)에 있는 모든 파일과 디렉토리들을 보여준다.

---

* 여러가지 옵션들을 붙일 수 있다.

```shell
$ ls -a # 숨김 파일까지 모두(all) 보여주기.

$ ls -l # long-format으로 보여주기.

$ ls -t # 가장 최근에 수정된 순서(time) 로 보여주기.

$ ls -r # 역순(reverse)으로 보여주기.
```

---

* 또한 이러한 옵션들을 섞어서 사용할 수 있다.
* 옵션들은 순서가 상관이 없다.

```shell
$ ls -al # 모든(all) 파일을 long-format으로 보여주기.

$ ls -tla # 모든(all) 파일을 long-format 으로 가장 최근에 수정된 순서로 보여주기.
```

* 추가로 이중에 `-l` 옵션에서 long-format 이 보여주는 내용을 더 알고싶다면 https://www.garron.me/en/go2linux/ls-file-permissions.html 를 참고하자.

---

* `-a` 옵션이 실제로 숨김파일을 출력해 주는지 보려면, 우선 숨김 파일을 만들어 보자 ( `touch`).

```shell
$ touch not_hidden.txt

$ touch .hidden.txt
```

* `$ touch` 명령어는 새로운 파일을 만든다. (디렉토리는 아님)
* Unix based OS 에서는 파일 혹은 디렉토리의 경우 이름 앞에 `.` 이 붙으면 숨김이다.
* `$ ls` 와 `$ls -a` 를 통해 비교해 보자.


## 2.3 Renaming, copying, deleting

이름 바꾸기, 복사하기, 지우기를 차례대로 해 볼 예정이다. 

* 이름바꾸기

```shell
$ echo "test text" > test
$ ls test
test
$ mv test test_file.txt
$ ls 
test_file.txt
$ cat test_file.txt
test text
```

* `mv` 는 파일의 위치를 바꾸는 것도 가능하지만, 현재 디렉토리 관련 내용을 배우지 않았기에, 일단은 Rename 기능만 소개.

---

* 복사하기

```shell
$ cp test_file.txt copy_file.txt
$ ls
test_file.txt
copy_file.txt
```

---

* 지우기

```shell
$ ls
test_file.txt
copy_file.txt
$ rm copy_file.txt
$ ls
test_file.txt
```

---

* 여기서부터 Tab(`⇥`) 키를 사용해 보도록 하면 좋을 듯 하다.
* 이번에는 옵션과 함께 마찬가지로 `test_file.txt` 역시 지워보도록 하자.

```shell
$ rm -i te⇥
$ rm -i test_file.txt
remove test_file.txt? n
$ ls
test_file.txt
```

* 뒤의 파일 이름이 자동 완성된다. `⇥` 키는 직접 사용하면서 느끼는 게 가장 좋다. 두번 누르게 되면 목록이 뜨게 된다.
* `-i` 옵션은 지우기 전에 확인을 받기위해 사용자에게 물어본다.
* `y` / `Y` 를 입력하고 `enter`를 눌렀을 경우에만 삭제된다. (기타 다른 모든 입력을 하고 `enter` 를 할 경우 무시된다.)
* 이번에는 `n` 을 누르고 `enter` 이후 확인해 보면 지워지지 않음을 볼 수있다.

---

```shell
$ rm -f test_file.txt
$ ls
$
```

* `-f` 옵션은 반대로 어떠한 확인이나 절차를 모두 무시하고 강제로(force) 삭제하는 명령어 이다.
* 정말 확실하지 않으면 사용을 자제하는 것이 좋다.

---

``` shell
$ touch a.txt b.txt c.txt d.txt e.txt
$ ls
a.txt b.txt c.txt d.txt e.txt
$ rm *.txt
$ ls
$
```

* 여기서 `*` 는 wild-card 라고 불리며, `$ rm *.txt` 는 마지막에 확장자가 `.txt` 로 끝나는 모든 파일을 삭제하라는 의미이다.
* **디렉토리의 삭제는 `rm` 혹은 `rm -f` 로 안된다. 이후 디렉토리 관련 챕터에서 다룰 예정이다.**



### Exercises

1. 숨겨지지 않은 파일들 중에서 `b` 로 시작하는 모든 파일과 디렉토리를 보여주는 명령어는 무엇일까?
2. 숨김파일 포함 모든 파일들을 long-form 으로 수정한 시간정렬 역으로 출력하는 명령어는?
3. 다음을 차례대로 해보자.
   1. `echo` 명령어와 redirect(`>`) 명령어를 사용하여, `'hello, world'`라는 텍스트를 담고있는 파일 `foo.txt` 를 생성한다. 
   2. 그리고 `cp` 명령어를 사용하여, `foo.txt` 를 복사한 `bar.txt` 를 만들자.
   3. (추가) `diff` 명령어를 사용하여 두 파일을 비교해보자. (manual page 를 이용해 보거나, `diff`명령어가 두가지 파일을 받아들일 수 있다는  사실을 활용해보자.)
4. `cat` 과 `>` 을 사용하여, `foo.txt` 를 복사한 `baz.txt`를 만들자 (`cp` 사용 금지!)
5. 한 줄 명령으로 `foo.txt` 와 `bar.txt` 의 내용을 연속으로 포함하는 파일 `quux.txt` 를 만들어보자. (`cat` 명령어는 여러개의 argument 를 받을 수 있다.)
6. `rm nothing` 과 `rm -f nothing` 을 비교해보면 어떤가?



## 번외: 왜 Unix 명령어는 이렇게 짧게 줄여 놨을까

* `ls` 나 `mv` 같은 명령어는 `list` 나 `move` 같이 써도 될 것 같은데, 왜 외우기 힘들게 줄여놨을까? 
* 과거에는 인터넷 환경이 지금과 비교했을 때 좋지 않았다, 때문에 중앙 서버 컴퓨터와 사용자가 사용하는 컴퓨터를 연결하여 서버 컴퓨터를 조작할 때 사용자가 입력한 키가 실제 중앙 컴퓨터에 도달하는데 입력 지연(delay)이 상당했다. 즉 터미널에서 실제 `a`키를 입력하면 짧게는1초부터 길게는 몇 초까지의 지연 이후 화면에 `a`가 나타났다는 것. 
* 그래서 가장 많이 쓰이는 unix 명령어들은 최대한 짧게 쓰게 된 것이다. 만약 `$ rm` 이 `$ remove` 였다면 3배, `$ ls` 가 `$ list` 였다면 2배의 추가 지연이 발생한다. (정말 가장 많이 쓰이는 명령어 중 이후에 배울 `$ cd` 는 `change directroy` 의 앞글자다..)



## 2.4 Summary

| Command          | Description                                        | Example                 |
| ---------------- | -------------------------------------------------- | ----------------------- |
| `>`              | 왼쪽의 출력물을 오른쪽의 파일로 Redirect(전송하기) | `$ echo foo > foo.txt`  |
| `>>`             | 왼쪽의 출력물을 오른쪽의 파일로 Append(붙이기)     | `$ echo bar >> foo.txt` |
| `cat <file>`     | `<file>` 의 내용물을 화면에 출력                   | `$ cat foo.txt`         |
| `ls`             | 파일/디렉토리 들의 목록을 보여줌                   | `$ ls`                  |
| `ls <file>`      | `<file>` 만을 보여줌                               | `$ ls foo.txt`          |
| `ls -a`          | (숨김파일 포함) 모두 나열                          | `$ ls -a`               |
| `ls -l`          | long-format 으로 나열                              | `$ ls -l`               |
| `ls -alt`        | all 을 long-form 으로 수정한 시간 기준으로 나열    | `$ ls -alt`             |
| `touch <file>`   | 비어있는 `<file>` 생성                             | `$ touch foo`           |
| `mv <old> <new>` | `<old>` 의 이름을 `<new>`로 바꿈.(지금 단계에서는) | `$ mv foo bar`          |
| `cp <old> <new>` | `<old>` 를 `<new>` 이름으로 복사                   | `$ cp bar foo`          |
| `rm <file>`      | `<file>` 을 지운다.                                | `$ rm foo`              |
| `rm -f <file>`   | `<file>` 을 강제(force)로 지운다.                  | `$ rm -f bar`           |


# 4. Directories

* 지금까지 수많은 Unix 명령어들로 file 들을 상대해 왔다면, 이제 *Directories(Folders)* 를 배울 차례이다. 
* 살펴 보겠지만, 파일들에서 적용할 수 있는 개념들이 디렉토리들에서도 적용되지만, 꽤나 많은 차이점들이 있다.



## 4.1 Directory structure - 디렉토리 구조

* Unix-Style 의 디렉토리 구조는 일반적으로 디렉토리 이름을 정 슬래시(`/`) 로 구분하며, (윈도우는 백 슬래시`\`)


*  `ls` Command 와 섞어서 다음과 같이 사용할 수 있다.

```shell
$ ls /Users/neo/TIL
$ ls /usr/local/bin
```

* 모든 Unix Based OS 에서는 모든 디렉토리들은 결국 궁극적으로 루트(*root*) 디렉토리의 하위 디렉토리이다. 이 *root* 디렉토리를 상징하는 마크가 `/` 이기도 하기에 결국 디렉토리 구조를 표현할 때는 `/` 로 시작하며 동시에 하위 디렉토리에 대한 구분을 `/`로 하게된다.

* 일반적인 사용자에게 가장 중요한 디렉토리는 홈(*home*) 디렉토리다. MacOS 의 경우 `/Users/neo` 과 같은 형식으로 이루어져 있다(root dir 아래 Users dir 아래 사용자계정명 dir). 이러한 홈 디렉토리의 경우 `~` 마크를 사용하게 된다. (`~` 는 영어로 tilde character 라고 함)

* 결과적으로 만약 MacOS 기준 Downloads 디렉토리의 위치는 `/Users/neo/Downloads` 이기도 하면서 동시에 `~/Downloads` 라고 표현할 수도 있다. `neo` 계정으로 로그인 한 상황이라면, 둘은 완전히 같은 디렉토리를 의미한다. ([오래전 키보드](https://unix.stackexchange.com/questions/34196/why-was-chosen-to-represent-the-home-directory)에서는 `~`  문자와 `Home` 키가 같은 키였다.)

* 모든 Unix 시스템은 '시스템 디렉토리(*System directoies*)' 라고 하여, 컴퓨터의 일반적인 작동에 반드시 필요한 프로그램들이 저장된 디렉토리가 있다. 이러한 시스템 파일이나 디렉토리들을 수정하는것은 슈퍼유저(superuser), 혹은 `root` 계정이라고 하는 특별한 권한이 있어야만 한다. (앞서 서술한 `/` 의 root dir 과는 무관하다.) 

* super user 는 너무나 권한이 강력하기때문에 이런 `root` 계정으로 컴퓨터에 로그인하는 것은 좋지 않은 방법이다. 때문에 super user 의 권한이 필요한 작업을 할때는 계정을 바꾸는 것이 아니라, 작업을 `sudo` 라고 하는 명령을 통해 기존 계정에서 super user의 권한을 빌리는 것이 가능하다.

  ```shell
  $ touch /opt/fake_file
  touch: /opt/fake_file: Permission denied # /opt dir에 대한 권한 없음 에러.

  $ sudo touch /opt/fake_file
  Password: 			# password 가 맞다면 성공적으로 fake_file 이 생성.

  $ ls -l /opt/fake_file
  -rw-r--r-- 1 root wheel 0 Jul 12 19:13 /opt/fake_file 
  # root 는 super user 가 이 파일을 소유하고 있고, wheel 은 Group 명이다. 현재는 admin 그룹이라고 쓰지만, 과거에는 배의 wheel 이라 하여 wheel 그룹을 의미한다.

  $ rm -f /opt/fake_file
  rm: /opt/fake_file: Permission denied

  $ sudo rm -f /opt/fakefile

  $ sudo ls -l /opt/fake_file
  ls: /opt/fake_file: No such file or directory
  ```

  ​

---

### Exercises

1. `~/my_dir/my_file` 을 발음해보자
2. `/Users/neo/my_dir` 에서 Home dir 은 어디이며, 사용자 이름은 무엇일까? 가장 아래에 있는 디렉토리의 이름은?
3. `yty` 라는 사용자에게 `/Users/yty/Documents` 와 `~/Documents` 는 어떻게 다른가?



## 4.2 Making directories - 디렉토리 생성

* 지금까지 우리는 수많은 `.txt.` 파일들을 생성하고 지워봤다. 이제는 이 파일들을 담을 디렉토리를 생성해 보자. 

* 보통의 PC 들은 GUI(Graphic User Interface)를 제공하지만, Unix 시스템에서는 `mkdir` (make directory) 명령어를 통해 디렉토리를 생성한다.

  ```shell
  $ mkdir text_files
  ```

* 디렉토리를 생성했으니 우리는 이제 파일들을 `*` (wild card) 를 사용하여 옮길 수 있다.

  ```shell
  $ mv *.txt text_files/
  $ ls text_files/
  sonnet1.txt		sonnets.txt		...
  ```

* 마지막으로, 이제 드디어 우리는 `cd` 명령어를(**c**hange **d**irectories) 통해 디렉토리간 이동을 할 수 있게 되었다.

* 방금 생성한 `text_files` 디렉토리로 위치를 `pwd` 를 이동해 보자. (present working directory) - `tab` 을 통한 자동완성기능을 열심히 사용하자.

  ```shell
  $ cd text_files
  ```

* 잘 이동했는지 보려면 `cd` 명령어 이후에 `pwd` 명령어와 `ls` 명령어를 입력해 확인하자!

---

### Exercise

1. 현재 존재하지 않는 디렉토리 `dir1` 안에 `dir2` 를 만들고자 한다. 각각 생성이 아닌 명령어 한번에 생성하는 옵션을 `man` 페이지에서 찾아보자. (`$ man mkdir`)
2. 1에서 알아낸 명령으로 한번에 `/foo/bar/baz` 까지 3개의 디렉토리를 생성해 보자.
3. 홈 디렉토리에서의 `ls` 명령어의 결과물을 파이프 하여 `grep` 를 통해 알파벳 'o' 가 포함된 모든 파일/폴더를 보여보도록 하자.



## 4.3 Navigating directories - 디렉토리 탐색하기

* 우리는 섹션 4.2 에서 어떻게 디렉토리 이름과 `cd` 명령어를 통해 디렉토리를 변경할 수 있는지 알게 되었다.

* 이렇게 디렉토리 이름을 지정해서 디렉토리간의 이동을 하는것이 보통이지만, 몇가지 특별한 형식을 통해서도 이동할 수 있다.

* 첫번째는 현재 위치한 디렉토리에서 한 단계 상위 디렉토리로 이동하는 명령어 `cd ..` 이다. (위로가기)

  ```shell
  $ pwd
  /Users/neo/CLI/text_files # 현재 위치는 다를 수 있다.
  $ cd ..
  $ pwd 
  /Users/neo/CLI
  ```

* 또한 `cd` 명령어 뒤에 아무런 위치도 지정하지 않을 경우 홈 디렉토리로 이동하게 된다.

  ```shell
  $ cd
  $ pwd
  /Users/neo
  ```

* 즉 `$ cd` 와 `$ cd ~` 는 완전히 같은 의미이다.

---

* 디렉토리를 변경할 때, 어떻게든 홈(home) 디렉토리를 명시하는 것이 꽤나 유용하다. 
* 예를 들면,  또다른 디렉토리를 생성하고, 그곳으로 이동한다고 해보자.

```shell
$ pwd
/Users/neo/CLI
$ mkdir second_directory
$ cd second_directory
```

* 이제 만약 우리가 `text_files` 디렉토리로 이동 싶다면, 우리는 다음과 같이 쓸 수 있다.

```shell
$ pwd 
/Users/neo/CLI/second_directory
$ cd ~/CLI/text_files
$ pwd
/Users/neo/CLI/text_files
```

* 어쩌다 보니, 이제 우리는 프롬프트(`$`) 뒤에 붙어있는 마크가 무엇을 의미하는지 알게 되었다.

---

* `..` 가 상대적으로 현재 위치보다 한단계 위의 디렉토리를 의미한다고 하면, `.` 은 현재 나의 위치를 의미한다.
* 가장 `.` 이 많이 사용되는 경우는, 파일을 현재의 위치로 옮기거나(`mv`) 복사할 경우(`cp`)다.

```shell
$ pwd
/Users/neo/CLI/text_files
$ cd ~/CLI/second_directory
$ ls # 아무것도 없다.
$ cp ~/CLI/text_files/sonnets.txt .
$ ls
sonnets.txt

```

*  `.`  가 널리 사용되는 또다른 경우는, `find` 명령어와의 결합(conjunction) 인데, 미친듯이 강력한 `grep` 과 비슷하지만,  일반적으로 다음과 같이 사용되는 경우가 99% 이다.

```shell
$ cd # cd ~
$ find . -name '*.txt'
# 현재 ~ 하위의 모든 디렉토리에서 확장자 .txt 를 찾아 보여준다.
```

* 현재 위치한 `~` 뿐만 아니라, 하위 디렉토리를 모두 뒤지며 `.txt` 를 찾아낸다. 이렇듯 `find` 명령어(유틸리티)는 특희 잘못 위치한 파일을 CLI 를 통해 찾아낼 때 엄청나게 유용하다.
* 만약 MacOS 를 사용한다면, `.` 을 많이 사용하는 경우중 하나는 `open .` 이다.

```shell
$ cd ~/CLI/text_files
$ open .
```

* `open` 명령어는 OS 에서 해당 파일을 열 때 기본값(default) 로 설정해 놓은 프로그램으로 파일이나 디렉토리를 연다. (몇몇 리눅스 시스템에서는  `xdg-open` 가 유사하게 동작한다.)
* 가령 `open foo.pdf` 는 PDF 파일을 기본 내장 프로그램으로 연다.(MacOS 의 경우에는 미리보기.)
* 위의 경우에는 디렉토리를 열고자 하며, 디렉토리를 탐색하는 기본 프로그램은 Finder 이므로 Finder 에서 해당 디렉토리를 보여준다.

---

* 마지막 탐색 명령어는, `cd -` 이며, 이전 디렉토리로 이동한다.(뒤로 가기)

```shell
$ pwd
/Users/neo/CLI/second_directory
$ cd ../text_files
$ pwd /Users/neo/CLI/text_files
$ cd -
$ pwd /Users/neo/CLI/second_directory
```

* `cd -` 는 다음과 같은 명령어들과 섞을 때 특히 더 유용하다.

### 명령어 결합하기

* CLI 를 사용하여 소프트웨어를 설치할 때, Unix 프로그램인 `configure` 과 `make` 를 사용할 경우, 명령어들을 결합하는 것은 매우 유용하다. 보통 아래와 같은 모습으로 사용한다.

```shell
$ ./configure ; make ; make install
```

* 이 명령어는 현재 디렉토리(`.`)에 있는  `configure` 프로그램을 실행하며, 이어서 `make` 와 `make install` 명령어를 모두 실행한다. ( 이해할 필요 X, 다음과 같은 명령이 실행되는 디렉토리에 있을 경우에만 사용가능.)
* 각각의 명령어가 세미 콜론`;` 으로 연결되어 있기 때문에, 3가지 명령어가 연속적으로 실행되는 것이다.
* 더 좋은 명령어 결합은 Double-ampersand (`&&`) 를 사용하는 것이다.

```shell
$ ./configure && make && make install
```

*  `&&` 과 `;` 의 차이는, 
  * `&&` 의 경우에는 이전의 명령어가 **성공**했을 경우에만 다음 명령어를 실행한다.
  * `;` 의 경우에는 이전 명령어의 성공 여부와 상관 없이 다음 명령어가 실행된다. 때문에 앞에서 error 가 날 경우 뒤이어 에러가 계속해서 발생할 수 있다.
* 이런 `&&` 와 `cd -` 를 결합하면 다음과 같은 명령어를 실행할 수 있다.

```shell
$ cd .. && git add . && git commit -m 'Finish chapter 4-3' && git push && cd -
```

* 위 명령어를 모두 이해할 필요는 없어도, 대략 다음과 같이 구성되어있는 것을 파악하면 된다.
  1. 상위 디렉토리로 이동.
  2. 현재 디렉토리에 있는 모든 파일과 디렉토리를 `git add` 함.
  3. `-m` 옵션으로 'Finish chapter 4-3' 을 넘기고 `git commit`.
  4. `git push`.
  5. 원래 있던 디렉토리로 이동.
* 해당 작업이 반복적이라면, `Ctrl-P` 나 방향키로 디렉토리 이동 없이 계속해서 사용할 수 있다.



### Exercise

1. `cd` 와 `cd ~` 의 차이점은? 있나?
2. `text_files` 디렉토리에서 `..` (위로가기)를 사용하여 `second_directory` 로 한번에 이동해보자.
3. 어떤 위치에 있던지, `text_files` 에 `nil` 이라는 이름의 파일을 어떻게든 이동없이 생성해 보자.
4. 3에서 만든 `nil` 파일을, 생성할 때 사용했던 경로와 다른 방법으로 삭제(`rm`) 해 보자.


## 4.4 Renaming, copying, and deleteing directories - 디렉토리 이름바꾸기, 복사하기, 지우기

* 디렉토리의 이름 바꾸기, 복사하기, 지우기의 명령어는 파일에서 사용하는 명령어와 비슷하지만, 약간의 다른 점들이 있다.
* 가장 차이가 적은 명령어는 `mv` 다. 파일에서와 거의 똑같이 동작한다.

```shell
$ mkdir foo
$ mv foo/ bar/
$ cd foo
-bash: cd: foo: No such file or directory
$ cd bar/
```

* `mv` 명령어가 재대로 동작했음을 Error메세지로 확인할 수 있다.  (`bash` 는 현재 동작하는 shell program 의 이름이다. 이 경우에는, [Bourne Again SHell](https://www.gnu.org/software/bash/) 이다.)
* 유일하게 존재하는 차이점은, 디렉토리 이름 뒤에 붙은 `/` 이다. (tab 자동 완성을 사용하면, 자동으로 생성됨.)

```shell
$ cd
$ mv bar foo
$ cd foo/
```

* `/`  를 붙이는 이슈는 `mv` 명령어에서는 사실 전혀 문제가 되지 않는다.

---

* 하지만 `cp` 에서는 이 이슈가 존재하는데, 일반적으로 디렉토리를 복사하는 행위는, 안에 있는 하위 디렉토리와 파일들 까지 모두 복사하려고 하는 것이다. 이럴 경우에, 많은 시스템들이 `/` 를 생략한다. 
* 또한, 파일들을 복사 할때는, `-r` 옵션 (recursive) 을 붙여야 한다.
* 예를들어, `text_files` 디렉토리의 내용물을 새로운 `foobar` 디렉토리에 복사하려 한다면, 다음과 같이 작성해야 한다.

```shell
$ cd ~/CLI/
$ mkdir foobar
$ cd foobar/
$ cp -r ../text_files .
$ ls
text_files
```

* 우선 복사를 위해 `..` 을 사용하여 (상대경로) 한 단계 위에있는 `text_files` 디렉토리를 현재(`.`)  디렉토리에 복사했다.
* 주의 할 것은, 언급한대로 `/` 를 제외하고 입력한 것인데, 만약 `/`를 포함하면, 다음과 같은 결과가 나타난다.

```shell
$ cp -r ../text_files/ .
$ ls
sonnet_1.txt sonnet_1_reversed.txdt welcome_to_the_black_parade.txt
```

* 다시말하면
  * `/` 를 붙일 경우, 해당 디렉토리에 있는 모든 내용을 가져오지만, 디렉토리 자체는 가져오지 않음.
  * `/` 를 붙이지 않을 경우, 해당 디렉토리 자체를 가져옴.
* 때분에 일반적으로 디렉토리를 복사할 때는 `/` 를 빼는것이 적절하다.
* 만약 해당 디렉토리의 내용물만을 가져 오고 싶은 경우에는 다음과 같이 쓰는것이 더 명확하다.

```shell
$ cp ../text_files/* .
```

---

* `mv` 이름바꾸기(옮기기) 와 `cp` 복사와 다르게 디렉토리 삭제는 전용 명령어 `rmdir`가 있다.
* 하지만 경험상, 거의 동작하지 않는다.

```shell
$ cd 
$ rmdir second_directory
rmdir: second_directory/: Directory not empty
```

* 위의 메세지는 99% 의 명령에서 나오는 에러 메세지인데,  `second_directory` 가 비어있지 않다는 것이다. `rmdir` 은 기본적으로 디렉토리 안의 내용이 아얘 없을때만 동작한다.
* 물론 해당 디렉토리 안에 있는 모든 파일/디렉토리들을 지우면 되지만 매우 귀찮은 직업이다.
* 그래서 거의 항상 디렉토리를 삭제할 때는 `rm -rf` 라고 하는 (**r**e**m**ove **r**ecursiveliy **f**iorce) 명령어를 사용하게 된다.
* 해당 명령어는 해당 디렉토리와 모든 하위 디렉토리/파일들을 **확인 메세지 없이** 삭제한다.

```shell
$ rm -rf second_directory/
$ ls second_directory
ls: second_directory: No shcu file or directory
```

* 다음 에러는 `second_directory`를 목록에서 보여줄 수 없다는 명령어다. 즉 성공적으로 `second_directory` 를 삭제했다는 것이다.
* `rm -rf`는 정말 편리한 명령어지만, 명심해야 한다. "With great power comes great responsibility"



### Grep redux

* 이제 우리는 디렉토리에 대해서도 어느정도 알게 되었고, `grep` 이라는 유용한 toolkit 역시 사용 할 수 있다.
* `cp`, `rm`, `grep` 은 'recursive' 옵션을 지원하며, 이 경우에는 디렉토리의 하위 디렉토리와 파일들을 grep 한다.
* 즉 우리는 특정 문자열이 들어간 파일을 디렉토리 계층구조에서 (hierarchy)  어디에 있는지 찾고 싶을 때 다음과 같이 CLI 를 사용할 수 있다.
* 일단 다음과 같이 setup 한다. `long_word.txt` 란 파일에 'sesquipedalian' 이라는 단어를 입력한다.

```shell
$ cd ~/CLI/text_files/
$ mkdir foo
$ cd foo/
$ echo sesquipedalian > long_word.txt
$ cd ~/CLI
```

* 그리고 `CLI` 디렉토리에서 해당 단어를 포함하는 파일을 찾아 보는 것이다.

```shell
$ grep sesquipedalian text_files # Doesn't work
grep: text_files: Is a directory
```

* 써 있듯이 grep 로는 디렉토리를 탐색할 수 없다.

```shell
$ grep -r sesquipedalian text_files
text_files/foo/long_word.txt:sesquipedalian
```

* 보통 대/소문자는 신경 쓰지 않지만, 혹시 모를 경우에 대비해 `-i` 옵션을 붙이는 습관을 들이는 것도 좋다.

```shell
$ grep -ri sesquipedalian text_files
text_files/foo/long_word.txt:sesquipedalian
```

* `grep -ri`를 장착한 이상, 우리는 이제 디렉토리들 안에서 원하는 문장이 들어간 파일을 자유롭게 찾아 낼 수 있다.



### Exercises

1. `foo` 디렉토리 하위에  `bar` 라는 디렉토리까지 한번에 만들고, `bar` 디렉토리를 `baz` 로 이름을 바꿔보자.
2. `text_files` 안에 들어있는 모든 파일들을 *디렉토리까지 포함해* `foo` 디렉토리로 복사해보자.
3. `text_files` 안에 들어있는 모든 파일들을 *디렉토리를 제외하고* `foo` 디렉토리로 복사해보자.
4. `foo` 디렉토리를 모두 한번에 삭제해보자.



## 4.5 Summary

| Command                | Description                  | Example                 |
| ---------------------- | ---------------------------- | ----------------------- |
| `mkdir <name`          | <name> 디렉토리 생성         | `$ mkdir foo`           |
| `pwd`                  | print working directory      | `$ pwd`                 |
| `cd <dir>`             | <dir> 로 이동                | `$ cd foo/`             |
| `cd ~/<dir>`           | 홈의 상대 <dir> 로 이동      | `$ cd ~/foo/`           |
| `cd`                   | 홈 dir 로 이동               | `$ cd`                  |
| `cd -`                 | 이전 dir 로 이동             | `$ cd ; pwd ; cd-`      |
| `.`                    | 현재 있는 dir                | `$ cp ~/foo.txt .`      |
| `..`                   | 한 단계 상위 dir             | `$ cd ..`               |
| `find`                 | 파일&디렉토리 찾기           | `$ find . -name foo*.*` |
| `cp -r <old> <new>`    | 재귀적 복사                  | `$ cp -r ~/foo .`       |
| `rm -rf <dir>`         | <dir> 의 파일/dir 모두 삭제  | `$ rm -rf foo/`         |
| `grep -ri <str> <dir>` | 재귀적 case-insensitive grep | `$ grep -ri foo bar/`   |



### Exercises

1. 홈 디렉토리에서 시작하여, 한줄로 다음 커맨드들을 작성해보자.
   1. `foo` 라는 dir 을 만든다.
   2. `foo` 로 현재 위치를 바꾼다.
   3.  "baz" 라는 내용이 들어간 `bar` 라는 파일을 생성한다.
   4. `bar` 의 내용물을 출력한다.
   5. 이전에 왔던 dir 로 돌아간다.
2. 방금 실행한 명령어를 다시 실행해보자. 몇개의 명령어가 실행되는가? 왜?
3. 왜 `rm -rf /`라는 명령어가 세상에서 제일 위험한지, 그리고 농담으로라도 터미널에 입력하면 안되는지 설명해 보자.
4. `rm -rf /` 를 더 위험하게 만드는 방법은 무엇이 있을까? 이 커맨드는 입력이 아니라 생각도 하면 안된다!
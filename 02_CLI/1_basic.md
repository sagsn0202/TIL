# 1. Basics - 기초

## 1.1 What is CLI?

* GUI : 컴퓨터 사용을 쉽게 만들었다. 컴퓨터의 대중화.
* CLI : In the begging was the command line. **The most powerful and flexible way to interact with a computer**.

## 1.2 Which OS?

* Unix Based OS ( Linux, Mac, etc..)
*  어느순간 반드시 Unix 커맨드들을 알아야 하는 시점이 온다 (서버).



## 1.3 Prompt?

* 컴퓨터가 새로운 명령을 받아드릴 준비가 되었다는 뜻으로 보여주는 표시(Symbol). 이 표시가 떠 있을 때 명령어를 입력하여야 한다.

* 일반적으로 `$` 사인을 사용하지만, 실제 컴퓨터에 표시되는 prompt 는 매우 다양하며 커스터마이즈 역시 가능하다. 여기서는 짧게 적기 위해 `$` 사인을 사용하도록 한다.

  ​

## 1.4 막히면?`Ctrl-C`

일단 `Ctrl-C` (` ^C`) - C stands for cancle

```shell
$ echo "hello
$ grep foobar
$ yes
$ tail
$ cat
```

* 다음 명령어를 쳐보면, 아주 당혹스럽다. 이렇게 뭔지 모를 경우에는 반드시 ` ^C`를 기억하자

  ​

## 1.5 `$ echo`

* `$ echo` : starndard out(화면출력)

  ```shell
  $ echo hello
  hello
  $
  ```


* `''` , `""` : 크게 상관없다.

  ```shell
  $ echo 'hello'
  hello
  $ echo "goodbye"
  goodbye
  ```

  ​

* `Ctrl-C`

  ```shell
  $ echo 'hello
  > ^C
  $
  ```

### Exercises

1. 터미널에 "Hello, World" 를 출력해 보자.
   * 추가연습 : 따옴표를 사용하고 / 사용하지 않고 해보자!
2. `echo 'hello` 라고 입력하고 이 문제상황에서 나와보자



## 1.6 `$ man`

* `$ man ` : Manual page(공식 매뉴얼 페이지)

  ```shell
  $ man echo
  ECHO(1)          BSD General Commands Manual         ECHO(1)

  NAME
     echo -- write arguments to the standard output

  SYNOPSIS
     echo [-n] [string ...]

  DESCRIPTION
     The echo utility writes any specified operands, separated by single blank
     (` ') characters and followed by a newline (`\n') character, to the stan-
     dard output.

     The following option is available:

     -n  Do not print the trailing newline character. This may also be
        achieved by appending `\c' to the end of the string, as is done by
        iBCS2 compatible systems. Note that this option as well as the
        effect of `\c' are implementation-defined in IEEE Std 1003.1-2001
        (``POSIX.1'') as amended by Cor. 1-2002. Applications aiming for
        maximum portability are strongly encouraged to use printf(1) to
        suppress the newline character.
  :                                                                             
  ```

  * `$ man echo` 는 `$ echo` 명령어의 매뉴얼 페이지이다.
  * 맨 마지막의 `:` 는 아래에 아직 정보가 더 있다라는 의미. 기존의 `$` 상태와 다른 상황이다. 마우스 스크롤, 키보드 화살표키, 스페이스바,`d`, `u` 등의 키로 정보를 더 확인할 수 있다. 나오려면 `q` 를 누른다.



## 1.7 편리한 Tips & Shortcuts

* 아래 `⌃`(Ctrl) 뒤의 알파벳은 소문자 대문자를 구분하지 않는다.

| Keybinding           | Description                                     |
| -------------------- | ----------------------------------------------- |
| ``←``,  `→`          | 커서 이동                                       |
| `↑`(`⌃P`) ,`↓`(`⌃N`) | 이전(Previous) 명령어, 다음(Next) 명령어        |
| ` ⌃C`                | 현재 입력중인 작업 취소(Cancle) 이후 새 줄 실행 |
| `⌃L`  (`$ clear`)    | 터미널 깔끔하게 만들기(cLear)                   |
| `⌃A` (`fn +  ←`)     | 현재 입력중인 줄 맨 앞으로 커서 이동            |
| `⌃E` (`fn +  →`)     | 현재 입력중인 줄 맨 뒤(End)로 커서 이동         |
| `⌃U`                 | 현재 입력중인 줄 전체 삭제                      |
| `⌃W`                 | 현재 커서 기준, 단어 단위로 삭제 (Word)         |
| `⌃D` (`$ exit`)      | 터미널 및 다른 프로그램 종료                    |
|                      |                                                 |

### Exercises

1. 화면에 `Use "man echo"` 라고 출력하는 명령어를 입력하여 실제로 출력해보자.
2. `sleep` 이라고 하는 명령어의 매뉴얼 페이지를 읽고, 우리의 터미널을 5초간 잠쟤워 보자.
3. 이번에는 터미널을 100초간 잠재워 보고, 중간에 깨워 보도록 하자.
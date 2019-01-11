# 3.Inspecting files - 파일 검사

* 파일을 생성, 조작하는 법을 배웠으니, 이번에는 어떻게 파일의 내용을 검사하는지 배워보자
* 이번 챕터는 파일 컨텐츠가 너무 길어 한 화면안에 안나올 때 더욱 중요하다. (`cat`)



## 3.1 Downloding a file (through `curl -O`)

* 실제로 내용물이 긴 파일을 사용하기 위해, 직접 입력하기보다는, 인터넷에서 다운로드 받아보도록 하자.
* 물론 Command Line Interface를 통해서.
* 사용할 명령어는 `curl` 이다. 현재 자신의  OS 에 `curl` 프로그램이 설치되어 있나 `which` 명령어를 통해 확인해 보자.
* 사용법은 `which` 이후에 찾고싶은 프로그램 이름을 사용하면 된다.

``` shell
$ which curl
/usr/bin/curl
```

* 현재 Mac 에서는 다음과 같이 나오지만, 시스템마다 다를 수 있다. 만약 아무것도 출력되지 않거나 `not found` 라고 나오면, `curl` 을 설치해야 한다.
* Google 에 **install curl <사용중인 OS>** 라고 검색하여 방법을 찾아 설치하도록 하자

---

* `curl` 이 설치되었다면, 파일을 다운로드 받아보도록 하자.

```shell
$ curl -OL neovansoarer.github.io/files/sonnet.txt
$ ls -rtl
```

* Option 으로 대문자 `O` 와 `L` 이 있다. (자세한건  `man curl` 참조)
  * `man` 페이지 검색은 `/` 이후 찾고싶은 문자열을 입력 -> `enter`하고 `n` 키(next)로 넘겨가며 찾는다.
* `ls -rtl` 명령을 통해서 맨 마지막에 `sonnet.txt` 가 잘 추가되었는지 확인하자.
* `sonnet.txt` 는 총 2620 줄로, `cat` 명령어로 확인하기에는 너무 길다. 
* 남은 부분은 이 2620 줄의 txt 파일을 검사해 보는 것으로 채워질 예정이다.

---

### Exercises

1. 다음을 차례대로 해보자.
   1. `$ curl -I https://neovansoarer.github.io`을 통해 *HTTP 헤더(header)*만 가져와 보자. (`-I` 옵션 : Header만 가져오는 옵션)
   2. 이번에는 `https://github.com` 만 헤더정보를 가져와 보자.
   3. 둘의 [HTTP status code](https://ko.wikipedia.org/wiki/HTTP_%EC%83%81%ED%83%9C_%EC%BD%94%EB%93%9C)가 어떻게 다른가? 각 코드는 무엇을 의미하는지 검색해 보자.
2. `ls` 명령어를 활용하여 `sonnets.txt` 가 있는지 확인하고, 용량이 몇 byte 인지 확인해 보자. (long format을 활용하자)
3. 2번에서 확인한  용량은 byte로 확인하기에는 너무 크다. 좀더 편하게 확인하기 위해 kb(kilobyte) 로 환산해보자. (보통 1000 byte 를 1kb 로 치지만 정확하게는 2^10 = 1024bytes = 1kb이다.) `ls -l`에서 용량을 좀더 사람이 보기 쉽게(human-readable하게) 해주는 옵션이 `-h` 이다. `-h` 옵션을 사용하여 `sonnet.txt` 가 사람이 읽기 쉬운 용량으로 얼마인지 확인해 보자.



## 3.2 Making `head`s and `tail`s of it - 무언가를 이해하다. 

파일 검사에서 상호 보완적인 두가지 명령어가 `head` 와 `tail` 이다.

* `head` 는 첫 10줄을, 

```shell
$ head sonnets.txt
Shake-speare's Sonnets

I

From fairest creatures we desire increase,
That thereby beauty's Rose might never die,
But as the riper should by time decease,
His tender heir might bear his memory:
But thou contracted to thine own bright eyes,
Feed'st thy light's flame with self-substantial fuel,
```

* `tail` 은 마지막 10줄을 보여준다.

```shell
$ tail sonnets.txt
The fairest votary took up that fire
Which many legions of true hearts had warm'd;
And so the general of hot desire
Was, sleeping, by a virgin hand disarm'd.
This brand she quenched in a cool well by,
Which from Love's fire took heat perpetual,
Growing a bath and healthful remedy,
For men diseas'd; but I, my mistress' thrall,
  Came there for cure and this by that I prove,
  Love's fire heats water, water cools not love.
```

---

### Wordcount(`wc`) and pipes(`|`) - 단어 세기와 파이프(pipe)

그런데, `head` 와 `tail` 명령어가 출력하는 내용이 실제로 10줄인 것은 어떻게 알 수 있을까? 가장 간단한 방법은 손으로 세어 보는 것이지만, 그것보다는 좀 더 스마트한 방법을 사용해 보자. 바로 `wc` 명령어 이다.



* 일단 `wc` 명령어는 기본적으로 `wc <file>` 과 같이 사용하며, `<file>`전체를 분석(inspect)한다.
* `sonnets.txt` 파일을 `wc` 명령어를 통해 분석해보자.

```shell
$ wc sonnets.txt
    2620   17670   95635 sonnets.txt
```

* 3개의 숫자는 각각 몇 줄인지, 몇 단어인지, 몇 byte 인지를 의미한다. 즉 `sonnets.txt` 는
  * 2620 줄
  * 17670 단어
  * 95635 바이트 로 이루어져 있다.

---

지금까지 배운것 만으로 `$ head sonnets.txt` 의 결과물이 몇 줄, 몇 단어, 몇 byte 인지 알아 낼 수 있을까?

```shell
$ head sonnets.txt > sonnets_head.txt
$ wc sonnets_head.txt
      10      46     294 sonnets_head.txt
```

* 성공적이다. 위 방법은 당연히 `tail` 명령어에도 적용할 수 있다.
* 그런데 뭔가 불편하고, 스마트하지 않다. 굳이 새로운 파일을 만들지 않고 한번에 체크할 수는 없을까?
* 바로 Pipe (`|`) 를 사용하면 된다. (Enter 키 위의 back slash `\` 버튼을 `shift` 키와 누른다.)

---

```shell
$ head sonnets.txt | wc
      10      46     294
```

*  pipe 는 좌측 명령의 출력을 우측 명령의 입력으로 보낸다.
* 즉 `wc ` 명령 뒤에 `head sonnets.txt` 의 출력을 붙인 것이다.
* 하지만 `wc head sonnets.txt` 라고 쓸 수는 없다. 왜냐하면  `wc`명령은 뒤에 오는 단어(토큰이라 한다.)들을 각각의 파일이나 디렉토리라고 판단하기 때문.
  *  실제로 Error 출력이 `wc` 라는 명령을 처리하는데 있어  `head` 라는 파일이나 디렉토리가 없다라고 나온 이후,
  * `sonnets.txt` 의 앞 10줄(`head`)이 아닌 `sonnets.txt` 전체를 word count(`wc`) 하여 출력한다.

---

간단하게 리다이렉션(`>`) 과 파이프(`|`)를 정리해 보자면,

* 우선 지금까지 **입력 / 출력** 이라고 불렀던 것들은 정확하게 말하면 **표준 입력 스트림(standard input stream) / 표준 출력 스트림(standard output stream)** 이 정식 명칭이다.


* 리다이렉션(`>`)의 경우,
  * 리다이렉션은 **파일**과 관련이 있다.
  * `[command] > [file]` 일 경우 명령의 출력을 파일의 입력으로 보내 저장한다.
  * `[command] < [file] ` 일 경우 파일을 명령의 입력으로 보낸다. 그래서 `$ head sonnet.txt` 와 `$ head < sonnet.txt` 의 결과는 같다. (중요하지 않음)
* 파이프(`|`)의 경우,
  * 파이프는 **명령(command)**과 그에 의해 실행되는 **프로세스**와 관련이 있다.
  * `[command_A] | [command_B]` 에서 command_A 의 출력을 command_B 의 입력으로 보낸다.

---

### Exercises

1. `$ tail sonnets.txt` 의 결과를 `wc` 로 파이프하여 확인해 보자.
2. `$ man head` 를 실행하여 `$ head <file>` 할 때 기본적으로 설정된 `<file>` 의 첫 10줄이 아닌 처음 - N번째 줄 까지 보여주는 법을 찾아보자. 
3. 2 에서 배운걸 활용하여, `sonnets.txt` 의 챕터 `I` 만을 출력하되, 뒤에서 14줄만을 출력해 보도록 하자. (*Hint* : 커맨드는 `head -n <i> sonnets.txt | tail -n <j>` 와 같은 형태로 나타날 것이며, `<i>, <j>` 는 `-n` 옵션을 위한 정수 인자이다.)
4. `tail` 명령어의 가장 유용한 응용은, `tail -f` 명령어를 활용해서, 해당 파일이 실시간으로 변하는걸 보여주는 것이다. 이것은 특히 특정 웹 서버의 로그(log)를 감시(monitoring) 할 때 ([tailing the log file](https://ko.wikipedia.org/wiki/Tail)) 많이 쓰인다. 로그 파일을 시뮬레이팅 해보기 위해, 
   1. `$ ping google.com` 를 통해 구글에 핑을 보내보자. (`ping` 명령은 서버가 작동하는지 핑을 보내본다. 자세한 건 `man` 페이지 참조!) 
   2. 잘 응답하는걸 확인 하고  `⌃C` 로 해당 프로세스를 종료.
   3. 이번에는 해당 핑 로그를 파일에 저장해보자. `$ ping google.com > google.log`
   4. 그리고 새로운 터미널 탭을 켜고 `$ tail -f` 를 통해 `google.log` 파일을 모니터링 해보자.



## 3.3 `less` is more  

`less` 명령어는 우리가 지금까지 `man` 페이지에서 봐오던, 일종의 미리보기 창이다.

```shell
$ less sonnets.txt
Shake-speare's Sonnets

I

From fairest creatures we desire increase,
That thereby beauty's Rose might never die,
But as the riper should by time decease,
His tender heir might bear his memory:
But thou contracted to thine own bright eyes,
Feed'st thy light's flame with self-substantial fuel,
Making a famine where abundance lies,
Thy self thy foe, to thy sweet self too cruel:
Thou that art now the world's fresh ornament,
And only herald to the gaudy spring,
Within thine own bud buriest thy content,
And tender churl mak'st waste in niggarding:
 Pity the world, or else this glutton be,
 To eat the world's due, by the grave and thee.

II

When forty winters shall besiege thy brow,
And dig deep trenches in thy beauty's field,
sonnets.txt
```

대략 이렇게 생겼다. 

* `man` 페이지와 마찬가지로, `q` 를 누르면 나올 수 있고, 
* 방향키로 한줄 씩 이동,
*  `u` (up)키와  `d`(down) 키로 반 페이지씩 이동,
*  `f`(forward), `b`(back) 키로 한 페이지씩 이동할 수 있다.
* `/<string>` -> `enter` 을 통해 찾고싶은 문자열을 검색할 수 있으며, 
* 이후 `n` (next) 키로 다음 검색, `N`(shift-n) 키로 이전 검색이 가능하다.
  * `/rose` 를 통해 테스트 해보자.
* 마지막으로 `G`(shift - g) 키는 줄을 의미하는데
  * `1G` 는 첫번째 줄로,
  * `100G` 는 백번째 줄로,
  * `G` 는 파일의 가장 마지막 줄로 이동한다.

한번 `$ less sonnets.txt` 를 통해 위의 커맨드들을 입력하며 익숙해 져 보자.

| 명령어                | 설명                           | 예시    |
| --------------------- | ------------------------------ | ------- |
| ` ↑`,` ↓` 키          | 한줄 씩 이동                   |         |
| `spacebar`, `f` / `b` | 한 페이지 아래 / 위로 이동     |         |
| `d  ` / `u`           | 반 페이지 아래/위 로 이동      |         |
| `/<string>`           | 파일에서 `<string>` 검색       | `/rose` |
| `n`                   | 검색 이후에 다음 키워드로 이동 |         |
| `N`                   | 이전 키워드로 이동             |         |
| `q`                   | `less` 종료                    |         |

---

### Exercises

1. `sonnets.txt` 를 `less` 로 실행하고 , 3페이지 아래로 - 3페이지 위로 이동해 보자. 그리고 파일의 마지막 줄로 갔다가 첫 줄로 이동해 보자.
2. `All` 이라고 하는 문자열을 검색해 보자. 뒤로 이동하면서 몇번 등장하는지 세어보도록 하자. 그리고 `$ grep All sonnets.txt | wc` 라고 입력하고 본인이 세어본 결과와 비교해 보자.( `grep` 는 다음 챕터에서 배운다! )
3. `man` 페이지가 `less` 프로그램을 사용하는 덕분에, 이제 우리는 `man` 페이지를 좀 더 잘 활용할 수 있게 되었다. `ls` 의 매뉴얼 중에서 "size" 라는 문자열을 찾아서. 파일을 크기순서로 정렬하여 목록을 보여주는 명령어를 찾아보자. 



## 3.4 Grepping

* 파일의 내용을 검사하는 가장 좋은 방법은 `grep` 이다. `grep` 은  “**g**lobally search a **r**egular **e**xpression and **p**rint”' 의 줄임말이지만 전혀 중요하지 않다. ("regular expression" 이란 정규표현식이라고 번역하는데 나중에 다시 들어볼 기회가 있겠지만 지금단계에서는 무시하자.)
* `grep` 의 가장 널리 사용되는 부분은, 단순히 파일에서 부분 문자열을 찾는 것이다. 예를 들어 이전 섹션에서 우리는  `less` 로 `sonnets.txt` 를 열고, `/rose` 를 활용하여 "rose"를 검색해 보았다, 
* 하지만 `grep` 를 활용하면 바로 찾을 수 있다.

```shell
$ grep rose sonnets.txt
The rose looks fair, but fairer we it deem
As the perfumed tincture of the roses.
Die to themselves. Sweet roses do not so;
Roses of shadow, since his rose is true?
Which, like a canker in the fragrant rose,
Nor praise the deep vermilion in the rose;
The roses fearfully on thorns did stand,
  Save thou, my rose, in it thou art my all.
I have seen roses damask'd, red and white,
But no such roses see I in her cheeks;
```

* 다음과 같이 "rose" 가 들어있는 모든 줄만 모아서 바로 볼 수 있다.

---

* 당연하게도 이 출력을 pipe 하여 `wc` 명령의 입력으로 보낼 수 있다.

```shell
$ grep rose sonnets.txt | wc
      10      82     419
```

* `wc` 의 결과물이 말해주기를, "rose" 라고 하는 문자열을 포함하는 줄이 10줄이 있다고 한다.
* 하지만 "Rose" 라고 하는 문자열은 검색하지 않았다. 대/소문자 구분 때문이다.

---

* 이럴 경우 대/소문자를 구분하지 않고 grep 하는 법을 찾아보자.
* `$ man grep` 에서`case` 라는 문자열을 찾아서 읽자!

```shell
$ grep -i rose sonnets.txt | wc
      12      96     508
```

* `grep` 유틸리티는 위에 언급한 *regular-expression (정규표현식)* 와의 조합에서 가장 강력하게 활용할 수 있다. 
* 하지만 지금 우리가 `grep` 와 `grep -i` 만 사용해도 충분히 강력하다. 

---

위의 기능을 활용하여, 실제 개발에서 정말 많이 쓰이는 *grepping process* 에 대해 알아보도록 하자. `grep` 을 사용해 Unix 에서 동작하는 프로세스들을 특정 문자열로 필터링하는 것이다. (Linux, MacOS, iOS, Android 등의 Unix 기반의 시스템에서는 **연속적으로 동작하는 프로그램을 프로세스라고 한다.**) 



프로세스들 중에서 사용자에게 필요없거나 강제로 종료해야할 프로세스가 있는 경우, 

1. `ps aux` 명령어로 전체 프로세스를 확인하고, 

   * 여기서 `ps` 는 **p**rocess **s**tatus 이고, 이상한 이유로 인하여(`man ps` 확인) 옵션 `-aux` 는 `-` 없이 `aux`  로 사용해야 한다.

2. `grep <process_name> ` 명령으로 찾는 프로세스만을 잡아낸다.

   * Ruby on Rails 에서는 `spring` 이라고 하는 테스트 서버 프로그램을 프로세스 리스트에서 찾아 지우는 일이 빈번하다.
   *  만약 `spring` 이라고 하는 프로세스 찾고 싶다고 한다면 다음과 같이 사용한다. (아래의 출력화며은 가정)

   ```shell
   $ ps aux | grep spring
    ubuntu 12241 0.3 0.5 589960 178416 ? Ssl Sep20 1:46
    spring app | sample_app | started 7 hours ago
   ```

   * 컴퓨터마다 다르겠지만, 이런 식으로 해당 프로세스가 출력된다. 
   * 이때 가장 중요한 것은, 처음 나타나는 숫자인데, 이것이 프로세스 id, 줄여서 pid 라고 한다.

3. `top` 명령을 사용하면 가장 cpu 를 많이 점유하는 프로그램 순으로 프로세스들을 보여준다.

   * 뭔가 어려워 보이지만, 단순히 현재 컴퓨터 리소스 사용 현황과 프로세스들을 보여줄 뿐이다.

   ```shell
   $ top
   Processes: 392 total, 2 running, 390 sleeping, 1649 threads                                                  18:13:15
   Load Avg: 1.78, 1.62, 1.58  CPU usage: 1.8% user, 1.20% sys, 97.71% idle
   SharedLibs: 297M resident, 69M data, 75M linkedit.
   MemRegions: 89360 total, 5510M resident, 240M private, 2568M shared. PhysMem: 14G used (1995M wired), 2246M unused.
   VM: 1755G vsize, 1097M framework vsize, 5248(0) swapins, 6784(0) swapouts.
   Networks: packets: 4588362/5986M in, 2393008/265M out. Disks: 2587908/26G read, 2150385/28G written.

   PID    COMMAND      %CPU TIME     #TH   #WQ  #PORT MEM    PURG   CMPRS  PGRP  PPID  STATE    BOOSTS           %CPU_ME
   44467  top          3.3  00:00.63 1/1   0    23    4136K+ 0B     0B     44467 28371 running  *0[1]            0.00000
   44272  Google Chrom 0.0  00:00.05 8     1    73    9256K  0B     0B     44181 44181 sleeping *0[1]            0.00000
   44216  Google Chrom 0.0  00:02.42 17    1    152   88M    0B     0B     44181 44181 sleeping *0[1]            0.00000
   44215  Google Chrom 0.0  00:00.96 17    1    151   55M    0B     0B     44181 44181 sleeping *0[1]            0.00000
   44214  Google Chrom 0.0  00:02.09 17    1    151   83M    0B     0B     44181 44181 sleeping *0[1]            0.00000
   44209  Google Chrom 0.0  00:49.62 19    1    190   195M   8192B  0B     44181 44181 sleeping *0[1]            0.00000
   ```

   * `q` 로 종료한다.

4. 원하지 않는 프로세스를 죽이고 싶을 경우에는 `kill` 명령어와 종료코드 `15` 와(`man` 페이지 확인) pid 를 함께 사용하여 종료한다.

   ``` shell
   $ kill -15 12241
   ```

5. 만약 이렇게 일일이 pid 를 통해 종료하려는 것이 아니라, 모든 `spring`  프로세스들을 kill 하고 싶다면, `pkill` 명령을 사용할 수 있다.

   ```shell
   $ pkill -15 -f spring
   ```

   * `pkill` 은 pid 가 아닌 프로세스 이름으로 동작한다.
   * `-f` 옵션을 붙이면  `$ ps aux | grep spring` 의 모든 출력 결과중에 `spring` 있을 경우 `pkill` 하게 된다. 기본적으로는 프로세스 이름에 spring 이 있을 경우에만 `pkill`.

---

### Exercises

1. `man grep` 를 통해서 ,"line number" 문자열을 검색하고, `sonnets.txt` 에 "rose" 문자열이 등장하는 줄의 번호를 출력하는 명령을 구성해 보자.
2. 위의 결과에 따르면 2203 번째 마지막 "rose"가 있다. `less sonne.txt` 를 통해 해당 줄로 이동해 보자. (`nG`)
3. `head`  명령과 pipe 하여, `sonnets.txt` 에서 등장하는 첫 번째 "rose" 문장과 그 줄 번호만을 출력해 보자.



## 3.5 Summary

| Command                    | Description                  | Example                 |
| -------------------------- | ---------------------------- | ----------------------- |
| `curl`                     | URL 과 상호작용              | `$ curl -O`             |
| `which`                    | 프래그램의 위치(path) 출력   | `$ which curl`          |
| `head <file>`              | 파일의 앞부분 출력           | `$ head foo`            |
| `tail <file>`              | 파일의 뒷부분 출력           | `$ tail bar`            |
| `wc <file>`                | 줄, 단어, 바이트를 카운트    | `$ wc foo`              |
| `cmd1 | cmd2`              | `cmd1` 을 `cmd2`로 pipe      | `$ head foo | wc`       |
| `ping <url>`               | 해당 URL 로 핑을 보냄        | `$ ping google.com`     |
| `less <file>`              | 파일을 탐색할 수 있다.       | `$ less sonnets.txt`    |
| `grep <string> <file>`     | 해당 문자열을 파일에서 검색  | `$ grep foo bar.txt`    |
| `grep -i <s> <f>`          | 대소문자 상관없이 검색       | `$ grep -i foo bar.txt` |
| `ps`                       | 프로세스들을 보여줌          | `$ ps aux`              |
| `top`                      | 프로세스들을 정렬해서 보여줌 | `$ top`                 |
| `kill -<level> <pid>`      | 프로세스를 pid로 kill        | `$ kill -15 12345`      |
| `pkill -<level> -f <name>` | 프로세스를 이름으로 kill     | `$ pkill -15 -f spring` |

---

### Exercise

1. `history` 명령어는 지금까지 실행한 터미널 명령어들을 어느 정도까지 보여준다. 당신의 `history` 중 17 번째 명령어는 무엇이였는지 확인해 보자. (*Hint* : `less` 로 pipe)
2. 지금까지 실행한 명령어들은 모두 몇 단어일까? (*Hint* : `wc` 로 `history` pipe)
3. 지금까지  `curl`  명령어를 몇번 사용했나 세어보자.
4. `curl` 명령어에서 `-OL` 옵션이 뭔지 읽고 설명해보자.


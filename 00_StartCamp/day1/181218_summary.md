# 12. 18.  수업 정리

## 1. 개발환경 설정

* chocolatey
  * 윈도우 패키지 매니저
* python -v 3.6.7
* git
  * Version Control System
* vscode
  * Code Editor
* chrome
  * Browser

## 2. 단축키

* clear, ctrl + l

* exit(), ctrl + z

## 3. list

### list 접근하기

```python
list_in_list = [[1, 2], 
    [3, 4],
    [5, 6]]
print(list_in_list[1][1])
```

list에서 1차원 및 2차원 접근을 알자.

## 4. dict

### dict 접근하기

```python
dict_in_list = [
{
    'name' : 'A',
    'phone' : '1'
},
{
    'name' : 'B',
    'phone' : '2'
},
{
    'name' : 'C',
    'phone' : '3'
}
]

print(dict_in_list[1]['name'])
```

list와 dict에서 1차원 및 2차원 접근을 알자.

## 5.  function

공식문서를 읽어보자.

```python
min(...)
    min(iterable, *[, default=obj, key=func]) -> value
    min(arg1, arg2, *args, *[, key=func]) -> value
```

[]은 선택사항이다.

## 6. method

a.b() -> 주어.동사()

method : objective가 할 수 있는 "특정한" 활동

```python
lang = 'python'
lang.capitalize()
lang.replace('on', 'off')
```

1. lang은 바뀌지 않는다. 그러나

```python
my_list = [4, 7, 9, 1, 3, 6]
my_list.sort()
my_list.reverse()
my_list.append(8)
```

2. my_list가 바뀔 수도 있다.

```python
sorted_list = my_list.sort()
None = list
```

​	.sort()는 해당 객체만 바꾼다.

| class  | list        |
| ------ | ----------- |
| object | `[1, 2, 3]` |

## 7. package

pip install [패키지]

https://pypi.org/ -> 패키지 찾고 설치


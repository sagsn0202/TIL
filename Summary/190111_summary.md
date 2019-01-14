# ~190111

클래스: 새로운 데이터 타입을 만드는 설계도

(변수와 메소드를 묶은 논리적 그룹)

그 안에 클래스 변수와 클래스 메소드(클래스를 cls로 참조)

+a) 클래스 메소드는 데코레이터로 정의



오브젝트: 클래스라는 설계도를 통해 만들어진 데이터 타입

(클래스의 예제 중 하나; 인스턴스 뜻은 예제)

그 안에 인스턴스 변수와 인스턴스 메소드(오브젝트를 self로 참조)



+a) 스태틱 메소드: 첫번째 인자로 self나 cls를 받지 않는 클래스 내 메소드



메소드 호출

```
| Method resolution order: | object | Class | builtin.object
```

+a) `super()` : Class 내 method를 상속받으며 원하는 기능을 추가할 때 super(Class_name, self) 함수 활용

+a) `interfaces` : 다른 클래스 내 같은 메소드

+a) `dunder method` : 메소드 호출 개념 아래에서 이해. 파이썬 자체의 빌트인 타입을 참조(수정)하거나 클래스 내에 빌트인 타입과 같은 새로운 메소드 생성.

+a) `polymorphism` : `+`는 `object.__add__(self, other)` 와 같음. 

`2 + 4 == 6`   `3.1 + 2.1 == 5.2`  `"Is this " + "addition?" == "Is this addition?"`  `[1, 2] + [3, 4] == [1, 2, 3, 4]` 등 데이터 타입에 따라 다른 기능.
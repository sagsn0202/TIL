# Hyper Text Markup Language

클라이언트(Client) - 요청(request) -> 서버(Server)

클라이언트(Client) <- 응답(response) - 서버(Server)

## 요청

### IP(Internet Protocol) 

172.217.27.78 (8비트, 0 ~ 255까지의 숫자로 구성된 숫자의 집합) 

각자가 가지고 있는 주소와 동일

### 도메인(Domain) 

google.com (호스트명)

**네트워크상의 컴퓨터**를 식별

### URL(Uniform Resource Locator) 

https://www.google.co.kr/search?q=구글 (도메인 + 경로)

실제로 **해당 서버**에 저장된 자료의 위치

## 기본 구조

### DOCTYPE 선언부

사용하는 문서의 종류를 선언

```html
<!DOCTYPE html>
```

### html 요소

HTML 문서의 최상위 요소로 문서의 root를 뜻하며, head와 body 부분으로 구분

```html
<html lang="ko">
    <head>
        <meta charset="UTF-8">
        <title></title>
    </head>
    <body>
        
    </body>
</html>
```

#### head 요소

문서 정보를 담으며 브라우저에 나타나지 않음

og(미리보기 제목, 설명, 이미지 등)와 같은 메타태그 선언 + 

CSS 선언 혹은 외부 로딩 파일 지정

#### body 요소

브라우저 화면에 나타나는 정보

## Tag와 DOM Tree

(Document Object Model)

### 요소(Element)

태그 + 내용

```html
<h1>
    content
</h1>
```

#### 속성(Attribute)

id, class, style은 태그와 상관없이 모두 사용

```html
<a 속성명="속성값"></a>
```

#### self-closing element

닫는 태그가 없는 태그도 존재

```html
<img src="url" alt="url's image" />
```

### DOM Tree

태그는 중첩 사용가능하며, 부모-자식이나, 형제관계 등을 갖는다.

## Semantic Tags

의미를 가지는 태그들을 활용하기 위한 노력

| 태그    | 설명                                                   |
| ------- | ------------------------------------------------------ |
| header  | 문서 전체나 section의 header                           |
| nav     | navigation                                             |
| aside   | side에 위치, main content와 관련성이 적은 content      |
| section | content의 group, 일반적으로 h1 ~ h6를 가짐             |
| article | 문서 안에서 *독립적으로* 구분되는 영역(신문 등의 기사) |
| footer  | 문서 전체나 section의 footer                           |

[그림 참조](http://tcpschool.com/html/html5_element_semantic)

* Non semantic: div, span 등

## units

CSS 크기단위 내용 참조

## box model

CSS box model 내용 참조

## inline - block

CSS Display 내용 참조

# Cascading Style Sheet

```css
Selector {Property: Value;}
```

## 활용

### Inline

```html
<body>
	<Selector style="Property: Value">Content</h1>
</body>
```

### Embedding

```html
<head>
	<style>
	Selector {
    	Property: Value;
	}
	</style>
</head>
```

### Link file

```css
Selector {Property: Value;}
```

## 프로퍼티 값의 단위

### 1. 키워드

### 2. 크기단위

#### 2-1. px

픽셀을 기준으로 절대적인 사이즈(대부분 1/96인치)

#### 2-2. %

상속 및 기본값 기준으로 상대적인 사이즈

#### 2-3. em

1배 = 1em = 100%

[코드 참조](http://tcpschool.com/examples/tryit/tryhtml.php?filename=css_boxmodel_units_01)

#### 2-4. rem

최상위 요소(html)를 기준으로 상대적인 사이즈

#### 2-5.  Viewport

디바이스를 기준으로 상대적인 사이즈

| 단위 | 비고                              |
| ---- | --------------------------------- |
| vw   | 너비의 1/100                      |
| vh   | 높이의 1/100                      |
| vmin | 너비 또는 높이 중 작은 쪽의 1/100 |
| vmax | 너비 또는 높이 중 큰 쪽의 1/100   |

#### 3. 색깔

| 단위 | 비고                                                         |
| ---- | ------------------------------------------------------------ |
| RGB  | 기본색(Red, Green, Blue)의 0부터 255까지의 값, rgb(0, 0, 0)  |
| RGBA | The alpha parameter is a number between 0.0 (fully transparent) and 1.0 (fully opaque), rgb(0, 0, 0, 0.5) |
| HEX  | RGB 색상값을 각각 16진수로 변환, #ffffff                     |

## Box model

**“페이지의 모든 엘리먼트는 사각형 박스이다.”**

박스모델에서 엘리먼트의 전체 너비는

`margin-right` + `border-right` + `padding-right` + `width` + `padding-left` + `border-left` + `margin-left`

엘리먼트의 전체 높이는

`margin-top` + `border-top` + `padding-top` + `height` + `padding-bottom` + `border-bottom` + `margin-bottom` 

### Content

실제 내용

### Padding

Border 안쪽의 여백, 배경색 및 그림은 Padding까지 적용

### Border

테두리

### Margin

Border 바깥의 여백, 배경색 지정 불가

[그림 확인](http://tcpschool.com/css/css_boxmodel_boxmodel)

[코드 참조](http://tcpschool.com/examples/tryit/tryhtml.php?filename=css_boxmodel_boxmodel_01)

## Display

### block

화면 크기 전체의 가로폭을 차지(width: 100%)하므로, 

1. 항상 새로운 라인에서 시작하며
2. block 요소 내에 inline 요소를 포함할 수 있다.

예) div, h1 ~ h6, p, ol, ul, li, hr, table, form

#### \<div> 요소

 여러 요소들의 스타일을 한 번에 적용하기 위해 사용

### inline

content의 너비만큼 가로폭을 차지하므로,

1. 새로운 라인에서 시작하지 않으며, 문장의 중간에 들어갈 수 있고
2. width, height, margin-top, margin-bottom을 지정할 수 없다. **단**, 상, 하 여백은 line-height로 지정한다.

예) span, a, strong, img, br, input, select, textarea, button

#### \<span> 요소

텍스트의 특정 부분에 따로 스타일을 적용하기 위해 사용

### Inline-block

block과 inline 특징을 모두 가지므로,

1. block 에서의 width, height, margin(top, bottom)을 지정할 수 있으며
2. Inline 처럼 한 줄에 표시된다.

[코드 참조](http://tcpschool.com/examples/tryit/tryhtml.php?filename=css_position_display_02)

### None

해당 요소의 공간조차 사라진다.

## Visibility

| visible | hidden                    |
| ------- | ------------------------- |
| 기본값  | 보이지 않으나 공간은 존재 |

[코드 참조](http://tcpschool.com/examples/tryit/tryhtml.php?filename=css_position_display_03)

## Selector

### 전체 선택자

```css
* { color: red; }
```

### HTML 요소 선택자

```css
h2 { color: teal; text-decoration: underline; }
```

### class 선택자

```html
<h2 class="headings">이 부분에 스타일을 적용합니다.</h2>

<p>클래스 선택자를 이용하여 스타일을 적용할 HTML 요소들을 한 번에 선택할 수 있습니다.</p>

<h3 class="headings">이 부분에도 같은 스타일을 적용합니다.</h3>
```

```css
 .headings { color: deepskyblue; text-decoration: overline; }
```

### id 선택자

```html
<h2 id="heading">이 부분에 스타일을 적용합니다.</h2>
```

```css
#heading { color: sandybrown; text-decoration: line-through; }
```

### 그룹 선택자

```css
h2, h3, p { background-color: lightgray; }
```

### 결합 선택자

#### 자손 선택자(descendent selector)

해당 요소의 하위 요소 중에서 특정 타입의 요소를 모두 선택

```css
div p {스타일;}
```

#### 자식 선택자(child selector)

해당 요소의 **바로 밑에 존재하는** 하위 요소 중에서 특정 타입의 요소를 모두 선택

```css
div > p {스타일;}
```

[코드 참조](http://tcpschool.com/examples/tryit/tryhtml.php?filename=css_selector_combinators_02)

### 동위 선택자(sibling selector)

동위 관계란 HTML 요소의 계층 구조에서 같은 부모(parent) 요소를 가지고 있는 요소들을 의미

#### 일반 동위 선택자(general sibling selector)

해당 요소와 동위 관계에 있으며, 해당 요소보다 뒤에 존재하는 특정 타입의 요소를 모두 선택

```css
div ~ p {스타일;}
```

[코드 참조](http://tcpschool.com/examples/tryit/tryhtml.php?filename=css_selector_sibling_01)

#### 인접 동위 선택자(adjacent sibling selector)

해당 요소와 동위 관계에 있으며, 해당 요소의 **바로** 뒤에 존재하는 특정 타입의 요소를 모두 선택

```css
div + p {스타일;}
```

[코드 참조](http://tcpschool.com/examples/tryit/tryhtml.php?filename=css_selector_sibling_02)

## 시험 범위 외

### Position

#### static

기본적인 요소의 배치 순서에 따라, 부모 요소의 위치를 기준으로 배치

##### relative

static(기본 위치)를 기준으로 좌표 포로퍼티(top, bottom, left, right)를 사용하여 위치 이동

##### fixed

부모 요소와 관계없이, viewport를 기준으로 좌표 포로퍼티(top, bottom, left, right)를 사용하여 위치 이동, 즉 스크롤시 화면에서 사라지지 않음

##### absolute

(static을 제외한) 조상 요소를 기준으로 좌표 프로퍼티(top, bottom, left, right)만큼 이동

[코드 참조](http://tcpschool.com/examples/tryit/tryhtml.php?filename=css_position_position_05)

### 그 외

z-index, overflow, background-image, Font & Text

# Bootstrap

## Grid system

### Grid options

|                     | Extra small <576px | Small ≥576px | Medium ≥768px | Large ≥992px | Extra large ≥1200px |
| ------------------- | ------------------ | ------------ | ------------- | ------------ | ------------------- |
| Max container width | None (auto)        | 540px        | 720px         | 960px        | 1140px              |
| Class prefix        | `.col-`            | `.col-sm-`   | `.col-md-`    | `.col-lg-`   | `.col-xl-`          |
| # of columns        | 12                 |              |               |              |                     |

viewports 관련 `sm`, `md`, `lg`, `xl` 등 기본 요소 재점검

## Text

[공식 사이트](https://getbootstrap.com/docs/4.0/utilities/text/), [w3schools](https://www.w3schools.com/bootstrap4/bootstrap_typography.asp)

둘 중에 단순한 것 기준

## Colors

[공식 사이트](https://getbootstrap.com/docs/4.0/utilities/colors/), [w3schools](https://www.w3schools.com/bootstrap4/bootstrap_colors.asp)

둘 중에 단순한 것 기준

## Spacing

[공식 사이트](https://getbootstrap.com/docs/4.0/utilities/spacing/#notation)

### horizontal centering

[공식 사이트](https://getbootstrap.com/docs/4.0/utilities/spacing/#horizontal-centering)

`display: block`, `width`가 있을 때, `.mx-auto` 로 horizontal margins을  `auto`

```html
<div class="mx-auto" style="width: 200px;">
  Centered element
</div>
```

## Components

[한 눈에 보기](https://hackerthemes.com/bootstrap-cheatsheet/)에서 이해 안되는 부분은 [공식 사이트](https://getbootstrap.com/docs/4.0/components/alerts/) 참조

## Flex

[CSS](http://tcpschool.com/css/css3_expand_flexbox)

[Bootstrap](https://getbootstrap.com/docs/4.0/utilities/flex/)


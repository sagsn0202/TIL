```javascript
const numbers = [1, 2, 3, 4];

console.log(numbers[0]);
console.log(numbers.length);
console.log(numbers.reverse());

numbers.push('a');
console.log(numbers);
console.log(numbers.pop());

numbers.unshift('a');
console.log(numbers);
console.log(numbers.shift());

console.log(numbers.includes(1));

numbers.push('a', 'a');
console.log(numbers.indexOf('a'));
console.log(numbers.indexOf('b'));

console.log(numbers.join('-'));
console.log(numbers.join());

1
4
[ 4, 3, 2, 1 ]
[ 4, 3, 2, 1, 'a' ]
a
[ 'a', 4, 3, 2, 1 ]
a
true
4
-1
4-3-2-1-a-a
4,3,2,1,a,a
```

```javascript
console.log(typeof 1);
console.log(typeof typeof 1);
console.log(typeof (()=>{}));
console.log(typeof function(){});
console.log(typeof NaN);
console.log('a' + 100);
console.log('a' * 100);
console.log('123' + 1);
console.log('123' * 1);
console.log(100 / 0);
console.log(typeof (100 / 0));
console.log(typeof undefined);
console.log(typeof null);
console.log(typeof {});
console.log(typeof []);

number
string
function
function
number
a100
NaN
1231
123
Infinity
number
undefined
object
object
object
```

```javascript
const numbersEachCall = (numbers, callback) => {
    let acc;
    for (const number of numbers) {
        acc = callback(number, acc);
    }
    return acc;
};

const add = (number, acc=0) => acc + number;
const sub = (number, acc=0) => acc - number;
const mul = (number, acc=1) => acc * number;

console.log(numbersEachCall([1, 2, 3, 4, 5], add));
console.log(numbersEachCall([1, 2, 3, 4, 5], sub));
console.log(numbersEachCall([1, 2, 3, 4, 5], mul));

console.log(numbersEachCall([1, 2, 3, 4, 5], (number, acc=0) => acc + number));

15
-15
120
15
```

filter

```javascript
const products = [
    {name: 'cucumber', type: 'vegetable'},
    {name: 'banana', type: 'fruit'},
    {name: 'carrot', type: 'vegetable'},
    {name: 'tomato', type: 'fruit'},
];

const fruits = products.filter(product => {
    return product.type === 'fruit';
});

console.log(fruits);

[ { name: 'banana', type: 'fruit' },
  { name: 'tomato', type: 'fruit' } ]
```

find

```javascript
const avengers = [
    {name: 'Tony Stark'},
    {name: 'Steve Rogers'},
    {name: 'Thor'},
];

const search_avenger = avengers.find(avenger => avenger.name === 'Tony Stark');

console.log(search_avenger);

{ name: 'Tony Stark' }
```

forEach

```javascript
const colors = ['red', 'blue', 'green'];
colors.forEach(color => {
    console.log(color)
});

red
blue
green
```

map

```javascript
const numbers = [1, 2, 3];

const tripleNumbers = numbers.map(number => {
    return number * 3;
});

console.log(tripleNumbers);

[ 3, 6, 9 ]
```

axios

```javascript
const axios = require('axios');

// Make a request for a user with a given ID
axios.get('/user?ID=12345')
  .then(function (response) {
    // handle success
    console.log(response);
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  })
  .then(function () {
    // always executed
  });

// Optionally the request above could also be done as
axios.get('/user', {
    params: {
      ID: 12345
    }
  })
  .then(function (response) {
    console.log(response);
  })
  .catch(function (error) {
    console.log(error);
  })
  .then(function () {
    // always executed
  });  

// Want to use async/await? Add the `async` keyword to your outer function/method.
async function getUser() {
  try {
    const response = await axios.get('/user?ID=12345');
    console.log(response);
  } catch (error) {
    console.error(error);
  }
}
```

fetch

```javascript
const URL = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1";
fetch(URL)
    .then(res => {
    // lottoData 상수에 res 에 담긴 내용을 Object 로 변환하여 저장한다.
        const lottoData = res.json();
    // lottoData 를 return 한다.
        return lottoData;
    })
    .then(lottoData => {
    // lottoData 를 콘솔에 출력한다.
    console.log(lottoData);
    // lottoData 에서 추첨 날짜(drwNoDate)를 콘솔에 출력한다.
    console.log(lottoData.drwNoDate);
    });
```

XHR

```javascript
const URL = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1";
const XHR = new XMLHttpRequest();
XHR.open('GET', URL);
XHR.send();
XHR.addEventListener('load', e => {
    const rawData = e.target.response;
    // rawdata 를 콘솔에 출력한다.
    console.log(rawData);
    // lottoData 상수에 rawData 를 Object 로 변환하여 저장한다.
    const lottoData = JSON.parse(rawData);
    // lottoData 를 콘솔에 출력한다.
    console.log(lottoData);
    // lottoData 에서 추첨 날짜(drwNoDate)를 콘솔에 출력한다.
    console.log(lottoData.drwNoDate);
});
```

promise

```javascript
function sendXHR(url) {
  return new Promise((resolve, reject) => {
    XHR = new XHLHttpRequest();
    XHR.open('GET', url);
    XHR.onload = () => {
      if (XHR.status === 200) {
        resolve(XHR.responseText);
      } else {
        reject(XHR.status);
      }
    };
    XHR.send()
  });
}

sendXHR('http://SOME_URL.com')
	.then(result => console.log(`Good: ${result}`))
	.catch(statusCode => console.log(statusCode));
```
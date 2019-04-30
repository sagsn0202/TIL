const mul = (num1, num2) => num1 * num2;

const square = num => num ** 2;
console.log(square(3));

const sayHello = (name = 'ssafy') => `Hi ${name}!`;
console.log(sayHello());

console.log((num => num ** 2)(4));
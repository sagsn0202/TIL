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
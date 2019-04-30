// ES5 for loop
// var numbers = [1, 2, 3];
// var doubleNumbers = [];
//
// for (var i = 0; i < numbers.length; i++) {
//     doubleNumbers.push(numbers[i] * 2);
// }
//
// console.log(doubleNumbers);

// ES6+
const numbers = [1, 2, 3];

function double(n) {
    return n * 2;
}
const doubleNumbers = numbers.map(double);

const tripleNumbers = numbers.map(number => {
    return number * 3;
});

console.log(tripleNumbers);

const paints = [
    {color: 'red'},
    {color: 'blue'},
    {color: 'white'},
    {sound: 'wow'},
];

const pluck = (array, key) => array.map(elem => {
    return elem[key];
});

console.log(pluck(paints, 'color'));
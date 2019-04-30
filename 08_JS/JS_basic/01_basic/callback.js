const numbersEachAdd = numbers => {
    let acc = 0;
    for (const number of numbers) {
        acc += number;
    }
    return acc;
};
console.log(numbersEachAdd([1, 2, 3, 4, 5]));

const numbersEachSub = numbers => {
    let acc = 0;
    for (const number of numbers) {
        acc -= number;
    }
    return acc;
};
console.log(numbersEachSub([1, 2, 3, 4, 5]));


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
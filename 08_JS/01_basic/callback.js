function myFunc () {
    return n => n + 1
}

const num_101 = myFunc()(100);
console.log(num_101);


function func1(cb1, cb2) {
    console.log(1);
    cb1(cb2(cb1));
}

function func2(callback) {
    console.log(2);
}

function  func3(callback) {
    console.log(3);
}

func1(func2, func3);
// 1
// fucn2(func3(func2))

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
let i = 0;
while (i < 10) {
    console.log(i++);
}
i = 0;
while (i < 10) {
    console.log(++i);
}

for (let j = 0; j < 10; j++) {
    console.log(j);
}

// for (let j = 0; j < 10; j--) {
//     console.log(j);
// }

// for - of loop
let sum = 0;
for (let number of [1, 2, 3]) {
    sum += number;
}
console.log(sum);
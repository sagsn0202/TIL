// rest operator 가 없다면,
function addAll(a, b, c, d, e) {
    const numbers = [a, b, c, d, e];
    let sum = 0;
    for (const number of numbers) {
        sum += number;
    }
    return sum;
}

// rest 와 함께라면
function addAll(...numbers) {
    let sum = 0;
    for (const number of numbers) {
        sum += number;
    }
    return sum;
}

// spread operator
// 1,2,3,45,6,7,8 = [1,2,3,4] + [5,6,7,8]
// [1, 2, 3, 4, 5, 6, 7, 8] = [...[1, 2, 3, 4], ...[5, 6, 7, 8]]

function first0last100(...numbers) {
    return [0, ...numbers, 100];
}

first0last100(1,2,3,4,5,6,7);
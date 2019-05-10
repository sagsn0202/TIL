const myObject = {
    coffee: 'Americano',
    iceCream: 'Cookie and Cream',
};
console.log(typeof myObject);

const jsonData = JSON.stringify(myObject);
console.log(jsonData);
console.log(typeof jsonData);

const parseData = JSON.parse(jsonData);
console.log(typeof parseData);
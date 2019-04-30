// const nothing = () => {};
//
// console.log('start');
// setTimeout(nothing, 3000);
// console.log('end');

const logEnd = () => {
    console.log('end')
};

console.log('start');
setTimeout(logEnd, 3000);

const sleep3s = () => {
    setTimeout(() => console.log('Wake up!'), 3000);
};

console.log('Start Sleeping');
sleep3s();
console.log('End of Program');
const makeCoffee = (order, serve) => {
    let cup;
    setTimeout(() => {
        cup = order;
        serve(cup)
    }, 2000);
    return cup;
};

const myCoffee = makeCoffee('Latte', console.log);
console.log(myCoffee);
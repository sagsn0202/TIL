const This = {
    a: 'Hi',
    b () {
        return this.a;
    },
    c: this.a,

    data: {
        message: 'Hi',
    },
    methods: {
        greeting () {
            return this.message;
        },
    },
};

console.log(This.b());
console.log(This.c);
console.log(This.methods.greeting());
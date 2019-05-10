function hi () {

}

const bye = () => {

};

// js 객체는 키와 값으로
[1, 2, 3, 4, 5].length;

const me = {
    name: 'Hwang Eun Seok',
    phone: '01012345678',
    email: 'sagsn0202@naver.com',
    intro: function () {
        return `Hi my name is ${this.name}.`
    },
};
console.log(me.intro());

const you = {
    name: 'Jung Da Hye',
    phone: '01012345678',
    email: 'sagsn0202@naver.com',
    intro: () => {
        return `Hi my name is ${this.name}.`
    },
    wait: function () {
        setTimeout(() => {
            console.log(this.email)
        }, 1000)
    },
};
console.log(you.intro());
console.log(you.wait());
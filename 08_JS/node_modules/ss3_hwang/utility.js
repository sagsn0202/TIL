module.exports = {
    addAll (numbers=[]) {
        let sum = 0;
        numbers.forEach(number => sum += number);
        return sum;
    },
    subAll () {},
    mulAll () {},
    name: 'hwang',
};

phoneNumber = '01012345678';
module.exports.phoneNumber = phoneNumber;
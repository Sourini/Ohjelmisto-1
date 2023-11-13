let looper = 1
const number_list = []
let number = 0

while (looper != 0) {
    number = parseInt(prompt('enter a number. quit by entering any number again.'))
    if (number_list.includes(number)) {
        console.log(number + ' is already in the list, exiting loop.')
        break
    }
    else {
        number_list.push(number)
    }

}

number_list.sort((a,b) => a-b);

for (let i = 0; i < number_list.length; i++) {console.log(number_list[i])}
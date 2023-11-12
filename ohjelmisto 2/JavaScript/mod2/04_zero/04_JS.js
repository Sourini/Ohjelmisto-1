let number = 1
let number_list = []

while (number != 0) {number = parseInt(prompt('enter a number. quit entering numbers by entering 0'))
    number_list.push(number)}

number_list.sort((a,b) => a-b).reverse();

for (let i = 0; i < number_list.length; i++) {console.log(number_list[i])}
dice_list = []
let return_value = 0

function dice_throw(){
    let rolled_number = Math.floor(Math.random() * 6) + 1;
    return rolled_number;
}

while (return_value != 6) {
    return_value = dice_throw();
    dice_list.push(return_value)
}

const unordered_list = document.createElement('ul');

for (let i = 0; i < dice_list.length; i++) {
    const listed_roll = document.createElement('li');
    listed_roll.textContent = dice_list[i];
    unordered_list.appendChild(listed_roll);
}

document.body.appendChild(unordered_list)
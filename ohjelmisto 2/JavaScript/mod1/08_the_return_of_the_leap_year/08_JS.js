const start = parseInt(prompt('Enter the starting year: '));
const end = parseInt(prompt('Enter the ending year: '));
let year = start;
let year_list = [];

while (year <= end) {
    if (year % 4 === 0) {
        if (year % 100 !== 0 || (year % 100 === 0 && year % 400 === 0)) {
            year_list.push(year);
        }
    }
    year += 1;
}

const add_list = document.createElement('ul');

for (let i = 0; i < year_list.length; i++) {
    const add_to_the_list = document.createElement('li');
    add_to_the_list.textContent = year_list[i];
    add_list.appendChild(add_to_the_list);
}

document.body.appendChild(add_list);

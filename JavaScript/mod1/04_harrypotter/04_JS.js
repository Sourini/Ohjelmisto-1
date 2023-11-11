hat = Math.floor(Math.random()*4)+1;
if (hat == 1) {house = "Gryffindor"}
if (hat == 2) {house = "Slytherin"}
if (hat == 3) {house = "Hufflepuff"}
if (hat == 4) {house = "Ravenclaw"}




const name = prompt('Enter your name: ')

document.querySelector('#sum').innerHTML = name +', your house is ' + house + '!';

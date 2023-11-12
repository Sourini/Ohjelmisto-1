const number = parseInt(prompt('Enter a number: '));
let prime = 0

for (let i = 2; i < number; i++) {
    if (number % i == 0) {prime++}
}
if (prime > 0 || number == 1 || number == 0 || number == -1) {document.querySelector('#sum').innerHTML = number + " is not a prime number.";}
if (prime == 0 && number != 1 && number != 0 && number != -1) {document.querySelector('#sum').innerHTML = number + " is a prime number.";}
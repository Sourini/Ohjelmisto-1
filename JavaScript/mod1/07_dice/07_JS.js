const dice_amount = parseInt(prompt('Enter the number of dice: '));
let dice_throw = 0;
for (let i = 0; i < dice_amount; i++) {
  dice_throw += Math.floor(Math.random() * 6) + 1;
}

document.querySelector('#sum').innerHTML = "The sum result: " + dice_throw;

const dice_amount = parseInt(prompt('Enter the number of dice: '));
const dice_sum_target = parseInt(prompt('Enter the  the sum of the eye numbers of interest: '));

let hit_target = 0

for (let i = 0; i < 10000; i++) {
  let dice_throw = 0;
  for (let i = 0; i < dice_amount; i++) {
    dice_throw += Math.floor(Math.random() * 6) + 1;
      if (dice_throw == dice_sum_target) {hit_target++}
  }
}
percentage = (hit_target / 100)
document.querySelector('#sum').innerHTML = "The chance to get " + dice_sum_target + " with " + dice_amount + " dice is " + percentage.toFixed(2) + "%.";
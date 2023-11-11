const start = parseInt(prompt('Enter the starting year: '));
const end = parseInt(prompt('Enter the ending year: '));
let year = start;
let answer = 0
while (year < end){

if (year % 4 == 0) {
  if (year % 100 == 0) {
    if (year % 400 == 0) {leap = true}
    else {leap = false}
  }
  else {leap = true}
}
else {leap = false}

if (leap == true) {document.querySelector('#sum').innerHTML = year + "is a leap year";}
year += 1
}
const year = prompt('Enter the year: ')


if (year % 4 == 0) {
  if (year % 100 == 0) {
    if (year % 400 == 0) {leap = true}
    else {leap = false}
  }
  else {leap = true}
}
else {leap = false}

if (leap == true) {answer = " is a leap year."}
else if (leap == false) {answer = " is not a leap year."}
else {answer = "error?"}

document.querySelector('#sum').innerHTML = 'The year ' + year + answer;
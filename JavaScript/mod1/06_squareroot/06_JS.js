
const answer = confirm('Should I calculate the square root?');

if (answer == true)
{
  const numero = parseInt(prompt('Enter the number: '))
  if (numero < 0) {document.querySelector('#sum').innerHTML = "The square root of a negative number is not defined"}
  else {document.querySelector('#sum').innerHTML = 'The square root of ' + numero + " is " +Math.sqrt(numero)}
}
else {document.querySelector('#sum').innerHTML =  "The square root is not calculated."}
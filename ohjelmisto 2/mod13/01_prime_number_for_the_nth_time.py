from flask import Flask, request

app = Flask(__name__)
@app.route('/prime_number/<number>')
def prime_number(number):
    number = int(number)
    prime = False
    if number > 2:
        for i in range(2, number):
            if number % i != 0:
                prime = True
            elif number % i == 0:
                prime = False
                break
    elif number == 2:
        prime = True
    if number < 2:
        prime = False
    vastaus = {
        "Number": number,
        "isPrime": prime
    }
    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
from flask import Flask
import random

num = random.randint(0, 9)
print(num)
app = Flask(__name__)

@app.route("/")
def main():
    return 'Quess a number between 0 and 9, put it in the url'


@app.route("/<int:number>")
def checkNumber(number):

    if number == num:
        return 'you win'
    elif number > num:
        return 'the number is lower'
    else:
        return 'the number is higher'
app.run()

from flask import Flask, render_template
import datetime
import requests




app = Flask("__name__")

@app.route("/")
def home():
    today = datetime.date.today()
    year = today.strftime("%Y")
    return render_template('index.html', year=year)



@app.route("/<name>")
def guessgerder(name):
    response = requests.get(f"https://api.genderize.io/?name={name}")
    data = response.json()
    print(data)
    gender = data['gender']
    return render_template("index.html",name=name, gender=gender)

if __name__ == "__main__":
    app.run(debug=True)
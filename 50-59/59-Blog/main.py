from flask import Flask, render_template
import requests

response = requests.get("https://api.npoint.io/55c37884740210ffe60d")
response.raise_for_status()
blog_data = response.json()
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html", all_posts=blog_data)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for post in blog_data:
        if post["id"] == index:
            requested_post = post
    return render_template('post.html', post=requested_post)


app.run(debug=True)
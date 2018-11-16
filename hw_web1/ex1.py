from flask import render_template, Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "FUCK YOU flask"

@app.route("/about-me")
def about_me():
    content = "My name is Duong Anh Minh. I am 21 years old . I live in Ha noi and I have a crush on YOU"
    return render_template("aboutme.html", content = content)

if __name__ == "__main__":
    app.run(debug=True)
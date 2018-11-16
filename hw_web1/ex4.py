from flask import Flask,render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to our page bitches"

@app.route("/user/<username>")
def user(username):
    users = {
        'huy' :  {
                'name' : 'Nguyen Quang Huy',
                'age' : 29,
        },
        'tuananh' : {
                'name' : 'Huynh Tuan Anh',
                'age' : 22,
        },
    }
    if username == "huy":
        return render_template("huy.html")
    elif username == "tuananh":
        return render_template("tuananh.html")
    else :
        return render_template("usernotfound.html")

if __name__ == "__main__":

    app.run(debug=True)
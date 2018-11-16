
from flask import Flask,redirect, url_for

app = Flask(__name__)

@app.route("/")
def techkid():
    return redirect("https://techkids.vn/", code=302)



if __name__ == "__main__":

    app.run(debug=True)
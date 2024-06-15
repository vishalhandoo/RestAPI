from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def result(station, date):
    temperature = str('23' + " C")
    return {"station": station,
            "date": date,
            "temperature": temperature}


if __name__ == "__main__":
    app.run(debug=True)

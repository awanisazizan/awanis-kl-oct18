from flask import Flask, render_template,request
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/goodbye")
def goodbye():
    return "Goodbye World!"

@app.route("/")
def formPage():
    return render_template('formPage.html')


if __name__ == "__main__":
    app.run()
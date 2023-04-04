from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/dojo')
def dojo():
    return 'Dojo'


@app.route('/say/<name>')
def hello(name):
    name = str(name)
    return f"Hello {name}"


@app.route('/repeat/<num>/<word>')
def repeater(num, word):
    num = int(num)
    word = str(word)
    return word * num


@app.errorhandler(404)
def four_oh_four(oops):
    return "Sorry! No response. Try again."


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask

app = Flask(__name__)

operations = {
    '+':lambda a,b:a+b
}

@app.route('/<a>/<b>/<operator>')
def action(a,b,operator):
    result = None
    # Call correct operation and update result
    return str(result)
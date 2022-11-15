from flask import Flask
from numerical_integration import numericalIntegration

app = Flask(__name__)
n = [5, 10, 100, 1000, 10000, 100000, 1000000]

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/numericalintegralservice/<lower>/<upper>")
def getIntegral(lower, upper):
    results = []
    for i in n:
        results.append(numericalIntegration(float(lower), float(upper), i))
    return str(results)
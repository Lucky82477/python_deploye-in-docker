from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Dockerized Python on EC2!"

# Addition API
@app.route('/add')
def add():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        result = num1 + num2
        return jsonify({
            "operation": "addition",
            "num1": num1,
            "num2": num2,
            "result": result
        })
    except:
        return jsonify({"error": "Please provide num1 and num2"}), 400


# Subtraction API
@app.route('/subtract')
def subtract():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        result = num1 - num2
        return jsonify({
            "operation": "subtraction",
            "num1": num1,
            "num2": num2,
            "result": result
        })
    except:
        return jsonify({"error": "Please provide num1 and num2"}), 400


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

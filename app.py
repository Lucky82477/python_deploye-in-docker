from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add():
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))
    return jsonify({"result": num1 + num2})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

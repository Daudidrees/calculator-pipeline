from flask import Flask, render_template, request

app = Flask(__name__)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operation = request.form['operation']

    if operation == 'add':
        result = add(num1, num2)
        operation_symbol = '+'
    elif operation == 'subtract':
        result = subtract(num1, num2)
        operation_symbol = '-'
    elif operation == 'multiply':
        result = multiply(num1, num2)
        operation_symbol = '*'
    elif operation == 'divide':
        result = divide(num1, num2)
        operation_symbol = '/'

    return render_template('result.html', num1=num1, num2=num2, operation=operation_symbol, result=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)

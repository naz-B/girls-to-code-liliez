from flask import Flask,render_template,request

app = Flask(__name__)


facts = [
    'Abacus, an instrument to calculate or count by using sliding counters and rod is indeed the worlds first calculator.',
    'Basic calculators can do only addition, subtraction, multiplication and division mathematical calculations.',
    'The first commercial calculator to calculate addition, subtraction, multiplication, and division was manufactured in 1851.',
    'Blaise Pascal invented the calculator. In 1645 Pascal published an eighteen-page pamphlet describing his calculating machine.'
]



@app.route('/')
def home():
    return render_template('home.html' , facts=facts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/calculator')
def calculator():
    return render_template('calculator.html')

@app.route('/calculate' ,methods=['POST'])
def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])

    operation = request.form['operation']

    if operation == 'add':
        result = add(num1, num2)
    elif operation == 'subtract':
        result = subtract(num1, num2)
    elif operation == 'multiply':
        result = multiply(num1, num2)
    elif operation == 'divide':
        result = divide(num1, num2)
    return render_template('calculator.html', result=result)

def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2

if __name__ == '__main__':
    app.run(debug=True)








































from flask import render_template
from app import app
from modules import calculator

# @app.route('/')
# def index

@app.route('/<operator>/<number_1>/<number_2>')
def result (operator, number_1, number_2):
    int_1 = int(number_1)
    int_2 = int(number_2)

    if operator == "add":
        return f"{calculator.add(int_1, int_2)}"
    elif operator == "subtract":
        sub = calculator.subtract(int_1, int_2)
        return str(sub)
        # return f"{calculator.subtract(int_1, int_2)}"
    elif operator == "multiply":
        return f"{calculator.multiply(int_1, int_2)}"
    elif operator == "divide":
        return f"{calculator.divide(int_1, int_2)}"
    else:
        return None

# def result(operator, num_1, num_2):
#    calculate = Calculator(int(num_1)), (num_2))
#    return render_template('index.html', title ='Home' calculator = getattr(calculate, operator)()))
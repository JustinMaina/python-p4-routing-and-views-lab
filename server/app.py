from flask import Flask

app = Flask(__name__)

# Index route
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Print string route
@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)  # Print the string in the console
    return f'<h1>{parameter}</h1>'  # Display the string in the web browser

# Count route
@app.route('/count/<int:parameter>')
def count(parameter):
    result = '<br>'.join(str(i) for i in range(parameter + 1))  # Generate the range and join with <br> for new lines
    return f'<h1>{result}</h1>'

# Math operation route
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return '<h1>Invalid operation</h1>'
    
    return f'<h1>{num1} {operation} {num2} = {result}</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
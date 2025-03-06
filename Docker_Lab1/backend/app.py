from flask import Flask, render_template, request

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Multiply route
@app.route('/multiply', methods=['GET', 'POST'])
def multiply():
    if request.method == 'POST':
        # Get the numbers from the form
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        result = num1 * num2
        return render_template('multiply.html', result=result, num1=num1, num2=num2)
    return render_template('multiply.html', result=None)

# About route
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5055)

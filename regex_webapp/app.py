# app.py
from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form['test_string']
    regex_pattern = request.form['regex_pattern']
    matched_strings = re.findall(regex_pattern, test_string)
    return render_template('index.html', matched_strings=matched_strings)

@app.route('/validate_email', methods=['POST'])
def validate_email():
    email = request.form['email']
    if re.match(r'^[\w\.-]+@[\w\.-]+$', email):
        return render_template('index.html', email_result='Valid email address.')
    else:
        return render_template('index.html', email_result='Invalid email address.')

if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0')

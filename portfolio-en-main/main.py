# Import
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

# Running content page
@app.route('/')
def index():
    return render_template('index.html')


# Dynamic skills
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_HTML = request.form.get('button_HTML')
    button_discord = request.form.get('button_discord')
    button_database = request.form.get('button_database')
    return render_template('index.html', button_python=button_python, button_HTML=button_HTML, button_discord=button_discord, button_database=button_database)
    
if __name__ == "__main__":
    app.run(debug=True)

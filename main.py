from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name

@app.route('/')
def products():
        products = ["Apple 3.20zl", "Banana 4.50zl", "Orange 2.12zl", "Grapes 5.99zl"]
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        html = "<h1>Welcome to our shop !</h1>"
        html += f"<p>Current server time: {current_time}</p>"
        html += "<h2>Our Products:</h2><ul>"
        for product in products:
            html += f"<li>{product}</li>"
        html += "</ul>"
        
        return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
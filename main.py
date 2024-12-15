from flask import Flask

app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name

@app.route('/')
def products():
    product_list = ["Apple", "Banana", "Orange"]
    html = "<h1>Lista produktów</h1><ul>"
    for p in product_list:
        html += f"<li>{p}</li>"
    html += "</ul>"
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
from flask import Flask, render_template
import json

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    with open('database/films.json') as file:
        data = json.load(file)

    return render_template('index.html', films=data)

if __name__ == '__main__':
    app.run()

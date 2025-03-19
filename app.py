from flask import Flask, render_template
from routes.submit import submit_user

app = Flask(__name__)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    return submit_user()

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')

    if "@" not in email:
        return jsonify({"error": "Invalid email address"}), 400

    if not phone.isdigit() or len(phone) != 10:
        return jsonify({"error": "Phone number must be exactly 10 digits"}), 400

    return jsonify({"message": "Data received!", "name": name, "email": email, "phone": phone})

if __name__ == '__main__':
    app.run(debug=True)

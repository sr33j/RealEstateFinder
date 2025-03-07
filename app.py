from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    try:
        return "Welcome to the Real Estate Finder!"
    except Exception as e:
        return str(e), 500

@app.route('/properties')
def properties():
    try:
        # Dummy data for example purposes
        properties = [
            {'id': 1, 'name': 'Cozy Cottage', 'location': '123 Main St'},
            {'id': 2, 'name': 'Luxury Villa', 'location': '456 Elm St'}
        ]
        return jsonify(properties)
    except Exception as e:
        return str(e), 500

@app.errorhandler(404)
def not_found(error):
    return "404 Not Found", 404

@app.errorhandler(500)
def internal_error(error):
    return "500 Internal Server Error", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
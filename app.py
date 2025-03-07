from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

@app.route('/')
def index():
    try:
        return render_template('index.html', title='Real Estate Finder')
    except Exception as e:
        app.logger.error(f"Error in index route: {str(e)}")
        return jsonify({"error": "An error occurred"}), 500

@app.route('/properties')
def properties():
    try:
        # Dummy data for demonstration
        properties = [
            {"id": 1, "name": "Beautiful House", "location": "City A"},
            {"id": 2, "name": "Luxury Apartment", "location": "City B"}
        ]
        return jsonify(properties)
    except Exception as e:
        app.logger.error(f"Error in properties route: {str(e)}")
        return jsonify({"error": "An error occurred"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
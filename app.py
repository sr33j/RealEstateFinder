from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        return str(e), 500

@app.errorhandler(404)
def page_not_found(e):
    return jsonify(error="Page not found"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return jsonify(error="Internal Server Error"), 500

@app.errorhandler(403)
def forbidden(e):
    return jsonify(error="Forbidden"), 403

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
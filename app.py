from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        return str(e), 500

@app.errorhandler(404)
def not_found_error(error):
    return 'Page not found', 404

@app.errorhandler(500)
def internal_error(error):
    return 'Internal Server Error', 500

@app.errorhandler(Exception)
def unhandled_exception(e):
    return 'An unexpected error occurred', 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
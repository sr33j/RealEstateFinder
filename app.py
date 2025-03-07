from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', title='Real Estate Properties', description='A website to find real estate properties')

if __name__ == '__main__':
    app.run(debug=True)
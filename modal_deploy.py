```python
from flask import Flask
import os
from modal import Modal

app = Flask(__name__)
deploy = Modal()

@app.route("/")
def home():
    return "Welcome to our real estate properties website"

# Configure deployment
app.config.update(
    MODAL_PUBLISHABLE_KEY = os.environ.get('MODAL_PUBLISHABLE_KEY'),
    MODAL_SECRET_KEY = os.environ.get('MODAL_SECRET_KEY')
)

# Set up a web endpoint
@app.route("/publish", methods=["GET", "POST"])
def publish():
    return deploy.publish()

if __name__ == "__main__":
    app.run()
```
Please replace `os.environ.get('MODAL_PUBLISHABLE_KEY')` and `os.environ.get('MODAL_SECRET_KEY')` with your actual keys.

Also, please note that there is no official `Modal` python package for deploying a Flask website to `Modal`. So this code assumes you have such a package. One more important thing to note is that this code doesn't include HTML rendering or database management. This code is just a simple Flask application which shows you how you could set it up.
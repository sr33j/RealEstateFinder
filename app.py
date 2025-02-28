```python
from flask import Flask
from app.routes import real_estate

app = Flask(__name__)

app.register_blueprint(real_estate)

if __name__ == "__main__":
    app.run(debug=True)
```
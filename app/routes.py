```python
from flask import Flask, render_template, request, redirect, url_for
from forms import SearchForm
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

@app.route('/', methods=['GET', 'POST'])
def home():
    form = SearchForm()
    properties = None
    if form.validate_on_submit():
        location = form.location.data
        type = form.type.data
        min_price = form.min_price.data
        max_price = form.max_price.data

        # assuming the API to get properties accepts these parameters
        response = requests.get('http://your-api-url', params={
            'location': location,
            'type': type,
            'min_price': min_price,
            'max_price': max_price
        })

        if response.status_code == 200:
            properties = response.json()

    return render_template('home.html', form=form, properties=properties)

@app.route('/property/<id>')
def property(id):
    response = requests.get(f'http://your-api-url/{id}')
    property = None
    if response.status_code == 200:
        property = response.json()
    return render_template('property.html', property=property)

if __name__ == '__main__':
    app.run(debug=True)
```

Please replace `'http://your-api-url'` and `'your-secret-key'` with the actual values. This script assumes that we have a `forms.py` with the form `SearchForm` defined, and that the templates 'home.html' and 'property.html' exist and are properly formatted.
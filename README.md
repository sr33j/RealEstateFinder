```markdown
# Real Estate Finder

A Flask-powered website designed to help users search and discover real estate properties.

## Purpose

This website serves as a tool that allows users to locate real estate properties. Whether searching for a new place to live, an investment property, or a vacation getaway location, the Real Estate Finder will streamline the search process by presenting all the necessary information such as property location, description, photos, pricing, and contact information. 

## Installation 

Follow the steps below to setup the project:

1. Make sure you have Python installed on your machine. You could download Python [here](https://www.python.org/).

2. Install Flask by running the following command in your terminal:

    ```
    pip install flask
    ```

3. Clone this repository:
  
    ```
    git clone <this-repository-url>
    ```
   
4. Go to the cloned repository:
  
    ```
    cd <repository-name>
    ```

## Run the website locally

After installation, you can run the website locally by using the commands below:

1. Set `FLASK_APP` environment variable to main.py:

    ```
   export FLASK_APP=main.py
    ```

2. Run the flask web server:

    ```
    flask run
    ```

3. Finally, open your browser and navigate to `http://127.0.0.1:5000`.

## Deployment using Modal

With Modal, you can deploy your Flask applications effectively. Follow the steps below:

1. First, install Modal by running the following command in your terminal:

    ```
    pip install modal
    ```

2. Next, initialize your Flask application with Modal:

    ```
    modal init
    ```

3. Finally, deploy your application:

    ```
    modal deploy
    ```

## Key Features

- Property Search: Our easy-to-use search functionality helps you find properties based on specific criteria.

- Location-based results: View the location of each property on an interactive map.

- Detailed Property Information: Each property includes detailed information, including a description, photos, price, and more.

- Contact the Seller: Provides a Contact form for each listing to connect potential buyers to sellers.

- User Profiles: Users can create profiles to save their favorite listings and have personalized recommendations.

Enjoy your house hunting experience!

```
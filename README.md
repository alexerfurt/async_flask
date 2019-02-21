async_flask_app

===========

Simple app demonstrating asynchronous flask communication, starting with HTTP requests that are send to and fetched by the flask webserver which updates the frontend instantaneously.

This repository is based on Shane Lynn's async_flask repo (https://github.com/shanealynn/async_flask)

To use - please clone the repository and then set up your virtual environment using the requirements.txt file with pip and virtualenv. You can achieve this with:


    git clone https://github.com/alexerfurt/async_flask_app
    cd async_flask_app
    pip install flask-socketio
    pip install -r requirements.txt

Start the application with:

<code>
python application.py
</code>

And visit http://localhost:5000 to see the updating numbers.

TODO: HTTP POST REQUEST from an example app to the backend. Use the following curl command for testing in the meantime:
  "curl --header "Content-Type: application/json"   --request POST   data '{"product_name": str, "confidence": int}'   http://localhost:5000/newstate"

# Modified counter-service.py (with bonus features)

from flask import Flask, request
import os

app = Flask(__name__)
counter = {'post': 0, 'get': 0}  # Separate counters for GET and POST

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        counter['post'] += 1
        return f"POST counter increased. POST count: {counter['post']}"
    else:
        counter['get'] += 1
        return f"Current counters - GET: {counter['get']}, POST: {counter['post']}"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 443))  # Default to 443 for bonus task
    app.run(debug=True, port=port, host='0.0.0.0', ssl_context='adhoc')
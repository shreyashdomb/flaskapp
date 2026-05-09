from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    """
    Main endpoint that returns a greeting message.
    
    Returns:
        JSON: A dictionary containing a greeting message
    """
    return jsonify({"message": "Hello, World!"})


@app.route('/health')
def health():
    """
    Health check endpoint for monitoring application status.
    Used by load balancers and orchestration platforms to verify service availability.
    
    Returns:
        JSON: A dictionary with the health status
    """
    return jsonify({"status": "healthy"})


@app.route('/product')
def product():
    """
    Product information endpoint that points to the product page.
    This endpoint provides information about product navigation.
    
    Returns:
        JSON: A dictionary containing product page navigation information
    """
    return jsonify({"message": "Pointing to product page"})


if __name__ == '__main__':
    # Run Flask development server on all interfaces (0.0.0.0) at port 5000
    # This allows the app to be accessible from outside the container/machine
    app.run(host='0.0.0.0', port=5000)

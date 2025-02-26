from flask import Flask, request, jsonify

app = Flask(__name__)

# This is the endpoint that will handle the incoming webhook POST requests
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json  # Parse the incoming JSON data
    print("Received Webhook Data:", data)  # For testing, we'll print it to the console
    return jsonify({"status": "success", "message": "Webhook received successfully!"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)

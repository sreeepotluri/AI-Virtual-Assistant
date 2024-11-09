from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

# Set up OpenAI API credentials securely (using environment variable)
openai.api_key = os.getenv('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')  # Make sure to set this environment variable

# Define the default route to return the index.html file
@app.route("/")
def index():
    return render_template("index.html")

# Define the /api route to handle POST requests
@app.route("/api", methods=["POST"])
def api():
    try:
        # Get the message from the POST request
        data = request.get_json()  # get JSON directly
        message = data.get("message")
        
        if not message:
            return jsonify({"error": "Message is required"}), 400
        
        # Send the message to OpenAI's API and receive the response
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message}]
        )
        
        # Return the content of the response
        response_message = completion.choices[0].message['content']
        
        return jsonify({"response": response_message})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

    

# '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'

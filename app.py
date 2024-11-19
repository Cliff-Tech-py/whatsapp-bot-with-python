from flask import Flask, request
from googlesearch import search
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/", methods=["POST"])
def bot():
    # User input from the incoming message
    user_msg = request.values.get('Body', '').lower()

    # Creating an object of MessagingResponse
    response = MessagingResponse()

    # Adding "geeksforgeeks.org" to the search query
    q = user_msg + " site:google.com"

    # List to store search results
    search_results = []

    # Searching for URLs
    try:
        for i in search(q, num_results=3):
            search_results.append(i)
    except Exception as e:
        return str(response.message(f"Error while fetching search results: {str(e)}"))

    # Adding the search results to the response
    response.message(f"--- Results for '{user_msg}' ---")
    for result in search_results:
        response.message(result)

    return str(response)

if __name__ == "__main__":
    app.run(debug=True)

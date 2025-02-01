import requests

API_URL = "http://127.0.0.1:5003/chat"
question = {"question": "What is authentication?"}

response = requests.post(API_URL, json=question)

print("Chatbot Response:", response.json().get("answer", "No response."))

# Test Related  
# suggestions_url = "http://127.0.0.1:5003/suggest"
# suggestions_response = requests.post(suggestions_url, json=question)

# print("Suggested Questions:", suggestions_response.json().get("related_questions", []))

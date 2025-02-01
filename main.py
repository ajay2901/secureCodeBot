# # from utils.preprocess import preprocess
# # from utils.model import Chatbot

# # # Initialize the chatbot
# # chatbot = Chatbot()

# # print("Chatbot: Hi! Ask me anything. Type 'exit' to quit.")
# # while True:
# #     user_input = input("You: ")
# #     if user_input.lower() == 'exit':
# #         print("Chatbot: Goodbye!")
# #         break
# #     response = chatbot.get_response(user_input)
# #     print(f"Chatbot: {response}")

# from utils.chatbot_logic import initialize_chatbot
# from fastapi import FastAPI
# from pydantic import BaseModel
# from fastapi.middleware.cors import CORSMiddleware

# app = FastAPI()

# # CORS for frontend communication
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Change this to your frontend URL for better security
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# def main():
#     print("Chatbot: Hi! I can answer your questions. Type 'exit' to quit.")
#     # Initialize chatbot with dataset path
#     chatbot = initialize_chatbot('data/Application_Security_500_QA.csv')

#     while True:
#         user_input = input("You: ").strip()
#         if user_input.lower() == 'exit':
#             print("Chatbot: Goodbye!")
#             break
#         # Fetch and display the answer
#         response = chatbot.get_answer(user_input)
#         print(f"Chatbot: {response}")

# if __name__ == "__main__":
#     main()


from fastapi import FastAPI
from pydantic import BaseModel
from utils.chatbot_logic import initialize_chatbot
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize chatbot
chatbot = initialize_chatbot('data/Application_Security_500_QA.csv')

class QuestionRequest(BaseModel):
    question: str

@app.post("/chat")
def chat(request: QuestionRequest):
    """Handles user questions and returns chatbot responses."""
    response = chatbot.get_answer(request.question)
    return {"answer": response}

# @app.post("/suggest")
# def suggest_questions(request: QuestionRequest):
#     """Returns related questions."""
#     suggestions = chatbot.suggest_related_questions(request.question)
#     return {"related_questions": suggestions}

@app.get("/")
def home():
    return {"message": "Chatbot API is running!"}

if __name__ == '__main__':
    app.run(debug=True)
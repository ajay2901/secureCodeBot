import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .preprocess import preprocess

class Chatbot:
    def __init__(self, dataset_path='data/Application_Security_500_QA.csv'):
        self.data = pd.read_csv(dataset_path)
        self.questions = self.data['Question'].tolist()
        self.answers = self.data['Answer'].tolist()
        self.processed_questions = [preprocess(q) for q in self.questions]
        self.vectorizer = TfidfVectorizer()
        self.X = self.vectorizer.fit_transform(self.processed_questions)
    
    def get_response(self, user_input):
        user_input_processed = preprocess(user_input)
        user_vector = self.vectorizer.transform([user_input_processed])
        similarities = cosine_similarity(user_vector, self.X)
        max_similarity_index = similarities.argmax()

        if similarities[0, max_similarity_index] > 0.2:  # Threshold for matching
            return self.answers[max_similarity_index]
        else:
            return "I'm sorry, I don't understand your question."

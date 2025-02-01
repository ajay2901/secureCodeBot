from sentence_transformers import SentenceTransformer, util
import torch

class NLPChatbot:
    def __init__(self, dataset):
        self.dataset = dataset
        self.questions = dataset['Question'].tolist()
        self.answers = dataset['Answer'].tolist()
        
        # Load a pre-trained model for embeddings
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        
        # Compute embeddings for all questions
        self.question_embeddings = self.model.encode(self.questions, convert_to_tensor=True)

    def get_answer(self, user_question):
        # Compute embedding for user question
        user_embedding = self.model.encode(user_question, convert_to_tensor=True)
        
        # Compute cosine similarity with all questions
        similarities = util.cos_sim(user_embedding, self.question_embeddings)
        
        # Find the most similar question
        max_similarity, idx = torch.max(similarities, dim=1)
        if max_similarity >= 0.4:  # Adjust threshold as needed
            return self.answers[idx.item()]
        else:
            return "I'm sorry, I couldn't find an answer to your question. Can you rephrase?"
        
    def suggest_related_questions(self, user_question, top_k=3):
        """Suggests the top K most similar questions."""
        user_embedding = self.model.encode(user_question, convert_to_tensor=True)
        similarities = util.cos_sim(user_embedding, self.question_embeddings)
        
        # Get top-k similar questions
        top_k_indices = torch.topk(similarities, k=top_k).indices.tolist()
        return [self.questions[idx] for idx in top_k_indices]

# Helper to initialize chatbot
def initialize_chatbot(filepath):
    from utils.preprocess import load_data
    data = load_data(filepath)
    return NLPChatbot(data)



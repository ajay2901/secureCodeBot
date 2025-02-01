# import nltk
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords

# nltk.download('punkt')
# nltk.download('stopwords')

# stop_words = set(stopwords.words('english'))

# def preprocess(text):
#     tokens = word_tokenize(text.lower())
#     return ' '.join([word for word in tokens if word.isalnum() and word not in stop_words])


import pandas as pd

def load_data(filepath):
    # Load the CSV file into a DataFrame
    data = pd.read_csv(filepath)
    # Ensure correct columns exist
    if set(['Label', 'Question', 'Answer']).issubset(data.columns):
        return data
    else:
        raise ValueError("CSV must contain 'Topic', 'Question', and 'Answer' columns.")


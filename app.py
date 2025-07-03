



# run : streamlit run app.py

import streamlit as st
import pickle
import time
from sklearn.feature_extraction.text import TfidfVectorizer
# converting the textual data to numerical data
vectorizer = TfidfVectorizer()


st.title("Twitter Sentimental Analysis")

# load model
model = pickle.load(open('trained_model.pkl', 'rb'))


tweet = st.text_input("Enter your tweet")

submit = st.button('Predict')

if submit:
    start = time.time()
    X_new_vectorized = vectorizer.transform([tweet])
    prediction = model.predict(X_new_vectorized)
    # prediction = model.predict([tweet])
    end = time.time()
    st.write('Prediction time taken: ', round(end-start, 2), 'seconds')
    
    print(prediction[0])
    st.write(prediction[0])

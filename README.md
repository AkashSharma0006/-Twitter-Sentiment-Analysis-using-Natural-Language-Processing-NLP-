# -Twitter-Sentiment-Analysis-using-Natural-Language-Processing-NLP-
# 🐦 Twitter Sentiment Analysis using Naive Bayes & NLP

This project performs **Sentiment Analysis on Twitter data** using **Natural Language Processing (NLP)** techniques and a **Naive Bayes classifier**. The final model is deployed as a user-friendly web app using **Streamlit**, where users can enter tweets and get real-time sentiment predictions.

---

## 🚀 Demo

🔗 [Try it on Streamlit (if deployed)](https://share.streamlit.io/your-app-link)

---

## 📂 Dataset

- **Source:** [Sentiment140 Dataset on Kaggle](https://www.kaggle.com/datasets/kazanova/sentiment140)
- **Size:** 1.6 million tweets
- **Target classes:**  
  - `0` = Negative  
  - `2` = Neutral  
  - `4` = Positive  

> The target labels were converted to:
- `0` = Negative  
- `1` = Positive  
- (Neutral class was removed in preprocessing for binary classification)

---

## 🧠 Project Features

- Preprocessing using **NLTK**: stopwords removal, stemming
- Feature extraction using **TF-IDF Vectorization**
- Classification using **Multinomial Naive Bayes**
- Model Evaluation using **accuracy, confusion matrix, classification report**
- Web interface built using **Streamlit**
- Model and vectorizer serialized using **Pickle**

---

## 🛠 Tech Stack

| Component       | Tools/Packages Used                  |
|----------------|---------------------------------------|
| Language        | Python                               |
| Libraries       | scikit-learn, pandas, numpy, nltk     |
| Model           | Multinomial Naive Bayes              |
| Frontend        | Streamlit                            |
| Deployment      | Local / Streamlit Cloud              |
| Serialization   | Pickle                               |

---

## 📁 Project Structure


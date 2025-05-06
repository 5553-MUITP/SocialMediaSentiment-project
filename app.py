# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sentiment_analyzer import analyze_sentiment  # Import the analyze_sentiment function

st.title("📊 Social Media Sentiment Analyzer")

uploaded_file = st.file_uploader("Upload a CSV file with a column named 'tweet'", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, encoding='ISO-8859-1')

    df['Sentiment'] = df['tweet'].apply(analyze_sentiment)

    st.subheader("Sample Data")
    st.write(df.head())

    st.subheader("Sentiment Distribution")
    sentiment_counts = df['Sentiment'].value_counts()

    fig, ax = plt.subplots()
    sentiment_counts.plot(kind='bar', color=['green', 'orange', 'gray'], ax=ax)
    plt.title("Sentiment Distribution")
    plt.xlabel("Sentiment")
    plt.ylabel("Number of Tweets")
    st.pyplot(fig)

    st.subheader("Example Tweets")
    for sentiment in ['Positive', 'Negative', 'Neutral']:
        st.markdown(f"**{sentiment} Tweets**")
        examples = df[df['Sentiment'] == sentiment]['tweet'].head(2).tolist()
        for tweet in examples:
            st.write(f"- {tweet}")

st.markdown("This tool uses TextBlob to classify tweets as Positive, Neutral, or Negative based on polarity scores.")

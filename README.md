
# 📊 Social Media Sentiment Analyzer

This is a **Social Media Sentiment Analyzer** built using **Streamlit**, **TextBlob**, and **Pandas**. The app allows users to upload a CSV file containing tweets, performs sentiment analysis, and displays the results visually. The app categorizes tweets into **Positive**, **Neutral**, or **Negative** sentiments and shows a sentiment distribution chart.

## 🛠 Requirements

Before you can run this app, you need to install the required Python libraries.

### **Dependencies**:
- Python >= 3.6
- `streamlit` - for creating the web interface
- `textblob` - for performing sentiment analysis
- `pandas` - for handling CSV file data
- `matplotlib` - for generating charts

You can install the required dependencies by running:

```bash
pip install -r requirements.txt
```

Where `requirements.txt` contains:

```txt
streamlit
textblob
pandas
matplotlib
```

## 🚀 Running the App

1. **Clone the repository** or download the project files.
2. **Navigate to the project directory** in the terminal.
3. Run the following command to start the Streamlit app:

   ```bash
   streamlit run app.py
   ```

4. Once the app is running, open your browser and go to `http://localhost:8501` to see the app in action.

### **Using the App**:
1. Upload a CSV file containing tweets (make sure the file has a column named `'tweet'`). Sample (TWEETS.csv given)
2. The app will display:
   - A sample of the uploaded data.
   - A sentiment distribution chart showing the counts of **Positive**, **Neutral**, and **Negative** tweets.
   - Example tweets for each sentiment type.

---

## 🧪 Running Unit Tests for Sentiment Analysis

The project also includes unit tests for the sentiment analysis function. You can use these tests to ensure that the sentiment analysis function works as expected.

### **Running Unit Tests**:

1. **Make sure you have the required dependencies** installed by running:

   ```bash
   pip install -r requirements.txt
   ```

2. **Navigate to the project directory** in the terminal.
3. **Run the unit tests** by executing the following command:

   ```bash
   python -m unittest test_sentiment_analyzer.py
   ```
### **Expected Output**:
If all tests pass, you should see the following output:

```bash
.....
----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
```

If any tests fail, the output will show which test failed and the reason for the failure.

---

## 🔧 Tools Used

- **Python**
- **Streamlit** (for the web interface)
- **TextBlob** (for sentiment analysis)
- **Pandas** (for handling data)
- **Matplotlib** (for data visualization)
- **unittest** (for unit testing)

---

## ✨ Features

- **File Upload**: Upload CSV files containing tweets for sentiment analysis.
- **Sentiment Classification**: Classifies tweets as **Positive**, **Neutral**, or **Negative** based on polarity scores.
- **Data Visualization**: Displays a bar chart of sentiment distribution.

---

## 📂 Directory Structure

```
SocialMediaSentimentApp/
├── app.py                     # Streamlit app to run the analysis
├── sentiment_analyzer.py       # Contains the sentiment analysis logic
├── test_sentiment_analyzer.py  # Unit tests for sentiment analysis
├── chat_data_without_sentiment.csv  # Sample data for testing
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```


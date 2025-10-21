import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from textblob import TextBlob
from collections import Counter
from io import StringIO
import spacy
nlp = spacy.load("en_core_web_sm")

# --- App Configuration ---
st.set_page_config(page_title="🧠 Linguistics Analyzer", layout="wide")
st.title("🧠 Linguistics: Language Pattern Analyzer")
st.write("Upload or paste text below to explore **word frequency**, **sentiment**, and **word clouds**.")

# --- Load NLP model ---
@st.cache_resource
def load_spacy():
    return spacy.load("en_core_web_sm")

nlp = load_spacy()

# --- Sidebar options ---
st.sidebar.header("⚙️ Settings")
analysis_type = st.sidebar.radio(
    "Choose Analysis:",
    ["Word Frequency", "Sentiment Analysis", "Word Cloud"]
)
min_word_length = st.sidebar.slider("Minimum word length", 1, 10, 3)
include_stopwords = st.sidebar.checkbox("Include stopwords?", False)
top_n = st.sidebar.slider("Top N Words", 5, 50, 20)

# --- Input Section ---
uploaded_file = st.file_uploader("📄 Upload a text file (.txt)", type=["txt"])
input_text = st.text_area("✍️ Or paste text here", height=200)

text = ""
if uploaded_file:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    text = stringio.read()
elif input_text:
    text = input_text
else:
    st.warning("Please upload a file or enter text to begin.")
    st.stop()

# --- Process text ---
doc = nlp(text)

# --- 1️⃣ Word Frequency ---
if analysis_type == "Word Frequency":
    words = [
        token.text.lower()
        for token in doc
        if token.is_alpha and (include_stopwords or not token.is_stop) and len(token.text) >= min_word_length
    ]
    freq = Counter(words)
    freq_df = pd.DataFrame(freq.most_common(top_n), columns=["Word", "Count"])

    st.subheader("🔤 Top Word Frequencies")
    st.bar_chart(freq_df.set_index("Word"))
    st.dataframe(freq_df)

# --- 2️⃣ Sentiment Analysis ---
elif analysis_type == "Sentiment Analysis":
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    st.subheader("💬 Sentiment Analysis")
    col1, col2 = st.columns(2)
    col1.metric("Polarity (−1 = Negative, +1 = Positive)", f"{polarity:.3f}")
    col2.metric("Subjectivity (0 = Objective, 1 = Subjective)", f"{subjectivity:.3f}")

    fig, ax = plt.subplots()
    ax.bar(["Polarity", "Subjectivity"], [polarity, subjectivity], color=["#4C9AFF", "#FFB74C"])
    ax.set_ylim(-1, 1)
    st.pyplot(fig)

# --- 3️⃣ Word Cloud ---
elif analysis_type == "Word Cloud":
    words = [
        token.text.lower()
        for token in doc
        if token.is_alpha and (include_stopwords or not token.is_stop) and len(token.text) >= min_word_length
    ]
    wc = WordCloud(width=800, height=400, background_color="white").generate(" ".join(words))

    st.subheader("☁️ Word Cloud")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wc, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)
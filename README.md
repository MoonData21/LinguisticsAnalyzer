Linguistics: Language Pattern Analyzer with spaCY:

A Streamlit web app for analyzing text using natural language processing (NLP). Explore word frequency, sentiment analysis, and word clouds for any text you provide. Perfect for writers, students, or anyone interested in language patterns.

Features----------

Word Frequency Analysis:

Shows the most common words in your text.

Filter words by length and choose whether to include stopwords.

Visualize results with a bar chart and table.

Sentiment Analysis:

Measures polarity (negative → positive) and subjectivity (objective → subjective).

Interactive visual display with metrics and bar chart.

Word Cloud Generator:

Generates a visually appealing word cloud of the most frequent words.

Customize filtering for word length and stopwords.

Upload or paste text

Upload a .txt file or paste your text directly into the text area.

Select an analysis type from the sidebar:

Word Frequency

Sentiment Analysis

Word Cloud

Include or exclude stopwords

Number of top words to display (for frequency analysis)

View results interactively:

Bar charts, data tables, metrics, and word clouds are displayed in the main app area.

Dependencies----------

Streamlit

spaCy
 (en_core_web_sm)

TextBlob

Matplotlib

WordCloud

Pandas

Note: spaCy requires downloading the English model:

python -m spacy download en_core_web_sm

Due to the NLP in the project, just run the project from the command line instead of uploading it to the Streamlit Cloud. 

Just run streamlit run app.py in the command line or powershell.

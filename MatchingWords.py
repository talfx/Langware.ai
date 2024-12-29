from Imports import *
import Config
from Context import *

def update_matching_words(url_entry,result_frame):
    url_text = extract_text_from_url(url_entry.get())
    matches = checkMatchingWords(Config.transcribed_text, url_text)
    context_dict = extract_context(url_text, matches)
    for widget in result_frame.winfo_children():
        widget.destroy()
    for word in matches:
        btn = tk.Button(result_frame, text=word, command=lambda w=word: show_context(w, context_dict))
        btn.pack(side=tk.LEFT, padx=5)


# Functions for text matching
def findKeyWords(text):
    tokens = re.findall(r'\b\w+\b', text.lower())
    return [word for word in tokens if word not in stop_words]

def tokenize_with_stem_and_lemma(text):
    tokens = re.findall(r'\b\w+\b', text.lower())
    processed_tokens = set()
    for word in tokens:
        if word not in stop_words:
            lemma = lemmatizer.lemmatize(word)
            stem = stemmer.stem(word)
            processed_tokens.add(lemma)
            processed_tokens.add(stem)
    return processed_tokens


def checkMatchingWords(transcript_text, url_text):
    url_keywords = set(findKeyWords(url_text))
    url_tokens = tokenize_with_stem_and_lemma(' '.join(url_keywords))

    # Preprocess transcript tokens to strip punctuation
    transcript_tokens = re.findall(r'\b\w+\b', transcript_text.lower())
    matches = {word for word in transcript_tokens
               if stemmer.stem(word.strip('.,!?')) in url_tokens or
               lemmatizer.lemmatize(word.strip('.,!?')) in url_tokens}
    return matches


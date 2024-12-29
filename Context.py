from Imports import *
from Config import *


def extract_text_from_url(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        for script_or_style in soup(["script", "style"]):
            script_or_style.extract()
        text = soup.get_text(separator=" ", strip=True)
        print(text)
        return text[:50000]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return ""


def extract_context(text, matched_words):
    words = text.split()
    stemmed_words = [stemmer.stem(word.lower().strip('.,!?')) for word in words]
    context_dict = {}
    for word in matched_words:
        word_stem = stemmer.stem(word.lower().strip('.,!?'))
        indices = [i for i, w in enumerate(stemmed_words) if w == word_stem]
        for index in indices:
            start = max(0, index - 3)
            end = min(index + 3, len(words))
            context = " ".join(words[start:end])
            context_dict[word] = context
    return context_dict


def show_context(word, context_dict):
    context = context_dict.get(word, "No context found.")
    formatted_context = f"{word}: {context}"
    messagebox.showinfo("Word Context", formatted_context)

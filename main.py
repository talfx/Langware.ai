from AudioTranscription import toggle_recording
from UI_Utils import toggle_button, window
import nltk
import os

venv_nltk_data = os.path.join(os.path.dirname(__file__), 'venv', 'nltk_data')
nltk.data.path.append(venv_nltk_data)

# Check and download each separately
resources = ['corpora/stopwords', 'corpora/wordnet', 'tokenizers/punkt']
downloads = ['stopwords', 'wordnet', 'punkt']

for resource, download_name in zip(resources, downloads):
    try:
        nltk.data.find(resource)
    except LookupError:
        nltk.download(download_name, download_dir=venv_nltk_data)

# Set up callback for toggle_button
toggle_button.config(command=lambda: toggle_recording())

# Start the Tkinter main loop
window.mainloop()


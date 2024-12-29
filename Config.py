from Imports import *

# Initialize tools
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# Functions for audio processing
audio_queue = queue.Queue()
recording = False
transcribed_text = ""
model = whisper.load_model("base")

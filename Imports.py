import tkinter as tk
from tkinter import messagebox
import threading
import sounddevice as sd
import whisper
import requests
import queue
from bs4 import BeautifulSoup
import re
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

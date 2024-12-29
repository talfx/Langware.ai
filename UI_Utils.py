from tkinter import Label, Button
# Set up the Tkinter window
import tkinter as tk
window = tk.Tk()
window.title("Speech to Text Transcription")
window.geometry("800x600")

# Create UI elements
url_label = tk.Label(window, text="Enter URL:")
url_label.pack(pady=5)

url_entry = tk.Entry(window, width=80)
url_entry.pack(pady=5)

toggle_button = tk.Button(window, text="Start Recording")
toggle_button.pack(pady=10)

audioLabel = tk.Label(window, text="Transcription: ")
audioLabel.pack(pady=10)

result_frame = tk.Frame(window)
result_frame.pack(pady=10)

def update_transcription_ui(new_text):
    """Update the UI with the latest transcribed text."""
    if audioLabel:
        audioLabel.config(text="Transcription: " + new_text)

def update_button_status(is_recording):
    """Update the button status depending on whether recording is in progress."""
    if toggle_button:
        if is_recording:
            toggle_button.config(text="Stop Recording")
        else:
            toggle_button.config(text="Start Recording")

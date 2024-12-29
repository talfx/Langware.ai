import threading
import sounddevice as sd
import Config
from UI_Utils import update_transcription_ui, update_button_status, url_entry, result_frame
from MatchingWords import update_matching_words

def record_audio():
    while Config.recording:
        try:
            audio_data = sd.rec(int(4 * 16000), samplerate=16000, channels=1, dtype='float32')
            sd.wait()
            Config.audio_queue.put(audio_data.flatten())
        except Exception as e:
            print(f"Error during recording: {e}")

def transcribe_audio():
    while Config.recording or not Config.audio_queue.empty():
        try:
            audio_data = Config.audio_queue.get()
            if audio_data is None:
                print("finish or waiting")
                break
            print("Still Transcribing")
            result = Config.model.transcribe(audio_data, fp16=False)
            Config.transcribed_text += result["text"] + " "
            update_transcription_ui(Config.transcribed_text)
            update_matching_words(url_entry, result_frame)

        except Exception as e:
            print(f"Error during transcription: {e}")

def toggle_recording():
    """Toggle recording state and update the button's text."""
    if Config.recording:
        stop_recording()
        update_button_status(False)
    else:
        start_recording()
        update_button_status(True)

def start_recording():
    """Start recording and transcription in separate threads."""
    Config.recording = True
    # Config.transcribed_text = ""  # Reset transcription text
    threading.Thread(target=record_audio, daemon=True).start()
    threading.Thread(target=transcribe_audio, daemon=True).start()

def stop_recording():
    """Stop the recording and transcription process."""
    Config.recording = False

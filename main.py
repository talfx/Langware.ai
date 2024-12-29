from AudioTranscription import toggle_recording
from UI_Utils import toggle_button, window

# Set up callback for toggle_button
toggle_button.config(command=lambda: toggle_recording())

# Start the Tkinter main loop
window.mainloop()

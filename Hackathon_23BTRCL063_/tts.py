# tts.py
import pyttsx3

class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()
        # Set properties
        self.engine.setProperty('rate', 150)  # Speed of speech
        self.engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)
        
        # Optional: change voice
        voices = self.engine.getProperty('voices')
        # Uncomment to use a different voice (index may vary by system)
        # self.engine.setProperty('voice', voices[1].id)  # Female voice
    
    def speak(self, text):
        """Convert text to speech"""
        print(f"Assistant: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

# Test code
if __name__ == "__main__":
    tts = TextToSpeech()
    tts.speak("Hello! I am your virtual assistant.")
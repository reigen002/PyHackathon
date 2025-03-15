# assistant.py
from voice_recognition import VoiceRecognizer
from nlu import IntentRecognizer
from task_executor import TaskExecutor
from tts import TextToSpeech
import time

class VirtualAssistant:
    def __init__(self):
        print("Initializing your virtual assistant...")
        self.voice_recognizer = VoiceRecognizer()
        self.intent_recognizer = IntentRecognizer()
        self.task_executor = TaskExecutor()
        self.tts = TextToSpeech()
        self.wake_word = "assistant"
        self.is_active = False
        self.running = True
    
    def process_command(self, command):
        """Process a single voice command"""
        # Check for wake word if not already active
        if not self.is_active:
            if self.wake_word in command.lower():
                self.is_active = True
                self.tts.speak("Yes, how can I help?")
                return
            return
        
        # Process the command
        intent_data = self.intent_recognizer.recognize_intent(command)
        
        # Check if goodbye intent
        if intent_data['intent'] == 'goodbye':
            response = self.task_executor.execute_task(intent_data)
            self.tts.speak(response)
            self.is_active = False
            return
            
        # Execute the task and get response
        response = self.task_executor.execute_task(intent_data)
        self.tts.speak(response)
        
        # Reset active state after a command is processed
        self.is_active = False
    
    def run(self):
        """Main loop to run the assistant"""
        self.tts.speak("Hello! I'm your virtual assistant. Say 'assistant' to activate me.")
        
        while self.running:
            try:
                # Listen for commands
                command = self.voice_recognizer.listen()
                if command:
                    self.process_command(command)
                time.sleep(0.5)  # Short pause to prevent CPU overuse
            except KeyboardInterrupt:
                self.running = False
                self.tts.speak("Shutting down. Goodbye!")
            except Exception as e:
                print(f"Error: {e}")
                self.tts.speak("I encountered an error. Please try again.")

if __name__ == "__main__":
    assistant = VirtualAssistant()
    assistant.run()
# nlu.py
import re

class IntentRecognizer:
    def __init__(self):
        # Define intents and their patterns
        self.intents = {
            'light_on': [r'turn on (?:the |)(?:lights|light)(?: in the |)(.*)', 
                         r'lights on(?: in the |)(.*)',
                         r'switch on (?:the |)(?:lights|light)(?: in the |)(.*)'],
            'light_off': [r'turn off (?:the |)(?:lights|light)(?: in the |)(.*)',
                          r'lights off(?: in the |)(.*)',
                          r'switch off (?:the |)(?:lights|light)(?: in the |)(.*)'],
            'set_temperature': [r'set (?:the |)temperature to (\d+)'],
            'check_weather': [r'what\'s the weather', r'weather forecast', r'is it (\w+) today'],
            'set_alarm': [r'set (?:an |)alarm for (.*)'],
            
            # New application control intents
            'open_youtube': [r'open youtube', r'launch youtube', r'play youtube', r'show youtube'],
            'open_browser': [r'open (?:the |)(?:web |)browser', 
                            r'launch (?:the |)browser', 
                            r'start (?:the |)browser',
                            r'open internet'],
            'open_application': [r'open (\w+)', 
                                r'launch (\w+)', 
                                r'start (\w+)', 
                                r'run (\w+)',
                                r'start up (\w+)'],
            
            # Basic conversation intents
            'greeting': [r'hello', r'hi', r'hey', r'good morning', r'good afternoon', r'good evening'],
            'goodbye': [r'goodbye', r'bye', r'see you', r'exit', r'quit', r'close']
        }
    
    def recognize_intent(self, text):
        """Extract intent and entities from text"""
        if not text:
            return {'intent': None, 'entities': {}}
            
        for intent, patterns in self.intents.items():
            for pattern in patterns:
                match = re.search(pattern, text)
                if match:
                    # Extract entities (captured groups)
                    entities = {}
                    if match.groups():
                        if intent == 'light_on' or intent == 'light_off':
                            location = match.group(1).strip()
                            entities['location'] = location if location else 'general'
                        elif intent == 'set_temperature':
                            entities['temperature'] = match.group(1)
                        elif intent == 'set_alarm':
                            entities['time'] = match.group(1)
                        elif intent == 'open_application':
                            app_name = match.group(1).strip()
                            entities['app_name'] = app_name
                    
                    # Special case for YouTube to override the general open_application
                    if intent == 'open_application' and 'app_name' in entities:
                        if entities['app_name'].lower() == 'youtube':
                            return {'intent': 'open_youtube', 'entities': {}}
                    
                    return {'intent': intent, 'entities': entities}
        
        return {'intent': 'unknown', 'entities': {}}

# Test code
if __name__ == "__main__":
    recognizer = IntentRecognizer()
    test_phrases = [
        "turn on the lights in the kitchen",
        "set the temperature to 72",
        "what's the weather",
        "open youtube",
        "launch browser",
        "open notepad",
        "start calculator"
    ]
    for phrase in test_phrases:
        result = recognizer.recognize_intent(phrase)
        print(f"Phrase: {phrase}")
        print(f"Intent: {result['intent']}")
        print(f"Entities: {result['entities']}")
        print("---")
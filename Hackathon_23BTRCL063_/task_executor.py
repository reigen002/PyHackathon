# task_executor.py
import requests
import datetime
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class TaskExecutor:
    def __init__(self):
        # In a real implementation, this would connect to your smart home API
        self.light_states = {
            "living room": False,
            "kitchen": False,
            "bedroom": False,
            "bathroom": False,
            "general": False
        }
        self.temperature = 70
        self.alarms = []
    
    def execute_task(self, intent_data):
        """Execute the task based on recognized intent"""
        intent = intent_data['intent']
        entities = intent_data['entities']
        
        if intent == 'light_on':
            return self.turn_light_on(entities.get('location', 'general'))
        elif intent == 'light_off':
            return self.turn_light_off(entities.get('location', 'general'))
        elif intent == 'set_temperature':
            return self.set_temperature(entities.get('temperature'))
        elif intent == 'check_weather':
            return self.check_weather()
        elif intent == 'set_alarm':
            return self.set_alarm(entities.get('time'))
        elif intent == 'greeting':
            return "Hello! How can I help you today?"
        elif intent == 'goodbye':
            return "Goodbye! Have a great day!"
        else:
            return "I'm not sure how to help with that."
    
    def turn_light_on(self, location):
        # In a real implementation, this would call your smart home API
        if location.lower() in self.light_states:
            self.light_states[location.lower()] = True
            return f"Turning on the lights in the {location}"
        else:
            return f"I don't know how to control lights in the {location}"
    
    def turn_light_off(self, location):
        if location.lower() in self.light_states:
            self.light_states[location.lower()] = False
            return f"Turning off the lights in the {location}"
        else:
            return f"I don't know how to control lights in the {location}"
    
    def set_temperature(self, temp):
        try:
            self.temperature = int(temp)
            return f"Setting temperature to {temp} degrees"
        except ValueError:
            return "I couldn't understand the temperature value"
    
    def check_weather(self):
        # This would normally use a weather API
        # For demo purposes, return a fixed response
        return "It looks like it's going to be sunny today with a high of 75 degrees."
    
    def set_alarm(self, time_str):
        self.alarms.append(time_str)
        return f"I've set an alarm for {time_str}"

# Test code
if __name__ == "__main__":
    executor = TaskExecutor()
    test_intents = [
        {'intent': 'light_on', 'entities': {'location': 'kitchen'}},
        {'intent': 'set_temperature', 'entities': {'temperature': '72'}}
    ]
    for intent_data in test_intents:
        response = executor.execute_task(intent_data)
        print(response)
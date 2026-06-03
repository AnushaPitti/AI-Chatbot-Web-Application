import json
import random
from difflib import SequenceMatcher


class ChatBot:
    def __init__(self, responses_file='responses.json'):
        # Read file in binary mode to bypass Windows encoding issues
        with open(responses_file, 'rb') as f:
            raw = f.read()
        self.data = json.loads(raw.decode('utf-8'))

    def similarity(self, a, b):
        return SequenceMatcher(None, a.lower(), b.lower()).ratio()

    def get_response(self, user_input):
        user_input = user_input.lower().strip()

        if not user_input:
            return "Please type something! I am here to help."

        best_match = None
        best_score = 0.0

        for category, content in self.data.items():
            if category == 'default':
                continue
            for pattern in content['patterns']:
                if pattern in user_input:
                    return random.choice(content['responses'])
                score = self.similarity(user_input, pattern)
                if score > best_score:
                    best_score = score
                    best_match = category

        if best_score > 0.5 and best_match:
            return random.choice(self.data[best_match]['responses'])

        return random.choice(self.data['default']['responses'])

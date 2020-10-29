import json
import os


class Storage:
    def __init__(self):
        self.filename = 'storage.json'
        self.messages = []

    def _load_all(self):
        if not os.path.exists(self.filename):
            with open(self.filename, 'w', encoding='UTF-8') as f:
                json.dump([], f)
        else:
            with open(self.filename, 'r', encoding='UTF-8') as f:
                self.messages = json.load(f)

    def _save_all(self):
        with open(self.filename, 'w', encoding='UTF-8') as f:
            json.dump(self.messages, f)

    def send_message(self, message: str):
        self._load_all()
        self.messages.append(message)
        self._save_all()

    def get_all_messages(self) -> list:
        self._load_all()
        return self.messages

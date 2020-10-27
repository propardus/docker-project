import os
from flask import Flask, render_template, request, redirect
import json


class Storage:
    def __init__(self):
        self.filename = 'storage.json'
        self.messages = []

    def _load_all(self):
        if not os.path.exists(self.filename):
            return
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


app = Flask(__name__)
storage = Storage()


@app.route('/')
def index():
    messages = storage.get_all_messages()
    return render_template('index.html', messages=messages)


@app.route('/send-message', methods=['POST'])
def send_message():
    message_text = request.form['message']
    storage.send_message(message_text)
    return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

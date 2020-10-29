import os
from flask import Flask, render_template, request, redirect
import json
from providers.redis_storage import Storage


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
    # app.run()
    app.run(host='0.0.0.0', port=5000)

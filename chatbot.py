
import google.generativeai as genai
from flask import Flask, render_template, request, jsonify

API_KEY = ""
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat_api():
    data = request.get_json()
    user_input = data.get('message', '')
    response = chat.send_message(user_input)
    return jsonify({'reply': response.text})

if __name__ == '__main__':
    app.run(debug=True)
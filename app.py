import os
import google.generativeai as genai
from flask import Flask, render_template, request

app = Flask(__name__)

# --- Gemini AI Setup ---
# Hum key yahan direct nahi likhenge, balki Environment Variable se uthayenge
API_KEY = os.environ.get("AIzaSyC1Z1aGLSG47u7ZsDOpMD2_L0GIY1vBvak")
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

@app.route('/')
def home():
    # Aapka puraana movie data yahan rahega
    return render_template('index.html')

@app.route('/ask-ai', methods=['POST'])
def ask_ai():
    user_query = request.form.get('query')
    # Gemini se movie recommendation mangna
    response = model.generate_content(f"Suggest some best Hindi movies or series for: {user_query}")
    return {"reply": response.text}

if __name__ == '__main__':
    app.run(debug=True)

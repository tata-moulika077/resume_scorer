from flask import Flask, render_template, request
import os
from utils.resume_parser import extract_text, calculate_score

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/score', methods=['POST'])
def score():
    if 'resume' not in request.files:
        return "No file uploaded"
    
    resume = request.files['resume']
    filepath = os.path.join(UPLOAD_FOLDER, resume.filename)
    resume.save(filepath)

    resume_text = extract_text(filepath)
    score, missing_keywords = calculate_score(resume_text)

    return render_template('result.html', score=score, missing=missing_keywords)

if __name__ == '__main__':
    app.run(debug=True)

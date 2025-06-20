# app.py

from flask import Flask, request, jsonify, render_template
import os
from werkzeug.utils import secure_filename
import docx
import pdfplumber
from models.summarizer import summarize_query  # ✅ Import summarization
import subprocess
import json
from models.summarizer import summarize_query  # existing T5 summarizer

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def extract_text_from_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        return '\n'.join([page.extract_text() or '' for page in pdf.pages])

def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    return '\n'.join([para.text for para in doc.paragraphs])

def summarize_with_ollama(context, query):
    prompt = f"Using the following documents:\n{context}\n\nGive a summary based on the query: {query}"
    result = subprocess.run(
        ["ollama", "run", "tinyllama"],
        input=prompt.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return result.stdout.decode('utf-8').strip()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    uploaded_files = request.files.getlist("files")
    query = request.form.get("query", "")
    engine = request.form.get("engine", "t5")  # new field
    all_texts = []

    for file in uploaded_files:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        if filename.endswith('.pdf'):
            all_texts.append(extract_text_from_pdf(file_path))
        elif filename.endswith('.docx'):
            all_texts.append(extract_text_from_docx(file_path))

    full_text = '\n'.join(all_texts)

    # Choose engine
    if engine == "ollama":
        summary = summarize_with_ollama(full_text, query)
    else:
        summary = summarize_query(full_text, query)

    return jsonify({
        "query": query,
        "engine": engine,
        "summary": summary
    })

if __name__ == '__main__':
    app.run(debug=True)

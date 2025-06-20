
# 🧠 Multi-document Query-Based Abstractive Summarizer

This project implements an abstractive summarization system that can answer user queries by synthesizing information from multiple documents. It uses deep learning techniques, specifically transformer models (T5), to generate human-like, semantically meaningful summaries for given queries.

---

## 📌 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Objectives](#project-objectives)
- [Model Architecture](#model-architecture)
- [Methodology](#methodology)
- [Dataset](#dataset)
- [Evaluation Metrics](#evaluation-metrics)
- [Web Application](#web-application)
- [Screenshots](#screenshots)
- [Installation](#installation)
- [Team](#team)
- [References](#references)

---

## 📖 Overview

Due to the exponential growth of textual information, extracting relevant content for a specific query is a significant challenge. This project addresses that problem by designing a **multi-document, query-based abstractive summarizer** powered by a fine-tuned T5 model. The system is designed to accept PDF/DOCX inputs and respond to user queries with concise and contextually accurate summaries.

---

## ✨ Features

- Multi-document support (.pdf, .docx)
- Query-based summarization using a fine-tuned `T5` model
- Optional support for external model (`Ollama` with `TinyLLaMA`)
- Web interface using Flask
- Evaluation via ROUGE and BERTScore

---

## 🎯 Project Objectives

- Develop an abstractive summarization model that can synthesize and condense information across documents in response to a query.
- Leverage advanced transformer architectures (e.g., T5) for high-quality text generation.
- Ensure outputs are logically coherent, semantically relevant, and factually correct.
- Provide a user-friendly interface for interaction.
- Evaluate using standard NLP metrics to ensure summary relevance and quality.

---

## 🧪 Model Architecture

- **Base Model**: `t5-small` (Hugging Face Transformers)
- **Training Strategy**: Fine-tuned on a custom dataset containing queries, document contexts, and summaries.
- **Decoding**: Beam search with repetition and length penalty for fluency and diversity.

---

## 🔍 Methodology

1. **Preprocessing**: JSON → CSV conversion, formatting to `"summarize: {query} context: {document}"`.
2. **Model Fine-Tuning**:
   - Input length: 512 tokens
   - Output length: 64 tokens
   - 5 epochs with early stopping
3. **Evaluation**:
   - ROUGE (textual overlap)
   - BERTScore (semantic similarity)

---

## 📁 Dataset

- Source: Open-source datasets from platforms like Kaggle and GitHub
- Format:
  - `input_text`: summarize: {query} context: {document}
  - `target_text`: Expected summary

---

## 📊 Evaluation Metrics

| Metric      | Score      |
|-------------|------------|
| BERTScore   | 82.63%     |
| ROUGE       | Moderate   |

*Note: ROUGE was relatively low due to the abstractive (rather than extractive) nature of the summaries.*

---

## 🌐 Web Application

### Flask-based Features:

- Upload interface for PDF/DOCX files
- Query input form
- Engine selector (T5 or Ollama)
- Dynamic summary generation and display

### Folder Structure:
```
/models
  └── summarizer.py
/qfs-t5
/templates
  └── index.html
/uploads
app.py
```

---

## 🖼️ Screenshots

> 📌 Add screenshots of your interface in this section if needed.

---

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/qfs-summarizer.git
cd qfs-summarizer

# Create virtual environment
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py
```

---

## 👥 Team

- **Aditya Narayan Panda** – [FET/BCE/2021-25/005]
- M.S.L.V. Saranya – [FET/BCE/2021-25/004]
- Dibyanshu Mohapatra – [FET/BCE/2021-25/008]
- Shreya Adya – [FET/BCE/2021-25/047]

**Project Guide**: Prof. (Dr.) Gopinath Palai  
**Institution**: Faculty of Engineering & Technology, Sri Sri University, Cuttack

---

## 📚 References

1. Suleiman, D. & Awajan, A. (2020). Deep Learning Based Abstractive Text Summarization.
2. Shakila et al. (2024). Abstractive Text Summarization: State of the Art.
3. Baumel et al. (2018). Query Focused Abstractive Summarization.
4. Verberne et al. (2020). Query-based Summarization of Discussion Threads.

# models/summarizer.py

from transformers import T5ForConditionalGeneration, T5Tokenizer

# Load once when the module is imported
model = T5ForConditionalGeneration.from_pretrained("./qfs-t5")
tokenizer = T5Tokenizer.from_pretrained("./qfs-t5")

def summarize_query(context, query):
    input_text = f"summarize: {query} context: {context}"
    inputs = tokenizer(input_text, return_tensors="pt", truncation=True, max_length=512)
    output = model.generate(**inputs, max_new_tokens=150)
    return tokenizer.decode(output[0], skip_special_tokens=True)

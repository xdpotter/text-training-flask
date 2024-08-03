from flask import Flask, request, jsonify, render_template, send_from_directory
from werkzeug.utils import secure_filename
from PIL import Image
import spacy
import fitz  # PyMuPDF
import os
import pytesseract  # Ensure pytesseract is imported

# Specify the path to the Tesseract executable if necessary
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load the trained SpaCy model from the specified path
model_path = r"C:\Users\mts\Documents\text_training_flask\model-best"
nlp = spacy.load(model_path)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

def convert_pdf_to_images(pdf_path):
    pdf_document = fitz.open(pdf_path)
    image_paths = []
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        pix = page.get_pixmap()
        img_path = os.path.join(app.config['UPLOAD_FOLDER'], f"page_{page_num}.png")
        pix.save(img_path)
        image_paths.append(img_path)
    return image_paths

def extract_text_from_image(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text

def process_text(text):
    doc = nlp(text)
    extracted_data = {}
    for ent in doc.ents:
        if ent.label_ not in extracted_data:
            extracted_data[ent.label_] = []
        extracted_data[ent.label_].append(ent.text)
    return extracted_data

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"})
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        if file_path.endswith('.pdf'):
            image_paths = convert_pdf_to_images(file_path)
            texts = [extract_text_from_image(img_path) for img_path in image_paths]
            full_text = " ".join(texts)
            display_image_path = image_paths[0]  # Display the first page image
        else:
            full_text = extract_text_from_image(file_path)
            display_image_path = file_path
        processed_data = process_text(full_text)
        return render_template('result.html', image_path=display_image_path, extracted_text=full_text, json_data=processed_data)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)

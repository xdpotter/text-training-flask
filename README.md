# text-training-flask

```markdown
# Text Extraction Flask Application

This Flask application allows users to upload PDF or image files (JPG/PNG). If a PDF file is uploaded, it converts the PDF to images, extracts text from the images using Tesseract OCR, processes the text with a trained SpaCy model, and displays the extracted text and JSON data on a web page.

## Features

- Upload PDF or image files.
- Convert PDF files to images.
- Extract text from images using Tesseract OCR.
- Process text using a trained SpaCy model.
- Display the uploaded image, extracted text, and JSON data on the web page.

## Prerequisites

- Python 3.6+
- Tesseract OCR (Ensure Tesseract is installed and its path is correctly set in `app1.py`)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/text-extraction-flask.git
    cd text-extraction-flask
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv myenv
    myenv\Scripts\activate  # On Windows
    # source myenv/bin/activate  # On Linux or macOS
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Ensure Tesseract OCR is installed. Download and install Tesseract from [here](https://github.com/tesseract-ocr/tesseract). Update the path to Tesseract executable in `app1.py` if necessary:

    ```python
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    ```

5. Place your trained SpaCy model in the specified path. Update the `model_path` variable in `app1.py` if necessary:

    ```python
    model_path = r"C:\Users\mts\Documents\text_training_flask\model-best"
    ```

## Running the Application

1. Navigate to the project directory:

    ```bash
    cd C:\Users\mts\Documents\text_training_flask
    ```

2. Activate the virtual environment:

    ```bash
    myenv\Scripts\activate  # On Windows
    # source myenv/bin/activate  # On Linux or macOS
    ```

3. Run the Flask application:

    ```bash
    python app1.py
    ```

4. Open your browser and go to:

    ```
    http://127.0.0.1:5000
    ```

## Usage

1. Upload a PDF or image file using the upload form on the home page.
2. After uploading, you will be redirected to a result page displaying:
   - The uploaded image.
   - The extracted text.
   - The extracted JSON data.

## Project Structure

```
text-extraction-flask/
│
├── app1.py                 # Main Flask application file
├── requirements.txt        # Python dependencies
├── templates/              # HTML templates
│   ├── index.html          # Upload form page
│   └── result.html         # Result display page
└── uploads/                # Directory to save uploaded files
```

## Contributing

Feel free to contribute to this project by opening issues or submitting pull requests. Please ensure that your contributions align with the project goals and coding standards.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Donations

If you find this project useful and would like to support its development, please consider making a donation. You can donate using Google Pay by scanning the QR code below:

![Google Pay QR Code](https://pin.it/55W7Vx8N3)

Your support is greatly appreciated!
```

This `README.md` file now includes a section for donations with the link to your Google Pay QR code image. Adjust any details as necessary.

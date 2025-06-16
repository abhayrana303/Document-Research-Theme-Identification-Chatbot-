
import pytesseract
from PIL import Image
import io
import fitz  # PyMuPDF

class DocumentIngestor:
    def __init__(self):
        self.documents = []

    def add_document(self, doc_id, filename, content):
        ext = filename.lower().split('.')[-1]
        if ext in ["jpg", "jpeg", "png", "bmp"]:
            text = self.extract_text_from_image(content)
        elif ext == "pdf":
            text = self.extract_text_from_pdf(content)
        else:
            try:
                text = content.decode("utf-8")
            except Exception:
                text = ""
        self.documents.append({
            "id": doc_id,
            "filename": filename,
            "text": text
        })

    def extract_text_from_image(self, content):
        image = Image.open(io.BytesIO(content))
        return pytesseract.image_to_string(image)

    def extract_text_from_pdf(self, content):
        text = ""
        with fitz.open(stream=content, filetype="pdf") as doc:
            for page in doc:
                text += page.get_text()
        return text

    def get_documents(self, ids=None):
        if ids:
            return [doc for doc in self.documents if doc["id"] in ids]
        return self.documents

    def summarize_documents(self):
        # Placeholder for summarization logic
        return "Summary of documents"
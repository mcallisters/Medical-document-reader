import pdfplumber
import os

# -----------------------------
# 1. Extract PDF text
# -----------------------------
def extract_pdf_text(pdf_path, start_page=0, end_page=None):
    texts = []
    with pdfplumber.open(pdf_path) as pdf:
        total_pages = len(pdf.pages)
        end = end_page if end_page is not None else total_pages
        for i in range(start_page, min(end, total_pages)):
            page = pdf.pages[i]
            text = page.extract_text()
            if text:
                texts.append(text)
            else:
                texts.append(f"[PAGE {i} – no selectable text, needs OCR]\n")
    return "\n\n".join(texts)

# -----------------------------
# 2. Save extracted text
# -----------------------------
def save_extracted_text(text: str, filename: str):
    """
    Saves extracted PDF text to a file in data/extracted/.
    """
    output_dir = "data/extracted"
    os.makedirs(output_dir, exist_ok=True)  # create folder if it doesn't exist
    file_path = os.path.join(output_dir, filename)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)
    
    print(f"✅ Extracted text saved to: {file_path}")
    return file_path

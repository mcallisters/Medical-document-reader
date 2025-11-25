from dotenv import load_dotenv
import os
from src.pdf_reader import extract_pdf_text, save_extracted_text
from src.llm_model import init_openai, build_messages, run_llm

# Load environment variables once
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("❌ OPENAI_API_KEY NOT found. Check .env file location.")
else:
    print("✅ OPENAI_API_KEY loaded successfully")


# -----------------------------
# Helper to save LLM output
# -----------------------------
def save_llm_output(text: str, filename: str):
    """
    Saves LLM output text to a file in data/results/.
    """
    output_dir = "data/results"
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, filename)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)
    
    print(f"✅ LLM output saved to: {file_path}")
    return file_path


# -----------------------------
# Main workflow
# -----------------------------
def main():
    pdf_path = "data/pdfs/my_document.pdf"

    # 1. Extract PDF text
    text = extract_pdf_text(pdf_path)

    # 2. Save extracted text
    save_extracted_text(text, "my_document.txt")

    # 3. Initialize OpenAI client
    client = init_openai()

    # 4. Build messages with refined bullet formatting
    messages = build_messages(text)

    # 5. Run LLM
    llm_result = run_llm(client, messages)
    print("\n=== LLM Output ===\n")
    print(llm_result)

    # 6. Save LLM output as nicely formatted bullets
    save_llm_output(llm_result, "my_document_llm_output.txt")


if __name__ == "__main__":
    main()

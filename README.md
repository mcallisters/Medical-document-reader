# Medical Document Reader

A Python tool to extract text from medical PDF documents and generate structured approval checklists and summaries using an OpenAI LLM.

## Features

- Extracts text from medical PDFs using `pdfplumber`
- Sends extracted text to OpenAI's GPT models to generate:
  - Coverage criteria
  - Exclusion criteria
  - Approval period
  - Additional notes (all in bullet-point format)
- Saves extracted text and LLM output to separate folders for easy reference
- Fully configurable API key loading via `.env` file
- Clean, modular design using functions (no classes required)

## Folder Structure

```
Medical-document-reader/
├── data/
│   ├── pdfs/          # Place your input PDFs here
│   ├── extracted/     # Extracted PDF text will be saved here
│   └── results/       # LLM output will be saved here
├── src/
│   ├── pdf_reader.py  # Functions to extract and save PDF text
│   └── llm_model.py   # Functions to build messages and call OpenAI LLM
├── .env               # Your API keys (OPENAI_API_KEY)
├── app.py             # Main script to run the program
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
```

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Medical-document-reader.git
cd Medical-document-reader
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your API key

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

## Usage

1. Place your PDF(s) in the `data/pdfs/` folder

2. Run the main script:

```bash
python app.py
```

3. Find your output:
   - **Extracted text**: `data/extracted/my_document.txt`
   - **LLM-generated checklist & summary**: `data/results/my_document_llm_output.txt`

## Requirements

- Python 3.7+
- pdfplumber
- openai
- python-dotenv

## License

[Add your license here]

## Contributing

[Add contribution guidelines here]

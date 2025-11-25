import openai
import os

# using specific functtion to initialize OpenAI client, buid messages, and call the LLM

def init_openai():
    # Explicitly tell the module which key to use
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        raise ValueError("Missing OPENAI_API_KEY in environment variables.")
    return openai

def build_messages(pdf_text: str) -> list[dict]: # build messages for LLM
    """
    Returns a list of messages for the LLM.
    pdf_text: the extracted text from the medical PDF
    """
    system_message = (
        "You are a medical regulatory document analyst.\n"
        "Your job is to read the provided medical PDF text and extract the approval requirements "
        "for a medication. You must be precise, structured, and avoid hallucinations."
        "Output should be in a clear bullet point format under specified headings."
    )

    user_message = (
        "Instructions:\n"
        "- Read the following PDF content.\n"
        "- Extract all approval requirements for the medication.\n"
        "- Organize your output into bullet points under these headings:\n"
        "  • Coverage Criteria\n"
        "  • Exclusion Criteria\n"
        "  • Approval Period\n"
        "- Add any additional notes as bullet points.\n"
        "- Do not include extra narrative; keep bullets clear and concise.\n\n"
        f"PDF content:\n{pdf_text}"
    )
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message},
    ]
    return messages

# call the LLM
def run_llm(client, messages: list[dict], model: str = "gpt-4.1") -> str:
    """
    Sends the messages to the OpenAI LLM and returns the response text.
    """
    response = client.chat.completions.create(
        model=model,
        messages=messages
    )
    return response.choices[0].message.content

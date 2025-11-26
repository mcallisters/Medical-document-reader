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
    "You are a medical regulatory document analyst. "
    "Your goal is to extract approval requirements from medical PDF text. "
    "Output must use checkbox formatting like '[ ] item', and no leading dashes. "
    "Do not hallucinate. Keep the output clean and structured."
)

    user_message = (
    "Read the PDF content below and extract all approval requirements.\n\n"
    "FORMAT RULES:\n"
    "- Use checkbox formatting ONLY: '[ ] Item description'\n"
    "- NO leading dash\n"
    "- Use the following exact section titles (no markdown symbols):\n"
    "  Coverage Criteria\n"
    "  Exclusion Criteria\n"
    "  Approval Period\n"
    "  Additional Notes\n"
    "- Indent nested items with four spaces.\n"
    "- Do not add commentary; list only facts found in the PDF.\n\n"
    f"PDF CONTENT:\n{pdf_text}"
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

import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile"
)

def summarize(text):
    prompt = f"Summarize this news article in 2-3 sentences:\n\n{text}"
    response = llm.invoke(prompt)
    return response.content

# Test
if __name__ == "__main__":
    test_text = """
    Apple announced a new iPhone model today with 
    improved camera features and longer battery life. 
    The device will be available in stores next month 
    at a starting price of $999.
    """
    print(summarize(test_text))
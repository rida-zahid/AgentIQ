import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile"
)

def extract(text):
    prompt = f"""Extract the following from this news text:
    - Main topic
    - Key entities (people, organizations, places)
    - Category (politics, tech, sports, etc)
    
    Text: {text}
    
    Reply in this format:
    Topic: ...
    Entities: ...
    Category: ...
    """
    response = llm.invoke(prompt)
    return response.content

# Test
if __name__ == "__main__":
    test_text = """
    Elon Musk's Tesla announced a new Gigafactory 
    in Texas, creating 5000 jobs. The factory will 
    produce the new Model Y electric vehicle.
    """
    print(extract(test_text))
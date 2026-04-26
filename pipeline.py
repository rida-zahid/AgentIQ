import sys
sys.path.append('.')

from tools.rag import search
from tools.summarizer import summarize
from tools.extractor import extract

def run_pipeline(query):
    print("\n" + "="*50)
    print(f"Query: {query}")
    print("="*50)

    # Step 1: RAG - find relevant articles
    print("\n Searching relevant articles...")
    results = search(query, top_k=3)
    
    # Combine results into one text
    combined_text = " ".join([r['headline'] + ". " + r['short_description'] for r in results])
    
    # Step 2: Summarize
    print("\n Summarizing...")
    summary = summarize(combined_text)
    print("Summary:", summary)
    
    # Step 3: Extract
    print("\n Extracting entities...")
    extracted = extract(combined_text)
    print("Extracted:", extracted)
    
    return {
        "query": query,
        "articles_found": results,
        "summary": summary,
        "extracted": extracted
    }

# Test
if __name__ == "__main__":
    run_pipeline("technology and artificial intelligence")
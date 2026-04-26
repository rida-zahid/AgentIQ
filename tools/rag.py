import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load data
df = pd.read_csv('data/news_2000.csv')

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Create embeddings
print("Creating embeddings...")
embeddings = model.encode(df['headline'].tolist(), show_progress_bar=True)

# Create FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

print("RAG ready! Total articles indexed:", index.ntotal)

# Search function
def search(query, top_k=3):
    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), top_k)
    results = df.iloc[indices[0]]
    return results[['headline', 'short_description']].to_dict('records')

# Test
if __name__ == "__main__":
    results = search("technology news")
    for r in results:
        print("\n---")
        print("Headline:", r['headline'])
        print("Description:", r['short_description'])
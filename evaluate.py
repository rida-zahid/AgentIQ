import sys
sys.path.append('.')
from tools.rag import search

from datasets import Dataset
from ragas.metrics import faithfulness, answer_relevancy
from ragas import evaluate

# Test questions
questions = [
    "What is happening in technology?",
    "Tell me about climate change",
    "What is the latest in sports?"
]

# Generate answers using RAG
data = {
    "question": [],
    "answer": [],
    "contexts": [],
}

print("Generating RAG answers...")

for q in questions:
    results = search(q, top_k=3)
    contexts = [r['headline'] + " " + r['short_description'] for r in results]
    answer = contexts[0] if contexts else "No answer found"
    
    data["question"].append(q)
    data["answer"].append(answer)
    data["contexts"].append(contexts)

# Create dataset
dataset = Dataset.from_dict(data)

# Evaluate
print("\nRunning RAGAS evaluation...")
results = evaluate(
    dataset,
    metrics=[answer_relevancy]
)

print("\n RAGAS Evaluation Results:")
print(results)
import gradio as gr
import sys
sys.path.append('.')

from agent import app as agent_app

def analyze(query):
    if not query:
        return "Please enter a query!", "", ""
    
    result = agent_app.invoke({"query": query})
    
    return (
        result["summary"],
        result["extracted"],
        result["final_response"]
    )

# Gradio UI
with gr.Blocks(title="AgentIQ") as demo:
    gr.Markdown("#  AgentIQ - Multi-Agent News Intelligence")
    gr.Markdown("Enter any topic to get AI-powered news analysis!")
    
    with gr.Row():
        query_input = gr.Textbox(
            label="Enter your query",
            placeholder="e.g. artificial intelligence news...",
            scale=4
        )
        submit_btn = gr.Button("Analyze ", scale=1)
    
    with gr.Row():
        summary_output = gr.Textbox(label=" Summary", lines=5)
        extracted_output = gr.Textbox(label="🔎 Extracted Info", lines=5)
    
    final_output = gr.Textbox(label=" Final Response", lines=8)
    
    submit_btn.click(
        fn=analyze,
        inputs=query_input,
        outputs=[summary_output, extracted_output, final_output]
    )

if __name__ == "__main__":
    demo.launch(share=True, inbrowser=True)
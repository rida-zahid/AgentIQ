import os
os.chdir('C:\\AgentIQ')

import mlflow
import sys
sys.path.append('.')

mlflow.set_tracking_uri("file:C:/AgentIQ/mlruns")

from agent import app as agent_app

mlflow.set_experiment("AgentIQ")

def run_with_tracking(query):
    with mlflow.start_run():
        mlflow.log_param("query", query)
        result = agent_app.invoke({"query": query})
        mlflow.log_metric("summary_length", len(result["summary"]))
        mlflow.log_metric("extracted_length", len(result["extracted"]))
        with open("result.txt", "w") as f:
            f.write(result["final_response"])
        mlflow.log_artifact("result.txt")
        print(" Run tracked in MLflow!")
        print("Summary:", result["summary"][:100], "...")
        return result

if __name__ == "__main__":
    run_with_tracking("technology and AI news")
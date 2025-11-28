import sys
import os
import argparse
from dotenv import load_dotenv
load_dotenv()


# Add project root (news_agent) to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.utils.data_loader import load_zenodo_dataset, preprocess_data
from src.classification.benchmark import run_benchmark
from src.rag.rag_engine import RAGEngine
from src.utils.formatting import print_card, print_header

def main():
    print_header("AI News Intelligence Agent Initialized")
    print("Type 'help' for a list of commands.")
    
    # Initialize RAG Engine once
    rag_engine = RAGEngine()
    dataset_loaded = False
    df = None

    while True:
        try:
            user_input = input("\n> ").strip()
            if not user_input:
                continue
                
            command = user_input.lower()
            
            if command in ["exit", "quit"]:
                print("Exiting...")
                break
                
            elif command == "help":
                help_text = [
                    "run classification benchmark - Compare models",
                    "upload dataset - Load and ingest data",
                    "rag search: <query> - Search news",
                    "generate summary - Summarize retrieved news",
                    "explain model performance - Analysis of models",
                    "ui optimized answer - Show demo card output",
                    "full analysis - Comprehensive report"
                ]
                print_card("Available Commands", help_text)
                
            elif command == "run classification benchmark":
                run_benchmark()
                
            elif command == "upload dataset":
                print("Loading dataset...")
                df = load_zenodo_dataset()
                df = preprocess_data(df)
                rag_engine.ingest_data(df)
                dataset_loaded = True
                print("Dataset uploaded and ingested successfully.")
                
            elif command.startswith("rag search:"):
                query = user_input.split(":", 1)[1].strip()
                if not dataset_loaded:
                    print("Please 'upload dataset' first.")
                else:
                    rag_engine.process_query(query)
                    
            elif command == "generate summary":
                if not dataset_loaded:
                    print("Please 'upload dataset' first.")
                else:
                    # Demo summary of random items
                    rag_engine.process_query("Summarize the latest news")
                    
            elif command == "explain model performance":
                explanation = [
                    "Traditional models are fast and effective for simple keyword-based topics.",
                    "BERT/DistilBERT captures semantic meaning, improving accuracy on subtle categories.",
                    "Gemini (LLM) excels at zero-shot tasks where no training data exists."
                ]
                print_card("Model Performance Explanation", explanation)
                
            elif command == "ui optimized answer":
                print_card("Demo Card", {"Status": "Active", "Theme": "Neon Purple", "User": "Authorized"})
                
            elif command == "full analysis":
                if not dataset_loaded:
                    print("Please 'upload dataset' first.")
                else:
                    print("Running full analysis...")
                    run_benchmark()
                    rag_engine.process_query("What are the key trends?")
                    
            else:
                print("Unknown command. Type 'help' for options.")
                
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()

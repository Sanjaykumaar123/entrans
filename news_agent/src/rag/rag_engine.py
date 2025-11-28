import os
import pandas as pd
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

class RAGEngine:
    def __init__(self):
        self.mock_mode = False
        
        api_key = os.environ.get("GOOGLE_API_KEY")
        if not api_key:
            print("❌ GOOGLE_API_KEY missing. Running in mock mode.")
            self.mock_mode = True
            return
        
        # Configure Gemini
        try:
            genai.configure(api_key=api_key)
            print("✅ Gemini initialized.")
        except Exception as e:
            print(f"❌ Gemini init failed: {e}")
            self.mock_mode = True

    def ingest_data(self, df, text_col='clean_text'):
        print("📥 Loading data into RAG Engine...")

        self.docs = []
        for _, row in df.iterrows():
            content = str(row.get(text_col, row.get('content', '')))
            title = str(row.get('title', content[:50] + "..."))
            category = str(row.get('category', 'General'))
            
            self.docs.append({
                "title": title,
                "content": content,
                "category": category
            })

        print(f"📄 Loaded {len(self.docs)} documents into memory.")

    def search(self, query, k=3):
        if self.mock_mode:
            # simple keyword search
            results = []
            for doc in self.docs:
                if any(w in doc["content"].lower() for w in query.lower().split()):
                    results.append(doc)
                if len(results) >= k:
                    break
            if not results:
                return self.docs[:k]
            return results
        
        # Gemini embedding search (no FAISS)
        try:
            q_embed = genai.embed_content(model="models/text-embedding-004", content=query)["embedding"]
            scores = []

            for doc in self.docs:
                d_embed = genai.embed_content(model="models/text-embedding-004", content=doc["content"])["embedding"]
                sim = sum(a*b for a,b in zip(q_embed, d_embed))
                scores.append((sim, doc))

            results = [d for _, d in sorted(scores, reverse=True)[:k]]
            return results
        except Exception as e:
            print(f"❌ Embedding search failed: {e}")
            return self.docs[:k]

    def generate_answer(self, query, docs):
        if self.mock_mode:
            return f"[MOCK] Based on data: {docs[0]['content'][:150]}..."

        context = "\n\n".join([d["content"] for d in docs])
        prompt = f"""
Use the context below to answer the user query.

Context:
{context}

User question: {query}

Answer:
"""
        try:
            response = genai.GenerativeModel("gemini-1.5-flash").generate_content(prompt)
            return response.text
        except:
            return "[MOCK] Gemini failed. Fallback answer."

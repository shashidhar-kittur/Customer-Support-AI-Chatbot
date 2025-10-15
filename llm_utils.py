import json
import os
from google import genai

try:
    client = genai.Client(api_key="API_KEY")
except Exception as e:
    print(f"Error initializing Gemini client: {e}")
    print("Please ensure your GEMINI_API_KEY environment variable is set.")
 

try:
    with open('data/faqs.json', 'r') as f:
        faqs = json.load(f)
except FileNotFoundError:
    print("WARNING: data/faqs.json not found. LLM will be used for all queries.")
    faqs = []

def generate_response(query, history):
    for faq in faqs:
        if query.lower() in faq.get('question', '').lower():
            return faq['answer'], False  # No escalation

    prompt = f"""
    You are a customer support bot. Use this conversation history: {history}
    FAQs: {json.dumps(faqs)}
    Query: {query}
    Respond helpfully. If you can't answer from FAQs, escalate by saying 'Escalating to human support.'
    Suggest next actions if needed.
    """
    
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash", 
            contents=prompt
        )
        
        answer = response.text
        escalate = "escalating" in answer.lower()
        
        return answer, escalate
    
    except Exception as e:
        print(f"LLM Generation Error: {e}")
        return "Sorry, I am experiencing a technical issue and cannot process your request right now.", True 

def summarize_conversation(history):
    prompt = f"Summarize this conversation: {history}"
    
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash", 
            contents=prompt
        )
        return response.text
    except Exception as e:
        print(f"LLM Summary Error: {e}")
        return "Summary failed due to a technical error."
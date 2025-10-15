AI Customer Support Bot
This repository contains an AI-powered customer support bot designed to handle FAQs, maintain conversation context, and escalate unresolved queries. It fulfills the requirements for a simulated customer support system with a backend API, LLM integration, and session tracking. An optional frontend is included for interactive testing.
Features

FAQ Handling: Responds to queries using a predefined FAQs dataset.
Contextual Memory: Stores conversation history per session in a SQLite database.
Escalation Simulation: Escalates unanswerable queries with a conversation summary.
Backend API: REST endpoints built with FastAPI.
LLM Integration: Uses OpenAI's GPT-4o-mini for response generation and summarization.
Optional Frontend: Streamlit-based chat interface for user interaction.

Project Structure
project/
├── app.py              # FastAPI backend with REST endpoints
├── database.py         # SQLite database for session tracking
├── llm_utils.py        # LLM integration and prompt logic
├── streamlit_app.py    # Optional Streamlit frontend
├── data/
│   └── faqs.json       # Sample FAQs dataset
├── README.md           # Project documentation
└── demo.mp4            # Demo video (to be added)

Setup Instructions

Clone the Repository:
git clone https://github.com/yourusername/ai-support-bot.git
cd ai-support-bot


Install Dependencies:Ensure Python 3.8+ is installed. Then:
pip install fastapi uvicorn openai sqlite3 streamlit requests


Set Up Environment:Create a .env file or set the OpenAI API key:
export OPENAI_API_KEY="your-api-key"

Replace "your-api-key" with your actual OpenAI API key (get from https://platform.openai.com).

Prepare FAQs Dataset:The data/faqs.json file contains sample FAQs. Modify it as needed for your use case.

Run the Backend:Start the FastAPI server:
uvicorn app:app --reload

The API will be available at http://localhost:8000.

Run the Frontend (Optional):Launch the Streamlit interface:
streamlit run streamlit_app.py

Access it at http://localhost:8501.


API Endpoints

POST /chat
Input: JSON with session_id (string) and query (string).
Output: JSON with response (bot's answer), escalate (boolean), and summary (if escalated).
Example:curl -X POST http://localhost:8000/chat -H "Content-Type: application/json" -d '{"session_id": "user123", "query": "How do I return an item?"}'





LLM Usage
The bot uses OpenAI's GPT-4o-mini for:

Response Generation: Matches queries to FAQs or generates answers for complex queries.
Conversation Summarization: Summarizes history during escalation.
Prompt Structure:You are a customer support bot. Use this conversation history: {history}
FAQs: {faqs}
Query: {query}
Respond helpfully. If you can't answer from FAQs, escalate by saying 'Escalating to human support.'
Suggest next actions if needed.

For summarization:Summarize this conversation: {history}



Testing

FAQ Queries: Test with questions in faqs.json (e.g., "What is your return policy?").
Non-FAQ Queries: Test with unrelated questions (e.g., "Why is the sky blue?") to trigger escalation.
Session Continuity: Use the same session_id to verify history retention.
Use Streamlit frontend to interact with the API.



Evaluation Focus

Conversational Accuracy: Responses match FAQs or escalate appropriately.
Session Management: History is retained across queries.
LLM Integration: Effective use of prompts for response generation and summarization.
Code Structure: Modular, commented, and follows Python best practices.

For issues or contributions, please open a GitHub issue or pull request.

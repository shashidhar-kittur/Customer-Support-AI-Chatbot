<xaiArtifact artifact_id="7747d092-9b7f-4e25-9545-1e84fbceec32" artifact_version_id="5e900637-7127-46e5-804d-978815f0783c" title="README.md" contentType="text/markdown">

# AI Customer Support Bot

This repository contains an AI-powered customer support bot designed to handle FAQs, maintain conversation context, and escalate unresolved queries. It fulfills the requirements for a simulated customer support system with a backend API, LLM integration, and session tracking. An optional frontend is included for interactive testing.

## Features
- **FAQ Handling**: Responds to queries using a predefined FAQs dataset.
- **Contextual Memory**: Stores conversation history per session in a SQLite database.
- **Escalation Simulation**: Escalates unanswerable queries with a conversation summary.
- **Backend API**: REST endpoints built with FastAPI.
- **LLM Integration**: Uses OpenAI's GPT-4o-mini for response generation and summarization.
- **Optional Frontend**: Streamlit-based chat interface for user interaction.

## Project Structure
```
project/
├── app.py              # FastAPI backend with REST endpoints
├── database.py         # SQLite database for session tracking
├── llm_utils.py        # LLM integration and prompt logic
├── streamlit_app.py    # Optional Streamlit frontend
├── data/
│   └── faqs.json       # Sample FAQs dataset
├── README.md           # Project documentation
└── demo.mp4            # Demo video (to be added)
```

## Setup Instructions
1. **Clone the Repository**:
   ```bash:disable-run
   git clone https://github.com/yourusername/ai-support-bot.git
   cd ai-support-bot
   ```

2. **Install Dependencies**:
   Ensure Python 3.8+ is installed. Then:
   ```bash
   pip install fastapi uvicorn openai sqlite3 streamlit requests
   ```

3. **Set Up Environment**:
   Create a `.env` file or set the Gemini flash 2.5 API key:
   ```bash
   export GEMINI_API_KEY="your-api-key"
   ```
   Replace `"your-api-key"` with your actual Gemini API key (get from [https://aistudio.google.com/](https://aistudio.google.com/apikey)).

4. **Prepare FAQs Dataset**:
   The `data/faqs.json` file contains sample FAQs. Modify it as needed for your use case.

5. **Run the Backend**:
   Start the FastAPI server:
   ```bash
   uvicorn app:app --reload
   ```
   The API will be available at `http://localhost:8000`.

6. **Run the Frontend (Optional)**:
   Launch the Streamlit interface:
   ```bash
   streamlit run streamlit_app.py
   ```
   Access it at `http://localhost:8501`.

## API Endpoints
- **POST /chat**
  - **Input**: JSON with `session_id` (string) and `query` (string).
  - **Output**: JSON with `response` (bot's answer), `escalate` (boolean), and `summary` (if escalated).
  - Example:
    ```bash
    curl -X POST http://localhost:8000/chat -H "Content-Type: application/json" -d '{"session_id": "user123", "query": "How do I return an item?"}'
    ```

## LLM Usage
The bot uses OpenAI's GPT-4o-mini for:
- **Response Generation**: Matches queries to FAQs or generates answers for complex queries.
- **Conversation Summarization**: Summarizes history during escalation.
- **Prompt Structure**:
  ```plaintext
  You are a customer support bot. Use this conversation history: {history}
  FAQs: {faqs}
  Query: {query}
  Respond helpfully. If you can't answer from FAQs, escalate by saying 'Escalating to human support.'
  Suggest next actions if needed.
  ```
  For summarization:
  ```plaintext
  Summarize this conversation: {history}
  ```

## Testing
- **FAQ Queries**: Test with questions in `faqs.json` (e.g., "What is your return policy?").
- **Non-FAQ Queries**: Test with unrelated questions (e.g., "Why is the sky blue?") to trigger escalation.
- **Session Continuity**: Use the same `session_id` to verify history retention.
- Use Streamlit frontend to interact with the API.


## Evaluation Focus
- **Conversational Accuracy**: Responses match FAQs or escalate appropriately.
- **Session Management**: History is retained across queries.
- **LLM Integration**: Effective use of prompts for response generation and summarization.
- **Code Structure**: Modular, commented, and follows Python best practices.

For issues or contributions, please open a GitHub issue or pull request.

</xaiArtifact>
```

# Portfolio AI – Chatbot API

A lightweight FastAPI microservice exposing **Portfolio AI**, an agent built with [crewAI] and powered by Joel Mbaka’s CV as its knowledge base. The agent leverages Google’s `models/text-embedding-004` for semantic retrieval.

Highlights
- **CLI & Web**: Interact via the command line (`crewai run`) or through HTTP endpoints (`/chat`, `/health`) with auto-generated docs at `/docs`.
- **FastAPI backend**: Async service wrapping synchronous `crew.kickoff` in a thread for non-blocking I/O.
- **Cloud-ready**: Optimised for Render.com—simple build (`pip install . --break-system-packages`) and start (`uvicorn portfolio_ai.api:app --app-dir src --host 0.0.0.0 --port $PORT`).

This repo showcases Joel Mbaka’s professional profile through an AI chatbot available locally or in the cloud.
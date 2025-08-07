# EdgeSage Example

This example demonstrates a fully offline local agent that uses `gpt-oss` models through [Ollama](https://ollama.ai/) and orchestrates tasks with [AutoGen](https://github.com/microsoft/autogen) and [LangGraph](https://github.com/langchain-ai/langgraph).

## Features
- Runs `gpt-oss` models (20B/120B) via Ollama.
- Multi-agent orchestration using AutoGen + LangGraph.
- Depth-control parameter to adjust Mixture-of-Experts usage for available GPU memory.
- Offline-first UI served through a Next.js 14 progressive web app.

## Quick start
```bash
# 1. Start services
docker compose up -d

# 2. Seed the Next.js app and agents
python agent.py

# 3. Open the UI
google-chrome http://localhost:3000
```
Disconnect from the network after launching the browser; the app continues to work offline.

## Project layout
- `agent.py` – AutoGen + LangGraph orchestration layer.
- `docker-compose.yml` – spins up the Next.js web app and Ollama server.
- `web/` – Next.js 14 PWA with offline caching.

This example is a starting point; adapt to suit your hardware and security requirements.

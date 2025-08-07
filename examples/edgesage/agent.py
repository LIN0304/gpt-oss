"""EdgeSage orchestrator.

This script wires together AutoGen and LangGraph to run gpt-oss models locally through
Ollama. It assumes an Ollama server is reachable at `http://localhost:11434` and that
`gpt-oss:20b` (or `gpt-oss:120b`) has been pulled.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict

from autogen import AssistantAgent, UserProxyAgent
from langgraph.graph import StateGraph
import requests


@dataclass
class ModelConfig:
    name: str = "gpt-oss:20b"
    depth: int = 1  # mixture-of-experts depth


class OllamaLLM:
    """Minimal client to query an Ollama model."""

    def __init__(self, model: ModelConfig) -> None:
        self.model = model

    def __call__(self, prompt: str) -> str:
        payload = {
            "model": self.model.name,
            "prompt": prompt,
            "options": {"depth": self.model.depth},
        }
        resp = requests.post("http://localhost:11434/api/generate", json=payload, timeout=60)
        resp.raise_for_status()
        return resp.json()["response"]


def build_agent(config: ModelConfig) -> AssistantAgent:
    llm = OllamaLLM(config)
    assistant = AssistantAgent("assistant", llm=llm)
    user = UserProxyAgent("user")

    sg = StateGraph(
        initial_state={},
        nodes=[user, assistant],
        edges={user: assistant, assistant: user},
    )
    return sg


if __name__ == "__main__":
    config = ModelConfig()
    graph = build_agent(config)
    print("EdgeSage graph ready. Try sending a message:")
    response = graph.run({"input": "Hello"})
    print(response)

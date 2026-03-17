# Intelligent Arithmetic Agent (Math Pirate)

A local AI Agent built with **Python** and **Ollama** that solves arithmetic problems by calling specific calculator tools. Instead of relying on the LLM's internal math capabilities, this agent uses **Function Calling** to ensure 100% accuracy.

---

## Overview

This project satisfies the requirements for **Task 2: Creating an Intelligent Agent**. It features a local LLM (Llama 3.2) equipped with a "Math Pirate" persona and access to real Python functions for arithmetic operations.

### Key Features
- **Local Execution:** Runs entirely on your machine via Ollama.
- **Tool Selection:** The agent intelligently decides which function (`add`, `subtract`, etc.) to call based on English queries.
- **Chain of Thought:** Capable of chaining multiple tool calls for multi-step problems.
- **Math Pirate Persona:** System-prompted to provide responses with a nautical flair.

---

## Tech Stack
- **Language:** Python 3.10+
- **LLM Runner:** [Ollama](https://ollama.com/)
- **Model:** `llama3.2` (Supports Tool Calling)
- **Library:** `ollama-python`

---

## Getting Started

### 1. Prerequisites
Install Ollama and pull the required model:
```bash
ollama pull llama3.2
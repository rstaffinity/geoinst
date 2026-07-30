# GTI Doctor — AI Assistant

> 🤖 **The AI chatbot is being prepared.** It will be served from a Cloudflare Worker + Vectorize backend (model: `@cf/meta/llama-3.1-8b-instruct-fp8`, embeddings: `@cf/baai/bge-m3`).

## What is GTI Doctor?

GTI Doctor is an AI assistant trained on every reference manual in this knowledge base (all 18 PDFs in our corpus). Ask it questions like:

- *"What's the typical installation procedure for a vibrating-wire piezometer in a sand layer?"*
- *"Give me the slope-stability instrumentation checklist from the FHWA manual."*
- *"How does the RSTAR Affinity mesh-network backhaul work?"*

Answers are grounded **only in this knowledge base** — the assistant will say so when it lacks the answer rather than inventing one.

## Status

| Component | State |
| --- | --- |
| Corpus ingestion (18 PDFs) | Pending extraction |
| Vectorize index creation | Not yet provisioned |
| Cloudflare Worker (template: tennis-doctor) | Scaffold ready, awaiting rename |
| Production URL | To be announced on deploy |

The GTI Doctor endpoint will be embedded as a chat widget on this page once the worker is live.

# GTI Doctor — AI Assistant

> 🤖 **The GTI Doctor AI assistant is now LIVE.** Ask it questions about geotechnical instrumentation — sensor specifications, installation procedures, application checklists — and it answers using grounded citations from the 18 reference manuals in this knowledge base (5,032 indexed chunks, 12.5 MB of text).

## Try GTI Doctor

**Visit**: <https://gti-doctor.henry-phamduc.workers.dev/>

The chat widget above serves all `/api/*` endpoints from the Cloudflare Worker + Vectorize index. The static site is the same intranet you're reading now.

## Example questions

- *What is a vibrating-wire piezometer and how is it installed in a borehole?*
- *Give me the slope-stability instrumentation checklist from the FHWA manual.*
- *How does the RSTAR Affinity mesh-network backhaul work?*
- *Which RST instrument would I use to monitor lateral movement in a 30 m deep excavated retaining wall?*

## How it works

| Component | Technology |
| --- | --- |
| LLM | `@cf/meta/llama-3.1-8b-instruct-fp8` (Workers AI, free tier) |
| Embeddings | `@cf/baai/bge-m3` (1024-dim multilingual) |
| Vector database | Cloudflare Vectorize (`gti-doctor-embeddings` index, 5,032 vectors) |
| Worker runtime | Cloudflare Workers (with Workers AI + Vectorize bindings) |
| Grounding | RAG pipeline — embed query → top-8 chunks → context-enriched prompt |

The assistant is trained **only** on this knowledge base. If a question is outside scope, it will say so instead of inventing an answer.

## API

| Endpoint | Method | Purpose |
| --- | --- | --- |
| `/api/health` | GET | Service heartbeat |
| `/api/info` | GET | Worker configuration |
| `/api/chat` | POST | RAG chat (streaming via SSE or batch JSON) |
| `/api/search` | POST | Pure semantic search (no LLM, just top-K chunks) |

Example:

```bash
curl -X POST https://gti-doctor.henry-phamduc.workers.dev/api/chat \
  -H "Content-Type: application/json" \
  -d '{"question":"What is a vibrating-wire piezometer?","stream":false}'
```

## Status

| Component | State |
| --- | --- |
| Corpus ingestion (18 PDFs, 5,032 chunks) | ✅ Complete |
| Vectorize index created | ✅ `gti-doctor-embeddings` (1024-dim, cosine) |
| Cloudflare Worker deployed | ✅ <https://gti-doctor.henry-phamduc.workers.dev/> |
| Chat endpoint | ✅ Verified — 200 OK, grounded answers with citations |
| Chat widget embedded in intranet | Pending |

# GTI Doctor — AI Assistant

> 🤖 **The GTI Doctor AI assistant is now LIVE.** Ask it questions about geotechnical instrumentation — sensor specifications, installation procedures, application checklists — and it answers using grounded citations from the 18 reference manuals in this knowledge base (5,032 indexed chunks, 12.5 MB of text).

**Visit**: <https://gti-doctor.henry-phamduc.workers.dev/>

<style>
.chat-iframe-wrapper { width: 100%; min-height: 640px; border: 1px solid var(--md-default-fg-color--lightest); border-radius: 8px; overflow: hidden; background: #fafafa; }
.chat-iframe-wrapper iframe { width: 100%; height: 640px; border: 0; }
.gti-actions { display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 18px; }
.gti-actions a { display: inline-block; padding: 10px 18px; background: var(--md-primary-fg-color); color: var(--md-primary-bg-color); text-decoration: none; border-radius: 6px; font-weight: 500; }
.gti-actions a:hover { filter: brightness(1.1); }
</style>

<div class="gti-actions">
  <a href="https://gti-doctor.henry-phamduc.workers.dev/" target="_blank">Open full chat ↗</a>
  <a href="#try-inline-chat">Try chat inline ↓</a>
</div>

<a id="try-inline-chat"></a>
<div class="chat-iframe-wrapper">
  <iframe src="https://gti-doctor.henry-phamduc.workers.dev/" title="GTI Doctor chat" loading="lazy"></iframe>
</div>

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
| Chat widget embedded in intranet | ✅ Live iframe above |

# Batches & Files — reference

## Message Batches API — 50% cheaper, asynchronous
For non-latency-sensitive work (bulk classification, extraction, evals). Up to 100k requests/batch;
most finish within an hour (max 24h). All Messages API features work (tools, caching, structured output).

```python
import anthropic, time
from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
from anthropic.types.messages.batch_create_params import Request

client = anthropic.Anthropic()
batch = client.messages.batches.create(requests=[
    Request(custom_id=f"item-{i}", params=MessageCreateParamsNonStreaming(
        model="claude-haiku-4-5", max_tokens=64,
        messages=[{"role": "user", "content": f"Classify sentiment: {text}"}]))
    for i, text in enumerate(items)
])

while client.messages.batches.retrieve(batch.id).processing_status != "ended":
    time.sleep(30)

for r in client.messages.batches.results(batch.id):   # results are UNORDERED
    if r.result.type == "succeeded":
        print(r.custom_id, r.result.message.content[0].text)  # key by custom_id, never position
```

## Files API — upload once, reference by id
Avoid re-uploading large docs across calls (beta header `files-api-2025-04-14`).

```python
f = client.beta.files.upload(file=("report.pdf", open("report.pdf", "rb"), "application/pdf"),
                             betas=["files-api-2025-04-14"])
resp = client.beta.messages.create(
    model="claude-opus-4-8", max_tokens=1024,
    betas=["files-api-2025-04-14"],
    messages=[{"role": "user", "content": [
        {"type": "text", "text": "Summarize this."},
        {"type": "document", "source": {"type": "file", "file_id": f.id}}]}],
)
```

## Gotchas (exam-relevant)
- Batch results arrive **unordered** — match by `custom_id`.
- Files API is **not** on Amazon Bedrock / Vertex (see `platform_availability.md`).
- Batches don't support the server-side refusal `fallbacks` parameter.

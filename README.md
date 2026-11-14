# CCN JSON API

A tiny JSON-in / JSON-out API function in Python, callable from JavaScript `fetch`, Wolfram Language, or any HTTP client.

```
POST /api   {"message": "hi"}   →   {"ok": true, "result": "I am here"}
```

## Files
| File | Purpose |
|---|---|
| `api/index.py` | The API function (`api_function`) + HTTP handler. Used by Vercel and locally. |
| `server.py` | Runs the API locally on port 8000. |
| `client_fetch.js` | JavaScript `fetch` example (browser or Node 18+). |
| `wolfram_client.wl` | Wolfram Language example (`URLExecute` + `HTTPRequest`). |

## Run locally
```bash
python3 server.py
curl -X POST http://localhost:8000/api -H "Content-Type: application/json" -d '{"message":"hi"}'
```

## Deploy (public URL, needed for Wolfram Cloud)
Import this GitHub repo at <https://vercel.com/new> — no settings needed. Your endpoint becomes `https://<project>.vercel.app/api`.

## Extend
Edit `api_function(data)` in `api/index.py`: it receives the request JSON as a dict and returns a dict.

---
© Computational Classnotes · CC BY-NC-SA 4.0

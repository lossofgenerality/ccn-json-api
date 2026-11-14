#!/usr/bin/env python3
"""
Run the API locally:   python3 server.py   ->  http://localhost:8000/api
Same code as the Vercel deployment (api/index.py). Standard library only.

© Computational Classnotes · CC BY-NC-SA 4.0
"""
import os
from http.server import ThreadingHTTPServer
from api.index import handler

PORT = int(os.environ.get("PORT", 8000))

if __name__ == "__main__":
    print(f"API listening on http://localhost:{PORT}/api")
    ThreadingHTTPServer(("0.0.0.0", PORT), handler).serve_forever()

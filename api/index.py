"""
JSON API function — receives JSON from fetch() / Wolfram URLExecute / any
HTTP client and returns a JSON result.

    POST /api   body: {"message": "hi"}   ->   {"ok": true, "result": "I am here"}

This file is used two ways:
  * Vercel serverless function (Vercel looks for the `handler` class in api/*.py)
  * Local server via ../server.py

© Computational Classnotes · CC BY-NC-SA 4.0
"""
import json
from http.server import BaseHTTPRequestHandler


# ---------------------------------------------------------------------------
# The API function: JSON in (dict) -> JSON out (dict). Edit this part.
# ---------------------------------------------------------------------------
def api_function(data: dict) -> dict:
    message = str(data.get("message", "")).strip().lower()
    if message == "hi":
        return {"ok": True, "result": "I am here"}
    return {"ok": True, "result": f"Received: {data.get('message')!r}"}


# ---------------------------------------------------------------------------
# HTTP plumbing (CORS + JSON parsing). Usually no need to touch.
# ---------------------------------------------------------------------------
class handler(BaseHTTPRequestHandler):
    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def _send_json(self, status: int, payload: dict):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self._cors()
        self.end_headers()
        self.wfile.write(body)

    def _path_ok(self):
        return self.path.split("?")[0].rstrip("/") in ("/api", "/api/index")

    def do_OPTIONS(self):
        self.send_response(204)
        self._cors()
        self.end_headers()

    def do_GET(self):  # health check: open /api in a browser
        if not self._path_ok():
            return self._send_json(404, {"ok": False, "error": "Not found"})
        self._send_json(200, {"ok": True, "result": "I am here"})

    def do_POST(self):
        if not self._path_ok():
            return self._send_json(404, {"ok": False, "error": "Not found"})
        try:
            length = int(self.headers.get("Content-Length", 0))
            data = json.loads(self.rfile.read(length) or b"{}")
            if not isinstance(data, dict):
                raise ValueError("JSON body must be an object")
        except ValueError as e:  # includes json.JSONDecodeError
            return self._send_json(400, {"ok": False, "error": f"Bad JSON: {e}"})
        try:
            self._send_json(200, api_function(data))
        except Exception as e:
            self._send_json(500, {"ok": False, "error": str(e)})

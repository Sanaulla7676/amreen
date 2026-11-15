from __future__ import annotations

import os
import threading
import webbrowser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent
os.chdir(ROOT)

server = None
for port in range(8000, 8021):
    try:
        server = ThreadingHTTPServer(("127.0.0.1", port), SimpleHTTPRequestHandler)
        break
    except OSError:
        continue

if server is None:
    raise RuntimeError("Ports 8000–8020 are all in use. Close another preview and try again.")

url = f"http://127.0.0.1:{server.server_address[1]}/"
print("Amreen's Academy preview is running.")
print(f"Open: {url}")
print("Keep this window open. Press Ctrl+C to stop the server.")
threading.Timer(1.0, lambda: webbrowser.open(url)).start()

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nStopping local preview...")
finally:
    server.server_close()

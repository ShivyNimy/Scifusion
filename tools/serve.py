#!/usr/bin/env python3
"""Serve the generated site locally.

    python3 tools/serve.py [port]

Binds 0.0.0.0 so the preview works from a browser outside the sandbox.
"""

import functools
import http.server
import socketserver
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "docs"


class Handler(http.server.SimpleHTTPRequestHandler):
    extensions_map = {
        **http.server.SimpleHTTPRequestHandler.extensions_map,
        ".js": "text/javascript",
        ".json": "application/json",
        ".svg": "image/svg+xml",
    }

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, fmt, *args):
        sys.stderr.write("%s\n" % (fmt % args))


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    if not ROOT.exists():
        sys.exit("docs/ is missing - run: python3 tools/build.py")
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.ThreadingTCPServer(("0.0.0.0", port), functools.partial(Handler, directory=str(ROOT))) as httpd:
        print(f"Scifusion preview: http://localhost:{port}/  (Ctrl+C to stop)")
        httpd.serve_forever()


if __name__ == "__main__":
    main()

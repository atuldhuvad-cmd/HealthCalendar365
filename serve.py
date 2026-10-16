"""
Robust Local Development Server for 365-Day Health Poster Studio (India)
Features:
1. Auto port detection (avoids busy/colliding ports like 8000 if occupied by another app).
2. Explicit IPv4 127.0.0.1 binding to avoid Windows IPv6 localhost (::1) ERR_EMPTY_RESPONSE.
3. Correct MIME types for .js, .json, .css, .png, and .webmanifest.
4. Opens browser automatically only AFTER the socket is actively listening.
5. Provides clickable fallback URLs in console.
"""

import http.server
import mimetypes
import os
import socket
import socketserver
import sys
import threading
import time
import webbrowser

# Ensure directory is project root
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(PROJECT_DIR)

# Fix Windows registry MIME type anomalies
mimetypes.init()
mimetypes.add_type("application/javascript", ".js")
mimetypes.add_type("text/javascript", ".js")
mimetypes.add_type("application/json", ".json")
mimetypes.add_type("image/png", ".png")
mimetypes.add_type("text/css", ".css")
mimetypes.add_type("application/manifest+json", ".webmanifest")
mimetypes.add_type("application/manifest+json", ".json")

class HealthStudioHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Enable CORS and prevent stale browser cache during local testing
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cache-Control", "no-cache, must-revalidate")
        super().end_headers()

    def guess_type(self, path):
        if path.endswith(".js"):
            return "application/javascript"
        if path.endswith(".json"):
            return "application/json"
        return super().guess_type(path)

    def log_message(self, format, *args):
        # Clean formatted server logging
        sys.stdout.write(f"[{self.log_date_time_string()}] {args[0]} -> status {args[1]}\n")

def check_port_available(port, host="127.0.0.1"):
    """Returns True if the port can be bound cleanly without collision."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((host, port))
            return True
        except OSError:
            return False

def find_best_port(host="127.0.0.1"):
    """Try 8000 first, then 8080, 8081, 8888, 5000, 3000, or let OS assign a free port."""
    preferred_ports = [8000, 8080, 8081, 8888, 5000, 3000]
    for port in preferred_ports:
        if check_port_available(port, host):
            return port
            
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, 0))
        return s.getsockname()[1]

def main():
    host = "127.0.0.1"
    port = find_best_port(host)
    url = f"http://{host}:{port}/index.html"

    print("=" * 65)
    print("   365-Day Health Poster Studio - India (Doctor's PWA)")
    print("=" * 65)
    print(f"\n[+] Serving files from: {PROJECT_DIR}")
    print(f"[+] Bound successfully to: {host}:{port}")
    print(f"[+] Studio URL: {url}\n")
    print("Opening browser automatically...")
    print("Press Ctrl+C in this window at any time to stop the server.")
    print("-" * 65)

    # Launch browser only after socket is guaranteed to be bound and open
    def launch_browser():
        time.sleep(0.4)
        chrome_paths = [
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
            os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe")
        ]
        for cpath in chrome_paths:
            if os.path.exists(cpath):
                try:
                    import subprocess
                    subprocess.Popen([cpath, url])
                    return
                except Exception:
                    pass
        webbrowser.open(url)

    threading.Thread(target=launch_browser, daemon=True).start()

    socketserver.TCPServer.allow_reuse_address = True
    try:
        with socketserver.TCPServer((host, port), HealthStudioHandler) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n[!] Server stopped by user.")
    except Exception as e:
        print(f"\n[ERROR] Failed to run server: {e}")

if __name__ == "__main__":
    main()

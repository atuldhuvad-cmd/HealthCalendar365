"""
Robust Local Development Server for 365-Day Health Poster Studio (India)
Features:
1. Auto port detection (avoids busy/colliding ports like 8000 if occupied by another app).
2. Explicit IPv4 127.0.0.1 binding to avoid Windows IPv6 localhost (::1) ERR_EMPTY_RESPONSE.
3. Correct MIME types for .js, .json, .css, .png, and .webmanifest.
4. Opens browser automatically only AFTER the socket is actively listening.
5. Provides clickable fallback URLs in console.
"""

import argparse
import functools
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

def get_lan_ip():
    """Detect the local machine's primary LAN IPv4 address."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except Exception:
        try:
            return socket.gethostbyname(socket.gethostname())
        except Exception:
            return "127.0.0.1"
    finally:
        s.close()

def main():
    parser = argparse.ArgumentParser(
        description="Robust Local Development Server for 365-Day Health Poster Studio (India)"
    )
    parser.add_argument(
        "--host",
        default="127.0.0.1",
        help="Host interface to bind to (default: 127.0.0.1, use 0.0.0.0 for LAN testing)"
    )
    parser.add_argument(
        "--port",
        type=int,
        default=None,
        help="Port to listen on (default: auto-detect best available)"
    )
    parser.add_argument(
        "--root",
        default=PROJECT_DIR,
        help="Directory to serve (default: project root)"
    )
    args = parser.parse_args()

    host = args.host
    root = os.path.abspath(args.root)
    if not os.path.isdir(root):
        print(f"[ERROR] Specified root directory does not exist: {root}")
        sys.exit(1)
    os.chdir(root)

    port = args.port if args.port is not None else find_best_port(host)
    desktop_url = f"http://127.0.0.1:{port}/index.html"

    print("=" * 65)
    print("   365-Day Health Poster Studio - India (Doctor's PWA)")
    print("=" * 65)
    print(f"\n[+] Serving files from: {root}")
    print(f"[+] Bound successfully to: {host}:{port}")

    if host == "0.0.0.0":
        lan_ip = get_lan_ip()
        phone_url = f"http://{lan_ip}:{port}/index.html"
        insecure_origin = f"http://{lan_ip}:{port}"
        print(f"[+] Local URL (this PC):   {desktop_url}")
        print(f"[+] Phone URL (LAN Wi-Fi): {phone_url}\n")
        print("[!] WARNING: Server is exposed to the local network.")
        print("[!] For Android Chrome PWA testing, enter this exact origin in")
        print("    chrome://flags/#unsafely-treat-insecure-origin-as-secure :")
        print(f"    {insecure_origin}\n")
    else:
        url = f"http://{host}:{port}/index.html"
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
                    subprocess.Popen([cpath, desktop_url])
                    return
                except Exception:
                    pass
        webbrowser.open(desktop_url)

    threading.Thread(target=launch_browser, daemon=True).start()

    socketserver.TCPServer.allow_reuse_address = True
    handler_factory = functools.partial(HealthStudioHandler, directory=root)
    try:
        with socketserver.TCPServer((host, port), handler_factory) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n[!] Server stopped by user.")
    except Exception as e:
        print(f"\n[ERROR] Failed to run server: {e}")

if __name__ == "__main__":
    main()

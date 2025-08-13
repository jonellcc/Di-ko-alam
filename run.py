import subprocess
import time
import os
import signal
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello World")

def run_http_server():
    server = HTTPServer(("0.0.0.0", 8080), HelloHandler)
    print("HTTP server running on port 8080")
    server.serve_forever()

def run_scripts():
    scripts = [
        "python3 bot.py",
        "python3 main.py",
        "python3 loader.py",
        "python3 modules.py",
        "python3 umay.py",
        "python3 gd.py",
        "python3 index.py"
    ]
    processes = []
    for i, script in enumerate(scripts):
        print(f"Launching {script}")
        process = subprocess.Popen(script, shell=True)
        processes.append(process)
        if i < len(scripts) - 1:
            time.sleep(1)
    return processes

if __name__ == "__main__":
    threading.Thread(target=run_http_server, daemon=True).start()
    while True:
        processes = run_scripts()
        time.sleep(120)
        for process in processes:
            os.kill(process.pid, signal.SIGTERM)
            process.wait()

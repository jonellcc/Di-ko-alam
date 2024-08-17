import subprocess
import time
import os
import signal

def run_scripts():
    scripts = [
        "python3 bot.py",
        "python3 main.py",
        "python3 loader.py",
        "python3 modules.py",
        "python3 umay.py"
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
    while True:
        processes = run_scripts()
        time.sleep(120)

        for process in processes:
            os.kill(process.pid, signal.SIGTERM)
            process.wait()

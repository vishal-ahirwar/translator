#flick
import os
import subprocess
import webbrowser
subprocess.Popen(["python", "-m", "http.server", "5500"], cwd="frontend")
webbrowser.open("http://localhost:5500")

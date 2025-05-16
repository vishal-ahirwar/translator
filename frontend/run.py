import os
import webbrowser
webbrowser.open("http://localhost:5500/")
os.system("cd frontend && python -m http.server 5500")

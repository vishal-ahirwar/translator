#flick
import os
current_path = os.getcwd()
os.system("cd backend && uvicorn main:app --host 0.0.0.0 --port 8000")

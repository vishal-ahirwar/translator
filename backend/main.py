#flick https://github.com/vishal-ahirwar/flick
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import MarianMTModel, MarianTokenizer
from fastapi.middleware.cors import CORSMiddleware

model_name = "HPLT/translate-en-hi-v1.0-hplt_opus"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

app = FastAPI()
# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can replace "*" with "http://localhost" for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class TranslationRequest(BaseModel):
    text: str

@app.post("/translate")
def translate(req: TranslationRequest):
    inputs = tokenizer(req.text, return_tensors="pt", padding=True)
    translated = model.generate(**inputs)
    hindi = tokenizer.decode(translated[0], skip_special_tokens=True)
    return {"translation": hindi}

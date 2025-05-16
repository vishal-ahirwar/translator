
## 🗣️ English to Hindi Translator API using Hugging Face and FastAPI

This project provides a simple and efficient REST API for translating English text into Hindi using the [HPLT/translate-en-hi-v1.0-hplt\_opus](https://huggingface.co/HPLT/translate-en-hi-v1.0-hplt_opus) model from Hugging Face Transformers. The backend is powered by **FastAPI**, offering a clean and minimal interface for machine translation tasks.

### 🔧 Features

* 🔤 Translate English text into Hindi
* 🚀 Powered by Hugging Face's pretrained MarianMT model
* ⚡ Fast and lightweight API with FastAPI
* 🧪 Testable via Postman or Swagger UI (`/docs`)
* 🛠️ Easy to extend into a web or mobile app

### 📦 Technologies

* Python
* FastAPI
* Transformers (Hugging Face)
* Uvicorn

### 🔗 API Endpoint

* `POST /translate`

  * Request Body:

    ```json
    {
      "text": "Hello, how are you?"
    }
    ```
  * Response:

    ```json
    {
      "translation": "नमस्ते, आप कैसे हैं?"
    }
    ```

---

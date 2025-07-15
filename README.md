
# FealtyX Backend Assignment – README

## 🏃‍♀️ Quick Start

```bash
# 1. Clone or download this repository
$ git clone <your‑fork‑url> && cd fealtyx_assignment

# 2. Create virtual env & install deps
$ python -m venv venv
$ source venv/bin/activate  # Windows: venv\Scripts\activate
$ pip install -r requirements.txt

# 3. Run local Ollama (first time only)
$ curl -fsSL https://ollama.com/install.sh | sh
$ ollama serve &  
$ ollama run llama3  

# 4. Launch FastAPI server
$ uvicorn main:app --reload

# 5. Open docs in browser
→ http://127.0.0.1:8000/docs
```

## 🛠️ API Reference

| Method | Endpoint                         | Purpose                      | Body / Params |
|--------|----------------------------------|------------------------------|---------------|
| POST   | `/students`                      | Create student               | `{name, age, email}` |
| GET    | `/students`                      | List all students            | – |
| GET    | `/students/{id}`                 | Get student by ID            | – |
| PUT    | `/students/{id}`                 | Update student               | `{name, age, email}` |
| DELETE | `/students/{id}`                 | Delete student               | – |
| GET    | `/students/{id}/summary`         | AI summary via Ollama        | – |

### Example `curl`

```bash
# Create
curl -X POST http://127.0.0.1:8000/students \
     -H "Content-Type: application/json" \
     -d '{"name":"Alice","age":20,"email":"alice@example.com"}'

# Summary
curl http://127.0.0.1:8000/students/1/summary
```

## 🧪 Running Tests

```bash
pytest -q
```

## 🚀 Deployment Notes

- **Docker**: Add a simple `Dockerfile` if you wish. Render/Railway both autodetect FastAPI + Uvicorn.
- **Env Vars**: No secrets in this app, but you can parameterize `OLLAMA_URL` and `OLLAMA_MODEL` via `os.getenv()`.

## ✨ Future Improvements

- Replace in‑memory store with PostgreSQL (SQLModel / SQLAlchemy)
- JWT authentication
- Caching summaries in Redis

---

Made with ❤️ for the FealtyX internship assignment.
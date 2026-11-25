# Machine Coding Template (Python + FastAPI)

A small reusable backend starter project for machine-coding practice.

## Project structure

- `main.py` — FastAPI app, sample POST and GET endpoints, logging
- `models.py` — Pydantic request and response models
- `services.py` — business logic
- `storage.py` — in-memory dictionary storage
- `requirements.txt` — dependencies

## Requirements

- Python 3.10+
- pip

## Setup (Windows PowerShell)

```powershell
python -m venv venv
.\\venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload
```

If PowerShell blocks activation, use Command Prompt:

```bat
venv\\Scripts\\activate.bat
```

## Run

```bash
uvicorn main:app --reload
```

Open:
- API docs: http://127.0.0.1:8000/docs
- Health check: http://127.0.0.1:8000/

## Test the sample endpoints

### Create an item

`POST /items`

```json
{
  "name": "Laptop",
  "description": "Dell Laptop",
  "price": 55000
}
```

Expected status: `201 Created`.

### List items

`GET /items`

Expected status: `200 OK`.

## Notes for the interview

- Data is stored in memory and resets when the server restarts.
- Replace the sample Item model, routes, service functions, and storage structure with the problem's domain.
- Keep business rules in `services.py`, request/response schemas in `models.py`, and in-memory data in `storage.py`.
- Add only the endpoints and validation required by the given problem.
- This is a starter template, not a production-ready service.

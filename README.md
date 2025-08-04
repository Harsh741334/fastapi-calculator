# FastAPI Application

A simple FastAPI application with mathematical operations.

## Features
- Addition endpoint using POST request
- Pydantic models for request validation
- JSON response format

## Local Development
```bash
pip install -r requirements.txt
uvicorn term02:app --reload
```

## API Endpoints
- `POST /sum` - Add two numbers

## Example Usage
```bash
curl -X POST -H "Content-Type: application/json" -d '{"a": 5, "b": 3}' http://localhost:8000/sum
```

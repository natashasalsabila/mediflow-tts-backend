# MediFlow TTS Backend

FastAPI backend for MediFlow queue announcement audio using `edge-tts`.

## Local Run

```powershell
pip install -r requirements.txt
python -m uvicorn server:app --host 0.0.0.0 --port 8000 --reload
```

Test:

```text
http://localhost:8000/
http://localhost:8000/tts?text=Nomor%20antrian%20GG-001%20silakan%20menuju%20Poli%20Gigi
```

## Render Deploy

Build command:

```text
pip install -r requirements.txt
```

Start command:

```text
uvicorn server:app --host 0.0.0.0 --port $PORT
```

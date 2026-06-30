from pathlib import Path
from urllib.parse import urljoin
import uuid

import edge_tts
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="MediFlow TTS Backend")

VOICE = "id-ID-GadisNeural"
AUDIO_DIR = Path("tts_audio")
AUDIO_DIR.mkdir(exist_ok=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

app.mount("/audio", StaticFiles(directory=AUDIO_DIR), name="audio")


@app.get("/")
def home() -> dict[str, str]:
    return {"message": "MediFlow Edge TTS Server Running"}


@app.get("/tts")
async def tts(text: str, request: Request) -> dict[str, str]:
    normalized_text = text.strip()
    if not normalized_text:
        raise HTTPException(status_code=400, detail="Text cannot be empty")

    filename = f"audio_{uuid.uuid4().hex}.mp3"
    output_path = AUDIO_DIR / filename

    communicate = edge_tts.Communicate(normalized_text, VOICE)
    await communicate.save(str(output_path))

    base_url = str(request.base_url)
    audio_url = urljoin(base_url, f"audio/{filename}")

    return {
        "status": "success",
        "text": normalized_text,
        "audio_url": audio_url,
    }

import io, time
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .config import settings
from .models import GenerateRequest, HealthResponse
from .generate import generate_image, get_pipe

app = FastAPI(title="Stable Diffusion Image Generator", version="0.1.0")

# CORS (útil si sirves el frontend desde otro dominio)
if settings.ENABLE_CORS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# ---------- Rutas API ----------

@app.get("/health", response_model=HealthResponse)
def health():
    # fuerza la carga perezosa si aún no está
    _ = get_pipe()
    return HealthResponse(status="ok", model=settings.MODEL_ID)

@app.post("/generate")
def generate(req: GenerateRequest):
    if not req.prompt or len(req.prompt.strip()) < 3:
        raise HTTPException(status_code=400, detail="Prompt vacío o demasiado corto.")

    start = time.time()
    image = generate_image(
        prompt=req.prompt.strip(),
        negative_prompt=req.negative_prompt,
        steps=req.num_inference_steps,
        guidance=req.guidance_scale,
        seed=req.seed,
        width=req.width,
        height=req.height,
    )
    elapsed = round(time.time() - start, 2)

    buf = io.BytesIO()
    image.save(buf, format="PNG")
    buf.seek(0)

    headers = {
        "X-Model": settings.MODEL_ID,
        "X-Elapsed": str(elapsed),
        "X-Seed": str(req.seed if req.seed is not None else -1)
    }
    return StreamingResponse(buf, media_type="image/png", headers=headers)

# ---------- Frontend estático ----------
# 👇 Esto se monta al final, así no pisa las rutas anteriores
app.mount("/", StaticFiles(directory="static", html=True), name="static")

import torch
from PIL import Image
from typing import Optional
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
from .config import settings

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
DTYPE = torch.float16 if DEVICE == "cuda" else torch.float32

_pipe = None  # singleton del pipeline

def get_pipe():
    global _pipe
    if _pipe is None:
        _pipe = StableDiffusionPipeline.from_pretrained(
            settings.MODEL_ID,
            torch_dtype=DTYPE,
            safety_checker=None,  # añade tu checker si lo necesitas
        )
        _pipe.scheduler = DPMSolverMultistepScheduler.from_config(_pipe.scheduler.config)

        if DEVICE == "cuda":
            _pipe = _pipe.to(DEVICE)
            # Optimizaciones “best effort”
            try:
                _pipe.enable_xformers_memory_efficient_attention()
            except Exception:
                pass
            _pipe.enable_attention_slicing()
            _pipe.enable_vae_tiling()
    return _pipe

def clamp(v, lo, hi):
    return max(lo, min(v, hi))

def generate_image(
    prompt: str,
    negative_prompt: Optional[str],
    steps: int,
    guidance: float,
    seed: Optional[int],
    width: int,
    height: int,
) -> Image.Image:
    pipe = get_pipe()

    width = clamp(width, 256, settings.MAX_SIZE)
    height = clamp(height, 256, settings.MAX_SIZE)
    steps = clamp(steps, 1, settings.MAX_STEPS)

    generator = torch.Generator(device=DEVICE)
    if seed is not None:
        generator = generator.manual_seed(seed)

    with torch.inference_mode():
        image = pipe(
            prompt=prompt,
            negative_prompt=negative_prompt or settings.DEFAULT_NEGATIVE,
            width=width,
            height=height,
            num_inference_steps=steps,
            guidance_scale=guidance,
            generator=generator
        ).images[0]

    # Aquí podrías aplicar un filtro/blur/placeholder si detectas NSFW con un clasificador externo
    return image

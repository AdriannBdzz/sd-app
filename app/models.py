from pydantic import BaseModel, Field
from typing import Optional

class GenerateRequest(BaseModel):
    prompt: str = Field(..., min_length=3, examples=["a cinematic photo of a corgi in sunglasses, 35mm, bokeh"])
    negative_prompt: Optional[str] = Field(default=None)
    num_inference_steps: int = Field(default=25, ge=1, le=75)
    guidance_scale: float = Field(default=7.0, ge=0, le=20)
    seed: Optional[int] = None
    width: int = Field(default=512, ge=256, le=1024)
    height: int = Field(default=512, ge=256, le=1024)

class HealthResponse(BaseModel):
    status: str
    model: str

import os

class Settings:
    # Modelo por defecto: SD 1.5 (estable y relativamente ligero)
    MODEL_ID: str = os.getenv("MODEL_ID", "runwayml/stable-diffusion-v1-5")
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "info")

    # Parámetros por defecto de generación
    DEFAULT_NEGATIVE: str = os.getenv("DEFAULT_NEGATIVE", "low quality, blurry, nsfw")
    MAX_SIZE: int = int(os.getenv("MAX_SIZE", "1024"))  # límite ancho/alto
    MAX_STEPS: int = int(os.getenv("MAX_STEPS", "75"))
    ENABLE_CORS: bool = os.getenv("ENABLE_CORS", "true").lower() == "true"

settings = Settings()

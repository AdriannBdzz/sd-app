# Stable Diffusion Image Generator (FastAPI + Diffusers)

MVP de generación de imágenes con Stable Diffusion usando **FastAPI** y **Diffusers**. Incluye frontend estático y despliegue con Docker.

## Requisitos

- Python 3.10+
- (Opcional) GPU NVIDIA con drivers + CUDA para rendimiento óptimo
- Docker + NVIDIA Container Toolkit (para despliegue en contenedor)

## Instalación local

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env        # y ajusta variables si quieres

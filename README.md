# 🧠 Stable Diffusion Image Generator  
### ✨ Aplicación web de generación de imágenes con IA — *FastAPI + Hugging Face Diffusers*

![preview](https://github.com/yourusername/sd-app/assets/preview-example.png)

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110%2B-009485?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Hugging Face](https://img.shields.io/badge/Diffusers-HuggingFace-yellow?logo=huggingface)](https://huggingface.co/docs/diffusers/index)
[![Docker](https://img.shields.io/badge/Docker-ready-blue?logo=docker)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

</div>

---

## 🧩 Descripción

**Stable Diffusion Image Generator** es una aplicación completa (backend + frontend) que permite generar imágenes a partir de texto utilizando el modelo **Stable Diffusion**.  
Desarrollada en **FastAPI** y **Python**, integra la librería **Diffusers** de Hugging Face y un frontend ligero en **HTML/CSS/JS**.

> 💡 Este proyecto combina *Machine Learning* y *desarrollo web* para demostrar cómo integrar modelos de IA reales en aplicaciones web escalables.

---

## 🚀 Características principales

✅ Generación de imágenes a partir de texto (*text-to-image*)  
✅ API REST con FastAPI  
✅ Frontend minimalista e interactivo (HTML + JS)  
✅ Compatible con modelos como `runwayml/stable-diffusion-v1-5` o `stabilityai/sdxl-turbo`  
✅ Configuración mediante `.env`  
✅ Preparado para despliegue con Docker (GPU opcional)

---

## 🧠 Tecnologías

| Área | Tecnologías |
|------|--------------|
| **Backend** | Python · FastAPI · Diffusers · PyTorch · Uvicorn |
| **Frontend** | HTML5 · CSS3 · JavaScript (Fetch API) |
| **Infraestructura** | Docker · .env configuration |
| **ML Models** | Stable Diffusion v1.5 / SDXL / Turbo |
| **Opcional (GPU)** | CUDA · xFormers |

---

## ⚙️ Instalación local

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/yourusername/sd-app.git
cd sd-app
```

### 2️⃣ Crear entorno virtual
```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
```

### 3️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar variables de entorno
Copia el archivo de ejemplo:
```bash
cp .env.example .env
```

Edita las variables según tus necesidades:
```bash
MODEL_ID=runwayml/stable-diffusion-v1-5
HOST=0.0.0.0
PORT=8000
ENABLE_CORS=true
```

### 5️⃣ Ejecutar el servidor
```bash
bash run.sh
```
o manualmente:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

📍 Abre [http://localhost:8000](http://localhost:8000) en tu navegador.

---

## 🖼️ Uso de la aplicación

1. Escribe un **prompt** descriptivo (por ejemplo:  
   > “a futuristic cyberpunk city at night, ultra detailed, cinematic lighting”)  
2. Ajusta parámetros opcionales:
   - `steps` (pasos de inferencia)
   - `guidance_scale` (nivel de creatividad vs precisión)
   - `width` / `height`
   - `seed` (reproducibilidad)
3. Pulsa **Generar imagen**.
4. La aplicación devolverá la imagen generada y el tiempo de inferencia.

---

## 🧪 API Reference

### 🔹 `GET /health`
Verifica el estado del servidor y modelo cargado.
```json
{
  "status": "ok",
  "model": "runwayml/stable-diffusion-v1-5"
}
```

### 🔹 `POST /generate`
Genera una imagen a partir de texto.

**Body (JSON):**
```json
{
  "prompt": "a corgi astronaut in space, digital art",
  "num_inference_steps": 20,
  "guidance_scale": 7.0,
  "width": 512,
  "height": 512,
  "seed": 1234
}
```

**Response:**  
- Content-Type: `image/png`  
- Headers: `X-Model`, `X-Elapsed`, `X-Seed`

---

## 🐳 Despliegue con Docker

```bash
docker build -t sd-app .
docker run --gpus all -p 8000:8000 sd-app
```

> Si no dispones de GPU, elimina `--gpus all` (la generación será más lenta en CPU).

---

## 🧠 Optimización de rendimiento

| Caso | Recomendaciones |
|------|-----------------|
| **Sin GPU** | Reducir resolución (`384x384`) y pasos (`8–12`) |
| **Con GPU NVIDIA** | Instalar Torch con CUDA y `xformers` |
| **Modo rápido** | Usar modelo `stabilityai/sdxl-turbo` con `steps=4–6` y `guidance_scale≈0` |

---

## 🧹 Limpieza de caché (liberar espacio)

Hugging Face almacena los modelos descargados (~2–7 GB) en:
```
C:\Users\<usuario>\.cache\huggingface\hub
```

Para liberar espacio:
```powershell
Remove-Item -Recurse -Force "$env:USERPROFILE\.cache\huggingface"
```

---

## 📂 Estructura del proyecto

```
sd-app/
├─ app/
│  ├─ main.py          # Rutas y servidor FastAPI
│  ├─ generate.py      # Carga y ejecución del modelo
│  ├─ config.py        # Configuración .env
│  └─ models.py        # Esquemas Pydantic
├─ static/
│  ├─ index.html       # Interfaz web
│  ├─ style.css        # Estilos
│  └─ app.js           # Lógica de cliente
├─ requirements.txt
├─ Dockerfile
├─ .env.example
└─ run.sh
```

---

## 🔮 Mejoras futuras

- [ ] Endpoint **img2img** (transformar imágenes)
- [ ] Integración **ControlNet**
- [ ] Sistema de **cola de trabajos (Redis + RQ)**
- [ ] **Galería** de imágenes generadas
- [ ] **Autenticación** de usuarios y límites de uso

---

## 👨‍💻 Autor

**Tu Nombre**  
💼 Desarrollador de Aplicaciones Web & Machine Learning  
📧 tu.email@ejemplo.com  
🌐 [tu-portfolio.com](https://tu-portfolio.com)  
🔗 [LinkedIn](https://linkedin.com/in/tuusuario) · [GitHub](https://github.com/yourusername)

---

## 📝 Licencia

Este proyecto se distribuye bajo la licencia **MIT**.  
El modelo *Stable Diffusion* conserva su propia licencia según su proveedor en Hugging Face.

---

⭐ **Si te gusta este proyecto, dale una estrella en GitHub y compártelo!**

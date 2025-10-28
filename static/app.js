async function generateImage() {
  const prompt = document.getElementById('prompt').value.trim();
  const steps = parseInt(document.getElementById('steps').value, 10);
  const guidance = parseFloat(document.getElementById('guidance').value);
  const width = parseInt(document.getElementById('width').value, 10);
  const height = parseInt(document.getElementById('height').value, 10);
  const seedInput = document.getElementById('seed').value;
  const seed = seedInput === "" ? null : parseInt(seedInput, 10);

  const status = document.getElementById('status');
  const img = document.getElementById('out');
  const dl = document.getElementById('download');
  const metaModel = document.getElementById('meta-model');
  const metaElapsed = document.getElementById('meta-elapsed');
  const metaSeed = document.getElementById('meta-seed');

  if (!prompt) {
    status.textContent = "Escribe un prompt 😊";
    return;
  }

  status.textContent = "Generando...";
  img.removeAttribute('src');
  dl.removeAttribute('href');

  try {
    const res = await fetch('/generate', {
      method: 'POST',
      headers: {'Content-Type':'application/json'},
      body: JSON.stringify({
        prompt,
        negative_prompt: "low quality, blurry, nsfw",
        num_inference_steps: steps,
        guidance_scale: guidance,
        width,
        height,
        seed
      })
    });

    if (!res.ok) {
      const text = await res.text();
      status.textContent = "Error: " + text;
      return;
    }

    const blob = await res.blob();
    const url = URL.createObjectURL(blob);
    img.src = url;
    dl.href = url;

    // meta headers
    const model = res.headers.get('X-Model');
    const elapsed = res.headers.get('X-Elapsed');
    const xseed = res.headers.get('X-Seed');

    metaModel.textContent = model ? `Modelo: ${model}` : "";
    metaElapsed.textContent = elapsed ? `Tiempo: ${elapsed}s` : "";
    metaSeed.textContent = xseed && xseed !== "-1" ? `Seed: ${xseed}` : "Seed: aleatoria";

    status.textContent = "Listo ✅";
  } catch (e) {
    status.textContent = "Error de red o servidor.";
    console.error(e);
  }
}

document.getElementById('generate').addEventListener('click', generateImage);


# 🧠 AutoTrain Web App (Flask)

Esta aplicación web ligera, desarrollada con Flask, permite configurar entrenamientos de modelos de lenguaje utilizando **Hugging Face AutoTrain Advanced**, directamente desde una interfaz web.

## 🚀 ¿Qué hace esta app?

- Proporciona un formulario web para:
  - Elegir el tipo de tarea (LLM, clasificación, etc.)
  - Subir datasets propios o referenciar datasets públicos de Hugging Face
  - Definir hiperparámetros (epochs, learning rate, etc.)
- Genera automáticamente el comando CLI para `autotrain-advanced`
- Ejecuta el entrenamiento localmente o en entornos con recursos como Colab o Spaces
- Devuelve la URL del modelo entrenado (cuando se publique en HF)

## 🧰 Requisitos

- Python 3.8 o superior
- Cuenta en Hugging Face con token activo ([crear token](https://huggingface.co/settings/tokens))

Instala las dependencias:

```bash
pip install -r requirements.txt


# PowerShell
$env:HUGGINGFACE_TOKEN="hf_..."  # Tu token personal
python app.py

# Accede desde tu navegador a:
📍 http://127.0.0.1:5000
```
![Captura de pantalla 2025-04-07 154616](https://github.com/user-attachments/assets/07d1e0a7-cb0c-4b04-a64e-636a87b4d09a)

Alternativamente puede iniciar la UI de la biblioteca:

```
autotrain app --port 8080 --host 127.0.0.1
```

![Captura de pantalla 2025-04-07 150511](https://github.com/user-attachments/assets/31b2f509-b987-48a6-b3d4-8f5065966cd9)


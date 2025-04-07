
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

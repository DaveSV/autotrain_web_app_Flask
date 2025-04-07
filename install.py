import os

# Crear la estructura del proyecto Flask
project_name = "autotrain_web_app"
os.makedirs(f"{project_name}/templates", exist_ok=True)
os.makedirs(f"{project_name}/static", exist_ok=True)

# Código base para app.py
app_py = '''from flask import Flask, request, render_template, redirect, url_for
import subprocess
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def train():
    if request.method == 'POST':
        model = request.form['model']
        dataset_path = request.form['dataset_path']
        project = request.form['project']
        epochs = request.form['epochs']
        batch = request.form['batch']
        use_peft = "--use-peft" if request.form.get('peft') == 'on' else ""
        quantization = f"--quantization {request.form['quantization']}" if request.form['quantization'] else ""

        command = f"autotrain llm --train --project-name {project} --model {model} --data-path {dataset_path} --output-path ./outputs/{project} --trainer sft {use_peft} {quantization} --epochs {epochs} --batch-size {batch}"

        os.makedirs(f'outputs/{project}', exist_ok=True)
        with open(f'outputs/{project}/command.sh', 'w') as f:
            f.write(command)

        subprocess.Popen(command, shell=True)

        return redirect(url_for('success', project=project))

    return render_template('form.html')

@app.route('/success/<project>')
def success(project):
    return f"Entrenamiento de <strong>{project}</strong> iniciado. El modelo estará disponible pronto en la carpeta <code>outputs/{project}</code>."

if __name__ == '__main__':
    app.run(debug=True)
'''

# HTML para el formulario
form_html = '''<!DOCTYPE html>
<html>
<head>
    <title>AutoTrain Web UI</title>
    <style>
        body { font-family: sans-serif; margin: 40px; }
        label { display: block; margin-top: 10px; }
        input, select { width: 300px; padding: 5px; }
    </style>
</head>
<body>
    <h1>AutoTrain - Entrenamiento Web</h1>
    <form method="post">
        <label>Modelo base:</label><input name="model" value="mistralai/Mistral-7B-Instruct">
        <label>Ruta dataset (.csv):</label><input name="dataset_path" value="./dataset.csv">
        <label>Nombre del proyecto:</label><input name="project" value="demo_proyecto">
        <label>Épocas:</label><input name="epochs" value="3">
        <label>Batch size:</label><input name="batch" value="2">
        <label>LoRA:</label><input type="checkbox" name="peft">
        <label>Quantization:</label>
        <select name="quantization">
            <option value="">None</option>
            <option value="4bit">4bit</option>
            <option value="8bit">8bit</option>
        </select>
        <br><br>
        <button type="submit">Entrenar</button>
    </form>
</body>
</html>
'''

# Guardar los archivos
with open(f"{project_name}/app.py", "w") as f:
    f.write(app_py)

with open(f"{project_name}/templates/form.html", "w") as f:
    f.write(form_html)

project_name

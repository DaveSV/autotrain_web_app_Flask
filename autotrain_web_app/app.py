from flask import Flask, request, render_template, redirect, url_for
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

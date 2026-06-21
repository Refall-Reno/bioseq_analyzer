import os
from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
from core.sequence_utils import process_fasta 

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        
        if file.filename == '':
            return redirect(request.url)

        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            from core.sequence_utils import process_fasta, generate_gc_plot, generate_csv
            top_3_sequences, all_data = process_fasta(filepath)
            
            plot_filename = generate_gc_plot(all_data)
            csv_filename = generate_csv(all_data)

            return render_template('result.html', 
                               top_3=top_3_sequences, 
                               all_data=all_data, 
                               plot_file=plot_filename, 
                               csv_file=csv_filename)

    return render_template('index.html')

if __name__ == '__main__':
    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000, debug=True)
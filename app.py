# app.py
import os
from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
from core.sequence_utils import process_fasta  # Mengimpor mesin pencari yang baru kita buat

app = Flask(__name__)

# Konfigurasi tempat menyimpan file FASTA yang diunggah user
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # Batas maksimal ukuran file 16 MB

# Memastikan folder upload tersedia
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Route utama ini sekarang bisa menerima file (POST) dan menampilkan halaman (GET)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 1. Mengecek apakah ada file yang diunggah
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        
        # 2. Jika user tidak memilih file tapi memencet tombol Upload
        if file.filename == '':
            return redirect(request.url)

        # 3. Jika file ada, kita simpan dan proses
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

          # 4. 🚀 MENJALANKAN MESIN BIOINFORMATIKA KITA 🚀
            from core.sequence_utils import process_fasta, generate_gc_plot, generate_csv
            top_3_sequences, all_data = process_fasta(filepath)
            
            # Membuat grafik dan CSV berdasarkan seluruh data
            plot_filename = generate_gc_plot(all_data)
            csv_filename = generate_csv(all_data)

            # 5. Mengirim data ke halaman web result.html
            return render_template('result.html', top_3=top_3_sequences, plot_file=plot_filename, csv_file=csv_filename)

    # Jika request.method == 'GET' (User baru pertama kali buka web)
    # Tampilkan halaman form upload (index.html)
    return render_template('index.html')

if __name__ == '__main__':
    if __name__ == '__main__':
    # host='0.0.0.0' artinya mengizinkan perangkat lain di jaringan yang sama untuk mengakses web ini
        app.run(host='0.0.0.0', port=5000, debug=True)
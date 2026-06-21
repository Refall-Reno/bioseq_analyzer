# 🧬 BioSeq Analyzer: Thermophilic Isolate Screening Platform

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web_Framework-black.svg?logo=flask&logoColor=white)
![Cloud](https://img.shields.io/badge/Deployment-PythonAnywhere-success.svg?logo=cloud&logoColor=white)
![Bioinformatics](https://img.shields.io/badge/Domain-Bioinformatics-ff69b4.svg)

**BioSeq Analyzer** adalah aplikasi web bioinformatika *cloud-based* yang dirancang khusus untuk memproses, menganalisis, dan mengevaluasi stabilitas termal (Thermal Stability) dari data sekuens DNA (Multi-FASTA) secara otomatis. 

Berbeda dengan skrip Python konvensional yang hanya berjalan di *localhost* komputer lokal, sistem ini telah **dideploy sepenuhnya ke Cloud Server (PythonAnywhere)**, menjadikannya platform yang dapat diakses secara global, kapan saja, dan dari perangkat apa saja (Mobile/Desktop/Tablet).

🌐 **Live Demo Application:** [https://refallreno.pythonanywhere.com](https://refallreno.pythonanywhere.com)

---

## ✨ Fitur Unggulan (The "Wow" Factor)

Aplikasi ini tidak hanya menampilkan angka matematis, tetapi dilengkapi dengan fitur-fitur berstandar industri perangkat lunak modern:

### 1. 🧠 Dynamic Biological Insight Engine (Smart Logic)
Aplikasi ini dilengkapi dengan algoritma evaluasi bersyarat (*If-Else Statement* menggunakan Jinja2) yang mampu bertindak layaknya analis bioinformatika. Sistem tidak hanya mengurutkan skor GC, tetapi juga **menginterpretasikan maknanya secara biologis**:
* 🔥 **Kandidat Termofilik (GC ≥ 60%):** Sistem otomatis merekomendasikan DNA untuk eksplorasi enzim termostabil (seperti *Taq Polymerase*) dan industri suhu tinggi.
* 🌡️ **Kandidat Mesofilik (40% ≤ GC < 60%):** Sistem mengklasifikasikannya sebagai bakteri suhu ruang normal (risiko denaturasi di suhu ekstrem).
* ❄️ **Bukan Termofilik (GC < 40%):** Sistem secara cerdas mendeteksi struktur *AT-rich* dan memberikan peringatan bahwa spesimen sangat rentan "meleleh".

### 2. ☁️ Global Cloud Deployment
Tidak perlu instalasi Python, *library*, atau menjalankan terminal secara lokal. Peneliti atau *user* hanya perlu membuka *browser* dari HP atau Laptop, mengunggah file FASTA, dan *server backend* kami yang akan melakukan komputasi beratnya. 

### 3. 🌓 Persistent Dark Mode Architecture
Dilengkapi dengan sistem UI/UX adaptif. Menggunakan integrasi JavaScript dan **LocalStorage Browser**, sistem akan "mengingat" preferensi tema pengguna (Light/Dark Mode). Transisi antar halaman (dari layar *Upload* ke layar *Report*) terjadi secara mulus tanpa *flash-bang* warna putih yang mengganggu mata.

### 4. 📊 Automated Data Visualization & Export
Hanya dengan 1 kali klik, *backend* secara sinkron akan:
* Mengekstraksi sekuens menggunakan *Biopython*.
* Menghitung rasio termodinamika nukleotida (A, T, G, C).
* Merender grafik perbandingan visual menggunakan *Matplotlib*.
* Menyusun dan memberikan akses unduh laporan mentah dalam format `.csv` otomatis.

---

## ⚙️ Arsitektur Sistem & Cara Kerja (Workflow)

Aplikasi ini menggunakan arsitektur *Client-Server* modern dengan alur kerja sebagai berikut:

1.  **Data Ingestion (Frontend):** Pengguna mengunggah file Multi-FASTA melalui *UI Upload Zone* yang responsif. Validasi ekstensi file dilakukan untuk memastikan integritas data.
2.  **Genomic Processing (Backend):** *Controller* Flask menerima *payload* file. Modul logika murni Python kemudian membedah file tersebut, memisahkan setiap *ID Sekuens*, menghitung *length* (panjang basa), dan melakukan kalkulasi frekuensi `(G+C) / (A+T+G+C) * 100`.
3.  **Data Sorting & Modeling:** Spesimen diurutkan berdasarkan parameter *GC Content* tertinggi ke terendah secara komputasional (*Descending Order*).
4.  **Dynamic Rendering (Jinja2 + AI Logic):** Flask mengirim paket data Top 3 kandidat ke mesin perender HTML (Jinja2). Di sinilah logika *If-Else Insight Biologis* dieksekusi secara otomatis sebelum dikirim kembali ke layar *user*.
5.  **Output Presentation:** *User* menerima laporan interaktif dalam hitungan detik, lengkap dengan grafik distribusi visual dan tombol ekspor *dataset* (CSV).

---

## 🛠️ Tech Stack & Dependencies

* **Backend Framework:** Python 3.10+, Flask
* **Bioinformatics Tools:** Biopython (Sequence Parsing)
* **Data Analysis & Viz:** Matplotlib (Plotting), CSV built-in module
* **Frontend Design:** HTML5, CSS3 Kustom, Bootstrap 5 (Responsive Grid)
* **Client-Side Scripting:** Vanilla JavaScript (LocalStorage & DOM Manipulation)
* **Cloud Infrastructure:** Linux-based server via PythonAnywhere

---

> *"Transforming raw sequences into actionable biological insights."* > **Developed by Moreno Ardiansyah** | 2026
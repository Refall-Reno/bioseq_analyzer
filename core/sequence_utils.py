# core/sequence_utils.py
from Bio import SeqIO
import matplotlib
# Menggunakan 'Agg' agar Matplotlib bisa berjalan di background Flask tanpa error GUI
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import os

def process_fasta(file_path):
    """
    Membaca file FASTA, menghitung frekuensi basa, dan GC Content.
    """
    sequences_list = [] 

    for record in SeqIO.parse(file_path, "fasta"):
        seq = str(record.seq).upper()
        
        counts = {
            'A': seq.count('A'),
            'T': seq.count('T'),
            'G': seq.count('G'),
            'C': seq.count('C')
        }
        
        total_bases = len(seq)
        gc_content = ((counts['G'] + counts['C']) / total_bases) * 100 if total_bases > 0 else 0.0
            
        seq_data = {
            'id': record.id,
            'length': total_bases,
            'gc_content': round(gc_content, 2),
            'freq': counts
        }
        sequences_list.append(seq_data)
        
    sequences_list.sort(key=lambda x: x['gc_content'], reverse=True)
    top_3_sequences = sequences_list[:3]
    
    return top_3_sequences, sequences_list

def generate_gc_plot(sequences_list):
    """
    Fungsi untuk membuat diagram batang (Bar Chart) GC Content ala Dashboard Sains.
    """
    plot_data = sequences_list[:10]
    ids = [seq['id'] for seq in plot_data]
    gc_values = [seq['gc_content'] for seq in plot_data]

    # Mengatur style grafik
    plt.figure(figsize=(10, 6), facecolor='#f4f7f6')
    ax = plt.axes()
    ax.set_facecolor('#f4f7f6')

    # Membuat bar chart dengan warna hijau sains (teal)
    bars = plt.bar(ids, gc_values, color='#20c997', width=0.6, edgecolor='#128c6e', linewidth=1.5, zorder=3)
    
    # Menambahkan angka di atas batang
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 2, f'{yval}%', ha='center', va='bottom', fontsize=10, fontweight='bold', color='#2c3e50')

    # Desain tipografi dan axis
    plt.title('Distribusi Kandungan GC (Top Kandidat)', fontsize=16, fontweight='bold', color='#2c3e50', pad=20)
    plt.xlabel('ID Sekuens', fontsize=12, fontweight='bold', color='#2c3e50', labelpad=15)
    plt.ylabel('Kandungan GC (%)', fontsize=12, fontweight='bold', color='#2c3e50', labelpad=15)
    plt.ylim(0, 115) 
    
    # Mempercantik grid dan garis tepi
    plt.grid(axis='y', linestyle='--', alpha=0.7, zorder=0)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#bdc3c7')
    ax.spines['bottom'].set_color('#bdc3c7')

    plt.xticks(rotation=20, ha='right', fontsize=10, fontname='monospace')
    plt.tight_layout()

    plot_filename = 'gc_chart.png'
    plot_path = os.path.join('static', 'plots', plot_filename) 
    plt.savefig(plot_path, dpi=300) # dpi=300 agar gambar High Resolution
    plt.close()
    
    return plot_filename

import pandas as pd

def generate_csv(sequences_list):
    """
    Fungsi untuk mengekspor data hasil analisis ke file CSV menggunakan pandas.
    """
    # Kita rapikan datanya dulu agar saat dibuka di Excel/CSV terlihat cantik
    flat_data = []
    for seq in sequences_list:
        flat_data.append({
            'Peringkat': sequences_list.index(seq) + 1,
            'ID Sekuens': seq['id'],
            'Panjang Genom (bp)': seq['length'],
            'GC Content (%)': seq['gc_content'],
            'A': seq['freq']['A'],
            'T': seq['freq']['T'],
            'G': seq['freq']['G'],
            'C': seq['freq']['C']
        })
        
    # Mengubah list menjadi DataFrame (Tabel Pandas)
    df = pd.DataFrame(flat_data)
    
    # Menyimpan file CSV ke folder static/uploads
    csv_filename = 'hasil_skrining_termofilik.csv'
    csv_path = os.path.join('static', 'uploads', csv_filename)
    df.to_csv(csv_path, index=False)
    
    return csv_filename
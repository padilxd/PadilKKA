FOTO [output](./images)

📊 Analisis Nilai Siswa Menggunakan Python

Proyek ini berisi analisis data nilai siswa dari beberapa mata pelajaran menggunakan Python, Pandas, dan visualisasi data (Matplotlib & Seaborn).
Semua hasil analisis, grafik, dan visualisasi telah terangkum dengan lengkap.

📁 Struktur Project
|-- nilai_siswa.csv
|-- analisis.py
|-- images/
      |-- bar_chart.png
      |-- boxplot.png
      |-- mean.png
      |-- median.png
      |-- modus.png
      |-- groupby.png
|-- README.md

📌 1. Informasi Dataset

Dataset berisi 22 baris dan 3 kolom, yaitu:

Kolom	Tipe Data	Keterangan
Nama	object	Nama siswa
Matpel	object	Mata pelajaran
Nilai	int64	Nilai siswa

✔ Tidak ada missing values.

📌 2. Hasil Analisis Data
🔹 2.1 Hasil print(data.info())

Dataset memuat informasi umum seperti tipe kolom dan jumlah data.

📷 Screenshot:


🔹 2.2 Hasil print(data.head())

5 baris pertama:

Nama	Matpel	Nilai
Ade	Bahasa Indonesia	87
Aira	Bahasa Indonesia	88
Badi	Bahasa Inggris	78
Cyla	Bahasa Inggris	90
Khansa	Matematika	98

📷 Screenshot:


🔹 2.3 Hasil print(data.describe())
Statistik	Nilai
Count	22
Mean	86.2727
Std Dev	6.706
Min	75
Median	87.5
Max	98

📷 Screenshot:


📌 3. Statistik Dasar
Keterangan	Nilai
Mean (Rata-rata)	86.27
Median	87.5
Modus	85

📷 Mean:


📷 Median:


📷 Modus:


📌 4. Nilai Max & Min per Mata Pelajaran

Hasil groupby('Matpel').agg(['max','min']):

Mata Pelajaran	Max	Min
Bahasa Indonesia	88	75
Bahasa Inggris	90	78
Fisika	95	75
Matematika	98	85
Produktif	90	80

📷 Screenshot:


📊 5. Visualisasi Data
▶ Grafik Batang (Bar Chart)

Menampilkan nilai per mata pelajaran.

📷


▶ Boxplot

Menunjukkan sebaran nilai & outlier.

📷


🧠 6. Analisis & Jawaban Pertanyaan
1. Mapel mana yang punya rata-rata tertinggi?

➡ Matematika, rata-rata 91,5.
Siswa konsisten mendapat nilai tinggi.

2. Mapel mana yang nilai minimumnya paling rendah?

➡ Bahasa Indonesia & Fisika, nilai minimum 75.

3. Bagaimana visualisasi membantu?

➡ Grafik memudahkan memahami data tanpa harus membaca angka satu-satu.
Kita bisa langsung tahu nilai mapel mana yang bagus dan yang harus ditingkatkan.

📝 7. Refleksi Siswa
1. Hal baru yang dipelajari

Cara memakai Python untuk analisis data

Membuat grafik dengan Matplotlib dan Seaborn

Membaca data CSV dan mengolahnya menjadi statistik

2. Kesulitan yang ditemui

Mengatur layout grafik agar rapi

Error saat nama kolom tidak sesuai

Menempatkan file gambar ketika ingin upload ke GitHub

3. Apakah AI membantu?

Ya. AI membantu:

Menjelaskan hasil analisis

Memberi kode Python

Membantu memperbaiki error

Membantu menyusun laporan ini

▶ Cara Menjalankan Program

Install library:

pip install pandas matplotlib seaborn


Jalankan file:

python analisis.py


Pastikan file nilai_siswa.csv dan folder images/ berada di direktori yang sama.

✨ Penutup

Proyek ini dibuat untuk memahami cara menganalisis data sederhana menggunakan Python dan menyajikan hasilnya dalam bentuk visual dan penjelasan.
Semoga bermanfaat untuk pembelajaran Data Science dasar.
Hasil Modus<img width="1245" height="48" alt="Hasil  modus" src="https://github.com/user-attachments/assets/c79a0711-a417-4f58-965d-6bd75908d67a" />
Grafik<img width="1536" height="754" alt="grafik_kka" src="https://github.com/user-attachments/assets/b4a722dc-1c59-47cf-a0d1-5554acfd29bc" />
Boxplot<img width="1536" height="754" alt="boxplot_kka" src="https://github.com/user-attachments/assets/80bf9297-a550-4844-b38d-db55a779b670" />
Hasil print(data info())<img width="1247" height="271" alt="Hasil print(data info())" src="https://github.com/user-attachments/assets/355e6366-8f86-4855-9dc0-0d986681b066" />
Hasil print(data head())<img width="1274" height="162" alt="Hasil print(data head())" src="https://github.com/user-attachments/assets/167a6dd6-c932-4680-9729-56b55d498c2d" />
Hasil print(data describe()<img width="1241" height="219" alt="Hasil print(data describe())" src="https://github.com/user-attachments/assets/48277497-0633-4c64-bbe3-43fce2685787" />
Hasil median<img width="1249" height="47" alt="Hasil median" src="https://github.com/user-attachments/assets/a4b7c7aa-355a-4546-bc2d-43bd35d9c848" />
Hasil mean<img width="1242" height="46" alt="Hasil mean" src="https://github.com/user-attachments/assets/fea2990d-5a8b-40f0-9536-b23015e5eab4" />
Hasil groupby maxmin<img width="1241" height="176" alt="Hasil groupby maxmin" src="https://github.com/user-attachments/assets/bbed0adf-0266-4de5-844a-20ddbf2fe5c3" />









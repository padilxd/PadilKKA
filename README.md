FOTO [output](./images)

Analisis dan Pertanyaan

1. Mapel mana yang memiliki rata-rata nilai tertinggi? ➡ Matematika memiliki rata-rata nilai tertinggi, yaitu 91,5. (Siswa pada mapel ini umumnya memperoleh nilai di atas 85.)

2. Mapel mana yang memiliki nilai terendah? ➡ Nilai terendah ada pada Bahasa Indonesia dan Fisika, yaitu 75. (Itu berarti ada siswa yang nilainya cukup rendah di dua mapel ini.)

3. Bagaimana visualisasi membantu dalam memahami data? ➡ Visualisasi seperti grafik batang (bar chart) dan boxplot membantu kita melihat perbandingan dan sebaran nilai antar mapel dengan cepat. Kita bisa langsung tahu mana mapel yang hasilnya bagus, mana yang perlu ditingkatkan — tanpa harus menghitung satu per satu.

Refleksi Siswa

1. Apa hal baru yang kamu pelajari dari kegiatan analisis dan visualisasi data? ➡ Saya belajar cara menggunakan Python (pandas, matplotlib, seaborn) untuk menganalisis data dan membuat grafik. Ternyata data yang awalnya hanya angka bisa jadi lebih mudah dipahami lewat grafik.

2. Kesulitan apa yang kamu alami dalam membuat grafik? ➡ Kadang sulit mengatur tampilan grafik agar rapi (misalnya ukuran tulisan, label, dan warna). Selain itu, kadang error muncul kalau nama kolom di CSV tidak sama dengan yang di kode Python.

3. Menurut kamu AI apa membantu dalam analisis sebuah data? ➡ Ya, AI sangat membantu dalam analisis data. AI bisa menjelaskan hasilnya, memberi saran, bahkan membantu menulis kode Python untuk membuat visualisasi atau menemukan pola dalam data dengan lebih cepat.

✅ 1️⃣ Hasil print(data.info())

Data memiliki 22 baris dan 3 kolom:

Nama → tipe object

Matpel → tipe object

Nilai → tipe int64

Tidak ada missing values.

✅ 2️⃣ Hasil print(data.head())

5 data teratas:

Nama	Matpel	Nilai
Ade	Bahasa Indonesia	87
Aira	Bahasa Indonesia	88
Badi	Bahasa Inggris	78
Cyla	Bahasa Inggris	90
Khansa	Matematika	98
✅ 3️⃣ Hasil print(data.describe())

Statistik kolom Nilai:

Count: 22

Mean: 86.2727

Std: 6.706

Min: 75

25%: 85

50% (Median): 87.5

75%: 90

Max: 98

✅ 4️⃣ Mean, Median, Modus
Keterangan	Nilai
Mean (rata-rata)	86.27
Median	87.5
Modus	85
✅ 5️⃣ Hasil groupby('Matpel').agg(['max','min'])

Nilai max/min tiap mata pelajaran:

Mata Pelajaran	Max	Min
Bahasa Indonesia	88	75
Bahasa Inggris	90	78
Fisika	95	75
Matematika	98	85
Produktif	90	80


Hasil Modus<img width="1245" height="48" alt="Hasil  modus" src="https://github.com/user-attachments/assets/c79a0711-a417-4f58-965d-6bd75908d67a" />
Grafik<img width="1536" height="754" alt="grafik_kka" src="https://github.com/user-attachments/assets/b4a722dc-1c59-47cf-a0d1-5554acfd29bc" />
Boxplot<img width="1536" height="754" alt="boxplot_kka" src="https://github.com/user-attachments/assets/80bf9297-a550-4844-b38d-db55a779b670" />
Hasil print(data info())<img width="1247" height="271" alt="Hasil print(data info())" src="https://github.com/user-attachments/assets/355e6366-8f86-4855-9dc0-0d986681b066" />
Hasil print(data head())<img width="1274" height="162" alt="Hasil print(data head())" src="https://github.com/user-attachments/assets/167a6dd6-c932-4680-9729-56b55d498c2d" />
Hasil print(data describe()<img width="1241" height="219" alt="Hasil print(data describe())" src="https://github.com/user-attachments/assets/48277497-0633-4c64-bbe3-43fce2685787" />
Hasil median<img width="1249" height="47" alt="Hasil median" src="https://github.com/user-attachments/assets/a4b7c7aa-355a-4546-bc2d-43bd35d9c848" />
Hasil mean<img width="1242" height="46" alt="Hasil mean" src="https://github.com/user-attachments/assets/fea2990d-5a8b-40f0-9536-b23015e5eab4" />
Hasil groupby maxmin<img width="1241" height="176" alt="Hasil groupby maxmin" src="https://github.com/user-attachments/assets/bbed0adf-0266-4de5-844a-20ddbf2fe5c3" />


✨ Penutup

Proyek ini dibuat untuk memahami cara menganalisis data sederhana menggunakan Python dan menyajikan hasilnya dalam bentuk visual dan penjelasan.
Semoga bermanfaat untuk pembelajaran Data Science dasar.






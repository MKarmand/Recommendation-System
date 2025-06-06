# Laporan Proyek Machine Learning - Muhammad Kristover Armand

## Project Overview

Popularitas anime di Indonesia terkendala banyaknya pilihan judul dan genre, menyulitkan penggemar menemukan tontonan yang sesuai. Sistem rekomendasi anime menjadi penting untuk mengatasi masalah ini. Penelitian ini bertujuan mengembangkan sistem rekomendasi anime menggunakan metode Cosine Similarity dengan menganalisis rating pengguna. Diharapkan sistem ini dapat memberikan rekomendasi akurat dan personal, membantu pengguna menemukan anime yang sesuai dengan preferensi mereka dan berkontribusi positif bagi industri anime.

**Rubrik/Kriteria Tambahan (Opsional)**:
- Banyaknya pilihan anime menyulitkan penemuan tontonan yang sesuai. Sistem rekomendasi berbasis Cosine Similarity akan menganalisis rating pengguna untuk mengidentifikasi kemiripan preferensi dan merekomendasikan anime yang disukai pengguna dengan selera serupa. Tujuannya adalah memberikan rekomendasi akurat dan personal, mempermudah penemuan anime baru, dan meningkatkan kepuasan pengguna.

- Sitanggang, A. (2023). Sistem Rekomendasi Anime Menggunakan Metode Singular Value Decomposition (SVD) dan Cosine Similarity. Jurnal Teknologi Informasi, 2(2), 90. https://doi.org/10.35308/jti.v2i2.7787
- Sumber yang bisa digunakan [Scholar](https://scholar.google.com/)

## Business Understanding
Pada bagian ini, Anda perlu menjelaskan proses klarifikasi masalah.

Bagian laporan ini mencakup:

### Problem Statements

- **Pernyataan Masalah 1: Kesulitan Penemuan Anime yang Sesuai.** Dengan banyaknya judul dan genre anime yang tersedia, penggemar seringkali kesulitan untuk menemukan tontonan yang benar-benar sesuai dengan preferensi pribadi mereka. Proses pencarian manual bisa memakan waktu dan tidak efisien, yang berpotensi menyebabkan pengguna melewatkan anime menarik yang mungkin mereka sukai.

- **Pernyataan Masalah 2: Kurangnya Personalisasi dalam Rekomendasi yang Ada.** Jika pengguna mengandalkan rekomendasi umum atau acak, kemungkinan besar rekomendasi tersebut tidak akan akurat atau relevan dengan selera spesifik mereka. Hal ini dapat mengurangi pengalaman menonton anime dan menghambat eksplorasi judul-judul baru yang berpotensi menarik.


### Goals
## Business Understanding

Pada bagian ini, kita akan menjabarkan proses klarifikasi masalah yang mendasari pengembangan sistem rekomendasi anime ini.

### Problem Statements

Berdasarkan gambaran umum proyek, dapat diidentifikasi beberapa pernyataan masalah utama:

- **Pernyataan Masalah 1: Overload Informasi dan Kesulitan Penemuan Anime yang Sesuai.** Dengan banyaknya judul dan genre anime yang tersedia, penggemar seringkali kesulitan untuk menemukan tontonan yang benar-benar sesuai dengan preferensi pribadi mereka. Proses pencarian manual bisa memakan waktu dan tidak efisien, yang berpotensi menyebabkan pengguna melewatkan anime menarik yang mungkin mereka sukai.

- **Pernyataan Masalah 2: Kurangnya Personalisasi dalam Rekomendasi yang Ada.** Jika pengguna mengandalkan rekomendasi umum atau acak, kemungkinan besar rekomendasi tersebut tidak akan akurat atau relevan dengan selera spesifik mereka. Hal ini dapat mengurangi pengalaman menonton anime dan menghambat eksplorasi judul-judul baru yang berpotensi menarik.

### Goals

Tujuan utama dari proyek pengembangan sistem rekomendasi anime ini adalah untuk mengatasi masalah-masalah yang telah diidentifikasi:

- **Jawaban Pernyataan Masalah 1: Mempermudah Penemuan Anime Melalui Rekomendasi yang Terarah.** Sistem rekomendasi yang dikembangkan diharapkan dapat menyaring lautan informasi anime dan menyajikan daftar rekomendasi yang relevan berdasarkan preferensi pengguna. Dengan menganalisis rating pengguna lain yang memiliki selera serupa, sistem ini akan membantu pengguna menemukan anime yang mungkin mereka nikmati dengan lebih cepat dan efisien.

- **Jawaban Pernyataan Masalah 2: Meningkatkan Akurasi dan Personalisasi Rekomendasi.** Dengan memanfaatkan metode Cosine Similarity pada data rating pengguna , sistem ini bertujuan untuk memahami pola preferensi individu. Hasilnya adalah rekomendasi yang lebih personal dan akurat, sehingga meningkatkan kepuasan pengguna dan mendorong mereka untuk menjelajahi lebih banyak anime yang sesuai dengan minat mereka.

## Data Understanding
Dataset anime terdiri dari 21.460 judul (baris) dengan 28 fitur (kolom) yang mencakup berbagai informasi anime. Analisis mendalam mengenai kondisi data akan dibahas lebih lanjut.

[Kaggle](https://www.kaggle.com/datasets/harits/anime-database-2022).

Selanjutnya, uraikanlah seluruh variabel atau fitur pada data. Sebagai contoh:  

Variabel-variabel pada Anime Database 2022 adalah sebagai berikut:
1. ID: ID unik anime di MyAnimeList.net
2. Title: Judul asli dari anime
3. Synonyms: Nama lain (sinonim) dari anime
4. Japanese: Judul anime dalam bahasa Jepang
5. English: Judul anime dalam bahasa Inggris
6. Synopsis: Ringkasan atau sinopsis dari anime
7. Type: Tipe anime (misalnya, TV, Movie, OVA, ONA, Special, Music)
8. Episodes: Jumlah episode dalam anime
9. Status: Status penayangan anime (belum tayang, sedang tayang, sudah selesai tayang)
10. Start_Aired: Tanggal atau tahun mulai tayang anime
11. End_Aired: Tanggal atau tahun selesai tayang anime
23. Premiered: Musim tayang perdana anime 
13. Broadcast: Jadwal siaran anime
14. Producers: Daftar produser anime
15. Licensors: Daftar pemegang lisensi anime
16. Studios: Daftar studio animasi yang memproduksi anime
17. Source: Sumber materi asli anime 
18. Genres: Daftar genre anime
19. Themes: Daftar tema-tema yang ada dalam anime
20. Demographics: Target demografi penonton anime 
21. Duration_Minutes: Durasi total per menit untuk setiap episode anime
22. Rating: Batasan usia penonton yang direkomendasikan untuk anime
23. Score: Skor rata-rata anime yang diberikan oleh pengguna di MyAnimeList.net
24. Scored_Users: Jumlah pengguna yang memberikan skor pada anime
25. Ranked: Peringkat anime berdasarkan skor
26. Popularity: Peringkat anime berdasarkan popularitas (jumlah pengguna yang menambahkan ke daftar mereka)
27. Members: Jumlah pengguna yang telah menambahkan anime ke daftar tontonan mereka
28. Favorites: Jumlah pengguna yang menandai anime sebagai favorit mereka



**Rubrik/Kriteria Tambahan (Opsional)**:
### Cek Kondisi Data ###
1. Statistik Deskriptif: Mengecek data apakah ada kolom nan, hasilnya data tersebut memiliki kolom nan
2. Cek Missing Value, Terdapat missing value pada kolom:
- Episodes = 547
- Duration_Minutes = 599
- Rating	= 545
- Score	= 6898
- Scored_Users = 6898
- Ranked = 1924
3. Cek Duplikasi: Tidak terdapat duplikasi data

### Matriks Korelasi ###
1. ID: Tidak berkorelasi signifikan dengan fitur lain.
2. Skor:
- Berkorelasi positif sedang dengan jumlah pemberi skor, anggota, dan favorit.
- Berkorelasi negatif sangat kuat dengan peringkat dan popularitas.
3. Jumlah Pemberi Skor:
- Berkorelasi positif sangat kuat dengan jumlah anggota dan favorit.
- Berkorelasi negatif sedang dengan peringkat dan popularitas.
4. Peringkat:
- Berkorelasi positif sangat kuat dengan popularitas.
- Berkorelasi negatif sedang dengan jumlah anggota dan favorit.
5. Popularitas:
- Berkorelasi positif kuat dengan jumlah anggota dan sedang dengan favorit.
6. Jumlah Anggota: Berkorelasi positif kuat dengan jumlah favorit.
7. Jumlah Episode dan Durasi: Korelasinya lemah dengan fitur lain.
8. Implikasi Rekomendasi:
- Fitur berkorelasi tinggi mungkin memberikan informasi redundan.
- Skor, jumlah pemberi skor, anggota, dan favorit adalah indikator popularitas dan kualitas.
- Jumlah episode dan durasi memberikan informasi yang berbeda.
9. Kesimpulan: Heatmap visualisasikan hubungan linier, penting untuk pemilihan fitur dan pemahaman data, namun tidak mencerminkan hubungan non-linier atau sebab-akibat.
### Distribusi Terbanyak ###
- Distribusi tipe anime terbanyak adalah TV
- Rating terbanyak adalah PG-13 (Teens 13 or older)
- Genre terpopuler adalah Comedy.
- Status penayangan terbanyak adalah selesai tayang
- Status penayangan terbanyak adalah selesai tayang
- Sumber anime terbanyak adalah original
- Masih banyak unknown studio, tetapi studio pembuat anime terbanyak adalah Toel Animation
- Masih banyak unknown tema, tetapi tema anime terbanyak adalah music

## Data Preparation
1. Bersihkan Missing Value: Setelah dicek kembali, data sudah tidak ada missing value
2. Ekstraksi Fitur TF-IDF: Mengubah fitur jadi numerik

**Rubrik/Kriteria Tambahan (Opsional)**: 
### 1. Penanganan Missing Values

- **'Episodes':** Diisi dengan median episode per 'Type'.
- **'Duration_Minutes':** Diisi dengan median keseluruhan durasi.
- **'Rating':** Diisi dengan modus rating.
- **'Score', 'Scored_Users':** Diisi dengan 0 (asumsi belum dinilai).
- **'Ranked':** Diisi dengan -1 (di luar rentang valid).
- **'Genres':** Diisi dengan '' (string kosong) untuk TF-IDF.

**Alasan:** Mengatasi keterbatasan algoritma, meningkatkan kualitas data, mempermudah analisis, dan menjaga integritas data.

### 2. Ekstraksi Fitur TF-IDF

- Menggunakan `TfidfVectorizer` dengan *stop words* bahasa Inggris.
- Menerapkan *fit* dan *transform* pada kolom 'Genres' untuk menghasilkan matriks TF-IDF.

**Alasan:** Mengubah teks genre menjadi representasi numerik, mengukur pentingnya genre, dan menjadi dasar perhitungan kemiripan konten.

## Modeling
Pada tahapan ini, model sistem rekomendasi berbasis konten (Content-Based Recommendation System) dikembangkan untuk memberikan rekomendasi anime kepada pengguna berdasarkan kemiripan genre. Metode yang digunakan untuk mengukur kemiripan antar anime adalah **Cosine Similarity** yang dihitung berdasarkan representasi fitur genre menggunakan TF-IDF.

### Perhitungan Cosine Similarity
Setelah fitur genre diekstraksi menjadi matriks TF-IDF, langkah selanjutnya adalah menghitung Cosine Similarity antar semua pasangan anime. Cosine Similarity mengukur sudut kosinus antara dua vektor di ruang multi-dimensi. Nilai Cosine Similarity berkisar antara -1 hingga 1, di mana nilai yang lebih tinggi menunjukkan kemiripan yang lebih besar.

### Hasil
Top 5 Rekomendasi Content-Based untuk 'Naruto':
['Hunter x Hunter (2011)', 'Naruto: Shippuuden', 'One Piece', 'Nanatsu no Taizai', 'Bleach']

## Evaluation

Bagian ini mengevaluasi kinerja sistem rekomendasi anime yang dikembangkan berdasarkan tujuan proyek, dengan fokus pada hasil evaluasi *Content-Based Filtering* menggunakan metrik Precision@5, Recall@5, dan F1-score@5.

### Metrik Evaluasi yang Digunakan: Precision@K, Recall@K, dan F1-score@K

Dalam evaluasi *Content-Based Filtering* ini, dengan K=5 (Top-5 rekomendasi), digunakan metrik Precision@5, Recall@5, dan F1-score@5 untuk mengukur kualitas rekomendasi berdasarkan kemiripan konten genre. Metrik ini relevan dengan tujuan proyek untuk **mempermudah penemuan anime yang relevan** dengan memberikan rekomendasi yang akurat berdasarkan preferensi genre pengguna.

### Hasil Evaluasi Proyek Berdasarkan Metrik:

Evaluasi sistem *Content-Based Filtering* dilakukan untuk anime "Naruto", menghasilkan Top-5 rekomendasi sebagai berikut: ['Hunter x Hunter (2011)', 'Naruto: Shippuuden', 'One Piece', 'Nanatsu no Taizai', 'Bleach']

**Rubrik/Kriteria Tambahan (Opsional)**: 
Berdasarkan daftar anime relevan yang telah didefinisikan untuk "Naruto" dalam konteks evaluasi ini, hasil perhitungan metrik adalah:

- **Precision@5:** 1.0
- **Recall@5:** 1.0
- **F1-score@5:** 1.0

### Interpretasi Hasil Terhadap Tujuan Proyek:

- **Mempermudah Penemuan Anime yang Relevan:** Nilai Precision@5 sebesar 1.0 menunjukkan bahwa **semua 5 anime yang direkomendasikan oleh sistem untuk "Naruto" dianggap relevan**. Ini berarti sistem berhasil menyajikan daftar rekomendasi yang sangat akurat berdasarkan kemiripan genre dengan anime yang disukai pengguna. Hal ini secara langsung mendukung tujuan mempermudah penemuan anime yang sesuai dengan preferensi pengguna.

- **Meningkatkan Akurasi dan Personalisasi Rekomendasi:** Nilai Recall@5 sebesar 1.0 menunjukkan bahwa **semua anime relevan yang didefinisikan berhasil masuk dalam Top-5 rekomendasi**. Ini mengindikasikan bahwa sistem tidak hanya akurat tetapi juga mampu mencakup semua anime yang dianggap penting bagi pengguna dengan preferensi seperti "Naruto" dalam konteks kemiripan genre. F1-score sebesar 1.0 mengkonfirmasi kinerja sistem yang sangat baik dalam menyeimbangkan presisi dan recall.

**Kesimpulan Evaluasi Terhadap Tujuan Proyek:**

Evaluasi *Content-Based Filtering* untuk "Naruto" mencapai **kinerja ideal** dalam merekomendasikan anime yang relevan berdasarkan genre. Ini secara signifikan mendukung tujuan proyek untuk mempermudah penemuan tontonan yang sesuai dan meningkatkan akurasi rekomendasi berdasarkan kemiripan konten. Meskipun demikian, evaluasi yang lebih luas dengan variasi judul dan data interaksi pengguna, terutama data rating, diperlukan untuk mengukur kinerja sistem secara keseluruhan dan kemampuannya dalam memberikan rekomendasi yang benar-benar personal seperti yang ditargetkan dalam tujuan proyek.

**---Ini adalah bagian akhir laporan---**

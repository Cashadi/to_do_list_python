# To-Do List CLI

To-Do List CLI adalah aplikasi berbasis command-line yang memungkinkan pengguna untuk mengelola daftar tugas dengan mudah. Aplikasi ini mendukung penambahan, penghapusan, dan pembaruan status tugas.


## Fitur

- Lihat Semua Tugas: Menampilkan daftar tugas beserta ID, judul, deskripsi, status, dan estimasi waktu pengerjaan.

- Tambah Tugas: Memungkinkan pengguna untuk menambahkan tugas baru ke dalam daftar.

- Tandai Tugas Selesai: Mengubah status tugas menjadi "Selesai".

- Hapus Tugas: Menghapus tugas dari daftar.


## Struktur Kode

| Fungsi                  | Deskripsi                                              |
| ----------------------- | ------------------------------------------------------ |
| `menu()`                | Menampilkan menu utama aplikasi.                       |
| `lihat_tugas(tasks)`    | Menampilkan semua tugas dalam daftar.                  |
| `tambah_tugas(tasks)`   | Menambahkan tugas baru dengan estimasi waktu otomatis. |
| `tandai_selesai(tasks)` | Mengubah status tugas menjadi “Selesai”.               |
| `hapus_tugas(tasks)`    | Menghapus tugas yang sudah selesai.                    |
| `edit_tugas(tasks)`     | Mengedit tugas yang belum selesai.                     |
| `main()`                | Fungsi utama yang menjalankan logika aplikasi.         |


## Logika Estimasi Waktu Otomatis

Setiap tugas mendapatkan estimasi waktu berdasarkan ID:
- Jika ID genap → 45 menit
- Jika ID ganjil → 30 menit


## Catatan Pengembangan

- Aplikasi menggunakan variabel global next_id untuk menjaga agar setiap tugas memiliki ID unik, meskipun tugas sebelumnya telah dihapus.

- Fitur edit hanya diizinkan untuk tugas yang belum selesai.

- Fitur hapus hanya diizinkan untuk tugas yang sudah selesai.


## Lisensi
Aplikasi ini bersifat open source dan dapat digunakan atau dimodifikasi secara bebas untuk keperluan belajar.

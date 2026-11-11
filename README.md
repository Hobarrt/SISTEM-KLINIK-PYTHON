# SISTEM KLINIK

## 1. Struktur Folder

Berikut adalah struktur folder yang digunakan dalam pengembangan Sistem Klinik. Struktur ini dibuat sederhana agar setiap bagian program memiliki fungsi dan tanggung jawab masing-masing.

```text
SISTEM_KLINIK/
│
├── main.py
│
├── data/
│   ├── users.json
│   ├── dokter.json
│   ├── pasien.json
│   ├── layanan.json
│   ├── jadwal.json
│   ├── reservasi.json
│   ├── log_riwayat.json
│   ├── inventaris_alat.json
│   ├── obat.json
│   └── transaksi.json
│
├── auth/
│   ├── login.py
│   └── register.py
│
├── admin/
│   ├── dashboard.py
│   ├── dokter.py
│   ├── jadwal.py
│   ├── layanan.py
│   └── inventaris.py
│
├── resepsionis/
│   ├── dashboard.py
│   ├── pasien.py
│   ├── reservasi.py
│   ├── pembayaran.py
│   └── struk.py
│
├── pasien/
│   ├── dashboard.py
│   ├── dokter.py
│   ├── jadwal.py
│   ├── reservasi.py
│   └── riwayat.py
│
└── modules/
    ├── database.py
    ├── reservasi.py
    ├── inventaris.py
    ├── pembayaran.py
    └── utils.py
```

## 2. Pembagian Fungsi File

Setiap file memiliki tugas masing-masing untuk mempermudah pengembangan dan pemeliharaan program.

| File | Fungsi |
|---|---|
| `main.py` | Menampilkan menu utama dan mengatur proses login serta navigasi berdasarkan role pengguna. |
| `database.py` | Membaca, mengelola, dan menyimpan data dalam format JSON. |
| `admin/` | Mengelola data dokter, jadwal, layanan, dan inventaris. |
| `resepsionis/` | Mengelola pasien, reservasi, pembayaran, dan pembuatan struk. |
| `pasien/` | Menampilkan informasi dokter, jadwal, reservasi, dan riwayat pasien. |
| `auth/` | Menangani proses login dan registrasi pengguna. |
| `modules/` | Menyimpan fungsi utama yang digunakan bersama oleh beberapa bagian program. |
| `utils.py` | Menangani validasi input, format rupiah, dan pembuatan ID. |

## 3. Penyederhanaan Fitur

Agar pengembangan program tidak terlalu kompleks, beberapa fitur akan disederhanakan tanpa menghilangkan fungsi utamanya.

| Fitur | Penyederhanaan |
|---|---|
| Dokter | Data dokter dan biaya jasa digabungkan dalam satu pengelolaan. |
| Jadwal | Pengelolaan jadwal dihubungkan langsung dengan data reservasi. |
| Inventaris | Inventaris alat dan obat dikelola melalui satu bagian program, tetapi data JSON tetap dipisahkan. |
| Log Riwayat | Semua perubahan reservasi dicatat dalam satu file JSON. |
| Pembayaran | Perhitungan biaya dan proses pembayaran digabungkan dalam satu bagian. |
| Struk | Struk dibuat langsung berdasarkan data transaksi yang tersimpan. |

## 4. Pembagian Tugas Anggota

Pengembangan Sistem Klinik direncanakan dikerjakan oleh 3 orang anggota dengan pembagian tugas sebagai berikut.

### Anggota 1 – Admin
Bertanggung jawab dalam pengelolaan bagian admin, meliputi:

- Mengelola data dokter.
- Mengelola jadwal dokter.
- Mengelola layanan klinik.
- Mengelola inventaris alat dan obat.

### Anggota 2 – Resepsionis
Bertanggung jawab dalam pengelolaan bagian resepsionis, meliputi:

- Mengelola data pasien.
- Mengelola reservasi pasien.
- Mengelola proses pembayaran.
- Membuat dan mencetak struk transaksi.

### Anggota 3 – Pasien
Bertanggung jawab dalam pengembangan bagian pasien, meliputi:

- Menampilkan informasi dokter.
- Melihat jadwal dokter.
- Membuat reservasi secara mandiri.
- Melihat riwayat reservasi.

### Integrasi Program

Beberapa bagian utama perlu dikerjakan bersama atau ditentukan satu orang sebagai koordinator agar seluruh fitur dapat terhubung dengan baik.

Bagian tersebut meliputi:

- `main.py` – Mengatur jalannya program dan menghubungkan setiap menu.
- `database.py` – Mengatur proses penyimpanan dan pengambilan data JSON.
- `utils.py` – Menyediakan fungsi bantuan yang digunakan oleh seluruh anggota.

---

## 5. Catatan Pengembangan

- Setiap anggota mengembangkan fitur sesuai pembagian tugas masing-masing.
- Gunakan struktur folder yang telah ditentukan agar kode tetap terorganisir.
- Semua data disimpan menggunakan format JSON.
- Fungsi yang digunakan bersama sebaiknya diletakkan di dalam folder `modules/`.
- Pastikan setiap fitur dapat terintegrasi dengan `main.py`.
- Lakukan pengujian setiap fitur sebelum menggabungkan seluruh program.

**Tujuan utama:** Membuat Sistem Klinik yang sederhana, terstruktur, dan mudah dikembangkan oleh seluruh anggota tim.

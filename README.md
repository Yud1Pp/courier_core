# Courier Incident Log – BeraniExpress

Modul Odoo sederhana untuk mencatat dan mengelola insiden operasional kurir di BeraniExpress, mulai dari pelaporan hingga penyelesaian.

## Informasi Umum

- **Addon Name**: courier_core
- **Model**: courier.incident
- **Target Platform**: Odoo 18.0
- **Fitur Utama**:
  - Pencatatan insiden kurir
  - Workflow status: Draft → Follow-up → Done
  - Validasi dan dekorasi UI berbasis status

---

## Instalasi Singkat

1. Letakkan folder `courier_core` ke dalam direktori `addons` Odoo.
2. Restart server Odoo.
3. Aktifkan **Developer Mode**.
4. Install modul **Courier Core** melalui Apps.

---

## Langkah Manual Pengujian Fitur

### 1️⃣ Create Incident (Status: Draft)

1. Masuk ke menu **Courier → Log Insiden**.
2. Klik tombol **New**.
3. Isi data wajib:
   - **Judul Insiden**
   - **Customer**
   - **Incident Datetime** (otomatis terisi)
4. (Opsional) Isi:
   - Shipment / Resi
   - Incident Type
   - Severity
   - Kronologi
5. Klik **Save**.
6. Pastikan status berada di **Draft**.

---

### 2️⃣ Mark Follow-up (Status: Follow-up)

1. Buka data insiden yang masih berstatus **Draft**.
2. Klik tombol **Follow-up** di bagian atas form.
3. Status akan berubah menjadi **Follow-up**.
4. Tambahkan **Catatan Tindak Lanjut** jika diperlukan.
5. Klik **Save**.

---

### 3️⃣ Resolve Incident (Status: Done)

1. Buka data insiden yang masih berstatus **Follow-up**.
2. Pastikan field **Catatan Tindak Lanjut** sudah terisi.
3. Klik tombol **Done**.
4. Sistem akan:
   - Mengubah status menjadi **Done**
   - Mengisi field **Resolved At** secara otomatis
5. Data insiden dinyatakan selesai.

---

## Catatan Tambahan

- Status **Follow-up** ditandai dengan warna _warning_ pada List View.
- Status **Done** ditandai dengan warna _success_ pada List View.
- Sistem akan menolak penyelesaian (Resolve) jika **Catatan Tindak Lanjut** kosong.

---

## Git Commit Convention

Repositori ini menggunakan **Conventional Commits**, contoh:

- `feat(model): add courier.incident model`
- `feat(view): add incident tree and form views`
- `docs(readme): add testing instructions`

---

## Penutup

Modul ini dibuat sebagai bagian dari **Odoo Technical Test – Incident Log System BeraniExpress** dengan fokus pada struktur kode yang rapi, workflow sederhana, dan commit history yang bersih.

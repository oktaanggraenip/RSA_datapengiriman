# RSA_datapengiriman

Instalasi

    Pastikan Anda sudah memiliki Python 3.x dan pip terinstall di komputer Anda, tentunya juga terdapat dalam PATH Environment Variables.
    
    Pastikan juga Anda sudah menginstall Flask, library yang dibutuhkan program ini, dengan menjalankan perintah berikut pada terminal atau command prompt:

   ```python
   ```pip install flask```

    Setelah itu, unduh file program python app.py dan simpan pada direktori yang diinginkan.

Penggunaan

    Buka terminal atau command prompt, masuk ke dalam direktori tempat app.py disimpan, kemudian jalankan perintah berikut:
    
    ```python
    ```python app.py

    Buka browser Anda dan akses alamat http://localhost:5000/.

    Isi teks yang ingin dienkripsi pada form yang tersedia dan klik tombol "Enkripsi".

    Program akan menampilkan hasil enkripsi pada halaman yang sama.

    Untuk melakukan dekripsi, masukkan teks yang telah dienkripsi pada form yang tersedia dan klik tombol "Dekripsi".

    Program akan menampilkan hasil dekripsi pada halaman yang sama.

Catatan: Program ini masih menggunakan kunci statis. Jika ingin menghasilkan kunci baru, ubahlah fungsi generate_key_pair() pada program.

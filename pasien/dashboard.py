


def menu_pasien(username_login, nama_login):
    login_aktif = True 

    while login_aktif == True:
        print("Halooo selamaat dataang di klinik kami,", nama_login)
        tampilkan_menu(
            "=== Menu Pasien ===", [
            ["1", "Lihat dokter dan biaya jasa"]
            ["2", "Lihat Jenis Layanan"]
            ["3", "Lihat jadwal dan slot yang tersedia"]
            ["4", "Reservasi Konsultasi"]
            ["5", "Ubah atau batalkan reservasi"]
            ["6", "Lihat status dan Riwayat Reservasi"]
            ["7", "Lihat Tagihan"]
            ["8", "Lihat riwayat pembayaran"]
            ["9", "Lihat dan Unduh Struk"]
            ["0", "Logout"]
        ])
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            lihat_dokter()

        elif pilihan == "2":
            lihat_layanan()

        elif pilihan == "3":
            lihat_jadwal_slot()

        elif pilihan == "4":
            reservasi_konsultan()

        elif pilihan == "5":
            ubah_batal_reservasi()

        elif pilihan == "6":
            lihat_riwayat()

        elif pilihan == "7":
            lihat_tagihan()

        elif pilihan == "8":
            riwayat_pemayaran()

        elif pilihan == "9":
            unduh_struk()

        elif pilihan == "0":
            login_aktif = False

        else:
            print("pilihan tidak valid")






def lihat_dokter():
    print("===Lihat dokter dan Biaya Jasa===")
    if not data_dokter:
        print("belum ada dokter yang tersedia")
    else:
        for dokter in data_dokter:
            print("Nama dokter: ", dokter["nama"])
            print("Spesialisasi dokter: ", dokter["spesialisasi"])
            print("Biaya jasa praktek: ", dokter["biaya_jasa"])

def lihat_layanan():
    print("===Lihat layanan yang tersedia===")
    if not data_layanan:
        print("Belum ada layanan yang tersediaa")
    else:
        for layanan in data_layanan:
            print(["layanan"])


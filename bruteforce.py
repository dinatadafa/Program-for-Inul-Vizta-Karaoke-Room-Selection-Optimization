def pilih_ruangan_karaoke(max_budget, daftar_ruangan, jumlah_orang, fasilitas_tambahan):
    ruangan_terpilih = None
    biaya_total_terendah = float('inf')
    list_ruangan_terpilih = []
    list_biaya_total = []

    # Iterasi melalui semua kombinasi ruangan
    for i in range(len(daftar_ruangan)):
        ruangan = daftar_ruangan[i]
        kapasitas = ruangan['kapasitas maksimum']
        harga_sewa = ruangan['harga_sewa']
        
        if kapasitas >= jumlah_orang and harga_sewa <= max_budget:
            biaya_total = harga_sewa * jumlah_jam

            # Menghitung biaya peminjaman fasilitas tambahan
            biaya_fasilitas_tambahan = 0
            if fasilitas_tambahan['alat_musik']:
                biaya_fasilitas_tambahan += fasilitas_tambahan['alat_musik'] * 20000 
            if fasilitas_tambahan['sistem_suara']:
                biaya_fasilitas_tambahan += fasilitas_tambahan['sistem_suara'] * 50000

            # Menambahkan biaya fasilitas tambahan ke biaya total
            biaya_total += biaya_fasilitas_tambahan

            # Memastikan biaya split bill tidak melebihi maksimum budget
            biaya_per_orang = biaya_total / jumlah_orang
            if biaya_per_orang > max_budget:
                continue

            if biaya_total < biaya_total_terendah:
                ruangan_terpilih = ruangan
                biaya_total_terendah = biaya_total

                list_ruangan_terpilih = [ruangan_terpilih['nama']]
                list_biaya_total = [biaya_total_terendah]

    return list_ruangan_terpilih, list_biaya_total

# Data input
max_budget = 1000000
daftar_ruangan = [
    {'nama': 'VVIP', 'kapasitas maksimum': 18, 'harga_sewa': 700000},
    {'nama': 'VIP', 'kapasitas maksimum': 15, 'harga_sewa': 600000},
    {'nama': 'Huge', 'kapasitas maksimum': 10, 'harga_sewa': 500000},
    {'nama': 'Large', 'kapasitas maksimum': 7, 'harga_sewa': 400000},
    {'nama': 'Medium', 'kapasitas maksimum': 5, 'harga_sewa': 300000},
    {'nama': 'Small', 'kapasitas maksimum': 3, 'harga_sewa': 200000}
]
jumlah_orang = int(input("Masukkan jumlah orang: "))
fasilitas_tambahan = {
    'alat_musik': int(input("Masukkan jumlah alat musik yang ingin disewa: ")),
    'sistem_suara': int(input("Masukkan jumlah sistem suara berkualitas yang ingin disewa: "))
}
database_fasilitas = {
    'alat_musik': 20000,
    'sistem_suara': 50000
}

# Memasukkan jumlah jam secara manual
jumlah_jam = int(input("Masukkan jumlah jam: "))

# Panggil fungsi pilih_ruangan_karaoke
ruangan_terpilih, biaya_total = pilih_ruangan_karaoke(max_budget, daftar_ruangan, jumlah_orang, fasilitas_tambahan)

# Tampilkan hasil
if ruangan_terpilih:
    print("Tipe ruangan yang dipilih:")
    for i in range(len(ruangan_terpilih)):
        print("- Tipe Ruangan:", ruangan_terpilih[i])
        print("Total biaya sewa: Rp", biaya_total[i])
else:
    print("Tidak ada ruangan yang sesuai dengan jumlah orang atau budget yang tersedia.")

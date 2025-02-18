def perkenalan(nama, nim, peran):
    print("Halo! Perkenalkan, nama saya", nama)
    print("NIM :", nim)
    print("Peran saya yaitu:", peran)
    print("-")

if __name__ == "__main__":
    anggota = [
        ("Yusuf Kurniawan", "2213010350", "Menjabat Sebagai Frontend"),
        ("Ilham Pebrianto Eko Saputro", "2213010378", "Menjabat Sebagai Backend"),
        ("Muhammad Rafi Maliki", "2213010348", "Menjabat Sebagai Ketua"),
        ("Ardya Zahira Ardhana", "2213010371", "Menjabat Sebagai Presenter")
    ]
    
    for nama, nim, peran in anggota:
        perkenalan(nama, nim, peran)

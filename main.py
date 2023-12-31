import json
from difflib import SequenceMatcher

file = open('data.json')
data_hewan = json.load(file)

def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

def tampilkan_hewan_cocok(matching_animals):
    print("\nHewan yang cocok:")
    for i, hewan in enumerate(matching_animals, start=1):
        print(f"{i}. {hewan}")

def tampilkan_saran(selected_animal_data):
    if selected_animal_data:
        print("\nSuggestion:")
        print(selected_animal_data.get("deskripsi", "Deskripsi tidak tersedia."))
    else:
        print("Data hewan tidak ditemukan.")

while True:

    search_criteria = {}

    print("Masukkan kriteria pencarian:")

    search_criteria["warna_kulit"] = input("Warna kulit: ").lower()
    search_criteria["ukuran_tubuh"] = input("Ukuran tubuh: ").lower()
    search_criteria["jenis_makanan"] = input("Jenis makanan: ").lower()

    matching_animals = []

    for hewan in data_hewan:

        similarity_warnakulit = similarity(search_criteria["warna_kulit"], hewan.get("warna_kulit", "").lower())
        similarity_ukurantubuh = similarity(search_criteria["ukuran_tubuh"], hewan.get("ukuran_tubuh", "").lower())
        similarity_jenismakanan = similarity(search_criteria["jenis_makanan"], hewan.get("jenis_makanan", "").lower())

        threshold = 0.6

        cocok_semua_kriteria = (similarity_warnakulit > threshold and
                                similarity_ukurantubuh > threshold and
                                similarity_jenismakanan > threshold)

        if cocok_semua_kriteria:
            matching_animals.append(hewan["nama"])

    if matching_animals:
        tampilkan_hewan_cocok(matching_animals)

        nomor_hewan = int(input("Pilih Nomor Hewan: "))

        if 1 <= nomor_hewan <= len(matching_animals):
            selected_animal = matching_animals[nomor_hewan - 1]
            selected_animal_data = next((hewan for hewan in data_hewan if hewan.get("nama") == selected_animal), None)
          
            tampilkan_saran(selected_animal_data)
            
            pilihan = input("\nApakah Anda ingin memilih hewan lagi? (y/n): ").lower()
            if pilihan != 'y':
                break
        else:
            print("Nomor hewan tidak valid.")
    else:
        print("Tidak ada hewan yang cocok dengan kriteria pencarian.")
        break

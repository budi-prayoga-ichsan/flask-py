# program_studi = {"IF": "Informatika", "SI": "Sistem Informasi", "TE": "Teknik Elektro"}

# # Mengubah menjadi list
# kunci_list = list(program_studi.keys())  # Hasilnya: ['IF', 'SI', 'TE']

# # Sekarang kita bisa akses pakai indeks
# a = program_studi.keys()
# # print(kunci_list)
# b = program_studi.items()
# print(a)
# print(b)
# # print(kunci_list[0])  # Output: IF
# # print(kunci_list[1])  # Output: SI

# for key in program_studi:
#     print(f"Kode: {key}, Nama Prodi: {program_studi[key]}")
try:
    hasil = 10 / 0
    print(hasil)

except Exception as e:
    print("Terjadi kesalahan!", e)

finally:
    print("selesai")
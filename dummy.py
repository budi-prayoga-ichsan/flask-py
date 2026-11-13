import random
from db import get_db_connection

# nama_depan = ["Andi", "agus", 1]

# nama = random.choice(nama_depan)
# print(nama)

# desimal = random.random()
# print(desimal)

# bulat = random.randint(1,10)
# print(bulat)


# 1. Daftar nama
nama_depan = [
    "Andi", "Budi", "Citra", "Doni", "Eka",
    "Fajar", "Gilang", "Hendra", "Indah", "Joko"
]

nama_belakang = [
    "Saputra", "Santoso", "Lestari", "Pratama",
    "Putri", "Wijaya", "Permana", "Ramadhan"
]

# 2. Dictionary program studi dan fakultas
program_studi = {
    "Teknik Informatika": "Fakultas Teknik",
    "Sistem Informasi": "Fakultas Teknik",
    "Teknik Elektro": "Fakultas Teknik",
    "Manajemen": "Fakultas Ekonomi",
    "Akuntansi": "Fakultas Ekonomi"
}

# 3. Menampung data mahasiswa
data_mahasiswa = []

for i in range(495):
    nim = 2310006 + i

    depan = random.choice(nama_depan)
    belakang = random.choice(nama_belakang)

    nama = depan + " " + belakang

    prodi = random.choice(list(program_studi.keys()))
    fakultas = program_studi[prodi]

    data_mahasiswa.append(
        (nim,nama,prodi,fakultas)
    )

db = get_db_connection()
cursor = db.cursor()

query = """
        INSERT IGNORE INTO mahasiswa(nim, nama, prodi, fakultas)
        VALUES (%s, %s, %s, %s)
        """

cursor.executemany(query,data_mahasiswa)
db.commit()
print("proses selesai")
print("Jumlah data yang dibuat: " , len(data_mahasiswa))
cursor.close()
db.close
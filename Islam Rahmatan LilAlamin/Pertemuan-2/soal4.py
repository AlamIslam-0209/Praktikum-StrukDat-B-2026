mahasiswa = {
    "A001" : {
        "nama": 'Budi',
        "prodi": 'Informatika',
        'ipk': 3.45
    },
    "A002" : {
        "nama": 'siti',
        "prodi": 'Sistem Informasi',
        'ipk': 3.20
    },
    "A003" : {
        "nama": 'Andi',
        "prodi": 'Informatika',
        'ipk': 3.75
    }
}

# print(mahasiswa)

for nim in mahasiswa:
    if mahasiswa[nim]["ipk"] > 3.5:
        print(mahasiswa[nim]["nama"])

total = 0
for nim in mahasiswa:
    total += mahasiswa[nim]["ipk"]

mean = total/len(mahasiswa)
print(f"{mean:.2f}")

mahasiswa.update({'A004': {"nama": 'Alam',
        "prodi": 'Informatika',
        'ipk': 4.5}})
print(mahasiswa)


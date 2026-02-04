Kelas_A = {"Struktur Data", "Basis Data", "AI", "Pemogaman Web"}
kelas_B = {"Struktur Data", "Machine Learning", "AI", "Cloud Computing"}

# Tentukan Mata kuliah Yang diambil kedua kelas
print("Mata Kuliah yang diamil kedua kelas", Kelas_A.intersection(kelas_B))

# Tentukan Mata kuliah yang hanya diambil  kelas A
print("Matkul yg ada di a dan tidak ada di B", Kelas_A.difference(kelas_B))


print("gabungan Matakuliah Unik dari Kelas A dan B", (Kelas_A.difference(kelas_B)).union(kelas_B.difference(Kelas_A)))


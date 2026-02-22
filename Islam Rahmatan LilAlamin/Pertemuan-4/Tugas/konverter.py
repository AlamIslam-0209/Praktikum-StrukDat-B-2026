from kurs import data_kurs

def idr_to_asing(jumlah_uang, kode_mata_uang):
    if kode_mata_uang in data_kurs:
        return jumlah_uang/data_kurs[kode_mata_uang]

def asing_to_idr(jumlah_uang, kode_mata_uang):
    if kode_mata_uang in data_kurs:
        return jumlah_uang * data_kurs[kode_mata_uang]
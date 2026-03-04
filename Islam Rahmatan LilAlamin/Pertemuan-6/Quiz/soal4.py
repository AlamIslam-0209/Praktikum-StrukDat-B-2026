level_diskon = (
(500000, 15), # belanja >= 500.000 -> diskon 15%
(300000, 10), # belanja >= 300.000 -> diskon 10%
(100000, 5), # belanja >= 100.000 -> diskon 5%
(0, 0), # default -> tidak ada diskon
)

def hitung_diskon(total_belanja, level_diskon, index = 0):
    pass
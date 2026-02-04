angka = [10, 20, 30, 40, 50]
print(f"def: {angka}")

angka.append(60)
print(f"Setelah ditambah 60: {angka}")

angka.remove(20)
print(f"setelah dikurang 20: {angka}")

print("maksimum angka:",max(angka))

print("minimum angka:", min(angka))

total = 0
for num in angka:
    total += num
mean = total / len(angka)
print("rata rata:", mean)
print(angka)
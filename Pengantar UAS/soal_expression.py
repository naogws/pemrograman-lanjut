# Ekspresi a: 15 mod 5
result_a = 15 % 5
print(f"Hasil dari 15 mod 5 adalah: {result_a}")

# Ekspresi b: 12 + 3 * 5 == 75
result_b = 12 + 3 * 5 == 75
print(f"Hasil dari 12 + 3 * 5 == 75 adalah: {result_b}")

# Ekspresi c: "PML" + "15523"
result_c = "PML" + "15523"
print(f"Hasil dari \"PML\" + \"15523\" adalah: {result_c}")

# Ekspresi d: "100" + 234
# Ekspresi ini akan menghasilkan TypeError karena mencoba menjumlahkan string dan integer
try:
    result_d = "100" + 234
except TypeError as e:
    result_d = str(e)
print(f"Hasil dari \"100\" + 234 adalah: {result_d}")

# Ekspresi e: ((11 % 3) + 2) != 8 / 2
result_e = ((11 % 3) + 2) != 8 / 2
print(f"Hasil dari ((11 % 3) + 2) != 8 / 2 adalah: {result_e}")
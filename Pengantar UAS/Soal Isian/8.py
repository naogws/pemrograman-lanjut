def mystery(n, m):
    p = 0
    e = 0
    while e < n:
        p += 1
        e += m
    return p

# Contoh penggunaan
print(mystery(4, 3))  # Outputnya adalah: 4

# Pelacakan nilai p dan e dari setiap iterasi:
# Iterasi 1: p = 1, e = 3
# Iterasi 2: p = 2, e = 6
# Nilai akhir: p = 2, e = 6
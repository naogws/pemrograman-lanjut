import json

# Soal 6: Apa hasil dari eksekusi kode berikut?
json_string = '[["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]'
result = json.loads(json_string)[1][2]
print(result)

# Outputnya adalah: 'f'
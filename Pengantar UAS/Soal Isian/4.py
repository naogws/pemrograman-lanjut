letters = ["a", "b", "o", "c", "p"]

# a. >>>letters[1]
result_a = letters[1]
print(result_a)

# b. >>>letters[len(letters)-2]
result_b = letters[len(letters)-2]
print(result_b)

# c. >>>letters + ["x"]
result_c = letters + ["x"]
print(result_c)

# d. >>>letters
result_d = letters
print(result_d)

# Output:
# 'b'
# 'c'
# ['a', 'b', 'o', 'c', 'p', 'x']
# ['a', 'b', 'o', 'c', 'p']
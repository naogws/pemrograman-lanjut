def pembagi_indeks1(nums, divisor):
    for i in range(len(nums)):
        if nums[i] % divisor == 0:
            return i
    return -1

vals_baru = [100, 66, 55, 64, 41, 35, 18, 64]
result_baru = pembagi_indeks1(vals_baru, 5)
print(result_baru)
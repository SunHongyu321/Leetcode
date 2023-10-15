def singleNumber(nums):
    result = 0
    for i in range(32): # 32 bits
        sum = 0
        mask = 1 << i
        for num in nums:
            if num & mask:
                sum += 1
        if sum % 3:
            result |= mask
# if the result is negative, we need to convert it to 32 bit integer
    if result & (1 << 31):
        return result - (1 << 32)
    return result

nums = [2,2,3,2]
print(singleNumber(nums))

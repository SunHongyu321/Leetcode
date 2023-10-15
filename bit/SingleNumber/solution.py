sum = 0
sum_ = 0
res = 0

def singleNumber1(nums):
    for i in range(32):
        sum_ = 0
        for j in range(len(nums)):
            sum_ += (nums[j] >> i) & 1
        res |= (sum_ % 3) << i


def singleNumber2(nums):
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

# nums = [2,2,3,2]
# print(singleNumber1(nums))
# print(singleNumber2(nums))


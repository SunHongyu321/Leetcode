#include<stdio.h>

int singleNumber(int* nums, int numsSize) {
    int result = 0;
    int sum = 0;
    for(int i = 0; i < numsSize; i++) {
        sum = 0;
        for(int j = 0; j < numsSize; j++) {
            sum += (nums[j] >> i) & 1;
        }
        result |= (sum % 3) << i;
    }
    return result;
}